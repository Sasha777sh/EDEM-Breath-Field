# 📚 Zenodo Submission Guide — EDEM-Breath-Field Protocol

**Цель:** Получить DOI для протоколов дыхательного резонанса (0.1 Гц) как научного артефакта

---

## 🎯 Зачем нужен Zenodo DOI

1. **Научная легитимность** — протоколы становятся цитируемыми
2. **Приоритет открытия** — фиксируется дата и авторство
3. **Корпоративное доверие** — компании видят научную основу
4. **Лицензирование** — DOI упрощает коммерческое лицензирование

---

## 📋 Что публиковать на Zenodo

### Вариант 1: Полный пакет (рекомендуется)

**Название:** "EDEM-Breath-Field: Open Hardware Protocol for Respiratory Resonance at 0.1 Hz (6 breaths/min)"

**Содержание:**
1. **Техническая спецификация:**
   - `docs/theory/equations.md`
   - `docs/discovery/edem_v9_penrose_bridge.md`
   - `arduino_breath_sensor.ino` (протокол калибровки)

2. **Научная документация:**
   - `docs/discovery/discovery_core.md`
   - `docs/theory/unified_laws.md`
   - Связь HRV ↔ дыхание 0.1 Гц

3. **Протоколы экспериментов:**
   - `docs/EXPERIMENTS_SUMMARY.md`
   - HRV measurement protocol
   - Breath Field calibration guide

**Формат:** ZIP-архив всех файлов

---

### Вариант 2: Минимальный пакет

**Название:** "EDEM-Breath-Field Protocol: 0.1 Hz Respiratory Resonance for HRV Coherence"

**Содержание:**
- Техническая спецификация (1 PDF)
- Протокол калибровки
- Связь с формулой E = A·R·L - S

---

## 📝 Заполнение метаданных на Zenodo

### Основные поля:

**Title:**
```
EDEM-Breath-Field: Open Hardware Protocol for Respiratory Resonance at 0.1 Hz
```

**Description:**
```
EDEM-Breath-Field is an open hardware protocol for synchronizing breathing at 0.1 Hz (6 breaths/min) to enhance Heart Rate Variability (HRV) coherence. The protocol is based on the Physics of Life formula E = A·R·L - S, connecting attention, resonance, love (coherence), and entropy (stress).

**Key Features:**
- Breathing rhythm: 0.1 Hz (6 breaths/min)
- HRV coherence enhancement
- Integration with Penrose-Hameroff Orch OR theory
- Open hardware implementation
- Arduino-compatible calibration

**Scientific Basis:**
- Connects respiratory rhythm to cardiac coherence
- Links to quantum biology (biophotons, microtubules)
- Experimental validation through HRV measurement

**License:** EDEM-Breath-Field License v1.0 (Open Hardware with Commercial Rights)

**Author:** Aleksandr Shelementev
```

**Keywords:**
```
respiratory resonance, HRV coherence, breathing protocol, 0.1 Hz, heart rate variability, open hardware, quantum biology, biophotonics, Orch OR, Penrose-Hameroff, physics of life
```

**Publication Type:**
- Software / Protocol / Hardware

**License:**
- Custom: "EDEM-Breath-Field License v1.0"
- Или: CC BY-SA 4.0 (для базовой версии)

**Related Identifiers:**
- GitHub: `https://github.com/Sasha777sh/EDEM-Breath-Field`
- (После получения DOI — добавить DOI в GitHub README)

---

## 🔗 Связь с GitHub

**После получения DOI:**

1. Добавить DOI badge в `README.md`:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXX)
```

2. Обновить лицензию с DOI:
```markdown
**Zenodo DOI:** 10.5281/zenodo.XXXXX
```

3. Упоминать DOI в коммерческих предложениях

---

## 📦 Подготовка ZIP-архива

**Структура архива:**

```
EDEM-Breath-Field-Protocol-v1.0.zip
├── README.md                    (описание протокола)
├── SPECIFICATION.md             (техническая спецификация)
├── CALIBRATION_GUIDE.md         (протокол калибровки)
├── HARDWARE/
│   └── arduino_breath_sensor.ino
├── DOCUMENTATION/
│   ├── theory/
│   │   ├── equations.md
│   │   └── unified_laws.md
│   └── discovery/
│       ├── discovery_core.md
│       └── edem_v9_penrose_bridge.md
├── EXPERIMENTS/
│   └── EXPERIMENTS_SUMMARY.md
└── LICENSE/
    └── EDEM_Breath_Field_License_v1.md
```

---

## 🚀 Пошаговая инструкция

### Шаг 1: Регистрация на Zenodo

1. Зайди на https://zenodo.org
2. Нажми "Sign up" → через GitHub (проще всего)
3. Подтверди email

### Шаг 2: Подготовка материалов

1. Создай ZIP-архив с файлами (структура выше)
2. Убедись, что все файлы в текстовом формате (не бинарники)
3. Добавь README с описанием

### Шаг 3: Загрузка

1. В Zenodo → "Upload"
2. Выбери "New Upload"
3. Загрузи ZIP-архив
4. Заполни все метаданные (см. выше)
5. Установи лицензию
6. Нажми "Publish"

### Шаг 4: Получение DOI

1. После публикации получишь DOI (например: `10.5281/zenodo.1234567`)
2. Сохрани DOI
3. Добавь в GitHub README
4. Упоминай в коммерческих предложениях

---

## 💡 Советы

1. **Версионирование:** Если обновляешь протокол — загружай новую версию на Zenodo (новый DOI)

2. **Связь версий:** В описании указывай "v1.0" и ссылку на предыдущие версии (если есть)

3. **Цитирование:** После получения DOI можешь цитировать себя в статьях

4. **Корпоративные предложения:** DOI показывает научную легитимность → проще лицензировать

---

## 📄 Пример описания для Zenodo

```
This release contains the EDEM-Breath-Field Protocol v1.0, an open hardware specification for respiratory resonance at 0.1 Hz (6 breaths/min) to enhance Heart Rate Variability (HRV) coherence.

**What's included:**
- Technical specification for 0.1 Hz breathing rhythm
- HRV measurement protocol
- Arduino-compatible calibration code
- Connection to Physics of Life formula (E = A·R·L - S)
- Integration with quantum biology (Orch OR, biophotons)

**Use cases:**
- Open hardware devices (DIY)
- Scientific research
- Commercial integration (requires license)

**License:** EDEM-Breath-Field License v1.0 (see LICENSE file)

**Related work:**
- GitHub repository: https://github.com/Sasha777sh/EDEM-Breath-Field
- Full documentation and course materials available in repository
```

---

**Готово! После публикации получишь DOI и сможешь использовать его для лицензирования.**
