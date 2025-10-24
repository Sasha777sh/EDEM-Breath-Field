#!/usr/bin/env python3
"""
Теневой Кодер: Python-Arduino мост для биомодуляции
Получает данные с Arduino и модулирует 432 Гц
"""

import serial
import json
import numpy as np
import sounddevice as sd
import hashlib
import time
from datetime import datetime
import os

class ArduinoBreathBridge:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.fs = 44100
        self.freq = 432
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.breath_data = []
        self.protection_enabled = True
        
    def connect_arduino(self):
        """Подключение к Arduino"""
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # ждём инициализации Arduino
            print(f"✅ Подключён к Arduino на {self.port}")
            return True
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")
            return False
    
    def read_breath_data(self):
        """Чтение данных дыхания с Arduino"""
        if not self.serial_conn:
            return None
            
        try:
            line = self.serial_conn.readline().decode('utf-8').strip()
            if line.startswith('{') and line.endswith('}'):
                data = json.loads(line)
                return data
        except Exception as e:
            print(f"⚠️ Ошибка чтения: {e}")
            
        return None
    
    def modulate_432hz(self, breath_envelope):
        """Модуляция 432 Гц по дыханию"""
        # Создаём базовый тон 432 Гц
        duration = 0.1  # 100мс буфер
        t = np.linspace(0, duration, int(self.fs * duration))
        base_tone = np.sin(2 * np.pi * self.freq * t)
        
        # Применяем модуляцию дыхания
        modulation_factor = np.clip(breath_envelope, 0.1, 1.0)
        modulated = base_tone * modulation_factor
        
        return modulated
    
    def start_breath_modulation(self, duration_seconds=60):
        """Основной цикл модуляции"""
        if not self.connect_arduino():
            return
            
        print(f"🌊 Начинаем биомодуляцию... Сессия: {self.session_id}")
        print("Дыши спокойно...")
        
        start_time = time.time()
        session_data = []
        
        try:
            while time.time() - start_time < duration_seconds:
                # Читаем данные с Arduino
                breath_data = self.read_breath_data()
                if breath_data and breath_data.get('calibrated', False):
                    
                    pressure = breath_data['pressure']
                    envelope = breath_data['envelope']
                    pwm = breath_data['pwm']
                    
                    # Защита от перегрузки
                    if self.protection_enabled and pressure > 4.8:
                        print("⚠️ ПЕРЕГРУЗКА! Пропускаем кадр")
                        continue
                    
                    # Модулируем 432 Гц
                    modulated_signal = self.modulate_432hz(envelope)
                    
                    # Воспроизводим
                    sd.play(modulated_signal, self.fs)
                    
                    # Сохраняем данные
                    session_data.append({
                        'timestamp': time.time(),
                        'pressure': pressure,
                        'envelope': envelope,
                        'pwm': pwm
                    })
                    
                    # Индикация
                    if len(session_data) % 20 == 0:
                        print(f"📊 Обработано: {len(session_data)} кадров")
                
                time.sleep(0.05)  # 20 Гц обновление
                
        except KeyboardInterrupt:
            print("\n⏹️ Остановка по запросу пользователя")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
        finally:
            self.save_session(session_data)
            if self.serial_conn:
                self.serial_conn.close()
    
    def save_session(self, session_data):
        """Сохранение сессии с хешированием"""
        if not session_data:
            print("❌ Нет данных для сохранения")
            return
            
        session_dir = f"arduino_sessions/{self.session_id}"
        os.makedirs(session_dir, exist_ok=True)
        
        # Сохраняем данные
        np.save(f"{session_dir}/breath_data.npy", session_data)
        
        # Создаём отчёт
        report = {
            'session_id': self.session_id,
            'timestamp': datetime.now().isoformat(),
            'duration': len(session_data) * 0.05,  # секунд
            'samples': len(session_data),
            'files': {
                'breath_data.npy': self.calculate_file_hash(f"{session_dir}/breath_data.npy")
            },
            'session_hash': self.create_session_hash()
        }
        
        with open(f"{session_dir}/session_report.json", 'w') as f:
            json.dump(report, f, indent=2)
        
        # Создаём .sha256
        self.create_sha256_file(f"{session_dir}/breath_data.npy")
        
        print(f"📁 Сессия сохранена в {session_dir}")
        print(f"🔐 Хеш сессии: {self.create_session_hash()}")
    
    def create_session_hash(self):
        """Создаём хеш сессии"""
        session_data = {
            'session_id': self.session_id,
            'frequency': self.freq,
            'sample_rate': self.fs
        }
        session_str = json.dumps(session_data, sort_keys=True)
        return hashlib.sha256(session_str.encode()).hexdigest()
    
    def calculate_file_hash(self, filepath):
        """SHA256 хеш файла"""
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    
    def create_sha256_file(self, filepath):
        """Создаём .sha256 файл"""
        file_hash = self.calculate_file_hash(filepath)
        with open(f"{filepath}.sha256", 'w') as f:
            f.write(f"{file_hash}  {os.path.basename(filepath)}\n")

def main():
    print("🔥 Теневой Кодер: Python-Arduino мост")
    print("=" * 50)
    
    # Определяем порт Arduino
    possible_ports = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0', '/dev/ttyACM1']
    port = None
    
    for p in possible_ports:
        if os.path.exists(p):
            port = p
            break
    
    if not port:
        print("❌ Arduino не найден! Проверьте подключение.")
        return
    
    print(f"🔌 Используем порт: {port}")
    
    bridge = ArduinoBreathBridge(port=port)
    bridge.start_breath_modulation(duration_seconds=60)

if __name__ == "__main__":
    main()
