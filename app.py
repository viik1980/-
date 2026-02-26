import streamlit as st
import pandas as pd
import datetime
import os

# --- ИНИЦИАЛИЗАЦИЯ ---
st.set_page_config(page_title="MAX | SYSTEM CORE", page_icon="💠", layout="wide")
DB_FILE = "max_leads_2026.csv"

# --- ФУТУРИСТИЧЕСКИЙ CSS ---
st.markdown("""
    <style>
    /* Импорт шрифтов: Orbitron для заголовков, Roboto Mono для данных */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400&display=swap');
    
    /* --- ОСНОВНОЙ ФОН И АТМОСФЕРА --- */
    .stApp {
        background-color: #050505;
        background-image: 
            linear-gradient(rgba(0, 10, 20, 0.9), rgba(0, 0, 0, 0.95)),
            repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0, 255, 255, 0.05) 2px, rgba(0, 255, 255, 0.05) 4px);
        background-size: cover;
        color: #e0e0e0;
        font-family: 'Roboto Mono', monospace; /* Шрифт терминала для основного текста */
    }
    
    /* Эффект "сканлайна" (полосы экрана) поверх всего */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.6) 50%, transparent 100%);
        background-size: 100% 4px;
        pointer-events: none;
        z-index: 999;
        opacity: 0.2;
    }

    /* --- ТИПОГРАФИКА --- */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    
    .hero-title {
        font-size: 6rem;
        font-weight: 900;
        text-align: center;
        /* Двойной градиент для текста: Огонь и Лед */
        background: linear-gradient(to right, #ff3c00, #ffcc00, #00e5ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255, 60, 0, 0.5);
        margin-bottom: 0px;
        line-height: 1.1;
    }
    
    .subtitle {
        text-align: center;
        color: #00e5ff; /* Кибер-синий */
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 8px;
        font-size: 1.2rem;
        text-transform: uppercase;
        margin-bottom: 60px;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
    }
    
    .section-header {
        border-bottom: 2px solid #ff3c00;
        display: inline-block;
        padding-bottom: 10px;
        margin-bottom: 30px;
        color: #ffffff;
        text-shadow: 0 0 10px #ff3c00;
    }

    /* --- КАРТОЧКИ ФУНКЦИОНАЛА (HUD MODULES) --- */
    .feature-card {
        background: rgba(10, 10, 10, 0.8);
        /* Скошенные углы (Стелс-геометрия) */
        clip-path: polygon(10% 0, 100% 0, 100% 90%, 90% 100%, 0 100%, 0 10%);
        border-top: 3px solid #ff3c00;
        padding: 30px;
        height: 280px;
        transition: all 0.4s ease;
        /* Внутреннее свечение */
        box-shadow: inset 0 0 20px rgba(255, 60, 0, 0.1);
        backdrop-filter: blur(5px);
    }
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-top-color: #00e5ff;
        box-shadow: inset 0 0 30px rgba(0, 229, 255, 0.3), 0 0 20px rgba(0, 229, 255, 0.2);
    }
    .feature-card h3 {
        color: #ffffff;
        font-size: 1.5rem;
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        display: block;
        text-shadow: 0 0 15px currentColor;
    }

    /* --- ФОРМА (CONTROL PANEL) --- */
    .stForm {
        background: rgba(20, 20, 20, 0.9);
        border: none;
        /* Сложная форма панели */
        clip-path: polygon(0 0, 95% 0, 100% 5%, 100% 100%, 5% 100%, 0 95%);
        padding: 40px;
        box-shadow: inset 0 0 30px rgba(0, 0, 0, 1);
        border-left: 4px solid #ff3c00;
    }

    /* Стилизация полей ввода Streamlit */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background-color: #0a0a0a !important;
        color: #00e5ff !important; /* Цвет текста ввода - синий неон */
        font-family: 'Roboto Mono', monospace !important;
        border: 1px solid #333 !important;
        border-radius: 0px !important; /* Квадратные поля */
        height: 50px;
        transition: 0.3s;
    }
    /* Подсветка при фокусе */
    .stTextInput > div > div > input:focus, .stSelectbox > div > div > div:focus-within {
        border-color: #ff3c00 !important;
        box-shadow: 0 0 15px rgba(255, 60, 0, 0.3) !important;
        background-color: #111 !important;
    }
    /* Labels (подписи к полям) */
    .stTextInput label, .stSelectbox label {
        color: #888 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.8rem !important;
        letter-spacing: 2px;
    }

    /* --- КНОПКА ЗАПУСКА (IGNITION BUTTON) --- */
    .stButton > button {
        background: linear-gradient(45deg, #ff3c00, #c70000) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        height: 70px;
        border: none !important;
        border-radius: 0px !important;
        clip-path: polygon(5% 0, 100% 0, 95% 100%, 0 100%); /* Скошенная кнопка */
        letter-spacing: 3px;
        transition: 0.5s;
        width: 100%;
        text-shadow: 0 1px 3px rgba(0,0,0,0.5);
    }
    .stButton > button:hover {
        box-shadow: 0 0 50px #ff3c00, inset 0 0 20px rgba(255,255,255,0.5);
        transform: skewX(-5deg) scale(1.05); /* Эффект скорости при наведении */
    }
    
    /* Разделитель */
    hr { border-color: #333; opacity: 0.5; }
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
st.markdown('<p class="subtitle">SYSTEM CORE V.2026 // ОПЕРАЦИОННЫЙ ЦЕНТР ПИЛОТА</p>', unsafe_allow_html=True)

# 2. ОПИСАНИЕ ФУНКЦИОНАЛА (HUD MODULES)
st.write("\n" * 2)
st.markdown('<h3 class="section-header">[ АКТИВНЫЕ МОДУЛИ СИСТЕМЫ ]</h3>', unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("""<div class="feature-card">
        <span class="feature-icon" style="color:#ff3c00;">🛡️</span>
        <h3>ANTI-SHF PROTOCOL</h3>
        <p style='color:#aaa; font-size: 0.9rem;'>Автоматическая защита от штрафов РТО. Алгоритм рассчитывает слоты отдыха в реальном времени, синхронизируясь с тахографом.</p>
    </div>""", unsafe_allow_html=True)

with col_f2:
    st.markdown("""<div class="feature-card">
        <span class="feature-icon" style="color:#00e5ff;">⚡</span>
        <h3>ROAD CHEF CORE</h3>
        <p style='color:#aaa; font-size: 0.9rem;'>База данных оптимального питания. Генерация рецептов на основе имеющихся ресурсов. Поддержание энергии экипажа.</p>
    </div>""", unsafe_allow_html=True)

with col_f3:
    st.markdown("""<div class="feature-card">
        <span class="feature-icon" style="color:#ffcc00;">📍</span>
        <h3>SECURE HUB FINDER</h3>
        <p style='color:#aaa; font-size: 0.9rem;'>Сканирование безопасных зон. Доступ к закрытому реестру проверенных стоянок и сервисов с рейтингом сообщества.</p>
    </div>""", unsafe_allow_html=True)

st.write("\n" * 5)
st.divider()

# 3. БЛОК ПРЕДЗАКАЗА
st.markdown('<h3 class="section-header">[ ИНИЦИАЛИЗАЦИЯ НОВОГО ПИЛОТА ]</h3>', unsafe_allow_html=True)
col_text, col_form = st.columns([1, 1.5], gap="large")

with col_text:
    st.write("\n" * 1)
    st.markdown("""
    <div style="background: rgba(255, 60, 0, 0.1); padding: 25px; border-left: 3px solid #ff3c00; clip-path: polygon(0 0, 100% 0, 100% 95%, 95% 100%, 0 100%);">
        <h4 style="font-family: Orbitron; color: #ff3c00;">ВНИМАНИЕ ЭКИПАЖУ</h4>
        <p style="font-size: 0.9rem;">Вы получаете доступ к профессиональному оборудованию, а не к игрушке. Ввод данных означает готовность к работе в системе нового поколения.</p>
        <p><b>Привилегии статуса TITAN:</b></p>
        <ul style="font-size: 0.9rem; color: #ccc;">
            <li>Закрепление уникального цифрового позывного (ID) навечно.</li>
            <li>Фиксация стоимости владения до официального релиза.</li>
            <li>Приоритетный доступ к нейросетевым функциям.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    # Я убрал картинку, так как она простит дизайн. Лучше оставить чистый техно-текст.

with col_form:
    with st.form("main_form"):
        st.markdown('<p style="font-family: Orbitron; color: #888; margin-bottom: 20px;">// ВВЕДИТЕ ДАННЫЕ ДЛЯ ГЕНЕРАЦИИ КЛЮЧА</p>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            first_name = st.text_input("ИМЯ ПИЛОТА")
            phone = st.text_input("КАНАЛ СВЯЗИ (ТЕЛЕФОН)")
        with c2:
            last_name = st.text_input("ФАМИЛИЯ")
            email = st.text_input("ЭЛЕКТРОННАЯ ПОЧТА")
            
        st.write("---")
        st.markdown('<p style="font-family: Orbitron; color: #ff3c00; margin-bottom: 20px;">// КОНФИГУРАЦИЯ БОРТА</p>', unsafe_allow_html=True)
        c3, c4 = st.columns([1, 2])
        with c3:
            board_num = st.text_input("ЖЕЛАЕМЫЙ ID БОРТА", placeholder="007")
        with c4:
            tier = st.selectbox("УРОВЕНЬ ДОСТУПА", ["TITAN (Founder Status // VIP)", "HEAVY (Professional)", "STANDARD (Базовый)"])
            
        st.write("\n" * 2)
        # Кнопка теперь выглядит как рычаг запуска
        submit = st.form_submit_button("ЗАПУСТИТЬ ПРОТОКОЛ РЕГИСТРАЦИИ ››")
        
        if submit:
            if first_name and email and phone and board_num:
                with st.spinner("ШИФРОВАНИЕ ДАННЫХ..."):
                    save_lead(first_name, last_name, phone, email, board_num, tier)
                    # Имитация задержки для эффекта сложной работы
                    import time
                    time.sleep(1.5) 
                st.success(f"ДОСТУП РАЗРЕШЕН. БОРТ MAX-{board_num} ЗАКРЕПЛЕН В СИСТЕМЕ.")
                st.balloons()
            else:
                st.error("ОШИБКА: НЕПОЛНЫЕ ДАННЫЕ ТЕЛЕМЕТРИИ.")

# --- ADMIN PANEL (Скрыта внизу) ---
st.write("\n" * 10)
st.divider()
with st.expander("🔐 СИСТЕМНЫЙ АДМИНИСТРАТОР (Вход по ключу)"):
    pwd = st.text_input("Пароль доступа", type="password")
    if pwd == "max_vip":
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.write("### РЕЕСТР ПИЛОТОВ")
            # Стилизация таблицы в темную тему
            st.dataframe(df.style.set_properties(**{'background-color': '#111', 'color': '#00e5ff', 'border-color': '#333'}))
            st.download_button("ЭКСПОРТ ДАННЫХ (CSV)", df.to_csv(index=False).encode('utf-8'), "leads.csv")
        else:
            st.warning("Реестр пуст")
