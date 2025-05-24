from faster_whisper import WhisperModel
import librosa
import numpy as np
import random

# Load Whisper model once
model = WhisperModel("base")

# Dummy classifier using pronunciation features
def fake_accent_classifier(audio_features):
    accent = "British"
    confidence = round(random.uniform(80, 99.9), 1)
    return accent, confidence

def transcribe_and_classify(audio_path):
    # Transcribe using faster-whisper
    segments, info = model.transcribe(audio_path)
    text = " ".join(segment.text for segment in segments)

    # Extract audio features (dummy)
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    audio_features = np.mean(mfcc.T, axis=0)

    # Classify accent
    accent, confidence = fake_accent_classifier(audio_features)

    return {
        "transcript": text,
        "accent": accent,
        "confidence": confidence
    }

