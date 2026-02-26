import streamlit as st
import random
import time

st.set_page_config(
    page_title="Дежурный Макс — Platinum Edition",
    page_icon="⚡",
    layout="wide"
)

# ==============================
# 🎨 PREMIUM CSS + АНИМАЦИИ
# ==============================

st.markdown("""
<style>

/* ====== Глобальный фон ====== */
html, body, [class*="css"]  {
    background: radial-gradient(circle at 20% 20%, #0f2027, #0a0f14 40%, #000000 80%);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* ====== Скрываем стандартный Streamlit ====== */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ====== HERO ====== */
.hero {
    text-align: center;
    padding-top: 60px;
    padding-bottom: 40px;
}

.hero h1 {
    font-size: 64px;
    background: linear-gradient(90deg, #00f5ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.hero p {
    font-size: 22px;
    color: #cccccc;
}

/* ====== Платиновая карта ====== */
.card-container {
    display: flex;
    justify-content: center;
    margin-top: 50px;
}

.platinum-card {
    width: 520px;
    height: 300px;
    border-radius: 20px;
    background: linear-gradient(135deg, #e6e6e6, #bfbfbf, #ffffff);
    box-shadow: 0 0 40px rgba(255,255,255,0.2);
    padding: 30px;
    position: relative;
    overflow: hidden;
    color: black;
    transition: 0.4s ease;
}

.platinum-card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 80px rgba(0,255,255,0.4);
}

.card-title {
    font-size: 22px;
    font-weight: bold;
}

.card-number {
    font-size: 26px;
    letter-spacing: 3px;
    margin-top: 40px;
}

/* ====== Лазер ====== */
.laser {
    position: absolute;
    width: 2px;
    height: 100%;
    background: #00ffff;
    box-shadow: 0 0 20px #00ffff;
    animation: laserMove 2s linear infinite;
}

@keyframes laserMove {
    0% { left: 0; opacity: 0; }
    10% { opacity: 1; }
    50% { left: 100%; opacity: 1; }
    100% { left: 100%; opacity: 0; }
}

/* ====== Карточки преимуществ ====== */
.feature-section {
    margin-top: 100px;
}

.feature-card {
    background: linear-gradient(145deg, #111111, #1c1c1c);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 0 30px rgba(0,255,255,0.05);
    transition: 0.4s ease;
    height: 100%;
}

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 50px rgba(123,47,247,0.4);
}

.feature-title {
    font-size: 22px;
    margin-bottom: 15px;
    color: #00f5ff;
}

.feature-text {
    color: #cccccc;
}

/* ====== Кнопка ====== */
.stButton>button {
    background: linear-gradient(90deg, #00f5ff, #7b2ff7);
    border: none;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    color: white;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #00f5ff;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# 🔥 HERO
# ==============================

st.markdown("""
<div class="hero">
    <h1>Дежурный Макс</h1>
    <p>Платиновый цифровой ассистент нового поколения</p>
</div>
""", unsafe_allow_html=True)

# ==============================
# 💎 Генерация уникального номера
# ==============================

def generate_number():
    return "MAX-" + str(random.randint(100000, 999999))

if "card_number" not in st.session_state:
    st.session_state.card_number = generate_number()

# ==============================
# 💳 Платиновая карта + лазер
# ==============================

st.markdown('<div class="card-container">', unsafe_allow_html=True)

st.markdown(f"""
<div class="platinum-card">
    <div class="laser"></div>
    <div class="card-title">PLATINUM ACCESS</div>
    <div class="card-number">{st.session_state.card_number}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")

if st.button("⚡ Выжечь новый уникальный номер"):
    st.session_state.card_number = generate_number()
    st.experimental_rerun()

# ==============================
# 🚘 Блок преимуществ (как в автосалоне)
# ==============================

st.markdown('<div class="feature-section">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Статус</div>
        <div class="feature-text">
        Это не просто сервис. Это цифровой уровень доступа.
        Ваш персональный интеллект, доступный 24/7.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Технология</div>
        <div class="feature-text">
        Искусственный интеллект, автоматизация, контроль задач,
        аналитика и стратегическое мышление — в одном интерфейсе.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Эксклюзивность</div>
        <div class="feature-text">
        Уникальный цифровой номер.
        Персональный доступ.
        Премиальное ощущение будущего.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.markdown("### Готовы активировать Platinum доступ?")
st.button("🚀 Активировать")
