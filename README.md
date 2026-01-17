# VisionAI Analytics Dashboard

### Advanced Object Detection, OCR, and Multilingual Translation Engine

VisionAI is a professional-grade web application built with **Python** and **Streamlit**, powered by **Microsoft Azure AI Services**. It provides a seamless experience for detecting objects in images, extracting text via OCR, and instantly translating that text into Sinhala.

---

## Key Features

- **Object Detection**: Identifies multiple objects in an image and draws high-precision bounding boxes.
- **Multilingual OCR**: Extracts printed or handwritten text from images with high accuracy.
- **Sinhala Translation**: Powered by Azure Translator to provide real-time Sinhala translations of extracted text.
- **Professional UI**: Featuring a modern "Blueprint Grid" interface with custom CSS and a responsive layout.
- **Confidence Metrics**: Displays AI certainty levels for every detection.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![PIL](https://img.shields.io/badge/Pillow-blue?style=for-the-badge)

- **Backend**: Python 3.x
- **Frontend**: Streamlit (with Custom CSS Injection)
- **AI Engine**: Azure AI Vision API
- **Translation Engine**: Azure AI Translator (REST API)
- **Image Processing**: PIL (Pillow)

---

## 📸 Screenshots

<img width="1898" height="820" alt="VisionAI" src="https://github.com/user-attachments/assets/efcd1c55-de0f-452d-bf5c-83e55d65330a" />


## 🚀 Getting Started

1. Clone the repository

git clone [https://github.com/YOUR_USERNAME/AzureObjectDetector.git](https://github.com/YOUR_USERNAME/AzureObjectDetector.git)
cd AzureObjectDetector

2. Install dependencies

pip install -r requirements.txt

3. Setup Environment Variables

Create a .env file in the root directory and add your Azure keys:

AZURE_ENDPOINT=your_vision_endpoint
AZURE_KEY=your_vision_key
AZURE_TRANSLATOR_KEY=your_translator_key
AZURE_TRANSLATOR_REGION=southeastasia
AZURE_TRANSLATOR_ENDPOINT=[https://api.cognitive.microsofttranslator.com/](https://api.cognitive.microsofttranslator.com/)

4. Run the App

streamlit run app.py
