import streamlit as st


add_selectbox = st.sidebar.selectbox(
        "What would you like to do?",
        ("New Patient Registration", "Old-Patient Veiw \ Update" , "Old Patient Re-Visit Again" , "Payment Details" , "Feedback")
    )


st.title("Doctor Recommended Video")

video_file = open('production ID_3760968.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)