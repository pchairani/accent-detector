import streamlit as st
from audio_utils import download_and_extract_audio
from accent_model import transcribe_and_classify

# --- Page config ---
st.set_page_config(page_title="Accent Detector", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌍 English Accent Detection Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Paste a video URL or upload a file to analyze the speaker's accent.</p>", unsafe_allow_html=True)

# --- Input Section ---
video_url = st.text_input("📎 Paste a public video URL (e.g., Loom or MP4):")

if video_url:
    with st.spinner("⏳ Processing video..."):
        audio_path = download_and_extract_audio(video_url)
        if audio_path:
            result = transcribe_and_classify(audio_path)
            st.success("✅ Analysis complete!")

            # --- Result Display ---
            st.markdown("### 🎯 Results")
            st.markdown(f"**🌐 Detected Accent:** `{result['accent']}`")
            st.markdown(f"**📊 Confidence Score:** `{result['confidence']}%`")
            st.markdown(f"**📝 Summary:** {result['summary']}")
        else:
            st.error("❌ Failed to process the audio.")

