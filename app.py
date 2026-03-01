import streamlit as st

st.title("SmartSurvey AI")
st.write("Generate professional survey questions automatically.")

topic = st.text_input("Enter Survey Topic")

def generate_questions(topic):
    questions = f"""
1. How satisfied are you with {topic}?
   - Very Satisfied
   - Satisfied
   - Neutral
   - Dissatisfied

2. How often do you use {topic}?
   - Daily
   - Weekly
   - Monthly
   - Rarely

3. What do you like most about {topic}?
   (Open-ended)

4. What improvements would you suggest for {topic}?
   (Open-ended)

5. Rate your overall experience with {topic} (1-5).

6. How likely are you to recommend {topic} to others? (1-5)

7. Where did you first hear about {topic}?
   - Social Media
   - Friend/Colleague
   - Search Engine
   - Advertisement

8. How clear is the information provided about {topic}? (1-5)
"""
    return questions

if st.button("Generate Survey Questions"):
    if topic:
        st.subheader("Generated Survey Questions:")
        st.text(generate_questions(topic))
    else:
        st.warning("Please enter a topic.")