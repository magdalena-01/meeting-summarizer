import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("tiny")  # You can try "small" or "medium" for better results
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    text = transcribe_audio("audio/example_meeting.mp3")
    print(text)