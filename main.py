from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

NAME = "Rua"
LLM_API_KEY = os.getenv("NVIDIA_API_KEY")
LLM_MODEL = "openai/gpt-oss-120b"

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

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = LLM_API_KEY
)


# Maintain conversation history manually (OpenAI-compatible format)
chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]


def ask_llm(user_input: str) -> str | None:
    """Send message to LLM chat, return reply or None on error."""
    chat_history.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=chat_history,
            temperature=0.7,
            # max_tokens=300,
            # tools=tools
            # tool_choice=auto
        )
        reply = response.choices[0].message.content.strip()
        chat_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print(f"[LLM Error]  {e}")
        # Remove the failed user message so history stays consistent
        chat_history.pop()
        return None


def main():
    print(f"{NAME}\t: Goodmorning sir! This is {NAME}, your highly capable AI assistant. How may i help you today?")
    
    while True:
        req = str(input("You\t: ")).strip()
        
        if (req.lower() in EXIT_WORDS):
            print(f"Goodbye boss. Shutting down...")
            break
        
        response = ask_llm(req)
        
        if response and SHUTDOWN_KEYWORD in response:
            response = response.replace(SHUTDOWN_KEYWORD, "").strip()
            print(f"{NAME}\t: {response}")
            break
        
        print(f"{NAME}\t: {response}")

if __name__ == "__main__":
    main()