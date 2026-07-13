from utils.language import (
    detect_language,
    translate_to_english,
    simplify_response
)

from utils.ai_engine import detect_crop

from utils.weather import get_weather

from utils.voice import listen_to_farmer
from utils.ai_engine import farmguardian_ai_response

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

from utils.ai_engine import farmguardian_ai_response

from utils.advisory import generate_advisory
from utils.image_processor import process_crop_image

from utils.weather import get_weather

crops = [
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
    "Oil Palm",
    "Sorghum",
    "Millet",
    "Plantain",
    "Banana",
    "Okra",
    "Ewedu",
    "Vegetable",
    "Potato",
    "Cucumber"
]


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

    st.header("🌱 Crop Diagnosis")

    if "farmer" in st.session_state:

        farmer_crops = st.session_state.farmer.get(
            "crops",
            []
        )

    else:

        farmer_crops = []


    description = st.text_area(
        "Describe the problem"
    )

    crop = detect_crop(
        description,
        farmer_crops
    )

    st.info(
        f"🌱 Detected Crop: {crop}"
    )

    image = st.file_uploader(
        "Upload Crop Image",
        type=["jpg", "png", "jpeg"]
    )

    if st.button("🔍 Analyze Crop"):

        result = farmguardian_ai_response(description)

        st.write(result["analysis"])



    # -------------------------
    # Voice Assistant
    # -------------------------

    st.divider()

    st.subheader("🎤 Ask by Voice")


    if "voice_question" not in st.session_state:
        st.session_state.voice_question = ""


    if st.button("🎙️ Record Question"):

        # Record the farmer's question, save it, and get an AI response
        question = listen_to_farmer()
        st.session_state.voice_question = question
        answer = farmguardian_ai_response(question)
        st.session_state.voice_answer = answer


if st.session_state.voice_question:

    st.write("🗣️ Farmer asked:")
    st.info(st.session_state.voice_question)


if "voice_answer" in st.session_state:

  if st.session_state.voice_answer:

    st.write(
        st.session_state.voice_answer["analysis"]
    )
   
if "voice_answer" not in st.session_state:
    st.session_state.voice_answer = None

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

        weather = get_weather(
            farmer["location"]
        )

        st.subheader("🌦 Current Weather")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🌡 Temperature",
                weather["temperature"]
            )

        with col2:
            st.metric(
                "💧 Humidity",
                weather["humidity"]
            )

        with col3:
            st.metric(
                "🌧 Rainfall",
                weather["rainfall"]
            )
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

        st.subheader("🌍 Current Farm Climate")

        weather_col1, weather_col2, weather_col3, weather_col4 = st.columns(4)

        with weather_col1:
            st.metric(
                "🌡 Temperature",
                weather["temperature"]
            )

        with weather_col2:
            st.metric(
                "💧 Humidity",
                weather["humidity"]
            )

        with weather_col3:
            st.metric(
                "🌧 Rainfall",
                weather["rainfall"]
            )

        with weather_col4:
            st.metric(
                "☁ Condition",
                weather["condition"]
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

Smallholder farmers in Nigeria often lose crops because
pests, diseases, and climate risks are detected too late.
Many farmers also lack access to timely agricultural
education and digital farming tools.


## Our Solution

FarmGuardian AI is an AI-powered agricultural assistant
designed for Nigerian smallholder farmers.

It provides:

🌱 AI-powered crop diagnosis

🎤 Voice-based farmer interaction

🌦 Climate-aware farming advisory

📊 Digital farm history records

📚 Accessible agricultural knowledge


## Technology

FarmGuardian AI combines:

🤖 Gemma AI intelligence

🌦 Weather data integration

🎙 Offline speech recognition

🌱 Agricultural knowledge systems


## Impact

Supporting farmers through accessible AI education,
better decision making, and climate-smart agriculture.


Built for Nigerian farmers.
Powered by Artificial Intelligence.
"""
)



# -----------------------------
# Footer
# -----------------------------

st.divider()


st.caption(
    "FarmGuardian AI 🌱 | Built for Nigerian smallholder farmers | Gemma 4 Hackathon"
)