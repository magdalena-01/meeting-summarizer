from transcribe import transcribe_audio
from summarize import summarize_transcript
from send_email import send_email

if __name__ == "__main__":
    audio_file = "audio/example_meeting.mp3"
    print("Transcribing...")
    transcript = transcribe_audio(audio_file)

    print("Summarizing...")
    summary = summarize_transcript(transcript)

    print("Sending email...")
    send_email(summary, "team@example.com")

    print("✅ All done!")