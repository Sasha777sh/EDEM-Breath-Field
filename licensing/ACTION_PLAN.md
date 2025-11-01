# 🚀 Action Plan — Полный план монетизации

**Цель:** Из протоколов → деньги и партнёры

---

## ✅ Шаг 1: Получить Zenodo DOI (ПРИОРИТЕТ #1)

### Действия:

1. **Собрать архив:**
   ```bash
   cd /Users/sanecek/tema/EDEM-Breath-Field
   ./licensing/zenodo/build_zenodo_package.sh
   ```
   Получишь: `EDEM-Breath-Field-Protocol-v1.0-YYYYMMDD.zip`

2. **Загрузить на Zenodo:**
   - Зайди на https://zenodo.org
   - Войди через GitHub
   - "New Upload" → загрузи ZIP

3. **Заполнить метаданные:**
   - **Title:** `EDEM Breath Field – Open Hardware for 0.1 Hz Breath Coherence`
   - **Authors:** Aleksandr Shelementev
   - **License:** CC-BY-SA 4.0
   - **Keywords:** HRV, coherence, breath, resonance, open hardware
   - **Description:** [из `licensing/zenodo/ZENODO_SUBMISSION_GUIDE.md`]

4. **Получить DOI:**
   - После публикации получишь DOI (например: `10.5281/zenodo.1234567`)
   - Сохрани DOI

5. **Обновить файлы:**
   - `web/landing/for_partners.html` → вставить DOI
   - `README.md` → добавить DOI badge
   - `licensing/partnerships/OUTREACH_TEMPLATES.md` → вставить DOI

**Критерий успеха:** DOI получен, все файлы обновлены

**Время:** 1-2 часа

---

## ✅ Шаг 2: Опубликовать Landing Page "For Partners"

### Действия:

1. **Обновить DOI в HTML:**
   - Открыть `web/landing/for_partners.html`
   - Найти `const doiNumber = '10.5281/zenodo.XXXXX';`
   - Заменить на реальный DOI
   - Найти `id="doi-number"` → заменить текст на реальный DOI

2. **Опубликовать страницу:**

   **Вариант A: GitHub Pages (бесплатно)**
   - Настройки репозитория → Pages
   - Источник: `main` branch, папка `/web/landing`
   - URL: `https://Sasha777sh.github.io/EDEM-Breath-Field/landing/for_partners.html`

   **Вариант B: Отдельный хостинг**
   - Загрузить `for_partners.html` на любой хостинг
   - Привязать домен (если есть): `partners.edem-breath-field.com`

3. **Проверить форму:**
   - Кнопка "Request License PDF" работает
   - Email/backend настроен (или заменить на `mailto:`)

**Критерий успеха:** Страница доступна по ссылке, DOI отображается

**Время:** 30 минут

---

## ✅ Шаг 3: Outreach — Связаться с партнёрами

### Неделя 1: Подготовка

- [ ] Обновить LinkedIn профиль (профессиональный)
- [ ] Подготовить сообщения (шаблоны в `licensing/partnerships/OUTREACH_TEMPLATES.md`)
- [ ] Найти контакты в LinkedIn (Polar, Whoop, Garmin)

### Неделя 2: Tier 3 (стартапы)

**Цели:**
- HRV4Training (LinkedIn)
- Elite HRV (LinkedIn)
- Welltory (LinkedIn)

**Действия:**
1. Найти контакты в LinkedIn
2. Отправить короткое сообщение (из `OUTREACH_TEMPLATES.md`)
3. Отслеживать отклики

**Время:** 2-3 часа (10 сообщений)

---

### Неделя 3: Tier 2

**Цели:**
- Apple Watch HealthKit team (если найдёшь контакты)
- Fitbit Developers
- Amazfit R&D

**Действия:** Аналогично Tier 3

**Время:** 2-3 часа

---

### Неделя 4: Tier 1 (главные цели)

**Цели:**
- **Polar:** Developers Forum / LinkedIn → Product Manager / CTO
- **Whoop:** Whoop Labs / LinkedIn → Technical Team
- **Garmin:** Developer Relations / LinkedIn → Health API Team

**Действия:**
1. Найти контакты (LinkedIn / сайт компании)
2. Отправить персонализированное сообщение:
   - Упомянуть конкретный продукт
   - Приложить ссылку на landing page
   - Предложить технический звонок

**Шаблоны:** `licensing/partnerships/OUTREACH_TEMPLATES.md`

**Время:** 3-4 часа (5-10 сообщений)

---

## ✅ Шаг 4: Подать заявки на гранты

### Площадки (в порядке приоритета):

1. **Gitcoin Grants** (самое простое)
   - Зайди на https://gitcoin.co/grants
   - Создай Grant (шаблон в `licensing/grants/GRANTS_APPLICATION.md`)
   - Бюджет: $1,000-$10,000

2. **OpenCollective**
   - Зайди на https://opencollective.com
   - Создай Collective: "EDEM Breath Field"
   - Создай кампанию (шаблон готов)
   - Бюджет: $5,000-$20,000

3. **NLNet** (Европа)
   - Зайди на https://nlnet.nl
   - Найди подходящую программу
   - Подай заявку (шаблон готов)
   - Бюджет: €5,000-€15,000

**Шаблоны:** `licensing/grants/GRANTS_APPLICATION.md`

**Время:** 2-3 часа на каждую заявку

---

## ✅ Шаг 5: Маркетинг — Технический язык

### Правила (из `licensing/MARKETING_GUIDE.md`):

**✅ ГОВОРИ:**
- "Biofeedback hardware for HRV coherence"
- "0.1 Hz respiratory resonance protocol"
- "Biosignal synchronization framework"
- "HRV coherence enhancement"

**❌ НЕ ГОВОРИ:**
- "Духовный протокол"
- "Энергетическая практика"
- "Метафизическая формула"

### Применение:

- [ ] Все тексты проверены на технический язык
- [ ] Landing page обновлён (убрать "эзотерику")
- [ ] Outreach сообщения проверены
- [ ] GitHub README обновлён

**Гайд:** `licensing/MARKETING_GUIDE.md`

---

## 📊 Временная шкала

### Месяц 1: Фундамент
- **Неделя 1:** Zenodo DOI + Landing page
- **Неделя 2:** Outreach Tier 3 (стартапы)
- **Неделя 3:** Outreach Tier 2
- **Неделя 4:** Outreach Tier 1 + Grants заявки

### Месяц 2: Результаты
- **Неделя 1-2:** Отклики от партнёров
- **Неделя 3-4:** Переговоры, тестовые интеграции

### Месяц 3: Заключение
- Первые лицензионные договоры
- Первые гранты (если одобрены)

---

## 💰 Целевые показатели

**Месяц 1:**
- DOI получен ✅
- Landing page опубликован ✅
- 20+ outreach сообщений отправлено ✅
- 2-3 grants заявки поданы ✅

**Месяц 2:**
- 2-5 откликов от партнёров
- 1-2 технических звонка
- Возможно: первый тестовый проект

**Месяц 3:**
- 1-2 лицензионных договора (royalty или fixed fee)
- Возможно: 1 grant одобрен ($5K-$10K)

**Месяц 6:**
- 3-5 партнёров с лицензиями
- Доход: $5,000-$20,000 (от лицензий + grants)

---

## 🎯 Фокус на результат

**Приоритеты:**
1. **DOI** — научная легитимность (делает всё остальное проще)
2. **Landing page** — профессиональная презентация
3. **Outreach** — реальные контакты
4. **Grants** — дополнительное финансирование

**Правило:** Не распыляйся. Сначала DOI + Landing, потом Outreach, потом Grants.

---

## ✅ Финальный чеклист

**Сейчас:**
- [ ] Запустить `./licensing/zenodo/build_zenodo_package.sh`
- [ ] Получить Zenodo DOI
- [ ] Обновить `for_partners.html` с DOI
- [ ] Опубликовать landing page

**На этой неделе:**
- [ ] Отправить 10-20 outreach сообщений (Tier 3)
- [ ] Подать 1-2 grants заявки

**На следующей неделе:**
- [ ] Outreach Tier 1 (Polar, Whoop, Garmin)
- [ ] Обработать отклики

---

**Готово! Все материалы готовы. Начинай с Zenodo DOI.**
