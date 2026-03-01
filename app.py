import streamlit as st

st.title("📊 SmartSurvey AI")
st.write("Generate professional survey questions automatically.")

if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = False

topic = st.text_input("Enter Survey Topic")

if st.button("Generate Survey Questions"):
    if topic.strip() != "":
        st.session_state.questions_generated = True
    else:
        st.warning("Please enter a topic.")

if st.session_state.questions_generated:

    st.subheader("Generated Survey Questions:")

    q1 = st.radio(
        f"1. How satisfied are you with {topic}?",
        ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied"]
    )

    q2 = st.radio(
        f"2. How often do you use {topic}?",
        ["Daily", "Weekly", "Monthly", "Rarely"]
    )

    q3 = st.text_area(f"3. What do you like most about {topic}?")

    q4 = st.text_area(f"4. What improvements would you suggest for {topic}?")

    q5 = st.slider(
        f"5. Rate your overall experience with {topic}",
        1, 5
    )

    if st.button("Submit Responses"):
        st.success("✅ Responses submitted successfully!")
