import streamlit as st
import base64
from pathlib import Path

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Emrald Regin HR — Portfolio",
                   layout="wide")

PROFILE_IMG = Path("emrald.jpeg")
RESUME_FILE = Path("resume.pdf")

def encode_file(path):
    return base64.b64encode(open(path, "rb").read()).decode()


# ---------------- GLOBAL MINIMAL CSS ----------------
st.markdown("""
<style>
/* Global background & font */
body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    background: #eef2f7;   /* Light grey-blue background */
    color: #1a1a1a !important;  /* Force all text to dark */
}

/* Override ALL text colors Streamlit sets */
* {
    color: #1a1a1a !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: #0d47a1 !important;  /* Deep blue */
    font-weight: 800;
}

/* Content cards */
.section {
    background: #ffffff;
    padding: 25px;
    border-radius: 14px;
    border: 1px solid #d9d9d9;
    margin-bottom: 25px;
    color: #1a1a1a !important;
}

/* Card titles */
.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #0d47a1 !important;
    margin-bottom: 8px;
}

/* Button styling */
.btn {
    background: #0d47a1;
    color: white !important;
    padding: 12px 22px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}

/* Image rounding */
img {
    border-radius: 14px;
}

/* Center class */
.center {
    text-align: center;
}
</style>

""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='center'>Emrald Regin H R</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='center'>Electrical & Electronics Engineering — TCE Madurai</h3>", unsafe_allow_html=True)

# PHOTO + RESUME BUTTON
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if PROFILE_IMG.exists():
        img_b64 = encode_file(PROFILE_IMG)
        st.markdown(
            f"<p class='center'><img src='data:image/jpeg;base64,{img_b64}' width='230'></p>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Add emrald.jpeg to show profile image.")

    if RESUME_FILE.exists():
        resume_b64 = encode_file(RESUME_FILE)
        st.markdown(
            f"<p class='center'><a class='btn' href='data:application/pdf;base64,{resume_b64}' "
            f"download='Emrald_Regin_Resume.pdf'>📄 Download Resume</a></p>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Add resume.pdf to enable resume download.")

st.write("---")


# ---------------- ABOUT ----------------
st.subheader("About Me")
st.markdown("""
<div class='section'>
I am an innovative Electrical and Electronics Engineering student specializing in 
Embedded Systems, IoT, and AI-based solutions.  
With strong experience in hackathons, research, and leadership roles,  
I focus on building impactful technologies for real-world applications.
</div>
""", unsafe_allow_html=True)


# ---------------- ACADEMICS ----------------
st.subheader("Academic Record")
st.markdown("""
<div class='section'>
<b>B.E — Electrical and Electronics Engineering</b><br>
Thiagarajar College of Engineering, Madurai — <b>CGPA: 9.51*</b> (up to 4th sem)<br><br>

<b>Class 12:</b> Carmel Higher Secondary School — 92.33% (2023)<br>
<b>Class 10:</b> Carmel Higher Secondary School — Pass (2021)
</div>
""", unsafe_allow_html=True)


# ---------------- INTEREST AREAS ----------------
st.subheader("Areas of Interest")
st.markdown("""
<div class='section'>
• Embedded Systems & IoT for Human Welfare<br>
• AI/ML for Energy Management<br>
• Microcontrollers<br>
• Real-Time Electrical Systems<br>
• Hackathons & Innovation Challenges  
</div>
""", unsafe_allow_html=True)


# ---------------- TECH SKILLS ----------------
st.subheader("Technical Skills")
st.markdown("""
<div class='section'>
<b>Programming:</b> Basics of Python, MATLAB, C, C++, Java, HTML<br><br>
<b>Tools:</b> MATLAB, Proteus, KiCad, AutoCAD Electrical, easyEDA, Keil, Processing PDE, 
Arduino IDE, PSIM/MULTISIM  
</div>
""", unsafe_allow_html=True)


# ---------------- PROJECTS ----------------
st.subheader("Projects")

projects = {
    "Digi Decelerator – Vehicle Speed Control System (2nd Prize – Titan Idea Harvest)": [
        "RF + RFID-based speed control automation",
        "Relay-based dynamic motor control via ESP32",
        "Won 2nd place at IDEA HARVEST"
    ],
    "Resonix – Safety Device for Hearing Impaired": [
        "ESP8266 + MAX4466 based smart alert wristband",
        "Detects emergency sirens; gives vibration alerts",
        "Showcased at IIC & TCE-TBI"
    ],
    "Near Work Monitor System (ACEi Hackathon with Aravind Eye Hospital)": [
        "Ultrasonic-based eye-distance monitoring",
        "Real-time alerting for safe working distance"
    ],
    "Smart Household Energy Audit App (Energathon '24 – 3rd Prize)": [
        "Android energy monitoring application",
        "UI for tracking & optimizing consumption"
    ],
    "NeuraWatt – AI-Powered Energy Meter (EEE Hackathon – 3rd Prize)": [
        "Predictive AI-based energy meter",
        "Budget alerts + load forecast system"
    ],
    "Ultrasonic RADAR System (TCE-TBI Internship)": [
        "Short-range obstacle detection radar",
        "Built using Arduino + Processing PDE"
    ],
    "Sound-Based Machine Health Monitoring": [
        "AI-based acoustic health monitoring",
        "ML model for anomaly detection"
    ],
    "Deepfake Detection System": [
        "Deep learning model for manipulated media",
        "High accuracy in competition evaluation"
    ]
}

for title, desc in projects.items():
    st.markdown(f"<div class='section'><div class='card-title'>{title}</div>", unsafe_allow_html=True)
    for point in desc:
        st.markdown(f"• {point}")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- INTERNSHIPS ----------------
st.subheader("Internships")
st.markdown("""
<div class='section'>
<b>ISRO IPRC (2 Weeks)</b> — Propulsion systems exposure & engine testing<br><br>
<b>JBJ Scientific (2 Weeks)</b> — IoT sensor calibration + prototype development<br><br>
<b>TCE In-Lab Internship</b> — MATLAB & C/C++ foundations<br><br>
<b>TCE-TBI Internship (Ongoing)</b> — Ultrasonic RADAR system development<br><br>
<b>Research:</b><br>
• NILM — Non-intrusive load monitoring<br>
• DSM — Demand-side management  
</div>
""", unsafe_allow_html=True)


# ---------------- CERTIFICATIONS ----------------
st.subheader("Certifications")
st.markdown("""
<div class='section'>
• MATLAB Onramp  
• Simulink Onramp  
• Symbolic Math with MATLAB  
• Statistics Onramp  
• Simscape Onramp  
• Diploma in Programming (2023)
</div>
""", unsafe_allow_html=True)


# ---------------- LEADERSHIP ----------------
st.subheader("Leadership & Roles")
st.markdown("""
<div class='section'>
• Vice President – IITM Build Club (2025–Present)<br>
• Joint Treasurer – IAEMP<br>
• IETSE Student Member<br>
• IEI Student Member<br>
• IoT Club Student Coordinator<br>
• Core Member – Build Club<br>
• CDC Coordinator<br>
• Class Representative (2023)
</div>
""", unsafe_allow_html=True)


# ---------------- ACHIEVEMENTS ----------------
st.subheader("Achievements")
st.markdown("""
<div class='section'>
• 2nd Place – Titan Idea Harvest<br>
• 3rd Prize – Energathon '24<br>
• 3rd Prize – EEE Hackathon<br>
• Finalist – EDII Hackathon, ACEi Hackathon, Sastra TBI, KARE Hackathon  
• Finalist – TCE Industries Hackathon, Cyber Hackathon, KPR Hackathon  
• Smart India Hackathon — Ongoing  
• MSME Challenge — Ongoing  
</div>
""", unsafe_allow_html=True)


# ---------------- VOLUNTEERING ----------------
st.subheader("Volunteering")
st.markdown("""
<div class='section'>
• Organized 6+ Build Club events<br>
• Organized 3+ IoT Club events<br>
• Active volunteer in department technical events  
</div>
""", unsafe_allow_html=True)


# ---------------- EXTRACURRICULAR ----------------
st.subheader("Extra-Curricular")
st.markdown("""
<div class='section'>
• Chess Player — College Level  
</div>
""", unsafe_allow_html=True)


# ---------------- PERSONAL DETAILS ----------------
st.subheader("Personal Details")
st.markdown("""
<div class='section'>
<b>Date of Birth:</b> 27 March 2006<br>
<b>Age:</b> 19<br>
<b>Gender:</b> Male<br>
<b>Languages:</b> Tamil, English<br><br>

<b>Email:</b> emraldreginhrofficial@gmail.com<br>
<b>Phone:</b> +91 9940896003  
</div>
""", unsafe_allow_html=True)

