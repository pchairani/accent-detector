# 🇬🇧 English Accent Detection Tool

This simple web tool detects English accents from video links like Loom or MP4.

It gives you:
- 🌐 The detected accent (British)
- 📊 A confidence score (like 85%)
- 📝 A short explanation and transcript

## How to Run

1. Clone the project:
   git clone https://github.com/pchairani/accent-detector.git
   cd accent-detector

2. Set up the environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install the needed tools:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

## Requirements
- Python 3.10
- Streamlit
- Whisper
- MoviePy
- yt-dlp
- librosa
- scikit-learn

## License
MIT License
