import os
from dotenv import load_dotenv
from google import genai
from prompts import create_prompt
import streamlit as st

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("📚 AI Study Notes Generator")

st.write("Generate AI-powered study notes in seconds!")

topic = st.text_input("Enter Topic")

level = st.selectbox(
    "Select Difficulty Level",
    ["Beginner", "Intermediate", "Advanced"]
)
generate = st.button("Generate Notes")
if generate:
    st.write("Generating notes...")

    prompt = create_prompt(topic,level)
    st.write("Topic:", topic)
    st.write("Level:", level)

    try:
        response = client.models.generate_content(
           model="gemini-flash-latest",
           contents=prompt
    )

        st.success("Notes generated successfully!")
        st.markdown(response.text) 
        os.makedirs("output", exist_ok=True)

        filename = os.path.join(
            "output",
             f"{topic.strip().replace(' ', '_')}_notes.md"
           )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        st.success(f"Notes saved to {filename}")   
    except Exception as e: 
      st.error(f"Something went wrong: {e}")
    