import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- СИСТЕМНАЯ КОНФИГУРАЦИЯ ---
st.set_page_config(page_title="MAX | OPERATION CENTER", page_icon="💠", layout="wide")
DB_FILE = "max_titan_registry.csv"

# --- ДИЗАЙН "FUTURE COCKPIT" (CARBON, NEON, DEPTH) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');
    
    /* ФОН: Глубокий карбон с динамической сеткой */
    .stApp {
        background-color: #050505;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(0, 242, 255, 0.05), transparent),
            linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.95)),
            repeating-linear-gradient(45deg, #111 0px, #111 2px, #0a0a0a 2px, #0a0a0a 10px);
        color: #f0f0f0;
        font-family: 'Roboto Mono', monospace;
    }

    /* ЭФФЕКТ СВЕЧЕНИЯ И ГЛУБИНЫ ДЛЯ ПАНЕЛЕЙ */
    .glass-panel {
        background: rgba(20, 20, 20, 0.8);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 20px;
        padding: 35px;
        margin: 20px 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 0 20px rgba(0, 242, 255, 0.05);
        transition: 0.4s ease;
    }
    .glass-panel:hover {
        border-color: #FF4D00;
        box-shadow: 0 0 30px rgba(255, 77, 0, 0.2), inset 0 0 30px rgba(255, 77, 0, 0.05);
        transform: translateY(-5px);
    }

    /* ЗАГОЛОВОК С ЭФФЕКТОМ ПОДСВЕТКИ */
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 7rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(180deg, #fff 0%, #444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 20px;
        margin-bottom: 10px;
        filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.3));
    }

    .neon-text {
        color: #00F2FF;
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.7);
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 5px;
    }

    /* ИННОВАЦИОННЫЙ БЛОК (АКЦЕНТ) */
    .highlight-box {
        background: linear-gradient(135deg, rgba(255, 77, 0, 0.1), transparent);
        border-left: 5px solid #FF4D00;
        padding: 20px;
        margin: 20px 0;
        border-radius: 0 15px 15px 0;
    }

    /* КНОПКА ЗАПУСКА */
    .stButton>button {
        background: linear-gradient(45deg, #FF4D00, #960000) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif !important;
        height: 80px;
        width: 100%;
        font-weight: 900 !important;
        letter-spacing: 5px !important;
        border: none !important;
        border-radius: 0px !important;
        clip-path: polygon(5% 0, 100% 0, 95% 100%, 0 100%);
        box-shadow: 0 10px 40px rgba(255, 77, 0, 0.4) !important;
        transition: 0.5s !important;
    }
    .stButton>button:hover {
        box-shadow: 0 0 60px #FF4D00 !important;
        transform: scale(1.02);
    }

    hr { border-color: #333; opacity: 0.2; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="hero-title">MAX</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;" class="neon-text">WELCOME TO THE NEW WORLD // PHASE: TITAN</p>', unsafe_allow_html=True)

st.write("\n" * 4)

# --- UNIT 01: THE CORE ALGORITHM ---
st.markdown('<h2 style="font-family:Orbitron; border-bottom: 1px solid #333; padding-bottom:10px;">[ UNIT 01: ТЕМПОРАЛЬНЫЙ ИНТЕЛЛЕКТ ]</h2>', unsafe_allow_html=True)

col_algo, col_viz = st.columns([1.5, 1])

with col_algo:
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color:#FF4D00; font-family:Orbitron;">АЛГОРИТМ "CHRONOS"</h3>
        <p style="font-size:1.1rem; line-height:1.8; color:#ccc;">
        Это не калькулятор топлива. Это <b>Предиктивный Штурман</b>. Введи километраж, среднюю скорость и рабочие окна — Макс развернет перед тобой 
        временную карту твоего будущего. Он учитывает <b>Пакет Мобильности</b> и РТО, выстраивая график так, чтобы ты знал: когда спать, 
        где нажать на газ и успеешь ли ты к цели.
        </p>
        <div class="highlight-box">
            <span style="color:#fff; font-weight:bold;">ВИДЕНИЕ В БУДУЩЕЕ:</span> 
            Система рассчитывает компенсации и паузы за тебя, предсказывая твой статус на 48 часов вперед.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_viz:
    st.markdown("""
    <div class="glass-panel" style="text-align:center;">
        <p style="color:#00F2FF; font-family:Orbitron; font-size:0.8rem;">ENGINE STATUS: ACTIVE</p>
        <div style="border: 1px solid #00F2FF; height: 150px; border-radius:10px; display:flex; align-items:center; justify-content:center;">
            <p style="color:#555; font-size:0.7rem;">[ ГРАФИК ПРОЕКЦИИ РТО - ВИЗУАЛИЗАЦИЯ ]</p>
        </div>
        <p style="color:#666; font-size:0.7rem; margin-top:15px;">Макс видит твою усталость еще до того, как ты ее почувствовал.</p>
    </div>
    """, unsafe_allow_html=True)

# --- UNIT 02: SAFETY & BIORHYTHMS ---
st.write("\n" * 2)
st.markdown('<h2 style="font-family:Orbitron; border-bottom: 1px solid #333; padding-bottom:10px;">[ UNIT 02: БИОРИТМИЧЕСКИЙ ЩИТ ]</h2>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color:#00F2FF; font-family:Orbitron;">РЕЖИМ "АНТИ-ЗОМБИ"</h3>
        <p style="color:#aaa;">Ненавидишь ночную езду? Макс перестроит реальность. Система адаптирует график под твои биоритмы. Коэффициент усталости рассчитает идеальное окно: 3 часа сна ночью для рывка, а затем полноценные 9 часов отдыха.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color:#00F2FF; font-family:Orbitron;">ЯЗЫКОВОЙ АГРЕССОР</h3>
        <p style="color:#aaa;">Макс — твой голос в чужой стране. Опиши суть в двух словах, и Макс сам решит вопрос с такси, загрузкой или полицией на языке той страны, где ты находишься. Ты больше не иностранец. Ты — Владелец Дороги.</p>
    </div>
    """, unsafe_allow_html=True)

# --- UNIT 03: REGISTRATION ---
st.write("\n" * 4)
st.markdown('<p style="text-align:center; font-family:Orbitron; font-size:2rem; letter-spacing:10px; color:#fff;">ИНИЦИАЛИЗАЦИЯ ТИТАНА</p>', unsafe_allow_html=True)

_, col_form_center, _ = st.columns([1, 2, 1])

with col_form_center:
    with st.form("titan_id_terminal"):
        st.markdown("<p style='text-align:center; color:#555;'>ВХОД В НОВЫЙ МИР</p>", unsafe_allow_html=True)
        
        c_n, c_s = st.columns(2)
        with c_n:
            name = st.text_input("NAME // ИМЯ")
            phone = st.text_input("PHONE // ТЕЛЕФОН")
        with c_s:
            surname = st.text_input("SURNAME // ФАМИЛИЯ")
            email = st.text_input("MAIL // ПОЧТА")
            
        st.write("---")
        board_id = st.text_input("ID БОРТА (001-999)", placeholder="Напр. 007")
        tier = st.selectbox("CLASS", ["PLATINUM FOUNDER (Alpha Group)", "TITAN (Pre-order)", "HEAVY (Pro)"])
        
        if st.form_submit_button("ЗАПУСТИТЬ ДВИГАТЕЛЬ СИСТЕМЫ"):
            if name and email and board_id:
                with st.spinner("СИНХРОНИЗАЦИЯ ТЕЛЕМЕТРИИ..."):
                    time.sleep(2)
                st.success(f"ПРОТОКОЛ АКТИВИРОВАН. ДОБРО ПОЖАЛОВАТЬ В БУДУЩЕЕ, БОРТ {board_id}!")
                st.balloons()
            else:
                st.error("КРИТИЧЕСКАЯ ОШИБКА: ДАННЫЕ НЕПОЛНЫЕ")

# --- FOOTER ---
st.write("\n" * 10)
st.markdown("<p style='text-align:center; color:#222; font-size: 0.8rem; letter-spacing:5px;'>D.MAX // THE NEW WORLD // 2026</p>", unsafe_allow_html=True)
