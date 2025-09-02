import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(prompt, model="gemini-1.5-flash"):
    try:
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM error: {str(e)}"
