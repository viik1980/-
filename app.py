import streamlit as st
import pandas as pd
import datetime
import os
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="MAX | Platinum Core")

DB_FILE = "max_leads_2026.csv"

# ---------------- SAVE ----------------
def save_lead(fname, lname, phone, email, board, tier):
    new_data = pd.DataFrame([[ 
        datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        fname, lname, phone, email, board, tier
    ]], columns=['Дата','Имя','Фамилия','Телефон','Email','Борт-номер','Пакет'])

    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# ---------------- PREMIUM GLOBAL STYLE ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

.stApp {
    background:
    radial-gradient(circle at 20% 20%, #1a1f25 0%, transparent 40%),
    radial-gradient(circle at 80% 80%, #101418 0%, transparent 40%),
    #000000;
    color: #f5f5f5;
    font-family: 'Orbitron', sans-serif;
}

.title {
    text-align:center;
    font-size:5rem;
    font-weight:900;
    letter-spacing:8px;
    background: linear-gradient(90deg,#ffffff,#9e9e9e);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle {
    text-align:center;
    color:#8be9fd;
    letter-spacing:4px;
    margin-bottom:40px;
}

.card-box {
    backdrop-filter: blur(20px);
    background: rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    padding:30px;
    border-radius:20px;
    transition:0.3s;
}
.card-box:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.08);
}

.stButton > button {
    height:70px;
    border-radius:20px;
    font-size:1.2rem;
    font-weight:700;
    background:linear-gradient(90deg,#ffffff,#cfd8dc);
    color:black;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown('<div class="title">DEЖУРНЫЙ MAX</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">PLATINUM ACCESS SYSTEM</div>', unsafe_allow_html=True)

# ---------------- 3D SCENE (ВСЕГДА ВИДНА) ----------------
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

let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(60, window.innerWidth/500, 0.1, 1000);
let renderer = new THREE.WebGLRenderer({alpha:true, antialias:true});
renderer.setSize(window.innerWidth, 500);
document.body.appendChild(renderer.domElement);

let light = new THREE.PointLight(0xffffff,1.5);
light.position.set(5,5,5);
scene.add(light);

let geometry = new THREE.BoxGeometry(5,3,0.2);
let material = new THREE.MeshPhysicalMaterial({
    color:0xe5e4e2,
    metalness:1,
    roughness:0.2,
    clearcoat:1
});
let card = new THREE.Mesh(geometry,material);
scene.add(card);

camera.position.z = 8;

// ---------- LASER ----------
function laserEffect(){
    let laserGeo = new THREE.CylinderGeometry(0.03,0.03,6);
    let laserMat = new THREE.MeshBasicMaterial({color:0xff0000});
    let beam = new THREE.Mesh(laserGeo,laserMat);
    beam.rotation.z = Math.PI/2;
    beam.position.y = 1.4;
    scene.add(beam);

    let sparks = [];
    for(let i=0;i<50;i++){
        let sparkGeo = new THREE.SphereGeometry(0.03);
        let sparkMat = new THREE.MeshBasicMaterial({color:0xffaa00});
        let spark = new THREE.Mesh(sparkGeo,sparkMat);
        spark.position.set(0,1.4,0);
        scene.add(spark);
        sparks.push(spark);
    }

    let pos = -3;
    let interval = setInterval(()=>{
        beam.position.x = pos;
        sparks.forEach(s=>{
            s.position.x = pos;
            s.position.y += (Math.random()-0.5)*0.2;
        });
        pos+=0.1;
        if(pos>3){
            clearInterval(interval);
            scene.remove(beam);
            sparks.forEach(s=>scene.remove(s));
        }
    },20);
}

setTimeout(laserEffect,2000);

// ---------- ANIMATION ----------
function animate(){
    requestAnimationFrame(animate);
    card.rotation.y += 0.005;
    renderer.render(scene,camera);
}
animate();

</script>
</body>
</html>
""", height=520)

st.divider()

# ---------------- FEATURES ----------------
st.markdown("## ПРЕИМУЩЕСТВА ПЛАТИНОВОГО ДОСТУПА")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card-box"><h3>ANTI-SHF AI</h3><p>Интеллектуальный контроль РТО. Минимизация штрафов. Автоматический анализ тахографа.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-box"><h3>FATIGUE CONTROL</h3><p>Предиктивная модель усталости. Защита водителя. Безопасность экипажа.</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card-box"><h3>ELITE STATUS</h3><p>Закрытый клуб пилотов. Уникальный цифровой ID. Приоритетный доступ к обновлениям.</p></div>', unsafe_allow_html=True)

st.divider()

# ---------------- FORM ----------------
st.markdown("## ВХОД В СИСТЕМУ")

with st.form("reg"):
    col1, col2 = st.columns(2)
    with col1:
        first = st.text_input("Имя")
        phone = st.text_input("Телефон")
    with col2:
        last = st.text_input("Фамилия")
        email = st.text_input("Email")

    board = st.text_input("Желаемый ID")
    tier = st.selectbox("Пакет", ["TITAN","HEAVY","STANDARD"])

    submit = st.form_submit_button("АКТИВИРОВАТЬ ДОСТУП")

    if submit:
        if first and phone and email and board:
            save_lead(first,last,phone,email,board,tier)
            st.success(f"Добро пожаловать, MAX-{board}")
        else:
            st.error("Заполни все поля")
