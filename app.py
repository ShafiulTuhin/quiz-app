import streamlit as st


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
    #Images
    if images:
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
    else:
        st.error("Please select difficulty level")

    st.button("CLick the button to initiate AI", type="primary")