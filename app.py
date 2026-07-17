import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

topic = input("Enter the topic: ")

prompt = f"""
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

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    print("\n")
    print(response.text)

    # Save notes to a file
    filename = f"{topic.strip().replace(' ', '_')}_notes.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"\n✅ Notes saved to {filename}")

except Exception as e:
    print(f"\n❌ Something went wrong: {e}")