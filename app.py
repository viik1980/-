import streamlit as st
import pandas as pd
import datetime
import os

# --- ИНИЦИАЛИЗАЦИЯ И СТИЛЬ ---
st.set_page_config(page_title="MAX | OPERATION CENTER", page_icon="🚨", layout="wide")

DB_FILE = "max_leads_2026.csv"

# Кастомный CSS для создания "дорогого" интерфейса
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1a1a, #000000);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Стилизация заголовков */
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(180deg, #ff4b4b 0%, #440000 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 50px;
    }

    /* Карточки функционала */
    .feature-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 75, 75, 0.3);
        padding: 30px;
        border-radius: 15px;
        height: 250px;
        transition: 0.3s;
    }
    .feature-card:hover {
        background: rgba(255, 75, 75, 0.05);
        border-color: #ff4b4b;
        transform: translateY(-5px);
    }

    /* Форма */
    .stForm {
        background: rgba(0, 0, 0, 0.5);
        border: 2px solid #222;
        padding: 40px;
        border-radius: 20px;
    }

    /* Кнопка */
    .stButton>button {
        background: #ff4b4b !important;
        color: black !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
        height: 60px;
        border: none !important;
        transition: 0.5s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 40px #ff4b4b;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ЛОГИКА СОХРАНЕНИЯ ---
def save_lead(fname, lname, phone, email, board, tier):
    new_data = pd.DataFrame([[
        datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        fname, lname, phone, email, board, tier
    ]], columns=['Дата', 'Имя', 'Фамилия', 'Телефон', 'Email', 'Борт-номер', 'Пакет'])
    
    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- КОНТЕНТ САЙТА ---

# 1. HERO SECTION
st.markdown('<p class="hero-title">DEЖУРНЫЙ MAX</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">ТВОЯ ПЕРСОНАЛЬНАЯ СИСТЕМА УПРАВЛЕНИЯ ДОРОГОЙ</p>', unsafe_allow_html=True)

# 2. ОПИСАНИЕ ФУНКЦИОНАЛА (ТРИ ГЛАВНЫХ МОДУЛЯ)
st.write("### [ МОДУЛИ СИСТЕМЫ ]")
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("""<div class="feature-card">
        <h3 style='color:#ff4b4b;'>🛡️ ANTI-SHF</h3>
        <p style='color:#bbb;'>Интеллектуальный контроль РТО. Больше никаких штрафов. Система сама рассчитывает время отдыха, учитывая специфику твоих маршрутов.</p>
    </div>""", unsafe_allow_html=True)

with col_f2:
    st.markdown("""<div class="feature-card">
        <h3 style='color:#ff4b4b;'>🍳 ROAD CHEF</h3>
        <p style='color:#bbb;'>Эксклюзивная база рецептов для кабины. Готовь быстро, вкусно и полезно из того, что есть под рукой. Твой желудок скажет спасибо.</p>
    </div>""", unsafe_allow_html=True)

with col_f3:
    st.markdown("""<div class="feature-card">
        <h3 style='color:#ff4b4b;'>📍 HUB FINDER</h3>
        <p style='color:#bbb;'>Доступ к проверенным точкам: лучшие стоянки, души, прачечные и сервисы, подтвержденные закрытым сообществом.</p>
    </div>""", unsafe_allow_html=True)

st.write("\n" * 5)
st.divider()

# 3. БЛОК ПРЕДЗАКАЗА
st.write("### [ ЦЕНТР РЕГИСТРАЦИИ ЭКИПАЖА ]")
col_text, col_form = st.columns([1, 1.5], gap="large")

with col_text:
    st.write("\n" * 2)
    st.markdown("""
    ### ПОЧЕМУ ТЫ ЗДЕСЬ?
    Ты не просто водитель. Ты — оператор сложной машины. Ты заслуживаешь инструменты, которые работают так же четко, как твой двигатель.
    
    **Что дает предзаказ:**
    1. **Статус TITAN:** Твой номер (например, MAX-077) навсегда в базе.
    2. **Фикс цены:** Стоимость для тебя не изменится после релиза.
    3. **Доступ к бета-тесту:** Попробуй функции раньше всех.
    """)
    st.image("https://images.unsplash.com/photo-1519003722824-194d4455a60c?q=80&w=1000&auto=format&fit=crop", caption="Max Project Concept 2026")

with col_form:
    with st.form("main_form"):
        c1, c2 = st.columns(2)
        with c1:
            first_name = st.text_input("ИМЯ")
            phone = st.text_input("ТЕЛЕФОН")
        with c2:
            last_name = st.text_input("ФАМИЛИЯ")
            email = st.text_input("EMAIL")
            
        st.write("---")
        c3, c4 = st.columns([1, 2])
        with c3:
            board_num = st.text_input("БОРТ №", placeholder="001")
        with c4:
            tier = st.selectbox("КОМПЛЕКТАЦИЯ", ["TITAN (Founder Edition)", "HEAVY (Premium)", "STANDARD"])
            
        st.write("\n")
        submit = st.form_submit_button("ЗАРЕГИСТРИРОВАТЬСЯ В СИСТЕМЕ")
        
        if submit:
            if first_name and email and phone and board_num:
                save_lead(first_name, last_name, phone, email, board_num, tier)
                st.success("ПРОТОКОЛ ПРИНЯТ. ТЫ В СПИСКЕ ПИЛОТОВ!")
                st.balloons()
            else:
                st.error("ЗАПОЛНИ ВСЕ ПОЛЯ ДАННЫХ")

# --- ADMIN PANEL ---
st.write("\n" * 15)
with st.expander("🔐 АРХИТЕКТОР (Вход по ключу)"):
    pwd = st.text_input("Пароль", type="password")
    if pwd == "max_vip":
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.write("### БАЗА ПРЕДЗАКАЗОВ")
            st.dataframe(df)
            st.download_button("СКАЧАТЬ В EXCEL (CSV)", df.to_csv(index=False).encode('utf-8'), "leads.csv")
        else:
            st.warning("База пуста")
