import streamlit as st

# ---- HEADER ----
st.title("Ruphashinee A/P Kandasamy")
st.subheader("Final Year Student | Bachelor of Information Technology")
st.markdown("---")

# ---- CONTACT ----
st.header("📌 Contact Information")
st.write("📧 Email: ruphashinee72@gmail.com")
st.write("📱 Phone: 016-5421464")
st.write("🔗 LinkedIn: [Ruphashinee Kandasamy](https://www.linkedin.com/in/ruphashinee-kandasamy-aa0623265)")

# ---- ABOUT ME ----
st.header("🙋 About Me")
st.write(
    "I am a passionate and motivated final-year student pursuing a **Bachelor of Information Technology** "
    "at Universiti Malaysia Kelantan. I am eager to apply my knowledge in software development, IoT systems, "
    "and data analytics to contribute to innovative projects. I am committed to continuous learning and "
    "developing both technical and interpersonal skills to build a successful career in IT."
)

# ---- EDUCATION ----
st.header("🎓 Education")
st.write("**Bachelor of Information Technology** – Universiti Malaysia Kelantan (2022 – Present)")
st.write("Key Areas: IoT Systems, Machine Learning, Database Systems, Software Engineering")

# ---- SKILLS ----
st.header("🛠️ Skills")
col1, col2 = st.columns(2)
with col1:
    st.write("- Python, Java, C++")
    st.write("- HTML, CSS, JavaScript")
    st.write("- SQL & Databases")
with col2:
    st.write("- IoT Development (Arduino, NodeMCU)")
    st.write("- Data Analysis & Visualization")
    st.write("- Problem-Solving & Team Collaboration")

# ---- PROJECTS ----
st.header("🚀 Projects")
st.subheader("1. Solar-Powered Smart Greenhouse System")
st.write(
    "- Developed an IoT-based greenhouse farming system using Arduino Mega and NodeMCU\n"
    "- Integrated sensors (DHT11, BH1750, ACS712) for automation\n"
    "- Enabled real-time monitoring through a cloud dashboard"
)

st.subheader("2. FBMKLCI Stock Index Forecasting (LSTM)")
st.write(
    "- Built a time-series forecasting model using LSTM\n"
    "- Conducted data preprocessing and Exploratory Data Analysis (EDA)\n"
    "- Improved prediction accuracy through deep learning techniques"
)

# ---- ACHIEVEMENTS ----
st.header("🏆 Achievements")
st.write("- Dean’s List Award (2023, 2024)")
st.write("- Best IoT Project – Faculty Innovation Showcase 2024")

# ---- EXTRA ----
st.header("🌟 Additional Information")
st.write("- Languages: English, Tamil, Malay")
st.write("- Interests: Technology, Research, Sustainable Agriculture, Innovation")

# ---- FOOTER ----
st.markdown("---")
st.write("Created with ❤️ using [Streamlit](https://streamlit.io/)") 
