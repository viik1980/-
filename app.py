import streamlit as st
import pandas as pd
import datetime
import os

# ====================== КОНФИГУРАЦИЯ ======================
st.set_page_config(
    page_title="ДЕЖУРНЫЙ МАКС | NEURAL NEXUS",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

DB_FILE = "max_titan_registry.csv"

# ====================== PREMIUM CSS ======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Inter:wght@400;500;600;700&display=swap');

.stApp {
    background: #050508;
    background-image: 
        radial-gradient(circle at 50% 15%, rgba(0, 242, 255, 0.13) 0%, transparent 55%),
        radial-gradient(circle at 85% 75%, rgba(189, 0, 255, 0.09) 0%, transparent 65%),
        linear-gradient(180deg, #050508 0%, #020205 100%);
    color: #f0f0f5;
    font-family: 'Inter', sans-serif;
}

.logo-container {
    display: flex;
    justify-content: center;
    margin: 40px 0 15px 0;
    filter: drop-shadow(0 0 70px rgba(0, 242, 255, 0.75)) 
            drop-shadow(0 0 120px rgba(189, 0, 255, 0.45));
    animation: logoPulse 7s ease-in-out infinite alternate;
}

@keyframes logoPulse {
    from { filter: drop-shadow(0 0 45px rgba(0, 242, 255, 0.65)); }
    to   { filter: drop-shadow(0 0 95px rgba(0, 242, 255, 0.95)) 
                  drop-shadow(0 0 160px rgba(189, 0, 255, 0.55)); }
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 900 !important;
    letter-spacing: 2px;
}

.gradient-title {
    background: linear-gradient(90deg, #00f2ff, #bd00ff, #00f2ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.neon-card {
    background: rgba(13, 13, 22, 0.78);
    backdrop-filter: blur(28px);
    border-radius: 32px;
    padding: 34px 28px;
    border: 1px solid rgba(0, 242, 255, 0.18);
    box-shadow: 0 10px 40px rgba(0, 242, 255, 0.12);
    transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}

.neon-card:hover {
    transform: translateY(-14px) scale(1.03);
    border-color: #bd00ff;
    box-shadow: 0 25px 70px rgba(189, 0, 255, 0.28), 
                inset 0 0 50px rgba(0, 242, 255, 0.15);
}

.stButton>button {
    background: linear-gradient(90deg, #00f2ff 0%, #bd00ff 100%) !important;
    color: #000 !important;
    font-size: 1.45rem !important;
    font-weight: 800 !important;
    height: 78px !important;
    border-radius: 20px !important;
    letter-spacing: 5px !important;
    box-shadow: 0 0 55px rgba(0, 242, 255, 0.7) !important;
    transition: all 0.4s ease !important;
}

.stButton>button:hover {
    transform: scale(1.06);
    box-shadow: 0 0 80px rgba(189, 0, 255, 0.9) !important;
}

.status-bar {
    background: rgba(0, 242, 255, 0.1);
    border: 1px solid rgba(0, 242, 255, 0.4);
    color: #00f2ff;
    font-family: 'Orbitron', sans-serif;
    padding: 8px 20px;
    border-radius: 50px;
    text-align: center;
    font-size: 1.1rem;
    margin-bottom: 30px;
    animation: statusGlow 3s ease-in-out infinite alternate;
}

@keyframes statusGlow { 0% { box-shadow: 0 0 15px rgba(0,242,255,0.6); } 100% { box-shadow: 0 0 30px rgba(0,242,255,1); } }
</style>
""", unsafe_allow_html=True)

# ====================== ЛОГОТИП ======================
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image("dmax_logo.png", use_column_width=True)   # ← твой финальный логотип здесь
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="gradient-title" style="text-align:center; font-size:3.4rem; margin:0;">ДЕЖУРНЫЙ МАКС</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.45rem; color:#aaa; letter-spacing:7px; margin-top:8px;">NEURAL NEXUS • ТВОЙ ЦИФРОВОЙ ШТУРМАН НА ДОРОГЕ</p>', unsafe_allow_html=True)

st.markdown('<div class="status-bar">🟢 МАКС ОНЛАЙН • 24/7 НЕЙРОННАЯ ПОДДЕРЖКА В ЕВРОПЕ</div>', unsafe_allow_html=True)

# ====================== ТАКТИЧЕСКИЕ СИСТЕМЫ ======================
st.markdown('<h2 style="text-align:center; margin:50px 0 30px; font-size:2.2rem;">// ТАКТИЧЕСКИЕ СИСТЕМЫ</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#00f2ff; margin-bottom:18px;">🧠 НЕЙРОСЕТЕВОЙ ТАХОГРАФ</h3>
        <p style="font-size:1.15rem; line-height:1.6;">Видит будущее маршрута на 8 часов вперёд. Учитывает Пакет Мобильности, погоду, твою усталость и говорит голосом: «Дотянешь или лучше встать через 47 минут».</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#bd00ff; margin-bottom:18px;">⚖️ ЦИФРОВОЙ ЮРИСТ</h3>
        <p style="font-size:1.15rem; line-height:1.6;">Мгновенно отвечает инспекторам на их языке. Знает все законы ЕС на сегодня. Никогда больше не заплатишь незаконный штраф.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#00f2ff; margin-bottom:18px;">🎙️ ГОЛОСОВОЙ ПЕРЕВОДЧИК</h3>
        <p style="font-size:1.15rem; line-height:1.6;">Скажи проблему одной фразой — Макс сам договорится с таксистом, грузчиком или сервисом на любом языке Европы.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="neon-card">
        <h3 style="color:#bd00ff; margin-bottom:18px;">💤 АНТИ-ЗОМБИ РЕЖИМ</h3>
        <p style="font-size:1.15rem; line-height:1.6;">Анализирует твои биоритмы и предлагает идеальные окна для отдыха. Ты всегда свежий и в безопасности.</p>
    </div>
    """, unsafe_allow_html=True)

# ====================== ФОРМА ======================
st.markdown('<h2 style="text-align:center; margin:60px 0 25px; font-size:2.3rem;">ИНИЦИАЛИЗАЦИЯ ПИЛОТА</h2>', unsafe_allow_html=True)

with st.form("pilot_activation", clear_on_submit=True):
    col_n, col_s = st.columns(2)
    with col_n:
        name = st.text_input("ИМЯ", placeholder="Алексей")
        phone = st.text_input("ТЕЛЕФОН", placeholder="+49 176 12345678")
    with col_s:
        surname = st.text_input("ФАМИЛИЯ", placeholder="Иванов")
        email = st.text_input("E-MAIL", placeholder="you@truckdriver.eu")
    
    board_id = st.text_input("ЖЕЛАЕМЫЙ ID БОРТА (3 цифры)", placeholder="777", max_chars=3)
    
    submitted = st.form_submit_button("АКТИВИРОВАТЬ ДЕЖУРНОГО МАКСА ››")
    
    if submitted:
        if name and email and board_id and len(board_id) == 3:
            new_data = pd.DataFrame([[
                datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
                name, surname, phone, email, board_id, "ALPHA"
            ]], columns=['Time', 'Name', 'Surname', 'Phone', 'Email', 'ID', 'Tier'])
            
            if not os.path.isfile(DB_FILE):
                new_data.to_csv(DB_FILE, index=False)
            else:
                new_data.to_csv(DB_FILE, mode='a', header=False, index=False)
            
            st.success(f"✅ ПРОТОКОЛ ПРИНЯТ! ДОБРО ПОЖАЛОВАТЬ В СЕТЬ, БОРТ {board_id}!")
            st.balloons()
            st.toast("Макс уже сканирует твой будущий маршрут...", icon="🛰️")
        else:
            st.error("Пожалуйста, заполни все обязательные поля")

# ====================== ФУТЕР ======================
st.markdown("---")
st.markdown('<p style="text-align:center; color:#666; font-size:0.95rem;">© 2026 ДЕЖУРНЫЙ МАКС • Все права защищены нейросетью</p>', unsafe_allow_html=True)
