import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import datetime
import time

# --- ИНИЦИАЛИЗАЦИЯ ---
st.set_page_config(page_title="D.MAX | CLOUD TERMINAL", page_icon="💠", layout="wide")

# Подключение к Google Таблицам
conn = st.connection("gsheets", type=GSheetsConnection)

# --- ПРЕМИУМ ДИЗАЙН (КАРБОН + ТЕМНОЕ СТЕКЛО) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Roboto+Mono&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1a1a, #000000);
        background-image: repeating-linear-gradient(45deg, #111 0px, #111 2px, #0a0a0a 2px, #0a0a0a 10px);
        color: #f0f0f0;
    }

    .glass-card {
        background: rgba(20, 20, 20, 0.7);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.8);
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        text-align: center;
        background: linear-gradient(180deg, #fff, #555);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 12px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #ff3c00, #a30000) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif !important;
        height: 65px;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 900 !important;
        letter-spacing: 3px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ГЛАВНЫЙ ЭКРАН ---
st.markdown('<p class="hero-title">D.MAX</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00e5ff; font-family:Orbitron;">CLOUD PILOT REGISTRY // VER 2.6</p>', unsafe_allow_html=True)

col_info, col_form = st.columns([1, 1.2], gap="large")

with col_info:
    st.markdown("""
    <div class="glass-card">
        <h3 style="font-family:Orbitron; color:#ff3c00;">ALPHA-GROUP TESTERS</h3>
        <p>Первые 10 пилотов, прошедших верификацию, получают пожизненный статус <b>PLATINUM FOUNDER</b>.</p>
        <hr style="opacity:0.1">
        <p><b>Что это дает:</b></p>
        <ul style="color:#aaa; font-size:0.9rem;">
            <li>Уникальный "хромированный" интерфейс в приложении.</li>
            <li>Отсутствие абонентской платы навсегда.</li>
            <li>Прямой доступ к разработчикам (Максу).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    with st.form("google_form"):
        st.markdown("<h3 style='text-align:center; font-family:Orbitron;'>АНКЕТА ПИЛОТА</h3>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("ИМЯ")
            phone = st.text_input("ТЕЛЕФОН")
        with c2:
            surname = st.text_input("ФАМИЛИЯ")
            email = st.text_input("EMAIL")
            
        board_id = st.text_input("ЖЕЛАЕМЫЙ ID (001-999)", placeholder="777")
        tier = st.selectbox("ПАКЕТ", ["TITAN (Pre-order)", "HEAVY (Pro)", "STANDARD"])
        
        if st.form_submit_button("ОТПРАВИТЬ ДАННЫЕ В СИСТЕМУ"):
            if name and email and phone:
                try:
                    # Читаем текущие данные из Google Sheets
                    existing_data = conn.read(worksheet="Sheet1", usecols=list(range(8)), ttl=0)
                    
                    # Создаем новую строку
                    new_entry = pd.DataFrame([{
                        "Дата": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
                        "Имя": name,
                        "Фамилия": surname,
                        "Телефон": phone,
                        "Email": email,
                        "Борт-номер": board_id,
                        "Пакет": tier,
                        "Статус": "В ОЖИДАНИИ" # По умолчанию
                    }])
                    
                    # Соединяем и записываем обратно
                    updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
                    conn.update(worksheet="Sheet1", data=updated_data)
                    
                    st.success("ДАННЫЕ ЗАПИСАНЫ В ОБЛАКО. ВЫ В СПИСКЕ!")
                    st.balloons()
                except Exception as e:
                    st.error(f"ОШИБКА ПОДКЛЮЧЕНИЯ: {e}")
            else:
                st.warning("ЗАПОЛНИТЕ ВСЕ ПОЛЯ")

# --- АДМИНКА ---
st.write("\n" * 10)
with st.expander("🔐 КЕРНЕЛ-ДОСТУП (Для тебя)"):
    if st.text_input("Password", type="password") == "max_vip":
        data = conn.read(worksheet="Sheet1", ttl=0)
        st.write("### ЖИВОЙ СПИСОК ПИЛОТОВ")
        st.dataframe(data)
