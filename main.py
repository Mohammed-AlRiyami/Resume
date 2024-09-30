import streamlit as st
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# --- PAGE SETUP --- 

about_page = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,
)

project_1_page = st.Page(
    page = "views/dashboard.py",
    title = "Activity Dashboard",
    icon = ":material/bar_chart:",
)

project_2_page = st.Page(
    page = "views/chatbot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:",
)


# --- NAVIGATION SETUP ---
pg = st.navigation(
    {
        "Info":[about_page],
        "Others":[project_1_page, project_2_page],    
    }
)
pg.run()

# --- SHARED FOR ALL PAGES ---
st.logo("assets/logo.png")
st.sidebar.text("Created and Designed by Mo🤠")









