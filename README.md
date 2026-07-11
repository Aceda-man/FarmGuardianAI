# 🌱 FarmGuardian AI

## Offline AI Agricultural Assistant for Smallholder Farmers

FarmGuardian AI is an intelligent agricultural assistant designed to help Nigerian smallholder farmers detect crop problems, understand climate risks, and receive practical farming recommendations.

The project combines agricultural knowledge, AI preparation, climate awareness, and farmer digital records to provide accessible agricultural support even in areas with limited internet access.

Built for the **Google Gemma Hackathon - Track 3: Safe Communities (SDG 11 & SDG 13)**.

---

# 🌍 The Problem

Millions of smallholder farmers face challenges such as:

- Limited access to agricultural extension officers
- Delayed detection of pests and diseases
- Increasing climate uncertainty
- Poor access to reliable farming information
- Limited digital tools for farm decision making

These challenges contribute to:

- Crop losses
- Reduced farmer income
- Food insecurity
- Climate vulnerability

---

# 💡 Our Solution: FarmGuardian AI

FarmGuardian AI provides farmers with an intelligent farming assistant that can:

🌱 Diagnose crop problems

📸 Analyze crop images

🌦 Consider climate conditions

📊 Store farm history

🗣 Support future local language interaction

🤖 Prepare for Gemma multimodal AI integration

---

# 🚀 Current Features

## 👨🏾‍🌾 Farmer Authentication

Farmers can:

- Create personal accounts
- Secure their profiles with passwords
- Store farm information
- Maintain private diagnosis history

Each farmer only sees their own records.

---

## 🌱 Crop Diagnosis System

Farmers can provide:

- Crop type
- Crop symptoms
- Crop images
- Weather conditions

The system prepares AI-ready agricultural assessments.

Example:

Input:

> "My maize leaves are turning yellow and have holes"

Output:

- Possible causes
- Risk level
- Climate consideration
- Recommended actions

---

## 📸 Image Processing

FarmGuardian AI currently prepares uploaded crop images for AI analysis.

Future Gemma integration will enable:

- Plant disease recognition
- Pest identification
- Visual crop assessment

---

## 🌦 Climate Risk Advisory

FarmGuardian AI considers climate factors:

- Temperature
- Rainfall conditions
- Flood risk
- Drought risk
- Location

The system provides climate-aware recommendations.

Aligned with:

**SDG 13: Climate Action**

---

## 📊 Digital Farm History

Farmers can:

- Save previous diagnoses
- Review past crop problems
- Track farm decisions

Each farmer has a private history.

---

# 🤖 Gemma 4 Integration Plan

The current version contains the complete AI preparation layer.

During final integration, Gemma will replace the temporary reasoning engine.

Architecture:

Farmer Input
  |
  ↓
 Crop Image + Symptoms + Climate Data
    |
    ↓
FarmGuardian Prompt Builder

  |
  ↓

Gemma Multimodal Model

  |
  ↓

Agricultural Recommendation

  |
  ↓

Farmer Friendly Response


Gemma will enable:

- Image-based crop diagnosis
- Better reasoning
- Multimodal understanding
- Local agricultural intelligence

---

# 🌍 SDG Alignment

## SDG 11 - Sustainable Communities

FarmGuardian AI supports safer and more resilient communities by improving:

- Access to agricultural information
- Farmer decision making
- Rural digital inclusion

---

## SDG 13 - Climate Action

FarmGuardian AI helps farmers adapt to climate challenges through:

- Climate-aware recommendations
- Weather risk consideration
- Drought and flood awareness
- Sustainable farming decisions

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Programming Language

- Python

## AI Preparation

- Gemma multimodal architecture
- Prompt engineering
- AI response processing

## Data Storage

- JSON-based farmer records
- Diagnosis history storage

## Image Processing

- Pillow (PIL)

---

# 📂 Project Structure


FarmGuardianAI/

│
├── app.py
│
├── utils/
│ │
│ ├── auth.py
│ ├── storage.py
│ ├── helpers.py
│ ├── advisory.py
│ ├── weather.py
│ ├── language.py
│ ├── image_processor.py
│ ├── gemma_prompt.py
│ └── ai_engine.py
│
├── data/
│ ├── farmers.json
│ └── history.json
│
├── requirements.txt
│
└── README.md


---

# ⚙️ Installation

Clone repository:

```bash

git https://github.com/Aceda-man/FarmGuardianAI.git

Enter project folder:

cd FarmGuardianAI

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py


🔮 Future Improvements
Gemma 4 multimodal integration
Voice assistant for farmers
Local language support
Offline mobile deployment
Real weather API integration
Satellite-based farm monitoring
Agricultural expert knowledge database
👨🏾‍🌾 Vision

FarmGuardian AI aims to become a digital agricultural companion for farmers by combining artificial intelligence and climate intelligence to create safer, smarter, and more sustainable farming communities.

Built for the Gemma Hackathon

FarmGuardian AI
