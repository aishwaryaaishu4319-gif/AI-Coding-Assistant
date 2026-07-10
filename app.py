import streamlit as st
from assistant import generate_response

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Coding Assistant Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-title{    font-size:40px;
    font-weight:bold;
    color:#4F8BF9;
}
.sub-title{
    font-size:18px;
    color:gray;
}
.feature-box{
    padding:15px;
    border-radius:10px;
    background-color:#f0f2f6;
    text-align:center;
    font-weight:bold;
}
.footer{
    text-align:center;
    color:gray;
    padding-top:20px;
}
            </style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 AI Coding Assistant")

    st.markdown("---")

    feature = st.selectbox(
        "Choose Feature",
        [
            "Code Generation",
            "Code Explanation",
            "Debug Code",
            "Optimize Code",
                        "Generate Test Cases",
            "Convert Code"
        ]
    )

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "C"
        ]
    )

    uploaded_file = st.file_uploader(
        "Upload Source Code",
                type=["py", "java", "cpp", "c", "js", "txt"]
    )

    st.markdown("---")

    st.info("💡 Tip: Paste your code or upload a source file.")

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<p class="main-title">🤖 AI Coding Assistant Pro</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Generate, Explain, Debug and Optimize Code using AI</p>',
    unsafe_allow_html=True
)
st.divider()

# -----------------------------
# Feature Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="feature-box">📖 Explain Code</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="feature-box">🐞 Debug Code</div>',
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        '<div class="feature-box">⚡ Optimize Code</div>',
        unsafe_allow_html=True
    )

st.write("")

# -----------------------------
# Code Input
# -----------------------------
user_input = st.text_area(
    "💻 Enter your code or prompt",
    height=320,
    placeholder="Paste your code here or describe what you want..."
)
# -----------------------------
# File Upload
# -----------------------------
if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    user_input = file_content

    st.success("✅ File uploaded successfully!")

    st.code(file_content, language=language.lower())

st.write("")

# -----------------------------
# Generate Button
# -----------------------------
if st.button("🚀 Generate AI Response", use_container_width=True):

    st.write("Button clicked!")

    if not user_input.strip():
        st.warning("Please enter some code or prompt.")
    else:
        st.write("Calling AI...")

        try:
            response = generate_response(
                prompt=user_input,
                feature=feature,
                language=language
            )

            st.success("AI Response Generated!")

            st.write(response)

        except Exception as e:
            st.error(str(e))
st.divider()

# -----------------------------
# Features Section
# -----------------------------
st.subheader("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("✔ Code Generation")
    st.success("✔ Code Explanation")
    st.success("✔ Debug Code")
    st.success("✔ Code Optimization")

with col2:
    st.success("✔ Generate Test Cases")
    st.success("✔ Multiple Languages")
    st.success("✔ Upload Source Files")
    st.success("✔ AI Powered by Groq")
    st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
<div style="text-align:center;color:gray;padding:20px;">
Developed with ❤️ using Python, Streamlit & Groq AI
</div>
""",
    unsafe_allow_html=True
)