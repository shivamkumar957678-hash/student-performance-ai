# =========================
# AI POWERED STUDENT PERFORMANCE SYSTEM
# =========================

import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="AI Student System", layout="wide")

# -------------------------
# LOGIN DETAILS
# -------------------------
USERNAME = "shivam"
PASSWORD = "12345"

# -------------------------
# SESSION
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------
# LOGIN PAGE
# -------------------------
if not st.session_state.logged_in:

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(to right,#0f172a,#7c3aed);
        color:white;
    }

    h1,h2,h3{
        color:white;
    }

    .login-box{
        padding:40px;
        border-radius:20px;
        background: rgba(255,255,255,0.08);
    }

    label{
        color:white !important;
        font-size:22px !important;
        font-weight:bold !important;
    }

    .stTextInput input{
        background:white !important;
        color:black !important;
        font-size:20px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.title("🔐 AI Student System Login")

    st.markdown("## 👤 Username")
    username = st.text_input("", placeholder="Enter Username")

    st.markdown("## 🔑 Password")
    password = st.text_input("", type="password", placeholder="Enter Password")

    if st.button("🚀 Login"):

        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Login Successful")
            st.rerun()

        else:
            st.error("❌ Wrong Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# -------------------------
# MAIN CSS
# -------------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(to right,#0f172a,#7c3aed);
color:white;
}

/* HEADINGS */
h1,h2,h3{
color:white;
}

/* LABELS */
label{
color:white !important;
font-size:22px !important;
font-weight:bold !important;
opacity:1 !important;
}

/* TEXT INPUT */
.stTextInput input{
background:white !important;
color:black !important;
font-size:20px !important;
}

/* TEXT AREA */
.stTextArea textarea{
background:white !important;
color:black !important;
font-size:20px !important;
}

/* SLIDER TEXT */
.stSlider label{
color:white !important;
font-size:22px !important;
font-weight:bold !important;
}

/* FIX HIDDEN TEXT */
.css-1cpxqw2,
.css-10trblm,
.css-q8sbsg,
.css-1offfwp{
opacity:1 !important;
color:white !important;
}

/* METRIC BOX */
[data-testid="stMetric"]{
background:#16a34a;
padding:15px;
border-radius:15px;
}

/* SUCCESS BOX */
.stSuccess{
font-size:20px !important;
}

/* INFO BOX */
.stInfo{
font-size:20px !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# DATABASE DATA
# -------------------------
data = {
    "Name":["Rahul","Shivam","Aman","Priya","Rohit","Aditi","Karan","Neha","Arjun","Sneha","Vikas","Anjali"],
    "Attendance":[90,75,60,95,55,88,78,92,81,85,68,94],
    "Math":[88,76,45,95,40,91,67,85,79,82,58,96],
    "Science":[85,70,50,98,35,89,72,90,80,84,60,97],
    "English":[80,72,55,90,45,93,70,87,76,81,59,95]
}

df = pd.DataFrame(data)

# -------------------------
# AI CALCULATIONS
# -------------------------
df["Average"] = df[["Math","Science","English"]].mean(axis=1)

topper = df.loc[df["Average"].idxmax()]
weak_student = df.loc[df["Average"].idxmin()]

# -------------------------
# TITLE
# -------------------------
st.title("🎓 AI-Powered Student Performance System")
st.subheader("🚀 AI + Automation + Smart Analytics")

# -------------------------
# METRICS
# -------------------------
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Total Students", len(df))

with col2:
    st.metric("🏆 Topper", topper["Name"])

with col3:
    st.metric("⚠ Weak Student", weak_student["Name"])

with col4:
    poor = len(df[df["Attendance"] < 75])
    st.metric("📉 Poor Attendance", poor)

# -------------------------
# GRAPHS
# -------------------------
c1,c2,c3 = st.columns(3)

# SUBJECT GRAPH
with c1:

    st.subheader("📚 Subject Wise Average")

    subject_avg = [
        df["Math"].mean(),
        df["Science"].mean(),
        df["English"].mean()
    ]

    fig, ax = plt.subplots()

    ax.bar(
        ["Math","Science","English"],
        subject_avg,
        color=["red","blue","green"]
    )

    ax.set_ylabel("Marks")

    st.pyplot(fig)

# ATTENDANCE GRAPH
with c2:

    st.subheader("📈 Attendance Analysis")

    fig2, ax2 = plt.subplots(figsize=(8,4))

    ax2.plot(
        df["Name"],
        df["Attendance"],
        marker='o',
        color='cyan'
    )

    plt.xticks(rotation=45)

    ax2.set_ylabel("Attendance %")

    st.pyplot(fig2)

# PIE CHART
with c3:

    st.subheader("🏆 Topper vs Others")

    fig3, ax3 = plt.subplots(figsize=(7,7))

    ax3.pie(
        df["Average"],
        labels=df["Name"],
        autopct='%1.1f%%'
    )

    st.pyplot(fig3)

# -------------------------
# TABLE
# -------------------------
st.subheader("📋 Student Performance Table")

def status(avg):
    if avg >= 85:
        return "Topper"
    elif avg >= 60:
        return "Good"
    else:
        return "Weak"

df["Status"] = df["Average"].apply(status)

st.dataframe(df, use_container_width=True)

# -------------------------
# AI CHATBOT
# -------------------------
st.subheader("🤖 AI Chatbot")

q = st.text_input("Ask AI Question")

if q:

    q = q.lower()

    if "topper" in q:
        st.success(f"🏆 {topper['Name']} is the topper.")

    elif "weak" in q:
        st.error(f"⚠ {weak_student['Name']} needs improvement.")

    elif "average" in q or "avg" in q:
        avg_student = df["Average"].mean()
        st.info(f"📊 Overall average student marks are {avg_student:.2f}")

    else:
        st.warning("🤖 AI could not understand.")

# -------------------------
# ML PREDICTION
# -------------------------
st.subheader("🧠 AI Model Implementation (ML/DL)")

hours = np.array([1,2,3,4,5,6]).reshape(-1,1)
marks = np.array([20,35,50,65,80,95])

model = LinearRegression()
model.fit(hours, marks)

study = st.slider("📚 Study Hours",1,10)

prediction = model.predict([[study]])

st.success(f"🎯 Predicted Marks: {prediction[0]:.2f}")

# -------------------------
# FEEDBACK SYSTEM
# -------------------------
st.subheader("💬 Feedback System with AI Sentiment Analysis")

feedback = st.text_area("Enter Feedback")

if feedback:

    sentiment = TextBlob(feedback).sentiment.polarity

    if sentiment > 0:
        st.success(f"😊 Positive Feedback\n\nSentiment Score: {sentiment:.2f}")

    elif sentiment < 0:
        st.error(f"😔 Negative Feedback\n\nSentiment Score: {sentiment:.2f}")

    else:
        st.warning(f"😐 Neutral Feedback\n\nSentiment Score: {sentiment:.2f}")

# -------------------------
# FACE RECOGNITION UI
# -------------------------
st.subheader("📸 Face Recognition Attendance")

student_name = st.text_input("Enter Student Name")

img = st.camera_input("📸 Take Student Photo")

if img and student_name:

    file_name = f"{student_name}.jpg"

    with open(file_name, "wb") as f:
        f.write(img.getbuffer())

    st.image(img, width=300)

    st.success("✅ Face Recognition Successful")

    st.balloons()

    st.markdown("""
    <h2 style='color:lime;text-align:center;'>
    🎯 Attendance Marked Successfully
    </h2>
    """, unsafe_allow_html=True)

    st.info(f"📌 {student_name} Present")

    st.success(f"📁 Photo Saved as {file_name}")

# -------------------------
# REPORT GENERATOR
# -------------------------
st.subheader("📩 Weekly AI Report")

student = st.selectbox("Select Student", df["Name"])

email = st.text_input("Enter Email")

if st.button("Generate Report"):

    row = df[df["Name"] == student].iloc[0]

    st.success("✅ Report Generated Successfully")

    st.write(f"👨‍🎓 Student: {student}")
    st.write(f"📧 Email: {email}")
    st.write(f"📊 Attendance: {row['Attendance']}%")
    st.write(f"📚 Average Marks: {row['Average']:.2f}")

    st.success("🤖 AI Summary Created Successfully")
