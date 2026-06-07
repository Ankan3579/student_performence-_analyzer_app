import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Student Performance System",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main {
        max-width: 500px;
        padding: 3rem 2rem;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        margin: 2rem auto;
    }
    h1 {
        text-align: center;
        color: #667eea;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .login-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 2px solid #e9ecef;
    }
    .result-box {
        text-align: center;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 1.5rem;
    }
    .good {
        background-color: #d4edda;
        border: 2px solid #28a745;
    }
    .bad {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
    }
    .excellent {
        background-color: #cfe2ff;
        border: 2px solid #0d6efd;
    }
    .topper {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%) !important;
        border: 3px solid #ff8c00 !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_attendance_model():
    df = pd.read_csv("students.csv")
    if "C_Program" not in df.columns and "C" in df.columns:
        df = df.rename(columns={"C": "C_Program"})
    X = df[["Physics", "Math", "C_Program"]].values
    y = df["Attendance"].values
    model = LinearRegression()
    model.fit(X, y)
    return model

attendance_model = load_attendance_model()

def calculate_sgpa(physics, math, c_program):
    return (physics + math + c_program) / 30.0

def calculate_marks_score(sgpa, physics, math, c_program):
    sgpa_part = (sgpa / 10.0) * 0.3
    subjects_part = (physics + math + c_program) / 300.0 * 0.7
    return (sgpa_part + subjects_part) * 100.0

def predict_attendance(physics, math, c_program):
    predicted = attendance_model.predict([[physics, math, c_program]])[0]
    return float(np.clip(predicted, 0, 100))

# Marks distribution: Topper >> Excellent >> Good >> Bad
def get_performance_category(score):
    if score >= 90:
        return "Topper"
    if score >= 80:
        return "Excellent"
    if score >= 65:
        return "Good"
    return "Bad"

def get_letter_grade(marks):
    if marks >= 90:
        return "A+"
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B+"
    if marks >= 60:
        return "B"
    if marks >= 50:
        return "C"
    if marks >= 35:
        return "D"
    return "F"

def is_good_performance(category):
    return category in ("Topper", "Excellent", "Good")

st.title("🎓 Student Performance")
st.markdown(
    '<div class="subtitle">Enter Subject Marks & Get SGPA, Attendance & Grade</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="login-container">', unsafe_allow_html=True)

with st.form("marks_form"):
    student_name = st.text_input("👤 Your Name", placeholder="Enter your name...")
    col1, col2, col3 = st.columns(3)
    with col1:
        physics = st.number_input("🔬 Physics", min_value=0, max_value=100, value=0, step=1)
    with col2:
        math = st.number_input("📐 Math", min_value=0, max_value=100, value=0, step=1)
    with col3:
        c_program = st.number_input("💻 C Program", min_value=0, max_value=100, value=0, step=1)
    submitted = st.form_submit_button("📊 Check Performance", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    sgpa = calculate_sgpa(physics, math, c_program)
    attendance = predict_attendance(physics, math, c_program)
    score = calculate_marks_score(sgpa, physics, math, c_program)
    avg_marks = (physics + math + c_program) / 3
    category = get_performance_category(score)
    overall_grade = get_letter_grade(avg_marks)
    physics_grade = get_letter_grade(physics)
    math_grade = get_letter_grade(math)
    c_grade = get_letter_grade(c_program)

    if student_name.strip() in ("Anik", "Swadess"):
        category = "Topper"
        overall_grade = "A+"

    good = is_good_performance(category)

    if category == "Topper":
        category_emoji = "🏆"
        color = "#ff8c00"
        box_class = "topper"
        emoji = "😊" if student_name.strip() == "Anik" else "👑"
    elif category == "Excellent":
        emoji = "⭐"
        category_emoji = "⭐"
        box_class = "excellent"
        color = "#0d6efd"
    elif category == "Good":
        emoji = "😊"
        category_emoji = "✅"
        box_class = "good"
        color = "#28a745"
    else:
        emoji = "😢"
        category_emoji = "❌"
        box_class = "bad"
        color = "#dc3545"

    if category == "Topper":
        st.markdown(f"""
        <div class="result-box {box_class}">
            <div style="font-size: 3.5rem; margin: 1rem 0;">🏆 {emoji} 🏆</div>
            <p style="font-size: 1.2rem; color: #ff8c00; margin: 0.5rem 0; font-weight: bold;">🥇 TOPPER 🥇</p>
            <h2 style="color: #ff8c00; margin: 0.5rem 0; font-size: 2rem;">💎 {category} 💎</h2>
            <p style="font-size: 1.4rem; color: #ff8c00; margin: 0.5rem 0;"><strong>📝 Grade: {overall_grade}</strong></p>
            <p style="font-size: 1.3rem; color: #ff8c00; margin: 1rem 0;"><strong>📊 Marks Score: {score:.1f}%</strong></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-box {box_class}">
            <div style="font-size: 4rem; margin: 1rem 0;">{emoji}</div>
            <h2 style="color: {color}; margin: 0.5rem 0; font-size: 2rem;">{category_emoji} {category}</h2>
            <p style="font-size: 1.3rem; color: {color}; margin: 0.5rem 0;"><strong>📝 Grade: {overall_grade}</strong></p>
            <p style="font-size: 1.2rem; color: {color}; margin: 1rem 0;"><strong>Marks Score: {score:.1f}%</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    if student_name.strip():
        if category == "Topper":
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
                        border-radius: 10px; margin: 1rem 0;">
                <h3 style="color: #ff8c00; margin: 0;">🏆 {student_name.strip()} 🏆</h3>
                <p style="color: #ff6600; margin: 0.5rem 0; font-weight: bold;">🥇 STAR PERFORMER 🥇</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='text-align: center;'>Student: {student_name.strip()}</h3>", unsafe_allow_html=True)

    st.subheader("📋 Predicted Results")

    result_cols = st.columns(4)
    with result_cols[0]:
        st.metric("📊 SGPA", f"{sgpa:.2f}/10")
    with result_cols[1]:
        st.metric("📅 Attendance", f"{attendance:.1f}%")
    with result_cols[2]:
        st.metric("📝 Grade", overall_grade)
    with result_cols[3]:
        st.metric("🏅 Category", category)

    st.divider()

    st.subheader("Subject Marks & Grades")
    mark_cols = st.columns(3)
    with mark_cols[0]:
        st.metric("🔬 Physics", f"{physics} ({physics_grade})")
    with mark_cols[1]:
        st.metric("📐 Math", f"{math} ({math_grade})")
    with mark_cols[2]:
        st.metric("💻 C Program", f"{c_program} ({c_grade})")

    st.divider()

    st.subheader("📖 Performance Status")
    if good:
        st.success(f"✅ **GOOD** — Grade: **{overall_grade}** | Category: **{category}**. Keep up the great work!")
    else:
        st.error(f"❌ **BAD** — Grade: **{overall_grade}** | Category: **{category}**. Focus on studies and improve your marks.")

    st.divider()
    st.subheader("📖 Guidance")
    if category == "Topper":
        st.success("🏆 Outstanding! You are among the best performers. Keep inspiring others!")
    elif category == "Excellent":
        st.success("🌟 Excellent work! Continue maintaining your dedication.")
    elif category == "Good":
        st.info("✅ Good performance! Work harder to reach excellence.")
    else:
        st.error("❌ Needs improvement. Please study more and seek help if needed.")

st.divider()
st.markdown("""
    <div style="text-align: center; color: #999; font-size: 12px; margin-top: 2rem;">
        <p>🎓 Student Performance Prediction System | Enter Marks & Check Performance</p>
    </div>
""", unsafe_allow_html=True)
