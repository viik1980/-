import streamlit as st
import pandas as pd
import datetime
import os
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="MAX | SYSTEM CORE", page_icon="💠", layout="wide")

DB_FILE = "max_leads_2026.csv"

# -------------------- SAVE FUNCTION --------------------
def save_lead(fname, lname, phone, email, board, tier):
    new_data = pd.DataFrame([[ 
        datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        fname, lname, phone, email, board, tier
    ]], columns=['Дата','Имя','Фамилия','Телефон','Email','Борт-номер','Пакет'])

    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# -------------------- PREMIUM CSS --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

.stApp {
    background: radial-gradient(circle at top, #0f1115, #000);
    color: #eaeaea;
    font-family: 'Orbitron', sans-serif;
}

.hero {
    text-align:center;
    font-size:5rem;
    font-weight:900;
    background: linear-gradient(90deg,#ffffff,#cfd8dc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    letter-spacing:8px;
}

.subtitle {
    text-align:center;
    color:#7dd3fc;
    letter-spacing:4px;
    margin-bottom:40px;
}

.glass {
    backdrop-filter: blur(20px);
    background: rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.1);
    padding:40px;
    border-radius:20px;
}

.stButton > button {
    height:65px;
    font-size:1.2rem;
    font-weight:700;
    border-radius:15px;
    background: linear-gradient(90deg,#cfd8dc,#90a4ae);
    color:black;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HERO --------------------
st.markdown('<div class="hero">DEЖУРНЫЙ MAX</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">SYSTEM CORE 2032 // PLATINUM ACCESS</div>', unsafe_allow_html=True)

st.divider()

# -------------------- 3D CARD --------------------
components.html("""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
body { margin:0; overflow:hidden; background:transparent;}
</style>
</head>
<body>
<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 600/400, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(600, 400);
document.body.appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(3,2,0.1);
const material = new THREE.MeshPhysicalMaterial({
    color:0xe5e4e2,
    metalness:1,
    roughness:0.25,
    clearcoat:1,
    clearcoatRoughness:0.1
});

const card = new THREE.Mesh(geometry, material);
scene.add(card);

camera.position.z = 5;

function animate(){
    requestAnimationFrame(animate);
    card.rotation.y += 0.01;
    renderer.render(scene,camera);
}
animate();
</script>
</body>
</html>
""", height=420)

st.divider()

# -------------------- FORM --------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

with st.form("reg"):
    col1, col2 = st.columns(2)

    with col1:
        first = st.text_input("ИМЯ")
        phone = st.text_input("ТЕЛЕФОН")

    with col2:
        last = st.text_input("ФАМИЛИЯ")
        email = st.text_input("EMAIL")

    board = st.text_input("ID БОРТА")
    tier = st.selectbox("УРОВЕНЬ", [
        "TITAN (Founder)",
        "HEAVY (Pro)",
        "STANDARD"
    ])

    submit = st.form_submit_button("АКТИВИРОВАТЬ ДОСТУП")

    if submit:
        if first and phone and email and board:
            with st.spinner("ГРАВИРОВКА ПЛАТИНЫ..."):
                save_lead(first,last,phone,email,board,tier)
                time.sleep(2)

            st.success(f"MAX-{board} АКТИВИРОВАН")
            st.balloons()

            components.html(f"""
            <div style="text-align:center;margin-top:20px;">
                <h2 style="color:#7dd3fc;">ЛАЗЕРНАЯ ГРАВИРОВКА ID MAX-{board}</h2>
                <div style="height:4px;background:red;animation:laser 1s linear infinite;"></div>
            </div>
            <style>
            @keyframes laser {{
                0% {{opacity:0.2;}}
                50% {{opacity:1;}}
                100% {{opacity:0.2;}}
            }}
            </style>
            """, height=150)

        else:
            st.error("ЗАПОЛНИ ВСЕ ДАННЫЕ")

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# -------------------- ADMIN --------------------
with st.expander("🔐 ADMIN"):
    pwd = st.text_input("Пароль", type="password")
    if pwd == "max_vip":
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.dataframe(df)
            st.download_button("Скачать CSV", df.to_csv(index=False), "leads.csv")
        else:
            st.warning("Нет данных")
