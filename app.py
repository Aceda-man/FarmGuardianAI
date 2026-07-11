

from utils.auth import (
    register_farmer,
    find_farmer,
)
import streamlit as st
from PIL import Image

from utils.helpers import (
    analyze_crop_problem,
    get_crop_count,
    get_problem_count,
)

from utils.storage import (
    save_diagnosis,
    load_history,
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

if "farmer" in st.session_state:

    history_count = len(
        load_history(
            st.session_state.farmer["id"]
        )
    )

else:

    history_count = 0

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
# Sidebar - Farmer Authentication
# -----------------------------

with st.sidebar:


    st.header(
        "👨🏾‍🌾 Farmer Account"
    )


    if "farmer" not in st.session_state:


        st.subheader(
            "Login / Register"
        )


        farmer_name = st.text_input(
            "Farmer name"
        )


        location = st.text_input(
            "Location"
        )



        if st.button(
            "Login"
        ):


            if farmer_name and location:


                farmer = find_farmer(
                    farmer_name,
                    location
                )


                if farmer:


                    st.session_state.farmer = farmer


                    st.success(
                        f"Welcome back {farmer['name']}!"
                    )


                    st.rerun()



                else:


                    farmer = register_farmer(

                        farmer_name,

                        location

                    )


                    st.session_state.farmer = farmer


                    st.success(
                        "New farmer profile created!"
                    )


                    st.rerun()



            else:


                st.warning(
                    "Please enter your name and location."
                )



    else:


        farmer = st.session_state.farmer


        st.success(
            f"""
            Logged in:

            👨🏾‍🌾 {farmer['name']}

            📍 {farmer['location']}
            """
        )



        st.divider()



        if st.button(
            "Logout"
        ):


            del st.session_state.farmer


            st.rerun()



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



    if st.button("🌱 Analyze Crop"):

        if "farmer" not in st.session_state:

            st.warning("Please login first.")

            st.stop()

        if description:

            result = analyze_crop_problem(crop, description)



            if result:


                st.success("🌱 Analysis completed successfully")

                save_diagnosis(
                    st.session_state.farmer["id"],
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
        "📊 My Farm History"
    )


    if "farmer" in st.session_state:


        history = load_history(
            st.session_state.farmer["id"]
        )


        if history:


            for item in history:


                with st.expander(
                    f"{item['crop']} - {item['diagnosis']}"
                ):


                    st.write(
                        "🌱 Crop:",
                        item["crop"]
                    )


                    st.write(
                        "Problem:",
                        item["problem"]
                    )


                    st.write(
                        "Diagnosis:",
                        item["diagnosis"]
                    )


                    st.write(
                        "Category:",
                        item["type"]
                    )


        else:


            st.info(
                "No diagnosis history available yet."
            )


    else:


        st.warning(
            "Please login to view your farm history."
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