import streamlit as st
from collections import Counter

# Архетипические описания для чисел
ARCHETYPES = {
    ... # (содержимое ARCHETYPES остаётся без изменений)
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
if 'calculate_matrix' in globals():
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
else:
    st.warning("Функция calculate_matrix() не определена. Пожалуйста, добавьте её для выполнения расчётов.")
