# 📦 Zenodo File List — Конкретный список файлов для публикации

**Что публиковать на Zenodo:** Точный список файлов для ZIP-архива

---

## ✅ Обязательные файлы (минимум для DOI)

### 1. Техническая спецификация протокола:

```
📄 README.md                          ← Создать специально для Zenodo
📄 SPECIFICATION.md                   ← Техническая спецификация 0.1 Гц
📄 CALIBRATION_GUIDE.md               ← Протокол калибровки устройств
```

### 2. Код протокола:

```
📄 arduino_breath_sensor.ino          ← Arduino код калибровки
📄 python_arduino_bridge.py           ← Python мост (если есть)
```

### 3. Научная документация:

```
📄 docs/theory/equations.md           ← Формула E = A·R·L - S
📄 docs/discovery/edem_v9_penrose_bridge.md  ← Связь HRV ↔ дыхание
📄 docs/theory/unified_laws.md        ← 9 законов (контекст)
```

### 4. Протоколы экспериментов:

```
📄 docs/EXPERIMENTS_SUMMARY.md        ← Сводка экспериментов
📄 docs/courses/pdf-guides/hrv_protocol.md  ← HRV протокол измерения
```

### 5. Лицензия:

```
📄 licensing/open-hardware/EDEM_Breath_Field_License_v1.md
```

---

## 📋 Структура ZIP-архива для Zenodo

```
EDEM-Breath-Field-Protocol-v1.0.zip
│
├── README.md                         ← Главный файл (описание)
├── SPECIFICATION.md                  ← Техническая спецификация
├── CALIBRATION_GUIDE.md              ← Руководство по калибровке
│
├── hardware/
│   ├── arduino_breath_sensor.ino     ← Arduino код
│   └── python_arduino_bridge.py      ← Python мост (если есть)
│
├── theory/
│   ├── equations.md                  ← Формула E = A·R·L - S
│   ├── unified_laws.md               ← 9 законов
│   └── edem_v9_penrose_bridge.md     ← HRV ↔ дыхание
│
├── experiments/
│   ├── EXPERIMENTS_SUMMARY.md        ← Сводка экспериментов
│   └── hrv_protocol.md               ← HRV протокол
│
└── LICENSE/
    └── EDEM_Breath_Field_License_v1.md
```

---

## 📄 Содержание каждого файла

### README.md (создать новый для Zenodo)

```markdown
# EDEM-Breath-Field Protocol v1.0

**Open Hardware Protocol for Respiratory Resonance at 0.1 Hz**

## Описание

EDEM-Breath-Field — это протокол открытого оборудования для синхронизации дыхания на частоте 0.1 Гц (6 вдохов/мин) с целью повышения когерентности Heart Rate Variability (HRV).

## Ключевые особенности

- **Частота дыхания:** 0.1 Гц (6 вдохов/мин)
- **Протокол:** 4-2-6-2 (вдох-пауза-выдох-пауза)
- **Результат:** Повышение HRV когерентности на 20-30%
- **Научная основа:** Формула E = A·R·L - S (Физика Живого)

## Структура архива

- `SPECIFICATION.md` — техническая спецификация
- `CALIBRATION_GUIDE.md` — протокол калибровки
- `hardware/` — Arduino код
- `theory/` — научная документация
- `experiments/` — протоколы экспериментов
- `LICENSE/` — лицензия

## Использование

1. **Для научных исследований:** Свободное использование с атрибуцией
2. **Для коммерческого использования:** Требуется лицензия (см. LICENSE/)

## Цитирование

Если используешь этот протокол в публикации, цитируй через Zenodo DOI:

```
Shelementev, A. (2025). EDEM-Breath-Field: Open Hardware Protocol for Respiratory Resonance at 0.1 Hz. Zenodo. https://doi.org/10.5281/zenodo.XXXXX
```

## Контакты

- GitHub: https://github.com/Sasha777sh/EDEM-Breath-Field
- Лицензия: EDEM-Breath-Field License v1.0
```

---

### SPECIFICATION.md (создать на основе существующих файлов)

**Что включить:**
1. Частота дыхания: 0.1 Гц (6 вдохов/мин)
2. Протокол 4-2-6-2 (детальное описание)
3. Связь с HRV LF band (0.1 Гц)
4. Технические параметры калибровки
5. Алгоритм синхронизации

**Источники:**
- `docs/theory/equations.md`
- `docs/discovery/edem_v9_penrose_bridge.md`
- `docs/courses/pdf-guides/hrv_protocol.md`

---

### CALIBRATION_GUIDE.md (создать на основе кода)

**Что включить:**
1. Протокол калибровки Arduino датчика
2. Калибровка под индивидуальный ритм
3. Валидация измерений
4. Troubleshooting

**Источники:**
- `arduino_breath_sensor.ino` (комментарии в коде)
- `docs/experiments/hardware_spec.md`

---

## 🚀 Инструкция по сборке архива

### Шаг 1: Создать папку

```bash
mkdir zenodo_package
cd zenodo_package
```

### Шаг 2: Скопировать файлы

```bash
# Из репозитория EDEM-Breath-Field:

# README (создать новый)
# SPECIFICATION.md (создать на основе docs/theory/equations.md + docs/discovery/edem_v9_penrose_bridge.md)
# CALIBRATION_GUIDE.md (создать на основе arduino_breath_sensor.ino)

# Код
cp arduino_breath_sensor.ino hardware/
cp python_arduino_bridge.py hardware/  # если есть

# Теория
cp docs/theory/equations.md theory/
cp docs/theory/unified_laws.md theory/
cp docs/discovery/edem_v9_penrose_bridge.md theory/

# Эксперименты
cp docs/EXPERIMENTS_SUMMARY.md experiments/
cp docs/courses/pdf-guides/hrv_protocol.md experiments/hrv_protocol.md

# Лицензия
cp licensing/open-hardware/EDEM_Breath_Field_License_v1.md LICENSE/
```

### Шаг 3: Создать ZIP

```bash
cd ..
zip -r EDEM-Breath-Field-Protocol-v1.0.zip zenodo_package/
```

---

## ✅ Чеклист перед загрузкой

- [ ] Все файлы скопированы
- [ ] README.md создан и заполнен
- [ ] SPECIFICATION.md создан (техническая спецификация)
- [ ] CALIBRATION_GUIDE.md создан
- [ ] Все пути к файлам корректны
- [ ] Лицензия включена
- [ ] ZIP создан и проверен
- [ ] Размер архива < 50 MB (лимит Zenodo)

---

## 📝 Альтернатива: Минимальный пакет

Если хочешь опубликовать только самое важное:

```
EDEM-Breath-Field-Protocol-v1.0-MINIMAL.zip
├── README.md                         ← Описание протокола
├── SPECIFICATION.md                  ← Техническая спецификация 0.1 Гц
├── arduino_breath_sensor.ino         ← Код калибровки
└── LICENSE.md                        ← Лицензия
```

**Размер:** ~100-200 KB  
**Содержание:** Только протокол, без всей теории

---

**Готово! Используй этот список для сборки архива на Zenodo.**
