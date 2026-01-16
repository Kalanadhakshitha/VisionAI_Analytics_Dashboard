import streamlit as st
import os
import requests, uuid
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from PIL import Image, ImageDraw

# Load environment variables
load_dotenv()

#page config
st.set_page_config(page_title="VisionAI - Final Edition", layout="wide")

#css Styles
st.markdown("""
    <style>
    /* Blueprint Grid Background */
    .stApp {
        background-color: #0f172a;
        background-image: 
            linear-gradient(rgba(0, 120, 212, 0.2) 2px, transparent 2px),
            linear-gradient(90deg, rgba(0, 120, 212, 0.2) 2px, transparent 2px),
            linear-gradient(rgba(0, 120, 212, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 120, 212, 0.1) 1px, transparent 1px);
        background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px;
        background-attachment: fixed;
        color: white;
    }
    
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 15px rgba(0, 120, 212, 0.8);
    }

    /* Modern Centered Uploader */
    [data-testid="stFileUploader"] {
        background-color: rgba(15, 23, 42, 0.85);
        border: 2px solid #0078d4;
        border-radius: 15px;
        padding: 15px;
    }

    /* Fixed Image Size */
    [data-testid="stImage"] img {
        max-width: 450px !important;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }

    /* White Text for Boxes & Metrics */
    .stAlert p {
        color: #ffffff !important;
        font-weight: 500;
    }
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-weight: bold;
    }

    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Azure Settings
VISION_ENDPOINT = os.getenv("AZURE_ENDPOINT")
VISION_KEY = os.getenv("AZURE_KEY")
TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
TRANSLATOR_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
TRANSLATOR_REGION = os.getenv("AZURE_TRANSLATOR_REGION")

client = ImageAnalysisClient(endpoint=VISION_ENDPOINT, credential=AzureKeyCredential(VISION_KEY))

def translate_to_sinhala(text):
    path = '/translate?api-version=3.0'
    params = f'&to=si'
    constructed_url = f"{TRANSLATOR_ENDPOINT}{path}{params}"
    headers = {
        'Ocp-Apim-Subscription-Key': TRANSLATOR_KEY,
        'Ocp-Apim-Subscription-Region': TRANSLATOR_REGION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{'text': text}]
    request = requests.post(constructed_url, headers=headers, json=body)
    return request.json()[0]['translations'][0]['text']

# Header Content
st.markdown('<h1 class="main-title">VisionAI Analytics Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#94a3b8;">• Powered by Azure AI</p>', unsafe_allow_html=True)

_, center_col, _ = st.columns([0.6, 1.8, 0.6])
with center_col:
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    draw = ImageDraw.Draw(image)

    with st.spinner('⏳ Scanning...'):
        uploaded_file.seek(0)
        image_data = uploaded_file.read()
        result = client.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.OBJECTS, VisualFeatures.CAPTION, VisualFeatures.READ]
        )

    tab1, tab2 = st.tabs(["🎯 DETECTION", "📝 TEXT ANALYSIS"])

    with tab1:
        c1, c2 = st.columns([1, 1])
        with c1:
            if result.objects:
                for obj in result.objects.list:
                    r = obj.bounding_box
                    draw.rectangle([(r.x, r.y), (r.x + r.width, r.y + r.height)], outline="#00ffcc", width=3)
            st.image(image)

        with c2:
            st.markdown("#### Scene Insights")
            if result.caption:
                st.info(f"{result.caption.text.capitalize()}")
                st.metric("Accuracy Score", f"{int(result.caption.confidence * 100)}%")

    with tab2:
        if result.read:
            full_text = " ".join([line.text for block in result.read.blocks for line in block.lines])
            if full_text.strip():
                t1, t2 = st.columns(2)
                with t1:
                    st.markdown("##### English OCR")
                    st.info(full_text)
                with t2:
                    st.markdown("##### Sinhala Translation")
                    st.success(translate_to_sinhala(full_text))