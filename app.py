import streamlit as st
from collections import Counter

# Архетипические описания для чисел
ARCHETYPES = {
    1: {
        "название": "Путь Воина / Лидера",
        "описание": "Воплощение силы воли, инициативности, самостоятельности",
        "свет": "Новатор, лидер, уверенный в себе",
        "тень": "Упрямство, эгоизм, страх одиночества",
        "задача": "Иди своим путём, не бойся быть первой и уникальной",
        "рекомендации": "Смелее проявляй лидерство, начни проект, который давно откладываешь"
    },
    5: {
        "название": "Путь Искателя",
        "описание": "Энергия свободы, перемен, жажды познания",
        "свет": "Гибкость, общительность, любознательность",
        "тень": "Неустойчивость, избегание обязательств",
        "задача": "Учись выстраивать внутренние опоры",
        "рекомендации": "Запланируй путешествие или обучающий курс, чтобы расширить горизонты"
    },
    7: {
        "название": "Путь Мудреца",
        "описание": "Энергия анализа, интуиции и уединения",
        "свет": "Глубина, размышление, знание",
        "тень": "Замкнутость, изоляция",
        "задача": "Открывайся миру, делись мудростью",
        "рекомендации": "Начни делиться знаниями — напиши пост или выступи с мини-лекцией"
    },
    9: {
        "название": "Путь Служителя",
        "описание": "Энергия гуманизма, сострадания, завершения",
        "свет": "Щедрость, зрелость, эмпатия",
        "тень": "Жертвенность, усталость от миссии",
        "задача": "Уважай свои границы, не растворяйся в других",
        "рекомендации": "Оцени, кому ты отдаёшь слишком много, и восстанови баланс энергии"
    },
    22: {
        "название": "Архитектор нового мира",
        "описание": "Масштабное созидание, глобальные идеи",
        "свет": "Мастерство, организатор больших систем",
        "тень": "Страх провала, выгорание",
        "задача": "Действуй пошагово, доверяй внутренней опоре",
        "рекомендации": "Сконцентрируйся на одном важном проекте и выстраивай чёткий план"
    },
    33: {
        "название": "Учитель Учителей",
        "описание": "Безусловная любовь, служение человечеству",
        "свет": "Сострадание, целительство, вдохновение",
        "тень": "Спасательство, самопожертвование, выгорание",
        "задача": "Создавай границы, чтобы сохранить энергию",
        "рекомендации": "Развивай практики восстановления энергии и осознанного взаимодействия"
    }
}

def calculate_matrix(day, month, year):
    def reduce(n):
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(d) for d in str(n))
        return n

    d = sum(int(i) for i in str(day))
    m = sum(int(i) for i in str(month))
    y = sum(int(i) for i in str(year))

    soul_code = reduce(d + m + y)
    karma_tail = reduce(d + m)
    life_path = reduce(soul_code + karma_tail)
    gift = reduce(d + y)
    body_code = reduce(m)
    birth_year_code = reduce(y)
    soul_gate = reduce(abs(soul_code - karma_tail))
    abundance_code = reduce(gift + body_code)
    incarnation_memory = reduce(birth_year_code + karma_tail)
    realization_code = reduce(life_path + gift)
    love_code = reduce(karma_tail + body_code)
    spirit_code = reduce(life_path + birth_year_code)

    return {
        "Число Жизненного Пути": life_path,
        "Число Души": soul_code,
        "Число Кармы": karma_tail,
        "Дар / Потенциал": gift,
        "Код Тела / Реализации": body_code,
        "Энергия года рождения": birth_year_code,
        "Врата Души": soul_gate,
        "Код Изобилия": abundance_code,
        "Инкарнационная память": incarnation_memory,
        "Канал Реализации": realization_code,
        "Канал Любви": love_code,
        "Канал Духа": spirit_code
    }

# 🎯 Психологический портрет на основе матрицы

def render_psychological_portrait(energies):
    st.subheader("🎯 Психологический портрет")
    counts = Counter(energies)

    # Повторы
    repeated = [f"Число {k} ({v} раз) — {ARCHETYPES[k]['название']}" for k, v in counts.items() if v > 1]
    if repeated:
        st.markdown("**Повторяющиеся энергии:**")
        for line in repeated:
            st.markdown(f"- {line}")

    # Мастер-энергии
    master_numbers = [k for k in energies if k in [11, 22, 33]]
    if master_numbers:
        st.markdown("**Мастер-энергии в матрице:**")
        for m in set(master_numbers):
            st.markdown(f"- {m} — {ARCHETYPES[m]['название']}")

    # Внутренние конфликты
    if 1 in energies and 33 in energies:
        st.markdown("**Внутренний конфликт:** Служение (33) ↔ Самость (1). Научиться сочетать помощь другим с проявлением себя.")

    # Обобщённый портрет
    if counts:
        dominant = counts.most_common(1)[0][0]
        archetype = ARCHETYPES.get(dominant)
        if archetype:
            st.markdown("**Обобщённый портрет:**")
            st.markdown(f"Выраженная энергия: **{dominant} — {archetype['название']}**")
            st.markdown(f"Суть: {archetype['описание']}")
            st.markdown(f"Ключевой вектор развития: {archetype['задача']}")
            st.markdown(f"Поддержка: {archetype['рекомендации']}")

    st.markdown("\n---\n")

# 💫 Вызов расчёта и отображения
st.title("🔢 Калькулятор чисел судьбы")
day = st.number_input("День", min_value=1, max_value=31, value=1)
month = st.number_input("Месяц", min_value=1, max_value=12, value=1)
year = st.number_input("Год", min_value=1900, max_value=2100, value=1984)

if st.button("Рассчитать"):
    result = calculate_matrix(day, month, year)
    for название, значение in result.items():
        if значение in ARCHETYPES:
            archetype = ARCHETYPES[значение]
            st.markdown(f"### 🔹 {название}: {значение} — {archetype['название']}")
            st.markdown(f"**Суть:** {archetype['описание']}")
            st.markdown(f"**Свет:** {archetype['свет']}")
            st.markdown(f"**Тень:** {archetype['тень']}")
            st.markdown(f"**Задача:** {archetype['задача']}")
            st.markdown(f"**Рекомендации:** {archetype['рекомендации']}")
            st.markdown("\n")
        else:
            st.markdown(f"### 🔹 {название}: {значение}")
            st.markdown("Описание отсутствует\n")

    energies = list(result.values())
    render_psychological_portrait(energies)
