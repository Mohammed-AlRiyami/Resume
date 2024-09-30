from pathlib import Path
import streamlit as st
from PIL import Image
from forms.contacts import contact_form

@st.dialog("Contact Me") 
def show_contact_form():
    contact_form()

# --- PATH SETTINGS ---
current_dir = Path(__file__).resolve().parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles/main.css"
resume_file = current_dir / "assets" / "Al-Riyami, Mohammed Resume.pdf"
profile_pic = current_dir / "assets" / "headshot.png"

# --- GENERAL SETTINGS ----
PAGE_TITLE = "Digtal Resume | Mohammed Al-Riyami"
PAGE_ICON = ":rocket:"
NAME = "Mohammed Al-Riyami"
DESCRIPTION = """ Junior Computer Science student at the University of Wisconsin-Madison | Previous IT intern at Oxy """

EMAIL = "mohammed24alriyami@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/mohammed-al-riyami-1a71482bb/",
    "GitHub" : "https://github.com/Mohammed-AlRiyami"
}
PROJECTS = {
    "🏆 Followed a new approach to scan hardware (i.e CPU, RAM, GPU) for more accute hardware selection during hardware refresh project!" : "https://github.com/Mohammed-AlRiyami",
    "🏆 Building a phenomenal resume website to highlight my work." : "https://github.com/Mohammed-AlRiyami"
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image(profile_pic, width = 240)

with col2:
    st.title(NAME, anchor=False)
    st.write(DESCRIPTION)
    st.download_button(
        label = "📃 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream"
    )
    # st.write("📫",EMAIL)
    
    if st.button("📨 Contact Me"):
        show_contact_form()

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- SOCIAL LINKS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔️ Strong hand on experience on Python, Java, Powershell
    - ✔️ Good understanding of ML algorithm and data structure
    - ✔️ Excellent team-player and project started
    """
)

# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write(
    """
    - 🧑‍💻 Programming: Python, Java,SQL
    - 📊 Data visulization: PowerBi, MS Excel
    - 🔏 Databases: Postgres, MongoDB, MySQL
    """
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")
st.write("🧑🏻‍💻IT Intern | Oxy (Occidental Petroleum) | 05/2024 - 08/2024")
st.write(
    """
        - ▶	Developed a PowerShell script to automate data organization into Excel sheets, decreasing manual processing time by about 50% and increasing data accuracy.
    
        - ▶	Utilized Power BI to create visually appealing dashboards, speeding up decision-making by providing real-time data insights and accelerating report generation.
    
        - ▶	Assisted in imaging PCs, enabling BitLocker, and deploying machines to end users.
    
        - ▶	Adhered to structured procedures for troubleshooting and resolving user machine issues.
    """
)

st.write("---")
st.write("🔬Research Assistant | Ané Lab, UW-Madison | 05/2023 - 12/2023")

st.write(
    """
        - ▶	Prepared plant tissue samples for research experiments, following standardized protocols.
    
        - ▶	Collaborated with a team to streamline sample processing, reducing processing time by 20%.
        
        - ▶	Maintained meticulous records of sample preparation processes, ensuring accuracy.    
    
        - ▶	Actively contributed to research discussions and data analysis during team meetings.    
    """
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")

for project, link in PROJECTS.items():
    st.write(f"[{project}({link})]")