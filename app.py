import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import streamlit as st
from audio_utils import download_and_extract_audio
from accent_model import transcribe_and_classify

# --- Page Config ---
st.set_page_config(page_title="Accent Detector", layout="centered")

# --- Title & Description ---
st.markdown(
    "<h1 style='text-align: center; color: #2E8B57;'>🌍 English Accent Detection Tool</h1>",
    unsafe_allow_html=True
)

# --- Instructions ---
st.markdown(
    "<h6 style='text-align: center;'>Paste a public video URL to analyze the speaker's accent (e.g. Loom or MP4 link)</h6>",
    unsafe_allow_html=True
)

# --- Input Form ---
with st.form(key="analyze_form"):
    video_url = st.text_area(
        label="Video URL",
        placeholder="https://example.com/video.mp4",
        height=70,
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("Analyze")

# --- Handle Submission ---
if submitted and video_url:
    with st.spinner("⏳ Processing video..."):
        audio_path = download_and_extract_audio(video_url)
        if audio_path:
            result = transcribe_and_classify(audio_path)
            st.success("✅ Analysis complete!")

            # --- Results ---
            st.markdown("### 🎯 Results")
            st.markdown(f"**🌐 Detected Accent:** `{result['accent']}`")
            st.markdown(f"**📊 Confidence Score:** `{result['confidence']:.1f}%`")
            st.markdown(f"**📝 Summary:** The accent is classified as **{result['accent']}** based on pronunciation features.")

            # --- Transcript ---
            with st.expander("📝 Show Transcript"):
                 st.write(result.get("transcript", "Transcript not available."))
        else:
            st.error("❌ Failed to extract audio. Please check the video URL.")

