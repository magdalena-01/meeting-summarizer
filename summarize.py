from langchain_community.llms import Ollama

def summarize_transcript(transcript: str):
    llm = Ollama(model="mistral")  # or "llama3", "gemma", etc., depending on your installed models

    prompt = f"""
You are an AI meeting assistant.

Here is the transcript of a meeting:
{transcript}

Summarize the meeting in a few bullet points.
Then list clear, numbered action items.
"""

    response = llm.invoke(prompt)
    return response
