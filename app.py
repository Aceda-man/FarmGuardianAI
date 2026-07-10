import streamlit as st
from PIL import Image

from utils.helpers import (
    analyze_crop_problem,
    get_crop_count,
    get_problem_count
)

from utils.storage import (
    save_diagnosis,
    load_history
)


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
    FarmGuardian AI helps Nigerian smallholder farmers
    identify crop problems and receive practical
    agricultural recommendations.

    Combining agricultural knowledge with future
    Gemma 4 multimodal intelligence.
    """
)


st.divider()



# -----------------------------
# Dashboard Metrics
# -----------------------------

crop_count = get_crop_count()

problem_count = get_problem_count()

history_count = len(
    load_history()
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🌱 Supported Crops",
        crop_count
    )


with col2:

    st.metric(
        "🐛 Agricultural Problems",
        problem_count
    )


with col3:

    st.metric(
        "📊 Diagnoses Made",
        history_count
    )


with col4:

    st.metric(
        "🇳🇬 Region Focus",
        "Nigeria"
    )



# -----------------------------
# Sidebar Farmer Profile
# -----------------------------

with st.sidebar:


    st.header(
        "👨🏾‍🌾 Farmer Profile"
    )


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

        📸 Image crop diagnosis

        🎙 Voice assistant

        🌍 Local language support

        📱 Offline AI deployment
        """
    )



# -----------------------------
# Navigation
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


    st.header(
        "🔍 Crop Diagnosis"
    )


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
                    "🌱 Analysis completed successfully"
                )


                save_diagnosis(

                    farmer_name,

                    location,

                    crop,

                    description,

                    result

                )



                st.subheader(

                    f"🔎 Identified Problem: {result['name']}"

                )


                st.info(

                    f"""
                    Problem Category:

                    {result['type']}
                    """

                )



                st.subheader(
                    "🩺 Symptoms"
                )


                for symptom in result["symptoms"]:

                    st.write(
                        "🔹",
                        symptom
                    )



                st.subheader(
                    "⚠️ Possible Cause"
                )


                st.write(
                    result["cause"]
                )



                st.subheader(
                    "✅ Recommended Management"
                )


                for action in result["management"]:

                    st.write(
                        "✅",
                        action
                    )



                st.warning(

                    """
                    Note:
                    Final version will use Gemma 4
                    for advanced image reasoning
                    and intelligent recommendations.
                    """

                )



            else:


                st.warning(

                    """
                    No matching agricultural issue found.

                    Gemma 4 integration will improve
                    diagnosis accuracy.
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
                    "🌱 Crop:",
                    item["crop"]
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
        Future Gemma 4 advisory system:

        🌱 Crop management recommendations

        🌧 Weather-based decisions

        🐛 Pest outbreak warnings

        🌾 Fertilizer guidance

        📍 Location-specific farming advice

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



    st.success(

        f"""
        Selected Region:

        {region}

        AI advisory system will be powered by Gemma 4.
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
        ## The Problem

        Many Nigerian smallholder farmers lose crops
        because diseases and pests are detected too late.


        ## Our Solution

        FarmGuardian AI provides accessible agricultural
        intelligence through:

        🌱 Crop diagnosis

        📚 Agricultural knowledge

        📊 Digital farm records

        🤖 Artificial intelligence


        ## Future Vision

        With Gemma 4 integration:

        • Image-based crop diagnosis

        • Local language support

        • Offline AI assistance

        • Smarter farming decisions


        Built for farmers, powered by AI.
        """

    )



# -----------------------------
# Footer
# -----------------------------

st.divider()


st.caption(
    "FarmGuardian AI 🌱 | Built for Nigerian smallholder farmers | Gemma 4 Hackathon"
)