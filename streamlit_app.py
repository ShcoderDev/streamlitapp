import streamlit as st

# Заголовок приложения
st.title("Калькулятор с большими кнопками")

# Инициализация состояния для хранения текущего выражения
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Функция для обновления выражения
def update_expression(value):
    st.session_state.expression += value

# Функция для вычисления результата
def calculate():
    try:
        # Вычисляем результат с помощью встроенной функции eval
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except Exception as e:
        st.session_state.expression = "Ошибка"


# Функция для очистки выражения
def clear_expression():
    st.session_state.expression = ""

# Поле ввода для отображения выражения
st.text_input("Выражение", value=st.session_state.expression, key="expression_display", disabled=True)

# CSS для увеличения размера кнопок
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Создаем сетку для кнопок
col1, col2, col3, col4 = st.columns(4)

# Первый столбец
with col1:
    st.button("7", on_click=update_expression, args=("7",))
    st.button("4", on_click=update_expression, args=("4",))
    st.button("1", on_click=update_expression, args=("1",))
    st.button("C", on_click=clear_expression)

# Второй столбец
with col2:
    st.button("8", on_click=update_expression, args=("8",))
    st.button("5", on_click=update_expression, args=("5",))
    st.button("2", on_click=update_expression, args=("2",))
    st.button("0", on_click=update_expression, args=("0",))

# Третий столбец
with col3:
    st.button("9", on_click=update_expression, args=("9",))
    st.button("6", on_click=update_expression, args=("6",))
    st.button("3", on_click=update_expression, args=("3",))
    st.button(".", on_click=update_expression, args=(".",))

# Четвертый столбец
with col4:
    st.button("÷", on_click=update_expression, args=("/",))  # Используем символ ÷ вместо /
    st.button("×", on_click=update_expression, args=("*",))  # Используем символ × вместо *
    st.button("--", on_click=update_expression, args=("-",))
    st.button("++", on_click=update_expression, args=("+",))

# Кнопка "=" (занимает всю ширину)
st.button("=", on_click=calculate)