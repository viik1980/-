import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- СИСТЕМНАЯ КОНФИГУРАЦИЯ ---
st.set_page_config(page_title="MAX | NEURAL NEXUS", page_icon="🧠", layout="wide")
DB_FILE = "max_titan_registry.csv"

# --- ДИЗАЙН "NEON FUTURE" (CYAN, PURPLE, CARBON, DIFFUSION) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* --- ГЛОБАЛЬНЫЙ ФОН --- */
    .stApp {
        background-color: #020205;
        background-image: 
            radial-gradient(circle at 50% 30%, rgba(189, 0, 255, 0.15), rgba(0, 242, 255, 0.05), transparent 70%),
            repeating-linear-gradient(45deg, #0a0a0a 0px, #0a0a0a 2px, #050505 2px, #050505 8px);
        color: #e0e0e0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* --- ЛОГОТИП И ЭФФЕКТ РАССЕИВАНИЯ СВЕТА --- */
    .logo-container {
        display: flex;
        justify-content: center;
        filter: drop-shadow(0 0 25px rgba(0, 242, 255, 0.6)) drop-shadow(0 0 45px rgba(189, 0, 255, 0.3));
        margin-bottom: 20px;
        animation: pulse 4s ease-in-out infinite alternate;
    }
    
    @keyframes pulse {
        from { filter: drop-shadow(0 0 20px rgba(0, 242, 255, 0.4)); }
        to { filter: drop-shadow(0 0 40px rgba(189, 0, 255, 0.6)); }
    }

    /* --- ЭФФЕКТЫ СТЕКЛА (DARK GLASS) --- */
    .neon-card {
        background: rgba(10, 10, 15, 0.7);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 40px;
        margin: 25px 0;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 
            0 0 30px rgba(0, 242, 255, 0.1),
            inset 0 0 30px rgba(189, 0, 255, 0.05);
        transition: 0.4s ease;
    }
    .neon-card:hover {
        border-color: rgba(0, 242, 255, 0.5);
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.3), inset 0 0 50px rgba(189, 0, 255, 0.1);
        transform: translateY(-5px);
    }

    .gradient-text {
        background: linear-gradient(to right, #bd00ff, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        filter: drop-shadow(0 0 10px rgba(189, 0, 255, 0.3));
        font-family: 'Orbitron', sans-serif;
    }

    /* --- ФОРМА --- */
    .stForm {
        background: rgba(5, 5, 10, 0.85) !important;
        backdrop-filter: blur(30px) !important;
        border: 2px solid #bd00ff !important;
        border-radius: 30px !important;
        padding: 50px !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #bd00ff, #00f2ff) !important;
        color: #000 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 1.4rem !important;
        height: 75px;
        border: none !important;
        border-radius: 10px !important;
        letter-spacing: 5px !important;
        box-shadow: 0 0 40px rgba(189, 0, 255, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ЛОГИКА СОХРАНЕНИЯ ---
def save_pilot(fname, lname, phone, email, board, tier):
    new_data = pd.DataFrame([[
        datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        fname, lname, phone, email, board, tier
    ]], columns=['Time', 'Name', 'Surname', 'Phone', 'Email', 'ID', 'Tier'])
    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- HERO SECTION С ЛОГОТИПОМ ПО ССЫЛКЕ ---
st.write("\n")
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    # Твоя ссылка вставлена сюда:
    logo_url = "https://i.postimg.cc/CKZCdVHW/logo.png"
    st.markdown(f"""
        <div class="logo-container">
            <img src="{logo_url}" style="width: 100%;">
        </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 style="text-align:center; font-size: 2.5rem; margin-top: -10px;"><span class="gradient-text">D.MAX: ТВОЙ ЦИФРОВОЙ ШТУРМАН</span></h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#aaa; letter-spacing: 5px; font-family:Orbitron;">МЫ СОЗДАЕМ БУДУЩЕЕ ДОРОЖНОЙ СТРАТЕГИИ</p>', unsafe_allow_html=True)

st.write("\n" * 4)

# --- МОДУЛИ ---
st.markdown('<h2 style="text-align:center; font-family:Orbitron;">// ТАКТИЧЕСКИЕ СИСТЕМЫ</h2>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#00f2ff;">🧠 НЕЙРОСЕТЕВОЙ ТАХОГРАФ</h3>
        <p style="font-size:1.1rem; color:#ccc;">
        Макс видит будущее твоего маршрута. Он рассчитывает график, учитывая Пакет Мобильности и твою усталость. 
        Он скажет голосом: <i>"Дотянешь или лучше стать раньше"</i>. Это твоя страховка от штрафов и переутомления.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#bd00ff;">⚖️ ЦИФРОВОЙ ЮРИСТ</h3>
        <p style="font-size:1.1rem; color:#ccc;">
        При проверке в любой стране Макс общается с инспекторами на их языке. Он защитит тебя от незаконных штрафов, 
        оперируя точными данными и законами ЕС в реальном времени.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#00f2ff;">🎙️ ГОЛОСОВОЙ ПЕРЕВОДЧИК</h3>
        <p style="font-size:1.1rem; color:#ccc;">
        Вкратце опиши Максу суть проблемы, и он сам решит вопрос с такси, загрузкой или сервисом на местном языке. 
        Макс — это твой голос, который звучит уверенно в любой точке мира.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#bd00ff;">💤 АНТИ-ЗОМБИ РЕЖИМ</h3>
        <p style="font-size:1.1rem; color:#ccc;">
        Макс подстраивает график под твои биоритмы. Он рассчитает коэффициент усталости и предложит идеальное окно для сна, 
        чтобы ты всегда был в форме и не ехал на пределе.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- ФОРМА ---
st.write("\n" * 5)
_, col_form_center, _ = st.columns([1, 2, 1])
with col_form_center:
    with st.form("titan_id_terminal"):
        st.markdown("<h3 style='text-align:center; color:#00f2ff; font-family:Orbitron;'>ИНИЦИАЛИЗАЦИЯ ПИЛОТА</h3>", unsafe_allow_html=True)
        c_n, c_s = st.columns(2)
        with c_n:
            name = st.text_input("ИМЯ")
            phone = st.text_input("ТЕЛЕФОН")
        with c_s:
            surname = st.text_input("ФАМИЛИЯ")
            email = st.text_input("E-MAIL")
        st.write("---")
        board_id = st.text_input("ЖЕЛАЕМЫЙ ID БОРТА (3 цифры)", placeholder="777")
        if st.form_submit_button("АКТИВИРОВАТЬ СИСТЕМУ ››"):
            if name and email and board_id:
                save_pilot(name, surname, phone, email, board_id, "ALPHA")
                st.success(f"ПРОТОКОЛ ПРИНЯТ. ДОБРО ПОЖАЛОВАТЬ В БУДУЩЕЕ, БОРТ {board_id}!")
                st.balloons()
