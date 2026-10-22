import streamlit as st
from PIL import Image
from api_calling import note_generate, audio_generator

#Title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate note summary and quizzes")

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photos of your notes",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    pil_images = [Image.open(img) for img in images]
    #Images
    if pil_images:
        if len(images) > 3:
            st.error("You can upload max 3 images")
        else:
            col = st.columns(len(images))

            st.subheader("Uploaded images")
            for i , img in enumerate(images):
                with col[i]:
                    st.image(img)

    #Difficulty:
    selectDifficulty = st.selectbox("Select the difficulty level",
                 ('Easy','Medium','Hard'),index=None)
    if selectDifficulty:
        st.markdown(f"Difficulty level: **{selectDifficulty}**")
 

    pressed = st.button("CLick the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("Please at least select 1 image")
    if not selectDifficulty:
        st.error("Please select difficulty level")

    if images and selectDifficulty:
        # Note
        with st.container(border=True):
            st.subheader("Your note:")
            with st.spinner("AI generating notes..."):
                generate_notes = note_generate(pil_images)
                st.markdown(generate_notes)

        #Audio
        with st.container(border=True):
            st.subheader("Audio Transcription:")
            with st.spinner("AI generating audio..."):
                st.audio(audio_generator(generate_notes))            

        #Quiz
        with st.container(border=True):
            st.subheader(f"Quiz level: {selectDifficulty}")
            st.text("Note will be shown here")