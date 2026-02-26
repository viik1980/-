import streamlit as st
import pandas as pd
import datetime
import os
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="MAX | SYSTEM CORE 2035", page_icon="💎", layout="wide")

DB_FILE = "max_leads_2026.csv"

def save_lead(fname, lname, phone, email, board, tier):
    new_data = pd.DataFrame([[ 
        datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        fname, lname, phone, email, board, tier
    ]], columns=['Дата','Имя','Фамилия','Телефон','Email','Борт-номер','Пакет'])

    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# ---------------- PREMIUM STYLE ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

.stApp {
    background: radial-gradient(circle at center, #0b0f14 0%, #000000 100%);
    color:white;
    font-family:'Orbitron', sans-serif;
}

.title {
    text-align:center;
    font-size:4.5rem;
    font-weight:900;
    background: linear-gradient(90deg,#ffffff,#9e9e9e);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    letter-spacing:10px;
}

.subtitle {
    text-align:center;
    color:#6ee7ff;
    margin-bottom:40px;
    letter-spacing:5px;
}

.glass {
    backdrop-filter: blur(25px);
    background: rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    padding:40px;
    border-radius:25px;
}

.stButton > button {
    height:70px;
    border-radius:20px;
    font-weight:700;
    font-size:1.2rem;
    background:linear-gradient(90deg,#dfe9f3,#ffffff);
    color:black;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">DEЖУРНЫЙ MAX</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">PLATINUM CORE ACTIVATION SYSTEM</div>', unsafe_allow_html=True)

# ---------------- FORM ----------------
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
    tier = st.selectbox("УРОВЕНЬ", ["TITAN","HEAVY","STANDARD"])

    submit = st.form_submit_button("АКТИВИРОВАТЬ ПЛАТИНУ")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- 3D ENGINE ----------------
if submit and first and phone and email and board:

    save_lead(first,last,phone,email,board,tier)

    st.success(f"MAX-{board} REGISTERED")

    components.html(f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
body {{ margin:0; overflow:hidden; background:transparent; }}
</style>
</head>
<body>
<script>

let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(60, 800/500, 0.1, 1000);
let renderer = new THREE.WebGLRenderer({{ alpha:true, antialias:true }});
renderer.setSize(800,500);
document.body.appendChild(renderer.domElement);

let light1 = new THREE.PointLight(0xffffff,1.5);
light1.position.set(5,5,5);
scene.add(light1);

let geometry = new THREE.BoxGeometry(4,2.5,0.15);
let material = new THREE.MeshPhysicalMaterial({{
    color:0xe5e4e2,
    metalness:1,
    roughness:0.2,
    clearcoat:1,
    reflectivity:1
}});
let card = new THREE.Mesh(geometry,material);
scene.add(card);

let loader = new THREE.FontLoader();
loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function(font) {{
    let textGeo = new THREE.TextGeometry("MAX-{board}", {{
        font: font,
        size: 0.4,
        height: 0.05,
    }});
    let textMat = new THREE.MeshStandardMaterial({{ color:0x111111 }});
    let textMesh = new THREE.Mesh(textGeo,textMat);
    textMesh.position.set(-1.8,-0.2,0.08);
    scene.add(textMesh);

    setTimeout(()=> {{
        laser();
    }}, 1000);
}});

function laser(){{
    let laserGeo = new THREE.CylinderGeometry(0.02,0.02,3);
    let laserMat = new THREE.MeshBasicMaterial({{color:0xff0000}});
    let beam = new THREE.Mesh(laserGeo,laserMat);
    beam.rotation.z = Math.PI/2;
    beam.position.y = 1.2;
    scene.add(beam);

    let pos = -2;
    let interval = setInterval(()=> {{
        beam.position.x = pos;
        pos += 0.05;
        if(pos>2){{
            clearInterval(interval);
            scene.remove(beam);
        }}
    }},20);
}}

camera.position.z = 7;

function animate(){{
    requestAnimationFrame(animate);
    card.rotation.y += 0.01;
    renderer.render(scene,camera);
}}
animate();

</script>
</body>
</html>
""", height=520)

elif submit:
    st.error("ЗАПОЛНИ ВСЕ ДАННЫЕ")
