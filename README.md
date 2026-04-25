# 🌾 CropDoctor AI — Smart Agricultural Disease Assistant

## 🧠 Overview

CropDoctor AI is a Gemma-inspired AI-powered assistant designed to help farmers detect crop diseases early using images or symptom descriptions. It provides intelligent predictions, severity analysis, confidence scoring, and actionable farming advice in English and Hindi through a simple Streamlit web app.

---

## 🚀 Features

- 📷 Upload crop leaf images for analysis  
- ✍️ Describe symptoms in natural language  
- 🤖 AI-based disease prediction (Gemma-style reasoning)  
- ⚠️ Severity classification (Low / Medium / High)  
- 🎯 Confidence scoring system  
- 🌍 Multilingual support (English + Hindi)  
- 🧠 Explainable AI (Why this prediction?)  
- 🌱 Simple, farmer-friendly recommendations  

---

## 🏗️ Tech Stack

- Python  
- Streamlit  
- Pillow  
- Rule-based AI engine (Gemma-style simulation)  

---

## 📂 Project Structure
cropdoctor-ai/
│
├── app.py
├── ai_engine.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/cropdoctor-ai-gemma.git
cd cropdoctor-ai-gemma
python3 -m venv venv
source venv/bin/activate
streamlit run app.py
