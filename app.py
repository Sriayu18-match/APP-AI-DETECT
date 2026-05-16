import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Secure Login System",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling to match the "Sleek Interface" and Dark Theme
st.markdown("""
<style>
    /* Dark Theme Base */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Center the login container */
    .main .block-container {
        max-width: 500px;
        padding-top: 5rem;
    }

    /* Input styling */
    .stTextInput > div > div > input {
        background-color: #0e1117 !important;
        color: white !important;
        border: 1px solid #414552 !important;
        border-radius: 8px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6 !important;
    }

    /* Button styling */
    div.stButton > button:first-child {
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 500 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.1) !important;
    }
    
    div.stButton > button:hover {
        background-color: #ff3333 !important;
        box-shadow: 0 6px 16px rgba(255, 75, 75, 0.2) !important;
        transform: translateY(-1px) !important;
    }

    /* Card simulation */
    .login-card {
        background-color: #262730;
        border: 1px solid #414552;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    /* Sidebar info simulation */
    .system-status {
        opacity: 0.5;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-top: 2rem;
        text-align: center;
    }

    /* Header styling */
    .header-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .header-icon {
        display: inline-block;
        padding: 0.75rem;
        border-radius: 12px;
        background-color: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.2);
        margin-bottom: 1rem;
        color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

# App Content
def main():
    # Header
    st.markdown("""
        <div class="header-container">
            <div class="header-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
            </div>
            <h1 style="font-size: 1.8rem; font-weight: 600; margin-bottom: 0.2rem;">Secure Login System</h1>
            <p style="color: #94a3b8; font-size: 0.9rem;">Enter your credentials to access the terminal</p>
        </div>
    """, unsafe_allow_html=True)

    # Login Form
    with st.container():
        # Streamlit doesn't have a direct "card" component, so we use a container
        # with columns for spacing if we were doing layout, but here we use the CSS injection
        
        username = st.text_input("Username", placeholder="admin_root")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        if st.button("Login to Dashboard", use_container_width=True):
            with st.spinner("Processing authentication..."):
                time.sleep(1.5)
                st.error("Invalid username or password", icon="🚨")

    # Footer / Infrastructure Info
    st.markdown("""
        <div class="system-status">
            Streamlit Infrastructure v4.2.1-stable<br>
            Node: 192.168.1.104 | Region: US-EAST-1
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
