import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="AI Cybersecurity Defense Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for "Professional Polish" Aesthetic
st.markdown("""
<style>
    /* Main Background and Text */
    .stApp {
        background-color: #0f1117;
        color: #e2e8f0;
    }
    
    /* Global Font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #1e2129;
        border: 1px solid #334155;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
    }
    
    div[data-testid="stMetricLabel"] p {
        color: #94a3b8 !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    div[data-testid="stMetricValue"] div {
        color: #ffffff !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }

    /* Attack Notification */
    .attack-alert {
        background-color: rgba(69, 10, 10, 0.3);
        border: 1px solid rgba(239, 68, 68, 0.5);
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.1);
    }
    
    .attack-text {
        color: #ef4444;
        font-size: 1.8rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -0.025em;
    }

    /* Sidebar/Header info */
    .header-info {
        background-color: #1e2129;
        border-bottom: 1px solid #334155;
        padding: 1rem 2rem;
        margin: -4rem -4rem 2rem -4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# Simulation Logic
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Time', 'Rate'])

# Generate random data
# Mengatur simulasi jumlah request login dalam kurun < 3 detik
request_rate = random.randint(1, 20) # Angka acak dari 1 sampai 20 percobaan

# Jika percobaan login (request rate) di atas 10 kali dalam window waktu tersebut
if request_rate > 10:
    status = "ATTACK"
    login_attempts = request_rate # Menyamakan metrik biar sinkron
    status_color = "#ef4444" 
else:
    status = "NORMAL"
    login_attempts = request_rate
    status_color = "#10b981"

# Update history (keep last 20 points)
current_time = datetime.now().strftime("%H:%M:%S")
new_row = pd.DataFrame({'Time': [current_time], 'Rate': [request_rate]})
st.session_state.history = pd.concat([st.session_state.history, new_row]).tail(20)

# Dashboard Layout
# --- Header ---
st.markdown(f"""
<div class="header-info">
    <div>
        <h1 style="margin:0; font-size: 1.5rem; color: white;">AI Cybersecurity Defense Dashboard</h1>
        <p style="margin:0; font-size: 0.7rem; color: #94a3b8; font-family: monospace;">REAL-TIME MONITORING SYSTEM (SIMULATION MODE)</p>
    </div>
    <div style="display: flex; align-items: center; gap: 15px;">
        <div style="background-color: #2d323e; border: 1px solid #475569; padding: 4px 12px; border-radius: 4px; display: flex; align-items: center; gap: 8px;">
            <div style="width: 8px; height: 8px; border-radius: 50%; background-color: {status_color}; animation: pulse 2s infinite;"></div>
            <span style="font-size: 0.7rem; font-weight: bold; color: #cbd5e1; letter-spacing: 0.1em;">SYSTEM {status}</span>
        </div>
        <div style="font-size: 0.7rem; color: #64748b; font-family: monospace;">UPTIME: 00:42:15</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Top Metrics ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Login Attempts", login_attempts, delta=f"{random.randint(1, 5)} new", delta_color="inverse" if login_attempts > 3 else "normal")

with col2:
    st.metric("Request Rate", f"{request_rate} ops/s", delta=f"{random.randint(-10, 20)} flux")

with col3:
    health_score = 24 if status == "ATTACK" else 98
    st.metric("Global Health Score", f"{health_score}%", delta="Critical" if status == "ATTACK" else "Optimal")

# --- Status Alert Bar ---
if status == "ATTACK":
    st.markdown("""
    <div class="attack-alert">
        <div style="background-color: #ef4444; padding: 12px; border-radius: 50%; flex-shrink: 0;">
            <svg style="width: 32px; height: 32px; color: white;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
        </div>
        <div>
            <div class="attack-text">SYSTEM STATUS: ATTACK DETECTED</div>
            <p style="margin:0; color: #fecaca; opacity: 0.7; font-size: 0.9rem;">Anomalous traffic patterns identified. Automated mitigation protocols engaged.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Main Visuals ---
chart_col, log_col = st.columns([3, 2])

with chart_col:
    st.markdown('<p style="font-size: 0.7rem; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Network Ingress Velocity (3s update)</p>', unsafe_allow_html=True)
    st.line_chart(st.session_state.history.set_index('Time'), color="#06b6d4" if status == "NORMAL" else "#ef4444")

with log_col:
    st.markdown('<p style="font-size: 0.7rem; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Security Activity Log</p>', unsafe_allow_html=True)
    
    # Generate dummy logs
    log_data = []
    events = ["NORMAL_REQ", "THREAT_BLOCK", "LOGIN_FAIL", "PORT_SCAN", "SYS_RECOVERY"]
    for i in range(10):
        ev = random.choice(events) if i > 0 else ("THREAT_BLOCK" if status == "ATTACK" else "NORMAL_REQ")
        log_data.append({
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Event": ev,
            "Details": f"ID: {random.randint(1000, 9999)}"
        })
    
    df_logs = pd.DataFrame(log_data)
    st.dataframe(df_logs, width='stretch', hide_index=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; border-top: 1px solid #334155; margin-top: 2rem; color: #475569; font-size: 0.6rem; letter-spacing: 0.4em; font-weight: bold;">
    CYBER DEFENSE COMMAND CENTER &copy; 2026
</div>
""", unsafe_allow_html=True)

# Auto Refresh logic
time.sleep(3)
st.rerun()
