import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
print("=" * 50)
print("        AI Study Notes Generator")
print("=" * 50)

topic = input("Enter the topic: ")
level = input("Enter the difficulty level (beginner/intermediate/advanced): ")
print("\nGenerating notes...")

from prompts import create_prompt

prompt = create_prompt(topic,level)

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    print("\n")
    print("\nGenerated Notes:\n")
    print(response.text)

    # Save notes to a file
    os.makedirs("output", exist_ok=True)
    filename = os.path.join("output",
    f"{topic.strip().replace(' ', '_')}_notes.md"
     )    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"\n✅ Notes saved to {filename}")

except Exception as e:
    print(f"\n❌ Something went wrong: {e}")