import streamlit as st
from PIL import Image

from utils.helpers import analyze_crop_problem
from utils.storage import save_diagnosis, load_history


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="FarmGuardian AI",
    page_icon="🌱",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("🌱 FarmGuardian AI")

st.subheader(
    "Offline Agricultural Intelligence Assistant"
)

st.write(
    """
    FarmGuardian AI helps smallholder farmers identify crop problems
    and receive practical agricultural recommendations.

    Powered by agricultural knowledge + future Gemma 4 intelligence.
    """
)


st.divider()


# -----------------------------
# Sidebar - Farmer Profile
# -----------------------------

with st.sidebar:

    st.header("👨🏾‍🌾 Farmer Profile")

    farmer_name = st.text_input(
        "Farmer name"
    )

    location = st.text_input(
        "Location"
    )


    language = st.selectbox(
        "Preferred Language",
        [
            "English",
            "Yoruba",
            "Hausa",
            "Igbo"
        ]
    )


    st.divider()


    st.info(
        """
        Future Gemma 4 Features:

        • Image diagnosis
        • Voice assistant
        • Local language support
        • Offline deployment
        """
    )



# -----------------------------
# Main Navigation
# -----------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🔍 Crop Diagnosis",
        "📊 Farm History",
        "🌦 Advisory",
        "ℹ️ About"
    ]
)



# =====================================================
# TAB 1 - CROP DIAGNOSIS
# =====================================================

with tab1:

    st.header("🔍 Crop Diagnosis")


    col1, col2 = st.columns(2)


    with col1:

        crop = st.selectbox(
            "Select Crop",

            [
                "Maize",
                "Rice",
                "Sorghum",
                "Millet",
                "Cassava",
                "Yam",
                "Sweet Potato",
                "Cowpea",
                "Groundnut",
                "Soybean",
                "Tomato",
                "Pepper",
                "Onion",
                "Cocoa",
                "Oil Palm",
                "Ginger"
            ]
        )


        description = st.text_area(
            "Describe what you see on the crop",

            placeholder=
            "Example: My maize leaves have holes and insects are inside the plant"
        )



    with col2:

        uploaded_image = st.file_uploader(
            "Upload crop image",

            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )


        if uploaded_image:

            image = Image.open(
                uploaded_image
            )

            st.image(
                image,
                caption="Uploaded Crop Image",
                use_container_width=True
            )



    st.divider()


    if st.button(
        "🌱 Analyze Crop",
        use_container_width=True
    ):


        if description:


            result = analyze_crop_problem(
                crop,
                description
            )


            if result:


                st.success(
                    "Analysis completed"
                )


                save_diagnosis(
                    farmer_name,
                    location,
                    crop,
                    description,
                    result
                )


                st.header(
                    f"Possible Issue: {result['name']}"
                )


                st.write(
                    "**Category:**",
                    result["type"]
                )


                st.subheader(
                    "Symptoms"
                )

                for symptom in result["symptoms"]:

                    st.write(
                        "🔹",
                        symptom
                    )


                st.subheader(
                    "Possible Cause"
                )

                st.write(
                    result["cause"]
                )


                st.subheader(
                    "Recommended Management"
                )

                for action in result["management"]:

                    st.write(
                        "✅",
                        action
                    )


            else:

                st.warning(
                    """
                    No matching problem found.

                    Gemma 4 integration will provide
                    advanced reasoning in the final version.
                    """
                )


        else:

            st.warning(
                "Please describe the crop problem first."
            )



# =====================================================
# TAB 2 - FARM HISTORY
# =====================================================

with tab2:

    st.header(
        "📊 Previous Farm Diagnoses"
    )


    history = load_history()


    if history:


        for item in history:


            with st.expander(
                f"{item['crop']} - {item['diagnosis']}"
            ):


                st.write(
                    "👨🏾‍🌾 Farmer:",
                    item["farmer"]
                )


                st.write(
                    "📍 Location:",
                    item["location"]
                )


                st.write(
                    "Problem:",
                    item["problem"]
                )


                st.write(
                    "Date:",
                    item["date"]
                )


    else:


        st.info(
            "No previous diagnoses yet."
        )



# =====================================================
# TAB 3 - FARMING ADVISORY
# =====================================================

with tab3:


    st.header(
        "🌦 Farming Advisory"
    )


    st.write(
        """
        Future Gemma 4 advisory features:

        🌱 Crop management advice

        🌧 Weather-based recommendations

        🐛 Pest outbreak alerts

        🌾 Fertilizer recommendations

        📍 Region-specific farming guidance
        """
    )


    region = st.selectbox(

        "Select farming region",

        [
            "North West",
            "North Central",
            "South West",
            "South East",
            "South South"
        ]

    )


    st.info(
        f"""
        Advisory region:

        {region}

        AI-powered recommendations will be added
        through Gemma 4 integration.
        """
    )



# =====================================================
# TAB 4 - ABOUT
# =====================================================

with tab4:


    st.header(
        "ℹ️ About FarmGuardian AI"
    )


    st.write(
        """
        FarmGuardian AI is an agricultural assistant
        designed for Nigerian smallholder farmers.

        It combines:

        ✅ Agricultural knowledge

        ✅ Crop diagnosis

        ✅ Digital farm records

        ✅ AI reasoning


        Future versions will integrate Gemma 4
        for multimodal crop understanding,
        local languages, and offline intelligence.
        """
    )



# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "FarmGuardian AI 🌱 | Built for Nigerian smallholder farmers | Gemma 4 Hackathon"
)