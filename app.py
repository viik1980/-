import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- ИНИЦИАЛИЗАЦИЯ ---
st.set_page_config(page_title="MAX | OPERATION CENTER", page_icon="💠", layout="wide")
DB_FILE = "max_titan_registry.csv"

# --- ПРЕМИУМ ТЕХНО-ДИЗАЙН ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d0d0d, #000000);
        background-image: 
            linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)),
            repeating-linear-gradient(45deg, #111 0px, #111 1px, transparent 1px, transparent 10px);
        color: #f0f0f0;
        font-family: 'Roboto Mono', monospace;
    }

    /* Заголовки в стиле Sci-Fi */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 6rem;
        text-align: center;
        background: linear-gradient(to bottom, #fff, #444);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 15px;
        margin-bottom: 0px;
    }

    .section-header {
        font-family: 'Orbitron', sans-serif;
        color: #00e5ff;
        border-left: 5px solid #ff3c00;
        padding-left: 20px;
        margin-top: 50px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    /* Стеклянные панели (Dark Glass) */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 20px;
        margin: 15px 0;
        transition: 0.3s;
    }
    .glass-panel:hover {
        border-color: #ff3c00;
        background: rgba(255, 255, 255, 0.05);
    }

    /* Описание фич */
    .feature-title {
        color: #ff3c00;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }

    .feature-desc {
        color: #aaa;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* Акцент на цитаты */
    .quote-box {
        font-style: italic;
        border-left: 2px solid #555;
        padding-left: 20px;
        color: #888;
        margin: 20px 0;
    }

    /* Форма */
    .stForm {
        background: rgba(10, 10, 10, 0.9) !important;
        border: 2px solid #222 !important;
        border-radius: 20px !important;
        padding: 40px !important;
        box-shadow: 0 50px 100px rgba(0,0,0,0.8) !important;
    }

    .stButton>button {
        background: linear-gradient(45deg, #ff3c00, #a30000) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif !important;
        height: 70px;
        width: 100%;
        font-weight: 900 !important;
        letter-spacing: 5px !important;
        border: none !important;
        transition: 0.5s !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<p class="main-title">D.MAX</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00e5ff; letter-spacing:8px; font-family:Orbitron;">БОЛЬШЕ, ЧЕМ ИНТЕЛЛЕКТ. ТВОЙ ЦИФРОВОЙ БРОНЕНОСЕЦ.</p>', unsafe_allow_html=True)

st.write("\n" * 3)

# --- ОПИСАНИЕ МАКСА (THE BRAIN) ---
st.markdown('<h2 class="section-header">UNIT 01: КТО ТАКОЙ МАКС?</h2>', unsafe_allow_html=True)

col_text, col_img = st.columns([1.5, 1])
with col_text:
    st.markdown("""
    <div class="glass-panel">
        <p class="feature-desc">
        Макс — это не просто приложение. Это <b>нейронный узел</b> твоего грузовика. Он не спит, не устает и видит дорогу на тысячи километров вперед. 
        Пока ты держишь руль, Макс берет на себя всю бюрократию, расчеты и языковые барьеры. 
        Он — твой адвокат перед законом, твой штурман в незнакомых городах и твой личный переводчик в любой стране мира.
        </p>
        <div class="quote-box">
        "Ты управляешь машиной. Макс управляет ситуацией."
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ФУНКЦИОНАЛ (THE ARSENAL) ---
st.markdown('<h2 class="section-header">UNIT 02: ТАКТИЧЕСКИЙ АРСЕНАЛ</h2>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass-panel">
        <p class="feature-title">🛡️ УМНЫЙ ТАХОГРАФ</p>
        <p class="feature-desc">Забудь про калькуляторы и страх штрафов. Макс чувствует время каждой клеткой процессора. РТО под полным контролем в реальном времени.</p>
    </div>
    <div class="glass-panel">
        <p class="feature-title">🧮 ТЕРМИНАЛ РАСЧЕТОВ</p>
        <p style="color:#aaa;">Умный калькулятор топлива, веса и маршрутных расходов. Ошибка исключена.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-panel">
        <p class="feature-title">🌍 ЯЗЫКОВОЙ АГРЕССОР</p>
        <p class="feature-desc">Нужно вызвать такси в пригороде Лиона или договориться на загрузке в Берлине? Просто скажи суть Максу. Он сам свяжется, объяснит задачу на идеальном французском или немецком и выдаст тебе готовый результат.</p>
    </div>
    <div class="glass-panel">
        <p class="feature-title">🛰️ КАРТОГРАФИЯ DEEP-CORE</p>
        <p style="color:#aaa;">Слой "Макс" на карте: только проверенные стоянки, безопасные хабы и актуальные запреты.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass-panel">
        <p class="feature-title">🎙️ ГОЛОСОВОЙ ИНТЕРФЕЙС</p>
        <p class="feature-desc">Руки на руле — Макс на связи. Полное управление голосом. Никакого тыканья в экран на скорости 90 км/ч.</p>
    </div>
    <div class="glass-panel">
        <p class="feature-title">🤖 ПРОДВИНУТЫЙ ИИ</p>
        <p style="color:#aaa;">Макс обучается твоему стилю езды и предлагает решения еще до того, как возникнет проблема.</p>
    </div>
    """, unsafe_allow_html=True)

# --- ПОЧЕМУ МАКС? ---
st.write("\n" * 4)
st.markdown('<h2 class="section-header">ПОЧЕМУ ПИЛОТЫ ВЫБИРАЮТ D.MAX?</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding: 40px;">
    <p style="font-size: 1.5rem; color:#fff; font-family: 'Roboto Mono';">МЫ НЕ ПРОДАЕМ СОФТ. МЫ ПРОДАЕМ СТАТУС И СПОКОЙСТВИЕ.</p>
    <p style="color:#666;"> Обычные водители пользуются навигаторами. Пилоты D.MAX владеют дорогой.</p>
</div>
""", unsafe_allow_html=True)

# --- РЕГИСТРАЦИЯ (REGISTRY) ---
st.write("\n" * 4)
st.markdown('<h2 class="section-header">ИНИЦИАЛИЗАЦИЯ В СИСТЕМЕ</h2>', unsafe_allow_html=True)

col_form_center, _ = st.columns([1.5, 1])

with col_form_center:
    with st.form("titan_preorder"):
        st.markdown("<h3 style='text-align:center; font-family:Orbitron;'>РЕГИСТРАЦИЯ БОРТ-НОМЕРА</h3>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("NAME // ИМЯ")
            phone = st.text_input("COMMS // ТЕЛЕФОН")
        with c2:
            surname = st.text_input("SURNAME // ФАМИЛИЯ")
            email = st.text_input("MAIL // ПОЧТА")
            
        st.write("---")
        board_id = st.text_input("TITAN ID (001-999)", placeholder="Напр. 077")
        tier = st.selectbox("STATUS TYPE", ["TITAN (Founder Edition)", "HEAVY (Pro Access)", "STANDARD"])
        
        if st.form_submit_button("ЗАРЕГИСТРИРОВАТЬ ЭКИПАЖ"):
            if name and email and phone:
                st.success(f"ПРОТОКОЛ АКТИВИРОВАН. БОРТ MAX-{board_id} ПРИНЯТ.")
                st.balloons()
            else:
                st.error("ОШИБКА: ДАННЫЕ НЕПОЛНЫЕ")

# --- FOOTER ---
st.write("\n" * 10)
st.markdown("<p style='text-align:center; color:#333; font-size: 0.7rem;'>SYSTEM CORE V.2026 // D.MAX PROJECT // ALL RIGHTS RESERVED</p>", unsafe_allow_html=True)
