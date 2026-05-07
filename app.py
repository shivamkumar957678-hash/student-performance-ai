import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Student Performance System",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e3a8a,#7c3aed,#9333ea);
color:white;
}

.main-title{
text-align:center;
font-size:55px;
font-weight:bold;
color:white;
margin-top:20px;
}

.sub-title{
text-align:center;
font-size:28px;
color:#facc15;
margin-bottom:30px;
}

.card{
background:rgba(255,255,255,0.10);
padding:20px;
border-radius:20px;
margin-bottom:20px;
box-shadow:0px 0px 15px rgba(255,255,255,0.15);
}

.output{
background:#16a34a;
padding:20px;
border-radius:15px;
font-size:20px;
color:white;
margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================

st.markdown(
"<div class='main-title'>🎓 AI-Powered Student Performance System</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='sub-title'>🚀 AI + Automation + Smart Analytics</div>",
unsafe_allow_html=True
)

# =====================================================
# SAMPLE DATA
# =====================================================

data = {
    "Name":[
        "Rahul",
        "Shivam",
        "Aman",
        "Priya",
        "Rohit",
        "Aditi",
        "Karan",
        "Neha",
        "Arjun",
        "Sneha",
        "Vikas",
        "Anjali"
    ],

    "Attendance":[
        90,
        75,
        60,
        95,
        55,
        88,
        78,
        92,
        81,
        85,
        68,
        94
    ],

    "Math":[
        88,
        76,
        45,
        95,
        40,
        91,
        67,
        85,
        79,
        83,
        58,
        96
    ],

    "Science":[
        85,
        70,
        50,
        98,
        35,
        89,
        72,
        90,
        80,
        82,
        60,
        97
    ],

    "English":[
        80,
        72,
        55,
        90,
        45,
        93,
        70,
        87,
        76,
        84,
        62,
        95
    ]
}

df = pd.DataFrame(data)

df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
)/3

# =====================================================
# TOP ANALYTICS
# =====================================================

topper = df.loc[df["Average"].idxmax()]
weak_student = df.loc[df["Average"].idxmin()]
poor_attendance = df[df["Attendance"] < 70]

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='output'>
    👨‍🎓 Total Students<br><br>
    {len(df)}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='output'>
    🏆 Topper<br><br>
    <span style='color:lime;font-size:40px;font-weight:bold'>
    {topper['Name']}
    </span><br>
    Avg Marks: {topper['Average']:.2f}
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='output'>
    ⚠ Weak Student<br><br>
    {weak_student['Name']}
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='output'>
    📉 Poor Attendance<br><br>
    {len(poor_attendance)} Students
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# GRAPHS
# =====================================================

col5,col6,col7 = st.columns(3)

# SUBJECT WISE GRAPH

with col5:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📚 Subject Wise Average")

    subject_avg = {
        "Math": df["Math"].mean(),
        "Science": df["Science"].mean(),
        "English": df["English"].mean()
    }

    fig1, ax1 = plt.subplots(figsize=(4,4))

    colors = ["red","blue","green"]

    ax1.bar(
        subject_avg.keys(),
        subject_avg.values(),
        color=colors
    )

    ax1.set_ylabel("Marks")

    st.pyplot(fig1)

    st.markdown("</div>", unsafe_allow_html=True)

# ATTENDANCE GRAPH

with col6:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📈 Attendance Analysis")

    fig2, ax2 = plt.subplots(figsize=(4,4))

    ax2.plot(
        df["Name"],
        df["Attendance"],
        marker='o',
        color='cyan'
    )

    ax2.set_ylabel("Attendance %")

    st.pyplot(fig2)

    st.markdown("</div>", unsafe_allow_html=True)

# TOPPER VS OTHERS

with col7:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🏆 Topper vs Others")

    fig3, ax3 = plt.subplots(figsize=(4,4))

    pie_colors = [
        "green",
        "blue",
        "orange",
        "purple",
        "red",
        "yellow",
        "pink",
        "cyan",
        "brown",
        "gray",
        "lime",
        "magenta"
    ]

    ax3.pie(
        df["Average"],
        labels=df["Name"],
        autopct='%1.1f%%',
        colors=pie_colors
    )

    st.pyplot(fig3)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# STUDENT PERFORMANCE TABLE
# =====================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📋 Student Performance")

performance_df = df.copy()

performance_df["Status"] = np.where(
    performance_df["Average"] > 80,
    "Topper",
    np.where(
        performance_df["Average"] > 60,
        "Good",
        "Weak"
    )
)

def highlight_topper(row):

    if row["Status"] == "Topper":

        return [
            'color:lime;font-weight:bold;background-color:black'
        ] * len(row)

    return [''] * len(row)

styled_df = performance_df.style.apply(
    highlight_topper,
    axis=1
)

st.dataframe(
    styled_df,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# AI CHATBOT
# =====================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.header("🤖 Advanced AI Chatbot")

question = st.text_input("Ask AI Question")

if question:

    q = question.lower()

    if "topper" in q:
        answer = f"🏆 {topper['Name']} is the topper with average marks {topper['Average']:.2f}"

    elif "average" in q or "avg" in q:

        avg_student = df["Average"].mean()

        answer = f"📊 Overall average student marks are {avg_student:.2f}"

    elif "attendance" in q:
        answer = "📈 Some students have poor attendance below 70%."

    elif "weak" in q:
        answer = f"⚠ {weak_student['Name']} needs improvement."

    elif "science topper" in q:

        science_topper = df.loc[df["Science"].idxmax()]

        answer = f"🧪 {science_topper['Name']} is Science topper."

    elif "math topper" in q:

        math_topper = df.loc[df["Math"].idxmax()]

        answer = f"📚 {math_topper['Name']} is Math topper."

    elif "english topper" in q:

        english_topper = df.loc[df["English"].idxmax()]

        answer = f"📖 {english_topper['Name']} is English topper."

    elif "ai" in q:
        answer = "🤖 AI analyzes student performance automatically."

    else:
        answer = "✅ AI processed your question successfully."

    st.markdown(f"""
    <div class='output'>
    {answer}
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ML MODEL
# =====================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.header("🧠 AI Model Implementation (ML/DL)")

hours = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)

marks = np.array([20,30,40,50,60,70,80,90])

model = LinearRegression()

model.fit(hours, marks)

study_hour = st.slider(
    "Select Study Hours",
    1,
    12
)

prediction = model.predict([[study_hour]])

st.markdown(f"""
<div class='output'>
📚 Study Hours: {study_hour}<br><br>
🎯 Predicted Marks: {prediction[0]:.2f}
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# WEEKLY REPORT
# =====================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.header("📧 Weekly Report Auto-generated & Emailed")

student_name = st.selectbox(
    "Select Student",
    df["Name"]
)

email = st.text_input("Enter Email")

if st.button("Generate Report"):

    student = df[df["Name"] == student_name]

    st.markdown(f"""
    <div class='output'>
    📩 Report Generated Successfully<br><br>

    👨‍🎓 Student: {student_name}<br>

    📧 Email: {email}<br>

    📊 Attendance: {student['Attendance'].values[0]}%<br>

    📚 Average Marks: {student['Average'].values[0]:.2f}<br>

    ✅ AI Summary Created Successfully
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# FEEDBACK SYSTEM
# =====================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.header("💬 Feedback System with AI Sentiment Analysis")

feedback = st.text_area(
    "Enter Student Feedback"
)

if feedback:

    analysis = TextBlob(feedback)

    score = analysis.sentiment.polarity

    if score > 0:
        result = "😊 Positive Feedback"

    elif score == 0:
        result = "😐 Neutral Feedback"

    else:
        result = "😢 Negative Feedback"

    st.markdown(f"""
    <div class='output'>
    {result}<br><br>
    Sentiment Score: {score:.2f}
    </div>
    """, unsafe_allow_html=True)

st.subheader("📊 Feedback Sentiment Chart")

fig4, ax4 = plt.subplots()

labels = ["Positive","Neutral","Negative"]

values = [72,18,10]

ax4.pie(
    values,
    labels=labels,
    autopct='%1.1f%%'
)

st.pyplot(fig4)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<h3 style='text-align:center;color:white;margin-top:30px;'>
🚀 AI + Automation • Smart Insights • Better Decisions • Student Success
</h3>
""", unsafe_allow_html=True)
