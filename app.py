
import streamlit as st

# Set page config FIRST
st.set_page_config(page_title="TalentScout AI Assistant", layout="centered")

import random
import openai
import os
import csv
from utils import generate_questions_from_openai


# Load OpenAI API Key
openai.api_key = st.secrets["openai"]["api_key"]


# Background images list
background_images = [
    "https://source.unsplash.com/1600x900/?technology",
    "https://source.unsplash.com/1600x900/?abstract",
    "https://source.unsplash.com/1600x900/?office",
    "https://source.unsplash.com/1600x900/?ai",
    "https://source.unsplash.com/1600x900/?coding"
]

def set_random_background():
    selected_image = random.choice(background_images)
    st.markdown(f'''
        <style>
        .stApp {{
            background: url({selected_image}) no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
    ''', unsafe_allow_html=True)

set_random_background()

# Session init
if "stage" not in st.session_state:
    st.session_state.stage = "greeting"
    st.session_state.answers = {}
    st.session_state.question_index = 0
    st.session_state.tech_stack = ""
    st.session_state.questions = []

# Styling
st.markdown("""
    <style>
    .main {background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;}
    .stButton > button {background-color: #4CAF50; color: white; border-radius: 8px; padding: 10px 20px; font-size: 16px;}
    .stTextInput > div > input {border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

st.title("TalentScout Hiring Assistant")

if st.session_state.stage == "greeting":
    st.subheader("Welcome Candidate!")
    st.write("This assistant will collect your info and ask technical questions based on your tech stack.")

    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (comma-separated)")
        submitted = st.form_submit_button("Next")

    if submitted:
        if all([full_name, email, phone, experience, position, location, tech_stack]):
            # Save details in session state
            st.session_state.stage = "answering_questions"
            st.session_state.full_name = full_name
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.experience = experience
            st.session_state.position = position
            st.session_state.location = location
            st.session_state.tech_stack = tech_stack
            st.session_state.questions = generate_questions_from_openai(tech_stack)

            # Save to CSV
            candidate_data = {
                "Full Name": full_name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Position": position,
                "Location": location,
                "Tech Stack": tech_stack
            }

            csv_file = "candidate_data.csv"
            file_exists = os.path.isfile(csv_file)

            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=candidate_data.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(candidate_data)

            set_random_background()

        else:
            st.warning("Please fill in all fields.")

elif st.session_state.stage == "answering_questions":
    q_index = st.session_state.question_index
    questions = st.session_state.questions

    if q_index < len(questions):
        st.subheader("Technical Questions")
        st.write(f"**Q{q_index+1}:** {questions[q_index]}")
        answer = st.text_input("Your Answer", key=f"answer_{q_index}")

        if st.button("Submit Answer"):
            if answer.strip():
                st.session_state.answers[questions[q_index]] = answer
                st.session_state.question_index += 1
                set_random_background()
            else:
                st.warning("Please answer before submitting.")
    else:
        # Save Q&A to text file
        qa_file = f"{st.session_state.full_name.replace(' ', '_')}_qa.txt"

        with open(qa_file, "w", encoding="utf-8") as f:
            f.write(f"Candidate: {st.session_state.full_name}\n")
            f.write(f"Email: {st.session_state.email}\n\n")
            for idx, (question, answer) in enumerate(st.session_state.answers.items(), start=1):
                f.write(f"Q{idx}: {question}\n")
                f.write(f"A{idx}: {answer}\n\n")

        st.session_state.stage = "completed"
        st.success("Thank you for completing the technical round! We’ll get back to you soon.")


elif st.session_state.stage == "completed":
    st.chat_message("assistant").write("This session is already completed. Thank you!")





