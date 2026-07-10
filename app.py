import streamlit as st


st.set_page_config(
    page_title="FarmGuardian AI",
    page_icon="🌱",
    layout="wide"
)


st.title("🌱 FarmGuardian AI")

st.subheader(
    "Offline Agricultural Intelligence Assistant"
)


st.write(
    """
    FarmGuardian AI helps smallholder farmers identify crop problems
    and receive practical agricultural advice.
    """
)


st.divider()


st.header("Crop Diagnosis")


crop = st.selectbox(
    "Select your crop",
    [
        "Tomato",
        "Maize",
        "Cassava",
        "Cowpea"
    ]
)


problem = st.text_area(
    "Describe the problem you are seeing"
)


image = st.file_uploader(
    "Upload crop image",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


if st.button("Analyze Crop"):

    if problem:

        st.success(
            "Analysis completed!"
        )

        st.write(
            """
            Possible issue:
            Disease detection will be powered by Gemma 4.
            
            Recommended solution:
            AI-generated agricultural advice will appear here.
            """
        )

    else:
        st.warning(
            "Please describe the crop problem."
        )
    