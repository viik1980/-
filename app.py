import streamlit as st
import pandas as pd
import datetime
import os

# --- КОНФИГУРАЦИЯ СТРАНИЦЫ ---
st.set_page_config(page_title="MAX | ПРЕДЗАКАЗ", page_icon="🔗", layout="wide")

DB_FILE = "max_preorders.csv"

# --- СТИЛИЗАЦИЯ (КИБЕР-ИНДУСТРИАЛ) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto+Mono:wght@300;500&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #121212, #000000);
        color: #e0e0e0;
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .main-title {
        text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #444444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        margin-bottom: 0;
    }

    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #1a1a1a !important;
        color: #ff4b4b !important;
        border: 1px solid #333 !important;
        font-family: 'Roboto Mono', monospace;
    }

    .stButton>button {
        background: transparent;
        color: #ff4b4b;
        border: 2px solid #ff4b4b;
        border-radius: 0px;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        padding: 20px;
        transition: 0.4s;
    }

    .stButton>button:hover {
        background: #ff4b4b;
        color: black;
        box-shadow: 0 0 30px #ff4b4b;
    }

    .info-panel {
        background: rgba(255, 255, 255, 0.02);
        border-left: 4px solid #ff4b4b;
        padding: 25px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ЛОГИКА ХРАНЕНИЯ ---
def save_data(fname, lname, phone, email, board, tier):
    new_entry = pd.DataFrame([[
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        fname, lname, phone, email, board, tier
    ]], columns=['Дата', 'Имя', 'Фамилия', 'Телефон', 'Email', 'Борт-номер', 'Комплектация'])
    
    if not os.path.isfile(DB_FILE):
        new_entry.to_csv(DB_FILE, index=False)
    else:
        new_entry.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- ИНТЕРФЕЙС ---
st.markdown('<p class="main-title">DEЖУРНЫЙ MAX</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-family: Roboto Mono;'>SYSTEM ACCESS: PRE-ORDER OPEN</p>", unsafe_allow_html=True)

st.write("---")

col_info, col_form = st.columns([1, 1.2], gap="large")

with col_info:
    st.markdown("""
    <div class="info-panel">
        <h3 style="color: #ff4b4b;">ЛИМИТИРОВАННАЯ СЕРИЯ</h3>
        <p>Вы находитесь на этапе бронирования цифровых мощностей проекта.</p>
        <p><b>Каждый борт получает:</b></p>
        <ul>
            <li>Уникальный позывной в радиоэфире системы</li>
            <li>Приоритет при расчете маршрутов</li>
            <li>Доступ к закрытому модулю "Шеф-повар в дороге"</li>
        </ul>
        <p style="font-size: 0.8rem; color: #555;">* Данные защищены протоколом шифрования.</p>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    with st.form("main_form", clear_on_submit=True):
        st.write("### АНКЕТА ПИЛОТА")
        
        c1, c2 = st.columns(2)
        with c1:
            first_name = st.text_input("ИМЯ")
        with c2:
            last_name = st.text_input("ФАМИЛИЯ")
            
        phone = st.text_input("НОМЕР ТЕЛЕФОНА", placeholder="+7 (___) ___-__-__")
        email = st.text_input("EMAIL")
        
        st.write("---")
        c3, c4 = st.columns([1, 2])
        with c3:
            board_num = st.text_input("НОМЕР БОРТА", placeholder="001")
        with c4:
            tier = st.selectbox("КОМПЛЕКТАЦИЯ", ["TITAN (VIP Владение)", "HEAVY (PRO Доступ)", "STANDARD (База)"])
        
        submit = st.form_submit_button("ЗАРЕГИСТРИРОВАТЬ В СИСТЕМЕ")
        
        if submit:
            if not (first_name and last_name and phone and email and board_num):
                st.error("ВСЕ ПОЛЯ ДОЛЖНЫ БЫТЬ ЗАПОЛНЕНЫ ДЛЯ ГЕНЕРАЦИИ КЛЮЧА")
            else:
                with st.spinner("Синхронизация с сервером..."):
                    save_data(first_name, last_name, phone, email, board_num, tier)
                    st.success(f"Борт MAX-{board_num} закреплен за экипажем {first_name} {last_name}!")
                    st.balloons()

# --- ПАНЕЛЬ АРХИТЕКТОРА (ДЛЯ ТЕБЯ) ---
st.write("\n" * 15)
with st.expander("🔐 ВХОД ДЛЯ АРХИТЕКТОРОВ"):
    adm_pass = st.text_input("Ключ доступа", type="password")
    if adm_pass == "max_vip": # Твой пароль
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.write("### РЕЕСТР ПРЕДЗАКАЗОВ")
            st.dataframe(df.style.highlight_max(axis=0, color='#1f1f1f'))
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("ЭКСПОРТ БАЗЫ (CSV)", data=csv, file_name="max_preorders.csv", mime="text/csv")
        else:
            st.info("Бортовой журнал пуст.")
