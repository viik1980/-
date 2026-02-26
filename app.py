import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- СИСТЕМНАЯ КОНФИГУРАЦИЯ ---
# Меняем иконку страницы на что-то более кибернетическое
st.set_page_config(page_title="D.MAX | NEURAL NEXUS", page_icon="🧠", layout="wide")
DB_FILE = "max_titan_registry.csv"

# --- ДИЗАЙН "NEON FUTURE" (CYAN, PURPLE, CARBON, DIFFUSION) ---
st.markdown("""
    <style>
    /* Импорт футуристичных шрифтов */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* --- ГЛОБАЛЬНЫЙ ФОН И АТМОСФЕРА --- */
    .stApp {
        background-color: #020205; /* Почти черный */
        background-image: 
            /* Радиальное свечение от центра в цветах логотипа */
            radial-gradient(circle at 50% 30%, rgba(189, 0, 255, 0.15), rgba(0, 242, 255, 0.05), transparent 70%),
            /* Текстура глубокого карбона */
            repeating-linear-gradient(45deg, #0a0a0a 0px, #0a0a0a 2px, #050505 2px, #050505 8px);
        color: #e0e0e0;
        font-family: 'Rajdhani', sans-serif; /* Технологичный, но читаемый шрифт */
    }

    /* --- ЭФФЕКТЫ СТЕКЛА И СВЕЧЕНИЯ (ГЛАВНЫЙ СТИЛЬ ПАНЕЛЕЙ) --- */
    .neon-card {
        background: rgba(10, 10, 15, 0.7); /* Темное стекло */
        backdrop-filter: blur(20px); /* Сильное размытие фона */
        border-radius: 25px;
        padding: 40px;
        margin: 25px 0;
        border: 1px solid rgba(255, 255, 255, 0.05); /* Тонкая рамка */
        /* ДВОЙНОЕ СВЕЧЕНИЕ: Циан + Фиолетовый с рассеиванием */
        box-shadow: 
            0 0 30px rgba(0, 242, 255, 0.1), /* Внешний ореол циан */
            inset 0 0 30px rgba(189, 0, 255, 0.05); /* Внутреннее свечение фиолетовый */
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }

    /* Эффект "сканирующего луча" при наведении */
    .neon-card::before {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 242, 255, 0.1), transparent);
        transition: 0.5s;
    }
    .neon-card:hover::before {
        left: 100%;
    }

    .neon-card:hover {
        border-color: rgba(0, 242, 255, 0.5);
        /* Усиление свечения при наведении */
        box-shadow: 
            0 0 50px rgba(0, 242, 255, 0.3),
            inset 0 0 50px rgba(189, 0, 255, 0.1);
        transform: scale(1.01);
    }

    /* --- ТИПОГРАФИКА БУДУЩЕГО --- */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    .gradient-text {
        /* Градиент текста точно как в логотипе: от фиолетового к циану */
        background: linear-gradient(to right, #bd00ff, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        filter: drop-shadow(0 0 10px rgba(189, 0, 255, 0.3));
    }

    .feature-title {
        font-size: 1.5rem;
        color: #00f2ff;
        margin-bottom: 15px;
        text-shadow: 0 0 15px rgba(0, 242, 255, 0.5);
        display: flex;
        align-items: center;
    }

    .feature-desc {
        font-size: 1.1rem;
        line-height: 1.7;
        color: #ccc;
        font-weight: 500;
    }

    /* Акцентные слова в тексте */
    .highlight {
        color: #bd00ff;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(189, 0, 255, 0.4);
    }

    /* --- ФОРМА-ТЕРМИНАЛ --- */
    .stForm {
        background: rgba(5, 5, 10, 0.85) !important;
        backdrop-filter: blur(30px) !important;
        border: 2px solid #bd00ff !important; /* Фиолетовая рамка */
        border-radius: 30px !important;
        padding: 50px !important;
        box-shadow: 0 0 60px rgba(189, 0, 255, 0.2) !important;
    }

    /* Поля ввода в стиле кибер-панк */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: #00f2ff !important;
        border: 1px solid #333 !important;
        border-radius: 5px !important;
        height: 55px;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
        transition: 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00f2ff !important;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4) !important;
    }

    /* КНОПКА ЗАПУСКА (НЕОНОВЫЙ РЕАКТОР) */
    .stButton>button {
        /* Градиент кнопки */
        background: linear-gradient(90deg, #bd00ff, #00f2ff) !important;
        color: #000 !important; /* Черный текст для контраста */
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 1.4rem !important;
        height: 75px;
        border: none !important;
        border-radius: 10px !important;
        letter-spacing: 5px !important;
        transition: 0.4s !important;
        /* Мощное свечение */
        box-shadow: 0 0 40px rgba(189, 0, 255, 0.4), 0 0 80px rgba(0, 242, 255, 0.2) !important;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 60px rgba(189, 0, 255, 0.6), 0 0 120px rgba(0, 242, 255, 0.4) !important;
    }

    /* Разделители */
    hr { border-color: #bd00ff; opacity: 0.3; }
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

# --- HERO SECTION С ЛОГОТИПОМ ---
# Используем колонки для центрирования логотипа
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    # ВАЖНО: Файл logo.png должен лежать рядом с app.py
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown('<h1 style="text-align:center; color:#00f2ff;">ДЕЖУРНЫЙ МАКС</h1>', unsafe_allow_html=True)

st.markdown('<h2 style="text-align:center; font-size: 2rem; margin-top: -20px;"><span class="gradient-text">ПЕРВЫЙ ИИ-КОМПАНЬОН С ДУШОЙ</span></h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#aaa; letter-spacing: 5px; font-family:Orbitron;">ЭТО НЕ ПРИЛОЖЕНИЕ. ЭТО ТВОЕ БУДУЩЕЕ НА ДОРОГЕ.</p>', unsafe_allow_html=True)

st.write("\n" * 4)

# --- РЕАЛЬНОСТЬ ПРОЕКТА ---
st.markdown("""
<div style="text-align:center; padding: 30px; border: 2px solid #bd00ff; border-radius: 20px; background: rgba(189, 0, 255, 0.1); box-shadow: 0 0 30px rgba(189, 0, 255, 0.2);">
    <h3 style="color:#fff; margin:0;">⚠️ СТАТУС ПРОЕКТА: <span style="color:#00f2ff;">АКТИВНОЕ ТЕСТИРОВАНИЕ</span></h3>
    <p style="font-size:1.1rem; margin-top:10px; color:#ddd;">
        Макс — это не концепт. Это реально существующий ИИ, который прямо сейчас обучается на тысячах километров реальных дорог. 
        Мы открываем доступ к "Ядру" только для избранных пилотов, готовых стать частью истории.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("\n" * 3)

# --- БЛОК 1: НЕЙРОСЕТЕВОЙ ТАХОГРАФ ---
st.markdown('<h2 style="text-align:center; font-family:Orbitron; margin-bottom:30px;">// МОДУЛЬ: ПРЕДИКТИВНАЯ НАВИГАЦИЯ</h2>', unsafe_allow_html=True)
c1, c2 = st.columns([1.3, 1])
with c1:
    st.markdown("""
    <div class="neon-card">
        <div class="feature-title">🧠 НЕЙРОСЕТЕВОЙ ТАХОГРАФ</div>
        <p class="feature-desc">
        Макс не просто считает часы. Он <span class="highlight">видит будущее твоего маршрута</span>. 
        Он объединяет данные тахографа, Пакета Мобильности, твою среднюю скорость и окна выгрузки в единый живой график.
        <br><br>
        Тебе не нужно гадать "дотяну ли я". Макс скажет голосом: <i>"До парковки 40 км, у тебя запас 15 минут. Едем, я забронировал место."</i> 
        Или: <i>"Вставай здесь, дальше риск нарушения 90%."</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
with c2:
     st.markdown("""
    <div class="neon-card" style="height: 90%; display:flex; align-items:center; justify-content:center; border-color:#bd00ff;">
        <p style="text-align:center; color:#bd00ff; font-size:1.5rem; font-family:Orbitron;">[ ВИЗУАЛИЗАЦИЯ ВРЕМЕННОГО ПОТОКА ]</p>
    </div>
    """, unsafe_allow_html=True)

# --- БЛОК 2: ЗАЩИТА И ГОЛОС ---
st.write("\n" * 2)
st.markdown('<h2 style="text-align:center; font-family:Orbitron; margin-bottom:30px;">// МОДУЛЬ: ЦИФРОВАЯ БРОНЯ</h2>', unsafe_allow_html=True)

c3, c4 = st.columns(2)

with c3:
    st.markdown("""
    <div class="neon-card">
        <div class="feature-title">⚖️ ЮРИДИЧЕСКИЙ ФАЙРВОЛ (AI-LAWYER)</div>
        <p class="feature-desc">
        Проверка BAG в Германии или жандармы во Франции? Макс берет удар на себя.
        Это твой <span class="highlight">цифровой адвокат</span>. Он знает законы каждой страны ЕС лучше инспектора. 
        Он сам будет общаться с полицией на их языке, оспаривая незаконные требования и защищая твой кошелек. 
        Ты больше не один против системы.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="neon-card">
        <div class="feature-title">🎙️ ГОЛОСОВОЙ ИНТЕРФЕЙС С ДУШОЙ</div>
        <p class="feature-desc">
        Забудь про кнопки. Макс понимает естественную речь. Вкратце опиши проблему: <i>"Макс, найди сервис, колесо спускает"</i> — 
        и он не просто найдет, он <span class="highlight">сам позвонит туда</span> на местном языке и договорится о визите. 
        Это не голосовой помощник. Это твой напарник.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- ТЕРМИНАЛ РЕГИСТРАЦИИ ---
st.write("\n" * 5)
st.markdown('<h2 style="text-align:center; font-size:3rem; letter-spacing:10px;"><span class="gradient-text">ДОСТУП К ЯДРУ СИСТЕМЫ</span></h2>', unsafe_allow_html=True)

_, col_form_center, _ = st.columns([1, 2, 1])

with col_form_center:
    with st.form("titan_id_terminal"):
        st.markdown("<p style='text-align:center; color:#00f2ff; font-family:Orbitron; letter-spacing:3px;'>ИНИЦИАЛИЗАЦИЯ ПИЛОТА НОВОГО ПОКОЛЕНИЯ</p>", unsafe_allow_html=True)
        st.write("\n")
        
        c_n, c_s = st.columns(2)
        with c_n:
            name = st.text_input("ИМЯ")
            phone = st.text_input("ТЕЛЕФОН")
        with c_s:
            surname = st.text_input("ФАМИЛИЯ")
            email = st.text_input("E-MAIL")
            
        st.write("---")
        # Добавил выбор роли, чтобы подчеркнуть важность тестеров
        role = st.radio("ЖЕЛАЕМАЯ РОЛЬ В ПРОЕКТЕ:", ["ПИЛОТ-ИСПЫТАТЕЛЬ (Alpha Group)", "РАННИЙ ДОСТУП (Pre-order)"], horizontal=True)
        board_id = st.text_input("ЖЕЛАЕМЫЙ ID БОРТА (3 цифры)", placeholder="777")

        
        st.write("\n" * 3)
        
        # Кнопка-реактор
        if st.form_submit_button("АКТИВИРОВАТЬ НЕЙРОСВЯЗЬ ››"):
            if name and email and board_id:
                with st.spinner("СИНХРОНИЗАЦИЯ С ИИ-ЯДРОМ..."):
                    time.sleep(2.5) # Эффект сложного процесса
                st.success(f"ПРОТОКОЛ ПРИНЯТ. ДОБРО ПОЖАЛОВАТЬ В БУДУЩЕЕ, БОРТ {board_id}!")
                st.balloons()
            else:
                st.error("ОШИБКА: НЕДОСТАТОЧНО ДАННЫХ ДЛЯ ГЕНЕРАЦИИ КЛЮЧА")

# --- FOOTER ---
st.write("\n" * 10)
st.markdown("<div style='text-align:center; border-top: 1px solid #333; padding-top:20px; color:#666; font-family:Orbitron;'>D.MAX PROJECT // CREATING THE FUTURE OF TRANSPORT // 2026</div>", unsafe_allow_html=True)


