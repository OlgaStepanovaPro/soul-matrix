# Матрица Души: калькулятор по дате рождения с веб-интерфейсом Streamlit

import streamlit as st

# Архетипические описания для чисел
ARCHETYPES = {
    1: "Лидер, воля, инициатива. Архетип: Воин, Маг, Прометей.",
    2: "Партнёрство, чувствительность. Архетип: Дипломат, Лунная Жрица.",
    3: "Творчество, самовыражение. Архетип: Артист, Ребёнок, Муза.",
    4: "Стабильность, структура. Архетип: Архитектор, Хранитель, Строитель.",
    5: "Свобода, путешествия, перемены. Архетип: Искатель, Одиссей.",
    6: "Забота, любовь, семья. Архетип: Хранительница очага, Деметра.",
    7: "Мудрость, анализ, отшельничество. Архетип: Мудрец, Отшельник.",
    8: "Сила, власть, материальный успех. Архетип: Управленец, Судья.",
    9: "Служение, сострадание, завершение. Архетип: Миссионер, Старец.",
    11: "Интуиция, вдохновение, пророчество. Архетип: Пророк, Проводник Света.",
    22: "Созидание мирового масштаба. Архетип: Архитектор новой Земли, Моисей.",
    33: "Божественное служение, любовь к человечеству. Архетип: Учитель Учителей."
}

def reduce_number(n):
    """
    Сокращает число до однозначного или мастер-числа (11, 22, 33)
    """
    while n not in [11, 22, 33] and n > 9:
        n = sum(int(d) for d in str(n))
    return n

def calculate_matrix(day, month, year):
    # Базовые суммы
    d = sum(int(i) for i in str(day))
    m = sum(int(i) for i in str(month))
    y = sum(int(i) for i in str(year))

    # Базовые коды
    soul_code = reduce_number(d + m + y)
    karma_tail = reduce_number(d + m)
    life_path = reduce_number(soul_code + karma_tail)
    gift = reduce_number(d)
    body_code = reduce_number(m)
    birth_year_code = reduce_number(y)

    # Дополнительные позиции
    soul_gate = reduce_number(abs(soul_code - karma_tail))
    abundance_code = reduce_number(gift + body_code)
    incarnation_memory = reduce_number(birth_year_code + karma_tail)
    realization_code = reduce_number(life_path + gift)
    love_code = reduce_number(karma_tail + body_code)
    spirit_code = reduce_number(life_path + birth_year_code)

    return {
        "Код Души": soul_code,
        "Кармический хвост": karma_tail,
        "Путь Души": life_path,
        "Дар/Потенциал": gift,
        "Код тела/реализация": body_code,
        "Энергия года рождения": birth_year_code,
        "Врата Души": soul_gate,
        "Код Изобилия": abundance_code,
        "Инкарнационная память": incarnation_memory,
        "Канал реализации": realization_code,
        "Канал любви": love_code,
        "Канал духа": spirit_code
    }

# Streamlit-интерфейс
st.set_page_config(page_title="Матрица Души", page_icon="🌀")
st.title("🌀 Калькулятор Матрицы Души")
st.markdown("Введите дату рождения, чтобы рассчитать вашу матрицу")

col1, col2, col3 = st.columns(3)
with col1:
    day = st.number_input("День", min_value=1, max_value=31, value=1)
with col2:
    month = st.number_input("Месяц", min_value=1, max_value=12, value=1)
with col3:
    year = st.number_input("Год", min_value=1900, max_value=2100, value=1984)

if st.button("Рассчитать матрицу"):
    result = calculate_matrix(day, month, year)
    st.subheader("✨ Результаты:")
    for k, v in result.items():
        archetype = ARCHETYPES.get(v, "Нет описания")
        st.markdown(f"**{k}**: {v}  ")
        st.markdown(f"*{archetype}*")
