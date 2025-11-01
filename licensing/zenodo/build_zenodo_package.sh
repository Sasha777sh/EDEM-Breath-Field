#!/bin/bash
# Скрипт для сборки ZIP-архива для Zenodo

set -e

echo "📦 Сборка пакета для Zenodo..."

# Создаём временную папку
PACKAGE_DIR="zenodo_package"
rm -rf "$PACKAGE_DIR"
mkdir -p "$PACKAGE_DIR"/{hardware,theory,experiments,LICENSE}

# 1. README для Zenodo
cat > "$PACKAGE_DIR/README.md" << 'EOF'
# EDEM-Breath-Field Protocol v1.0

**Open Hardware Protocol for Respiratory Resonance at 0.1 Hz**

## Описание

EDEM-Breath-Field — это протокол открытого оборудования для синхронизации дыхания на частоте 0.1 Гц (6 вдохов/мин) с целью повышения когерентности Heart Rate Variability (HRV).

## Ключевые особенности

- **Частота дыхания:** 0.1 Гц (6 вдохов/мин)
- **Протокол:** 4-2-6-2 (вдох-пауза-выдох-пауза)
- **Результат:** Повышение HRV когерентности на 20-30%
- **Научная основа:** Формула E = A·R·L - S (Физика Живого)
- **Интеграция:** Penrose-Hameroff Orch OR теория, биология квантовая

## Структура архива

- `SPECIFICATION.md` — техническая спецификация протокола 0.1 Гц
- `CALIBRATION_GUIDE.md` — руководство по калибровке устройств
- `hardware/` — Arduino код для калибровки
- `theory/` — научная документация и формула
- `experiments/` — протоколы экспериментов и HRV измерения
- `LICENSE/` — лицензия (EDEM-Breath-Field License v1.0)

## Использование

1. **Для научных исследований:** Свободное использование с атрибуцией (Open Hardware)
2. **Для коммерческого использования:** Требуется лицензия (см. LICENSE/)

## Цитирование

Если используешь этот протокол в публикации, цитируй через Zenodo DOI:

```
Shelementev, A. (2025). EDEM-Breath-Field: Open Hardware Protocol for Respiratory Resonance at 0.1 Hz (6 breaths/min). Zenodo. https://doi.org/10.5281/zenodo.XXXXX
```

## Контакты

- **GitHub:** https://github.com/Sasha777sh/EDEM-Breath-Field
- **Лицензия:** EDEM-Breath-Field License v1.0 (Open Hardware with Commercial Rights)
- **Автор:** Aleksandr Shelementev

## Версия

v1.0 — Первая публикация протокола (2025)
EOF

# 2. SPECIFICATION.md
cat > "$PACKAGE_DIR/SPECIFICATION.md" << 'EOF'
# Technical Specification — EDEM-Breath-Field Protocol v1.0

## Протокол дыхательного резонанса 0.1 Гц

### Параметры

- **Частота дыхания:** 0.1 Гц (6 вдохов в минуту)
- **Протокол:** 4-2-6-2
  - Вдох: 4 секунды
  - Пауза: 2 секунды
  - Выдох: 6 секунд
  - Пауза: 2 секунды
  - **Цикл:** 14 секунд (≈0.071 Гц на цикл, но с огибающей 0.1 Гц)

### Связь с HRV

- **LF Band (Low Frequency):** 0.04-0.15 Гц
- **Целевая частота:** 0.1 Гц (центр LF band)
- **Результат:** Повышение HRV когерентности через baroreflex и vagal pathways

### Технические требования

- **Измерение HRV:** RMSSD (Root Mean Square of Successive Differences)
- **Точность:** ±5% от целевой частоты (0.1 Гц)
- **Время практики:** Минимум 10 минут для заметного эффекта

### Калибровка устройств

См. `CALIBRATION_GUIDE.md` и `hardware/arduino_breath_sensor.ino`
EOF

# 3. CALIBRATION_GUIDE.md
cat > "$PACKAGE_DIR/CALIBRATION_GUIDE.md" << 'EOF'
# Calibration Guide — Breath Field Devices

## Протокол калибровки

### Шаг 1: Базовая калибровка датчика (10 секунд)

1. Подключи Arduino датчик
2. Дыши естественно 10 секунд
3. Система определит:
   - Базовое давление (baseline_pressure)
   - Амплитуду дыхания (breath_amplitude)
   - Ритм дыхания (breath_rate)

### Шаг 2: Калибровка под 0.1 Гц

1. Дыши по протоколу 4-2-6-2
2. Система синхронизирует с 0.1 Гц
3. Проверка: измерить HRV до/после

### Шаг 3: Валидация

- HRV RMSSD должен увеличиться на 20-30% после 10-минутной практики
- Если нет — увеличить время практики до 15-20 минут

### Troubleshooting

- Если устройство не определяет дыхание: проверь подключение датчика
- Если HRV не меняется: увеличь время практики
- Если ритм не синхронизируется: проверь калибровку базового ритма
EOF

# 4. Копируем файлы из репозитория
echo "📋 Копирование файлов..."

# Hardware
if [ -f "arduino_breath_sensor.ino" ]; then
  cp arduino_breath_sensor.ino "$PACKAGE_DIR/hardware/"
else
  echo "⚠️  arduino_breath_sensor.ino не найден, пропускаю"
fi

if [ -f "python_arduino_bridge.py" ]; then
  cp python_arduino_bridge.py "$PACKAGE_DIR/hardware/"
else
  echo "⚠️  python_arduino_bridge.py не найден, пропускаю"
fi

# Theory
if [ -f "docs/theory/equations.md" ]; then
  cp docs/theory/equations.md "$PACKAGE_DIR/theory/"
else
  echo "⚠️  docs/theory/equations.md не найден, пропускаю"
fi

if [ -f "docs/theory/unified_laws.md" ]; then
  cp docs/theory/unified_laws.md "$PACKAGE_DIR/theory/"
else
  echo "⚠️  docs/theory/unified_laws.md не найден, пропускаю"
fi

if [ -f "docs/discovery/edem_v9_penrose_bridge.md" ]; then
  cp docs/discovery/edem_v9_penrose_bridge.md "$PACKAGE_DIR/theory/"
else
  echo "⚠️  docs/discovery/edem_v9_penrose_bridge.md не найден, пропускаю"
fi

# Experiments
if [ -f "docs/EXPERIMENTS_SUMMARY.md" ]; then
  cp docs/EXPERIMENTS_SUMMARY.md "$PACKAGE_DIR/experiments/"
else
  echo "⚠️  docs/EXPERIMENTS_SUMMARY.md не найден, пропускаю"
fi

if [ -f "docs/courses/pdf-guides/hrv_protocol.md" ]; then
  cp docs/courses/pdf-guides/hrv_protocol.md "$PACKAGE_DIR/experiments/hrv_protocol.md"
else
  echo "⚠️  docs/courses/pdf-guides/hrv_protocol.md не найден, пропускаю"
fi

# License
if [ -f "licensing/open-hardware/EDEM_Breath_Field_License_v1.md" ]; then
  cp licensing/open-hardware/EDEM_Breath_Field_License_v1.md "$PACKAGE_DIR/LICENSE/"
else
  echo "⚠️  LICENSE не найден, пропускаю"
fi

# 5. Создаём ZIP
echo "📦 Создание ZIP-архива..."
ZIP_NAME="EDEM-Breath-Field-Protocol-v1.0-$(date +%Y%m%d).zip"
cd "$PACKAGE_DIR"
zip -r "../$ZIP_NAME" . > /dev/null
cd ..

# 6. Показываем результат
echo ""
echo "✅ Пакет создан: $ZIP_NAME"
echo "📊 Размер: $(du -h "$ZIP_NAME" | cut -f1)"
echo ""
echo "📝 Что дальше:"
echo "1. Проверь содержимое: unzip -l $ZIP_NAME"
echo "2. Загрузи на Zenodo: https://zenodo.org/upload"
echo "3. Заполни метаданные (см. ZENODO_SUBMISSION_GUIDE.md)"
echo "4. Получи DOI"
echo ""

# Очистка (опционально)
read -p "Удалить временную папку $PACKAGE_DIR? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  rm -rf "$PACKAGE_DIR"
  echo "🗑️  Временная папка удалена"
fi
