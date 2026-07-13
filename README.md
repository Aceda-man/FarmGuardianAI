# 🌱 FarmGuardian AI

## AI-Powered Agricultural Intelligence Assistant for Nigerian Smallholder Farmers


FarmGuardian AI is an AI-driven agricultural assistant designed to help smallholder farmers detect crop problems, receive farming recommendations, understand climate risks, and maintain digital farm records.

By combining **artificial intelligence, offline speech recognition, agricultural knowledge, and climate intelligence**, FarmGuardian AI aims to make expert farming support more accessible to farmers, especially those in low-connectivity environments.

---

# 🌍 The Problem

Agriculture remains one of the most important sectors in Nigeria, supporting millions of livelihoods. However, many smallholder farmers face challenges such as:

- Late detection of crop diseases
- Limited access to agricultural experts
- Unpredictable weather conditions
- Lack of digital farm records
- Barriers caused by internet availability and technical literacy

A farmer may notice that a crop is unhealthy but may not know:

- What disease is affecting it
- How serious the problem is
- What action should be taken
- How weather conditions may affect recovery

This delay can lead to significant crop losses and reduced income.

---

# 💡 Our Solution

FarmGuardian AI provides farmers with an intelligent agricultural companion that helps them make better farming decisions.

The system allows farmers to:

🌱 Diagnose crop problems  
🎤 Ask farming questions using voice  
🌦 Receive climate-based farming recommendations  
📊 Maintain digital farm history  
🤖 Get AI-powered agricultural guidance  

The goal is simple:

> Make agricultural intelligence accessible to every farmer, regardless of technical background or connectivity limitations.

---

# ✨ Key Features

## 🌱 AI Crop Diagnosis

Farmers can describe crop problems and upload crop images for intelligent analysis.

The system helps identify:

- Possible diseases
- Pest-related problems
- Environmental stress
- Recommended actions

Future versions will use Gemma multimodal intelligence for image-based crop understanding.

---

## 🎤 Offline Voice Assistant

Many farmers may not be comfortable typing questions.

FarmGuardian AI includes offline speech recognition using Vosk technology.

Farmers can ask questions naturally:

Example:

> "Why are my maize leaves turning yellow?"

The system converts speech into text and provides agricultural guidance.

This improves accessibility for farmers with limited digital experience.

---

## 🌦 Climate Intelligence

Weather conditions strongly influence crop health.

FarmGuardian AI connects climate information with agricultural decisions.

The system considers factors such as:

- Temperature
- Rainfall
- Humidity
- Environmental conditions

Example:

High humidity + tomato farming:

→ Increased fungal disease risk

The AI can recommend preventive actions.

---

## 📊 Digital Farm Records

Farmers can maintain records of:

- Previous diagnoses
- Crop problems
- Recommendations received
- Farming history

This allows farmers to track patterns and improve future decisions.

---

## 👨🏾‍🌾 Farmer Personalization

Each farmer has a personalized profile containing:

- Farm information
- Preferred crops
- Farming experience
- Location

Recommendations become more relevant to individual farming conditions.

---

# 🤖 Artificial Intelligence Architecture

FarmGuardian AI uses a modular AI architecture.
             Farmer

                |
    -------------------------
    |                       |
  Voice                  Image/Text
    |                       |
    ↓                       ↓

Offline Speech          AI Engine
Recognition             (Gemma Ready)

    |                       |
    -------------------------
                |
                ↓

      Agricultural Intelligence

                |
    -------------------------
    |          |            |

 Diagnosis   Climate     Recommendations

                |
                ↓

          Farmer Action

          
---

# 🧠 Gemma Integration

FarmGuardian AI is designed for integration with Google's Gemma models.

Gemma will provide:

- Agricultural reasoning
- Crop disease interpretation
- Image understanding
- Context-aware recommendations
- Natural language interaction

The architecture allows the prototype AI engine to be replaced with Gemma without changing the application interface.

---

# 📴 Offline-First Approach

Connectivity remains a major challenge in rural communities.

FarmGuardian AI focuses on accessibility through:

✅ Offline voice recognition  
✅ Lightweight architecture  
✅ Local farmer profiles  
✅ Future offline AI deployment  

The long-term vision is an agricultural assistant that can operate effectively even in areas with limited internet access.

---

# 🌍 Sustainable Development Goal Alignment

## SDG 4 — Quality Education

FarmGuardian AI supports agricultural education by providing farmers with accessible knowledge and decision-support tools.

Instead of depending only on physical agricultural extension services, farmers can access learning and guidance through AI.

## SDG 11 — Sustainable Communities

By supporting farmers and improving agricultural decision-making, the platform contributes to stronger and more resilient communities.

## SDG 13 — Climate Action

The climate intelligence component helps farmers adapt to changing environmental conditions.

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Programming Language

- Python

## Artificial Intelligence

- Google Gemma (Integration)
- Prototype Agricultural Reasoning Engine

## Speech Recognition

- Vosk Offline Speech Recognition

## Audio Processing

- SoundDevice
- SciPy

## Data Management

- Local farm records database

## Environment Management

- Python Virtual Environment

---

# 📂 Project Structure

FarmGuardianAI/

│
├── app.py # Streamlit application

├── utils/

│ ├── ai_engine.py # AI decision engine

│ ├── voice.py # Offline speech recognition

│ ├── weather.py # Climate intelligence

│ ├── auth.py # Farmer authentication

│ └── history.py # Farm records

│
├── models/

│ └── Vosk speech model

│
├── requirements.txt

├── README.md

└── .gitignore

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Aceda-man/FarmGuardianAI.git

Navigate into the project:

cd FarmGuardianAI

Create a virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py

🎯 Future Improvements

Future versions will include:

🌍 Local language support (Yoruba, Hausa, Igbo)
📱 Mobile application deployment
🛰 Satellite crop monitoring
🌱 More crop disease datasets
📴 Fully offline AI model deployment
🤖 Advanced Gemma multimodal diagnosis
🧑🏾‍🌾 Agricultural extension expert integration
👥 Impact Vision

FarmGuardian AI aims to become a digital agricultural companion that connects farmers with reliable knowledge anytime and anywhere.

By combining AI with agricultural expertise, we can help farmers make faster, smarter, and more sustainable decisions.

Built For

🌱 Gemma AI Hackathon

Built with the vision of empowering Nigerian smallholder farmers through accessible artificial intelligence.