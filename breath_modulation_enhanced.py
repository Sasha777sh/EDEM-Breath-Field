#!/usr/bin/env python3
"""
Теневой Кодер: Улучшенная биомодуляция катушки
Защищённая версия с хешированием, калибровкой и защитой от перегрузки
"""

import numpy as np
import sounddevice as sd
import hashlib
import json
import time
from datetime import datetime
import os
from scipy import signal
from scipy.signal import butter, filtfilt

class BreathModulator:
    def __init__(self):
        self.fs = 44100
        self.freq = 432  # основной тон
        self.duration = 60
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.calibration_data = None
        self.protection_enabled = True
        
    def create_session_hash(self):
        """Создаём хеш сессии для легализации"""
        session_data = {
            'timestamp': self.session_id,
            'frequency': self.freq,
            'sample_rate': self.fs,
            'duration': self.duration
        }
        session_str = json.dumps(session_data, sort_keys=True)
        return hashlib.sha256(session_str.encode()).hexdigest()
    
    def calibrate_breath_pattern(self):
        """Калибровка под индивидуальный ритм дыхания"""
        print("🔧 Калибровка дыхания...")
        print("Дыши спокойно 30 секунд рядом с микрофоном")
        
        # Записываем базовый паттерн
        calibration = sd.rec(int(30 * self.fs), samplerate=self.fs, channels=1)
        sd.wait()
        
        # Анализируем ритм
        breath_envelope = np.abs(calibration).reshape(-1)
        
        # Находим пики дыхания
        peaks, _ = signal.find_peaks(breath_envelope, distance=int(0.5 * self.fs))
        if len(peaks) > 0:
            breath_rate = len(peaks) / 30  # дыханий в секунду
            self.calibration_data = {
                'breath_rate': breath_rate,
                'min_amplitude': np.percentile(breath_envelope, 10),
                'max_amplitude': np.percentile(breath_envelope, 90),
                'session_hash': self.create_session_hash()
            }
            print(f"✅ Калибровка завершена. Ритм: {breath_rate:.2f} Гц")
            return True
        else:
            print("❌ Не удалось определить ритм дыхания")
            return False
    
    def apply_protection_filters(self, audio_data):
        """Защита от помех и перегрузки"""
        if not self.protection_enabled:
            return audio_data
            
        # Фильтр от сетевых помех (50/60 Гц)
        nyquist = self.fs / 2
        low_cutoff = 0.5  # убираем очень низкие частоты
        high_cutoff = 20  # убираем высокие частоты
        
        b, a = butter(4, [low_cutoff/nyquist, high_cutoff/nyquist], btype='band')
        filtered = filtfilt(b, a, audio_data)
        
        # Ограничение амплитуды
        max_amplitude = 0.8
        filtered = np.clip(filtered, -max_amplitude, max_amplitude)
        
        return filtered
    
    def modulate_with_breath(self):
        """Основная функция модуляции с защитой"""
        if not self.calibration_data:
            print("❌ Сначала проведите калибровку!")
            return
            
        print(f"🌊 Начинаем модуляцию... Сессия: {self.session_id}")
        print("Дыши спокойно рядом с микрофоном...")
        
        # Записываем дыхание
        breath = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=1)
        sd.wait()
        
        # Применяем защитные фильтры
        breath_clean = self.apply_protection_filters(breath)
        
        # Извлекаем огибающую дыхания
        envelope = np.abs(breath_clean).reshape(-1)
        
        # Нормализуем по калибровочным данным
        min_amp = self.calibration_data['min_amplitude']
        max_amp = self.calibration_data['max_amplitude']
        envelope = np.interp(envelope, (min_amp, max_amp), (0.2, 1.0))
        
        # Создаём модулированный сигнал
        t = np.linspace(0, self.duration, len(envelope))
        signal_432 = np.sin(2 * np.pi * self.freq * t)
        modulated_signal = signal_432 * envelope
        
        # Записываем сессию
        self.save_session_data(breath_clean, envelope, modulated_signal)
        
        # Воспроизводим
        print("🔊 Воспроизведение модулированного сигнала...")
        sd.play(modulated_signal, self.fs)
        sd.wait()
        
        print("✅ Сессия завершена")
    
    def save_session_data(self, breath_data, envelope, signal):
        """Сохранение данных сессии с хешированием"""
        session_dir = f"breath_sessions/{self.session_id}"
        os.makedirs(session_dir, exist_ok=True)
        
        # Сохраняем сырые данные
        np.save(f"{session_dir}/breath_raw.npy", breath_data)
        np.save(f"{session_dir}/envelope.npy", envelope)
        np.save(f"{session_dir}/modulated_signal.npy", signal)
        
        # Создаём отчёт
        report = {
            'session_id': self.session_id,
            'timestamp': datetime.now().isoformat(),
            'calibration': self.calibration_data,
            'files': {
                'breath_raw.npy': self.calculate_file_hash(f"{session_dir}/breath_raw.npy"),
                'envelope.npy': self.calculate_file_hash(f"{session_dir}/envelope.npy"),
                'modulated_signal.npy': self.calculate_file_hash(f"{session_dir}/modulated_signal.npy")
            },
            'session_hash': self.create_session_hash()
        }
        
        with open(f"{session_dir}/session_report.json", 'w') as f:
            json.dump(report, f, indent=2)
        
        # Создаём .sha256 файлы
        for filename in ['breath_raw.npy', 'envelope.npy', 'modulated_signal.npy']:
            self.create_sha256_file(f"{session_dir}/{filename}")
        
        print(f"📁 Данные сохранены в {session_dir}")
        print(f"🔐 Хеш сессии: {self.create_session_hash()}")
    
    def calculate_file_hash(self, filepath):
        """Вычисляем SHA256 хеш файла"""
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    
    def create_sha256_file(self, filepath):
        """Создаём .sha256 файл для верификации"""
        file_hash = self.calculate_file_hash(filepath)
        with open(f"{filepath}.sha256", 'w') as f:
            f.write(f"{file_hash}  {os.path.basename(filepath)}\n")

def main():
    print("🔥 Теневой Кодер: Биомодуляция катушки")
    print("=" * 50)
    
    modulator = BreathModulator()
    
    # Калибровка
    if modulator.calibrate_breath_pattern():
        # Основная модуляция
        modulator.modulate_with_breath()
    else:
        print("❌ Калибровка не удалась. Проверьте микрофон.")

if __name__ == "__main__":
    main()
