from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()

NAME = "Rua"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3.5-flash"

EXIT_WORDS = ["exit", "leave", "quit", "shutdown"]
SHUTDOWN_KEYWORD = "[SHUTDOWN]"

SYSTEM_PROMPT = f"""You are {NAME}, a highly capable personal AI voice assistant — like JARVIS from Iron Man.
You are helpful, witty, precise, and concise. Your responses are spoken aloud, so:
- Keep answers short and natural — 1 to 3 sentences for simple queries, more only when truly needed.
- Never use markdown, bullet points, asterisks, numbered lists, or any special formatting.
- Use plain conversational language only — no characters that would sound odd when read aloud.
- Maintain a warm, confident, and slightly formal tone.
- Occasionally address the user as "sir" in the JARVIS style, but don't overdo it.
- If the user says goodbye, tells you to go to sleep, rest, shut down, take a break, or anything that signals the end of the conversation, respond with a warm farewell and append the exact text {SHUTDOWN_KEYWORD} at the very end of your response. Only append this when the user is clearly ending the session."""

client = genai.Client(api_key=GEMINI_API_KEY)

gemini_chat = client.chats.create(
    model=GEMINI_MODEL,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.7,
        # max_output_tokens=300,
    )
)


def ask_gemini(user_input: str) -> str | None:
    """Send message to Gemini chat session, return reply or None on error."""
    try:
        response = gemini_chat.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error]  {e}")
        return None


def main():
    print(f"{NAME}\t: Goodmorning sir! This is {NAME}, your highly capable AI assistant. How may i help you today?")
    
    while True:
        req = str(input("You\t: ")).strip()
        
        if (req.lower() in EXIT_WORDS):
            print(f"Goodbye boss. Shutting down...")
            client.close()
            break
        
        response = ask_gemini(req)
        
        if response and SHUTDOWN_KEYWORD in response:
            response = response.replace(SHUTDOWN_KEYWORD, "").strip()
            print(f"{NAME}\t: {response}")
            client.close()
            break
        
        print(f"{NAME}\t: {response}")

if __name__ == "__main__":
    main()