import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- СИСТЕМНАЯ КОНФИГУРАЦИЯ ---
st.set_page_config(page_title="D.MAX | NEURAL NEXUS", page_icon="🧠", layout="wide")
DB_FILE = "dmax_pilots_registry.csv"

# --- THE "D.MAX" ULTRA-SPEC CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* ФОН С ЭФФЕКТОМ ЛЕТЯЩИХ ЧАСТИЦ */
    .stApp {
        background-color: #020205;
        background-image: 
            radial-gradient(circle at 50% 30%, rgba(189, 0, 255, 0.1), transparent 70%),
            repeating-linear-gradient(45deg, #0a0a0a 0px, #0a0a0a 2px, #050505 2px, #050505 8px);
        overflow: hidden;
    }

    /* АНИМАЦИЯ ЧАСТИЦ (ИЗЮМИНКА) */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(white, rgba(255,255,255,0) 2px);
        background-size: 100px 100px;
        opacity: 0.1;
        animation: particles 60s linear infinite;
        pointer-events: none;
    }
    @keyframes particles {
        from { background-position: 0 0; }
        to { background-position: 500px 1000px; }
    }

    /* ЛОГОТИП И СВЕЧЕНИЕ */
    .logo-glow {
        display: flex;
        justify-content: center;
        filter: drop-shadow(0 0 30px rgba(0, 242, 255, 0.5));
        margin-bottom: 20px;
        animation: pulse 3s ease-in-out infinite alternate;
    }
    @keyframes pulse { from { opacity: 0.8; } to { opacity: 1; filter: drop-shadow(0 0 50px rgba(189, 0, 255, 0.6)); } }

    /* СТАЛЬНАЯ КАРТА (BRUSHED STEEL) */
    .steel-card {
        width: 100%; max-width: 480px; height: 280px;
        border-radius: 12px;
        background: linear-gradient(135deg, #777, #bbb 40%, #888 60%, #555);
        position: relative;
        padding: 30px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.1);
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .steel-card::after { /* Шлифовка */
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(rgba(255,255,255,0.03) 0px, rgba(255,255,255,0.03) 1px, transparent 1px, transparent 2px);
        pointer-events: none;
    }

    /* ЛАЗЕРНАЯ ГРАВИРОВКА */
    .laser-etched {
        font-family: 'Orbitron', sans-serif;
        color: #1a1a1a;
        text-shadow: 1px 1px 1px rgba(255,255,255,0.2), -1px -1px 1px rgba(0,0,0,0.5);
        font-weight: 900;
        text-transform: uppercase;
    }

    /* СТЕКЛЯННЫЕ ПАНЕЛИ */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        transition: 0.4s;
    }
    .glass-panel:hover { border-color: #bd00ff; box-shadow: 0 0 30px rgba(189, 0, 255, 0.2); }

    .gradient-header {
        background: linear-gradient(to right, #bd00ff, #00f2ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-family: 'Orbitron', sans-serif; font-weight: 900;
    }

    /* ФОРМА */
    .stForm {
        background: rgba(5,5,10,0.8) !important;
        border: 2px solid #bd00ff !important;
        border-radius: 30px !important;
        padding: 40px !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #bd00ff, #00f2ff) !important;
        color: #000 !important; font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important; height: 70px; border-radius: 10px !important;
        box-shadow: 0 0 30px rgba(189, 0, 255, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ЛОГИКА ---
def save_pilot(fname, lname, phone, email, board, role):
    new_data = pd.DataFrame([[datetime.datetime.now(), fname, lname, phone, email, board, role]], 
                            columns=['Time', 'Name', 'Surname', 'Phone', 'Email', 'ID', 'Role'])
    if not os.path.isfile(DB_FILE): new_data.to_csv(DB_FILE, index=False)
    else: new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- ВЕРХНЯЯ ЧАСТЬ ---
st.write("\n")
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    logo_url = "https://i.postimg.cc/CLg33k38/image-7.jpg"
    st.markdown(f'<div class="logo-glow"><img src="{logo_url}" style="width:100%;"></div>', unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center;"><span class="gradient-header">D.MAX // THE FUTURE IS HERE</span></h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#666; letter-spacing:10px; font-family:Orbitron;">PREDICTIVE ROAD INTELLIGENCE</p>', unsafe_allow_html=True)

st.write("\n" * 4)

# --- МОДУЛИ СИСТЕМЫ ---
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color:#00f2ff; font-family:Orbitron;">[ CHRONOS ALGORITHM ]</h3>
        <p style="color:#aaa;">Это больше не калькулятор. D.MAX вычисляет будущее. Вводишь данные — получаешь идеальный график сна и движения по РТО и Пакету Мобильности. 
        <b>Анти-Зомби</b> режим подстроит маршрут под твои биоритмы, чтобы ты всегда был на пике формы.</p>
    </div>
    <div class="glass-panel" style="margin-top:20px;">
        <h3 style="color:#bd00ff; font-family:Orbitron;">[ LEGAL FIREWALL ]</h3>
        <p style="color:#aaa;">Цифровой юрист в твоем кармане. Макс знает законы каждой страны ЕС и общается с инспекторами на их языке. 
        Твоя защита от незаконных штрафов теперь автоматизирована.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color:#00f2ff; font-family:Orbitron;">[ VOICE NEURAL LINK ]</h3>
        <p style="color:#aaa;">Руки на руле, мысли на дороге. Макс понимает тебя с полуслова. "Макс, вызови такси" или "Макс, дотяну до парковки?" 
        — он сам сделает звонки и даст ответ на основе живых данных.</p>
    </div>
    <div class="glass-panel" style="margin-top:20px;">
        <h3 style="color:#bd00ff; font-family:Orbitron;">[ SMART PREVIEW ]</h3>
        <p style="color:#aaa;">Система видит твое "окно" выгрузки и бронирует места на стоянках заранее. 
        D.MAX — это твой персональный штурман, который решает проблемы до их появления.</p>
    </div>
    """, unsafe_allow_html=True)

# --- РЕГИСТРАЦИЯ И ГЕНЕРАЦИЯ СТАЛЬНОЙ КАРТЫ ---
st.write("\n" * 5)
_, col_form, _ = st.columns([1, 2, 1])

with col_form:
    if 'registered' not in st.session_state:
        with st.form("dmax_terminal"):
            st.markdown("<h2 style='text-align:center; font-family:Orbitron;'>INITIALIZE PILOT</h2>", unsafe_allow_html=True)
            f_n, f_s = st.columns(2)
            with f_n: name = st.text_input("ИМЯ")
            with f_s: surname = st.text_input("ФАМИЛИЯ")
            phone = st.text_input("ТЕЛЕФОН")
            email = st.text_input("E-MAIL")
            board_id = st.text_input("BOARD ID (Напр. 077)")
            if st.form_submit_button("ACTIVATE PROTOCOL ››"):
                if name and board_id:
                    save_pilot(name, surname, phone, email, board_id, "ALPHA")
                    st.session_state.registered = True
                    st.session_state.p_name = f"{name} {surname}"
                    st.session_state.p_id = board_id
                    st.rerun()
    else:
        # ВЫВОД СТАЛЬНОЙ КАРТЫ
        qr_url = f"https://chart.apis.google.com/chart?chs=200x200&cht=qr&chl=DMAX-ID-{st.session_state.p_id}&choe=UTF-8"
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; gap: 40px;">
            <div class="steel-card">
                <div style="display:flex; justify-content:space-between;">
                    <img src="{logo_url}" style="width:70px; filter: drop-shadow(0 0 10px #00f2ff);">
                    <div class="laser-etched" style="font-size:0.6rem; text-align:right;">D.MAX // TITAN CORE<br>SECURITY LEVEL: ALPHA</div>
                </div>
                <div class="laser-etched" style="font-size:1.8rem; text-align:center; margin-top:20px;">{st.session_state.p_name}</div>
                <div style="display:flex; justify-content:space-between; align-items:flex-end;">
                    <div class="laser-etched" style="font-size:1.2rem;">ID: MAX-{st.session_state.p_id}</div>
                    <div class="laser-etched" style="font-size:0.7rem; color:#333;">FOUNDER EDITION</div>
                </div>
            </div>
            <div class="steel-card" style="align-items:center; justify-content:center;">
                <img src="{qr_url}" style="width:140px; border: 4px solid #1a1a1a; border-radius:10px;">
                <div class="laser-etched" style="font-size:0.8rem; margin-top:15px;">SCAN TO VERIFY ACCESS</div>
            </div>
            <button onclick="window.location.reload();" style="background:none; border:1px solid #333; color:#555; cursor:pointer;">ЗАРЕГИСТРИРОВАТЬ ДРУГОЙ БОРТ</button>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# --- FOOTER ---
st.write("\n" * 10)
st.markdown("<p style='text-align:center; color:#222; font-family:Orbitron; font-size:0.8rem;'>D.MAX NEURAL LINK // 2026 // END OF TRANSMISSION</p>", unsafe_allow_html=True)
