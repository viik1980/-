import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- ИНИЦИАЛИЗАЦИЯ ---
st.set_page_config(page_title="MAX | SYSTEM CORE", page_icon="💠", layout="wide")
DB_FILE = "max_leads_2026.csv"

# --- CARBON FIBER & CYBERPUNK CSS ---
st.markdown("""
    <style>
    /* Импорт шрифтов */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400&display=swap');
    
    /* --- ОСНОВНОЙ ФОН: ГЛУБОКИЙ КАРБОН --- */
    .stApp {
        background-color: #0a0a0a;
        /* Сложная текстура карбона: плетение + глянец + затемнение */
        background-image: 
            linear-gradient(to bottom, rgba(0,0,0,0.6), rgba(0,0,0,0.95)), /* Затемнение */
            repeating-linear-gradient(45deg, rgba(255,255,255,0.03) 0px, rgba(255,255,255,0.03) 2px, transparent 2px, transparent 8px), /* Плетение 1 */
            repeating-linear-gradient(-45deg, rgba(0,0,0,0.2) 0px, rgba(0,0,0,0.2) 2px, transparent 2px, transparent 8px), /* Плетение 2 (тени) */
            linear-gradient(to right, #111, #222); /* Базовый темный металл */
        background-size: 100% 100%, 20px 20px, 20px 20px, 100% 100%;
        color: #e0e0e0;
        font-family: 'Roboto Mono', monospace;
    }
    
    /* Эффект "сканлайна" поверх карбона */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 50%, transparent 100%);
        background-size: 100% 3px;
        pointer-events: none;
        z-index: 999;
        opacity: 0.3;
        mix-blend-mode: overlay;
    }

    /* --- ТИПОГРАФИКА --- */
    h1, h2, h3, h4 {
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 0 2px 5px rgba(0,0,0,0.8);
    }
    
    .hero-title {
        font-size: 6rem;
        font-weight: 900;
        text-align: center;
        /* Агрессивный огненный градиент */
        background: linear-gradient(to bottom, #ff5f00, #ff2a00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(255, 60, 0, 0.4));
        margin-bottom: 0px;
        line-height: 1.1;
    }
    
    .subtitle {
        text-align: center;
        color: #00e5ff;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 8px;
        font-size: 1.2rem;
        text-transform: uppercase;
        margin-bottom: 60px;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.6);
    }
    
    .section-header {
        border-bottom: 3px solid #ff3c00;
        display: inline-block;
        padding-bottom: 10px;
        margin-bottom: 30px;
        color: #ffffff;
        box-shadow: 0 5px 15px -5px rgba(255, 60, 0, 0.5);
    }

    /* --- КАРБОНОВЫЕ МОДУЛИ (HUD MODULES) --- */
    .feature-card {
        /* Текстура карбоновой плиты */
        background: 
            linear-gradient(135deg, rgba(30,30,30,0.9), rgba(10,10,10,1)),
            repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 4px);
        
        clip-path: polygon(15% 0, 100% 0, 100% 85%, 85% 100%, 0 100%, 0 15%); /* Более агрессивная геометрия */
        border-top: 4px solid #ff3c00;
        border-bottom: 1px solid #333;
        padding: 30px;
        height: 280px;
        transition: all 0.3s ease;
        /* Эффект объема и свечения по краям */
        box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 0 20px rgba(255, 60, 0, 0.1);
    }
    .feature-card:hover {
        transform: translateY(-5px) scale(1.01);
        border-top-color: #00e5ff;
        box-shadow: 0 15px 40px rgba(0, 229, 255, 0.2), inset 0 0 30px rgba(0, 229, 255, 0.2);
    }
    .feature-card h3 {
        color: #ffffff;
        font-size: 1.5rem;
        border-bottom: 1px solid #444;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        display: block;
        filter: drop-shadow(0 0 8px currentColor);
    }

    /* --- ФОРМА-ТЕРМИНАЛ (CONTROL PANEL) --- */
    .stForm {
        /* Карбоновый блок управления */
        background: 
            linear-gradient(to bottom, rgba(40,40,40,0.95), rgba(20,20,20,1)),
            repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 4px);
        border: none;
        clip-path: polygon(0 0, 97% 0, 100% 3%, 100% 100%, 3% 100%, 0 97%);
        padding: 40px;
        /* Металлическая рамка с подсветкой */
        box-shadow: 
            inset 0 0 0 2px #333, /* Внутренняя рамка */
            inset 0 0 40px rgba(0,0,0,0.8),
            0 20px 50px rgba(0,0,0,0.5);
        border-left: 5px solid #ff3c00;
        border-right: 5px solid #ff3c00;
    }

    /* Поля ввода - как экраны приборов */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background-color: #080808 !important;
        color: #00e5ff !important;
        font-family: 'Roboto Mono', monospace !important;
        border: 2px solid #222 !important;
        border-radius: 0px !important;
        height: 55px;
        transition: 0.3s;
        box-shadow: inset 0 0 10px rgba(0,0,0,1);
    }
    /* Активное поле */
    .stTextInput > div > div > input:focus, .stSelectbox > div > div > div:focus-within {
        border-color: #ff3c00 !important;
        background-color: #000 !important;
        box-shadow: inset 0 0 15px rgba(255, 60, 0, 0.2), 0 0 15px rgba(255, 60, 0, 0.4) !important;
        color: #ff3c00 !important;
    }
    .stTextInput label, .stSelectbox label {
        color: #aaa !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.8rem !important;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* --- РЫЧАГ ЗАПУСКА (IGNITION) --- */
    .stButton > button {
        background: linear-gradient(to bottom, #ff3c00, #960000) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 1.3rem !important;
        height: 75px;
        border: none !important;
        border-radius: 0px !important;
        /* Сложная форма кнопки */
        clip-path: polygon(10% 0, 90% 0, 100% 100%, 0 100%);
        letter-spacing: 4px;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Пружинящий эффект */
        width: 100%;
        text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        box-shadow: 0 10px 20px rgba(255, 60, 0, 0.3);
        border-top: 2px solid rgba(255,255,255,0.3) !important; /* Блик сверху */
    }
    .stButton > button:hover {
        background: linear-gradient(to bottom, #ff5f00, #c70000) !important;
        box-shadow: 0 0 60px #ff3c00, inset 0 0 30px rgba(255, 60, 0, 0.5);
        transform: scale(1.03) translateY(-2px);
    }
    .stButton > button:active {
        transform: scale(0.98) translateY(2px);
    }
    
    /* Разделитель */
    hr { border-color: #333; opacity: 0.3; margin: 50px 0; }
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
st.write("\n" * 4)
st.markdown('<h3 class="section-header">[ АКТИВНЫЕ МОДУЛИ СИСТЕМЫ ]</h3>', unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("""<div class="feature-card">
        <span class="feature-icon" style="color:#ff3c00;">🛡️</span>
        <h3>ANTI-SHF PROTOCOL</h3>
        <p style='color:#ccc; font-size: 0.9rem; font-family: Roboto Mono;'>Автоматическая защита от штрафов РТО. Алгоритм рассчитывает слоты отдыха в реальном времени, синхронизируясь с тахографом.</p>
    </div>""", unsafe_allow_html=True)

with col_f2:
    st.markdown("""<div class="feature-card">
        <span class="feature-icon" style="color:#00e5ff;">⚡</span>
        <h3>ROAD CHEF CORE</h3>
        <p style='color:#ccc; font-size: 0.9rem; font-family: Roboto Mono;'>База данных оптимального питания. Генерация рецептов на основе имеющихся ресурсов. Поддержание энергии экипажа.</p>
    </div>""", unsafe_allow_html=True)

with col_f3:
    st.markdown("""<div class="feature-card">
        <span class="feature-icon" style="color:#ffcc00;">📍</span>
        <h3>SECURE HUB FINDER</h3>
        <p style='color:#ccc; font-size: 0.9rem; font-family: Roboto Mono;'>Сканирование безопасных зон. Доступ к закрытому реестру проверенных стоянок и сервисов с рейтингом сообщества.</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# 3. БЛОК ПРЕДЗАКАЗА
st.markdown('<h3 class="section-header">[ ИНИЦИАЛИЗАЦИЯ НОВОГО ПИЛОТА ]</h3>', unsafe_allow_html=True)
col_text, col_form = st.columns([1, 1.6], gap="large")

with col_text:
    st.write("\n" * 2)
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(40,40,40,0.9), rgba(10,10,10,1));
        padding: 30px;
        border-left: 4px solid #ff3c00;
        clip-path: polygon(0 0, 100% 0, 100% 95%, 90% 100%, 0 100%);
        box-shadow: inset 0 0 30px rgba(0,0,0,0.8);
    ">
        <h4 style="font-family: Orbitron; color: #ff3c00; margin-top: 0;">ВНИМАНИЕ ЭКИПАЖУ</h4>
        <p style="font-size: 0.95rem; line-height: 1.6;">Вы получаете доступ к профессиональному оборудованию, а не к игрушке. Ввод данных означает готовность к работе в системе нового поколения.</p>
        
        <div style="margin-top: 25px; border-top: 1px solid #333; padding-top: 15px;">
            <p style="font-family: Orbitron; color: #00e5ff; font-size: 1rem;">ПРИВИЛЕГИИ СТАТУСА TITAN:</p>
            <ul style="font-size: 0.9rem; color: #aaa; list-style-type: square;">
                <li><span style="color:#ff3c00;">[ID]</span> Закрепление уникального цифрового позывного навечно.</li>
                <li><span style="color:#ff3c00;">[$]</span> Фиксация стоимости владения до релиза.</li>
                <li><span style="color:#ff3c00;">[AI]</span> Приоритетный доступ к нейросетевым функциям.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    with st.form("main_form"):
        st.markdown('<p style="font-family: Orbitron; color: #888; margin-bottom: 25px; text-align: center;">// ТЕРМИНАЛ ВВОДА ДАННЫХ //</p>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            first_name = st.text_input("ИМЯ ПИЛОТА")
            phone = st.text_input("КАНАЛ СВЯЗИ (ТЕЛЕФОН)")
        with c2:
            last_name = st.text_input("ФАМИЛИЯ")
            email = st.text_input("ЭЛЕКТРОННАЯ ПОЧТА")
            
        st.markdown('<hr style="border-color: #ff3c00; opacity: 0.2; margin: 30px 0;">', unsafe_allow_html=True)
        st.markdown('<p style="font-family: Orbitron; color: #ff3c00; margin-bottom: 20px;">// КОНФИГУРАЦИЯ БОРТА</p>', unsafe_allow_html=True)
        
        c3, c4 = st.columns([1, 2])
        with c3:
            board_num = st.text_input("ЖЕЛАЕМЫЙ ID БОРТА", placeholder="007")
        with c4:
            tier = st.selectbox("УРОВЕНЬ ДОСТУПА", ["TITAN (Founder Status // VIP)", "HEAVY (Professional)", "STANDARD (Базовый)"])
            
        st.write("\n" * 3)
        # Кнопка-рычаг
        submit = st.form_submit_button("ЗАПУСТИТЬ ПРОТОКОЛ РЕГИСТРАЦИИ ››")
        
        if submit:
            if first_name and email and phone and board_num:
                with st.spinner("ШИФРОВАНИЕ ДАННЫХ..."):
                    save_lead(first_name, last_name, phone, email, board_num, tier)
                    time.sleep(2) # Эффект сложной работы
                
                st.success(f"ДОСТУП РАЗРЕШЕН. БОРТ MAX-{board_num} ЗАКРЕПЛЕН В СИСТЕМЕ.")
                # Эффектный финал
                st.markdown("""
                    <div style='background: rgba(0,229,255,0.1); border: 2px solid #00e5ff; padding: 20px; text-align: center; margin-top: 20px;'>
                        <h3 style='color: #00e5ff; margin:0;'>ДОБРО ПОЖАЛОВАТЬ В ЭЛИТУ.</h3>
                        <p style='margin:0;'>Ожидайте зашифрованный пакет инструкций на {email}</p>
                    </div>
                """.format(email=email), unsafe_allow_html=True)
                st.balloons()
            else:
                st.error("ОШИБКА: НЕПОЛНЫЕ ДАННЫЕ ТЕЛЕМЕТРИИ. ПОВТОРИТЕ ВВОД.")

# --- ADMIN PANEL (Скрыта внизу) ---
st.write("\n" * 10)
st.divider()
with st.expander("🔐 СИСТЕМНЫЙ АДМИНИСТРАТОР (Вход по ключу)"):
    pwd = st.text_input("Пароль доступа", type="password")
    if pwd == "max_vip":
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.write("### РЕЕСТР ПИЛОТОВ")
            # Стилизация таблицы под темный терминал
            st.dataframe(df.style.set_properties(**{
                'background-color': '#0a0a0a',
                'color': '#00e5ff',
                'border-color': '#333',
                'font-family': 'Roboto Mono'
            }))
            st.download_button("ЭКСПОРТ ДАННЫХ (CSV)", df.to_csv(index=False).encode('utf-8'), "leads.csv")
        else:
            st.warning("Реестр пуст")
