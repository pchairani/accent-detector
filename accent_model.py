import whisper
import librosa
import numpy as np
import random

# Load Whisper model once
model = whisper.load_model("base")

# Dummy classifier using pronunciation features
def fake_accent_classifier(audio_features):
    accent = "British"
    confidence = round(random.uniform(80, 99.9), 1)
    return accent, confidence

def transcribe_and_classify(audio_path):
    # Transcribe using Whisper
    transcription = model.transcribe(audio_path)

    # Extract audio features (dummy)
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    audio_features = np.mean(mfcc.T, axis=0)

    # Classify accent
    accent, confidence = fake_accent_classifier(audio_features)

    return {
        "transcript": transcription["text"],
        "accent": accent,
        "confidence": confidence
    }

