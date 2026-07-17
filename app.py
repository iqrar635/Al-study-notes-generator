import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

topic = input("Enter the topic: ")

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=f"""
Create beginner-friendly study notes on {topic}.

Include:
1. Definition
2. Key Concepts
3. Advantages
4. Disadvantages
5. Applications
6. Important Interview Questions

Use headings and bullet points.
"""
)

print("\n")
print(response.text)