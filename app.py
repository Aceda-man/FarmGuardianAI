from utils.language import (
    detect_language,
    translate_to_english,
    simplify_response
)

from utils.weather import create_weather_profile

import streamlit as st
from PIL import Image

from utils.auth import (
    register_farmer,
    login_farmer
)

from utils.helpers import (
    analyze_crop_problem,
    get_crop_count,
    get_problem_count,
)

from utils.storage import (
    save_diagnosis,
    load_history,
)
from utils.gemma_prompt import (
    build_farmguardian_prompt,
)

from utils.ai_engine import (
    farmguardian_ai_response,
)

from utils.advisory import generate_advisory
from utils.image_processor import process_crop_image



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
# Sidebar Authentication
# -----------------------------

with st.sidebar:

    st.header(
        "👨🏾‍🌾 Farmer Account"
    )


    # =========================
    # NOT LOGGED IN
    # =========================

    if "farmer" not in st.session_state:

        # -------- LOGIN --------

        st.subheader(
            "🔐 Login"
        )

        login_name = st.text_input(
            "Farmer Name",
            key="login_name_input"
        )


        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password_input"
        )


        if st.button(
            "Login",
            key="login_button"
        ):


            if login_name and login_password:


                farmer = login_farmer(
                    login_name,
                    login_password
                )


                if farmer:

                    st.session_state.farmer = farmer

                    st.success(
                        "Login successful!"
                    )

                    st.rerun()


                else:

                    st.error(
                        "Incorrect name or password"
                    )


            else:

                st.warning(
                    "Fill all login fields"
                )



        st.divider()



        # -------- CREATE ACCOUNT --------

        st.subheader(
            "📝 Create Farmer Account"
        )


        new_name = st.text_input(
            "Farmer Name",
            key="register_name"
        )


        new_password = st.text_input(
            "Create Password",
            type="password",
            key="register_password"
        )


        new_location = st.text_input(
            "Farm Location",
            key="register_location"
        )


        crops = st.multiselect(

            "Main crops grown",

            [
                "Maize",
                "Rice",
                "Cassava",
                "Yam",
                "Cowpea",
                "Tomato",
                "Pepper",
                "Groundnut",
                "Soybean",
                "Cocoa",
                "Oil Palm"
            ],

            key="register_crops"

        )


        farm_size = st.selectbox(

            "Farm size",

            [
                "Less than 1 hectare",
                "1-5 hectares",
                "5-20 hectares",
                "Above 20 hectares"
            ],

            key="register_size"

        )



        experience = st.selectbox(

            "Farming experience",

            [
                "Beginner",
                "Intermediate",
                "Experienced"
            ],

            key="register_experience"

        )


        language = st.selectbox(

            "Preferred language",

            [
                "English",
                "Yoruba",
                "Hausa",
                "Igbo"
            ],

            key="register_language"

        )



        if st.button(
            "Create Account",
            key="create_account_button"
        ):


            if (

                new_name

                and

                new_password

                and

                new_location

            ):


                farmer = register_farmer(

                    new_name,

                    new_location,

                    new_password,

                    crops,

                    farm_size,

                    experience,

                    language

                )


                if farmer:


                    st.session_state.farmer = farmer


                    st.success(
                        "Account created!"
                    )


                    st.rerun()



                else:


                    st.warning(
                        "Account already exists"
                    )



            else:


                st.warning(
                    "Please fill name, password and location"
                )




    # =========================
    # LOGGED IN
    # =========================

    else:

        farmer = st.session_state.farmer

        st.success(
            f"""
👨🏾‍🌾 {farmer.get('name')}

📍 {farmer.get('location')}

🌱 Crops:
{", ".join(farmer.get('crops', []))}

📏 Farm:
{farmer.get('farm_size','Not provided')}

⭐ Experience:
{farmer.get('experience','Not provided')}

🗣 Language:
{farmer.get('language','English')}
            """
        )

        st.divider()

        if st.button("🚪 Logout", key="logout_button"):
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

        crop = st.text_input(
            "Crop (optional)",

            placeholder=
            "Example: Maize, Tomato, Cassava"
        )

        st.subheader(
            "🌦 Current Weather Condition"
        )


        temperature = st.slider(

            "Temperature (°C)",

            15,

            45,

            30

        )


        rainfall = st.selectbox(

            "Rainfall Condition",

            [

                "Low",
                "Moderate",
                "High"

            ]

        )


        flood_risk = st.selectbox(

            "Flood Risk",

            [

                "Low",
                "Medium",
                "High"

            ]

        )


        drought_risk = st.selectbox(

            "Drought Risk",

            [

                "Low",
                "Medium",
                "High"

            ]

        )

        st.subheader(
            "🎤 Voice Assistant"
        )

        voice_input = st.text_input(

            "Voice transcript (future microphone input)",

            placeholder=
            "Example: My maize leaves are turning yellow"

        )

        description = st.text_area(

            "Describe what you see on the crop",

            placeholder=
            """
Example:

My maize leaves are turning yellow
and some leaves have holes.
            """

        )



        uploaded_image = st.file_uploader(

            "Upload crop image",

            type=[
                "jpg",
                "jpeg",
                "png"
            ],

            key="diagnosis_image"

        )

        if uploaded_image:
            processed_image, image_info = process_crop_image(uploaded_image)

            if processed_image:
                st.image(
                    processed_image,
                    caption="Uploaded Crop Image",
                    use_container_width=True,
                )

                st.success("📸 Image prepared for AI analysis")

                # store image context for later use in analysis
                st.session_state.image_context = image_info

                with st.expander("Image Information"):
                    st.write(image_info)
            else:
                st.error("Unable to process image")



    st.divider()



    if st.button(

        "🌱 Analyze Crop",

        key="analyze_crop_button"

    ):


        if "farmer" not in st.session_state:


            st.warning(
                "Please login first."
            )

            st.stop()



        if not description:


            st.warning(
                "Please describe the crop problem."
            )

            st.stop()



        farmer = st.session_state.farmer



        # ==============================
        # CREATE GEMMA READY PROMPT
        # ==============================



        climate_data = generate_advisory(

            farmer["location"],

            farmer.get(
                "crops",
                []
            )

        )

        weather = create_weather_profile(
            temperature,
            rainfall,
            flood_risk,
            drought_risk
        )

        image_context = st.session_state.get("image_context")

        if voice_input and not description:

            description = voice_input

        detected_language = detect_language(description)
        translated_message = translate_to_english(description, detected_language)

        prompt = build_farmguardian_prompt(
            farmer,
            crop,
            translated_message,
            climate_data,
            weather,
            image_context
        )

        ai_result = farmguardian_ai_response(
            prompt
        )

        if ai_result:


            st.success(

                "🌱 FarmGuardian AI Analysis Complete"

            )



            st.subheader(

                "🤖 Agricultural Assessment"

            )


            st.write(
                ai_result["analysis"]
            )

            st.subheader(
                "💡 Why FarmGuardian AI Thinks This"
            )

            st.write(
                """The AI considers:

🌱 Crop symptoms

📸 Image features

🌦 Weather conditions

📍 Location climate risks

Agricultural knowledge database
"""
            )

            st.subheader(
                "⚠️ Risk Level"
            )

            if "confidence" in ai_result:

                st.metric(

                    "🤖 AI Confidence",

                    f"{ai_result['confidence']}%"

                )

            st.warning(

                ai_result["risk"]

            )



            st.subheader(

                "🌦 Climate Consideration"

            )


            st.write(

                ai_result["climate_warning"]

            )



            st.subheader(

                "✅ Recommended Actions"

            )


            for action in ai_result["recommendations"]:


                st.write(

                    "🔹",

                    action

                )



            # Save AI result

            save_diagnosis(

                farmer["id"],

                crop,

                description,

                ai_result

            )



            st.info(

                """
Gemma 4 integration point:

This temporary AI engine will be
replaced with Gemma 4 during the
live hackathon.
                """

            )


        else:


            st.error(

                "AI analysis failed."

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
                    f"{item['crop']} - {item['risk']} Risk"
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
                        "🤖 AI Analysis:"
                    )

                    st.write(
                        item["analysis"]
                    )

                    st.write(
                        "⚠️ Risk Level:",
                        item["risk"]
                    )

                    st.write(
                        "🌦 Climate Advice:"
                    )

                    st.write(
                        item["climate_warning"]
                    )

                    st.write(
                        "✅ Recommendations:"
                    )

                    for advice in item["recommendations"]:
                        st.write(
                            "🔹",
                            advice
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
# TAB 3 - ADVISORY                                                                                          
# =====================================================

with tab3:


    st.header(
        "🌦 Personalized Climate Advisory"
    )


    if "farmer" in st.session_state:


        farmer = st.session_state.farmer


        st.write(
            f"""
            👨🏾‍🌾 Farmer:
            {farmer['name']}


            📍 Location:
            {farmer['location']}


            🌱 Crops:
            {", ".join(farmer.get('crops', []))}
            """
        )



        if st.button(
            "🌦 Generate Climate Advisory",
            key="climate_advisory_button"
        ):


            advisory = generate_advisory(

                farmer["location"],

                farmer.get(
                    "crops",
                    []
                )

            )


            st.subheader(
                "⚠️ Climate Risks"
            )


            for risk in advisory["risks"]:

                st.warning(
                    risk
                )



            st.subheader(
                "🌱 Crop Specific Risks"
            )


            for item in advisory["crop_advice"]:

                st.write(
                    f"### {item['crop']}"
                )


                for risk in item["risks"]:

                    st.write(
                        "🔹",
                        risk
                    )



            st.subheader(
                "✅ Recommended Actions"
            )


            for action in advisory["recommendations"]:

                st.success(
                    action
                )


    else:


        st.warning(
            "Please login first."
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