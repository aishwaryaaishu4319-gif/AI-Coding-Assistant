import streamlit as st
from assistant import generate_response

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Coding Assistant Pro",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Session State ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "requests" not in st.session_state:
    st.session_state.requests = 0

# ---------------- Title ----------------
st.title("🤖 AI Coding Assistant Pro")
st.markdown("### Your Personal AI Programming Assistant")

st.divider()

# ---------------- Dashboard ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📈 Total Requests", st.session_state.requests)

with col2:
    st.metric("📂 Uploaded Files", len(st.session_state.history))

with col3:
    st.metric("⚡ AI Features", "6")

st.divider()

# ---------------- Sidebar ----------------
st.sidebar.title("⚙️ AI Features")

feature = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Code Generation",
        "Code Explanation",
        "Bug Detection",
        "Code Conversion",
        "Documentation Generator",
        "Unit Test Generator"
    ]
)

language = st.sidebar.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "SQL",
        "HTML",
        "CSS",
        "React",
        "NodeJS"
    ]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Code File",
    type=["py", "java", "cpp", "c", "js", "txt"]
)

# ---------------- Input ----------------
if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    st.success("✅ File Uploaded Successfully")
else:
    code = st.text_area(
        "Enter your code or prompt",
        height=300
    )

# ---------------- Generate ----------------
if st.button("🚀 Generate Response", use_container_width=True):

    if code.strip() == "":
        st.warning("Please enter code or prompt.")
        st.stop()

    prompt = f"""
Feature:
{feature}

Programming Language:
{language}

User Input:
{code}

Provide the best response.
"""

    with st.spinner("AI is Thinking..."):

        result = generate_response(prompt)

    st.session_state.requests += 1

    st.session_state.history.append(
        {
            "Feature": feature,
            "Language": language,
            "Response": result
        }
    )

    st.success("Completed Successfully")

    st.subheader("🤖 AI Response")

    st.code(result)

    st.download_button(
        "⬇ Download Response",
        result,
        file_name="response.txt"
    )

# ---------------- History ----------------
st.divider()

st.subheader("📜 History")

for item in reversed(st.session_state.history):

    with st.expander(f"{item['Feature']} ({item['Language']})"):
        st.code(item["Response"])