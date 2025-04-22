import streamlit as st
from google import genai
import json as js

client = genai.Client(api_key="AIzaSyB1MSHiCCh0G5Nbxk49LQJUWUcaCzVFSE8")
with open("landing_page_language.json", "r", encoding="utf-8") as f:
    translations = js.load(f)

# 2. Initialize session_state for language
if "lang" not in st.session_state:
    st.session_state.lang = translations["defaultLanguage"]
    
# 4. Helper to fetch the right string
def t(key_path: str) -> str:
    """
    key_path: dot‑separated path into the JSON, e.g. "nav.detectDisease"
    """
    node = translations[st.session_state.lang]
    for part in key_path.split("."):
        node = node.get(part, "")
    return node

# Set page title and layout
st.set_page_config(page_title="LeafScan: Plant Disease Detector", page_icon="🌿", layout="wide")
# Styling the main layout
st.markdown("""
    <style>
        .main {
            background-color: #e8f5e9;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #2e7d32;
        }
        .subtitle {
            font-size: 24px;
            text-align: center;
            color: #388e3c;
        }
        .description {
            font-size: 18px;
            text-align: center;
            color: #555;
            margin-top: 20px;
        }
        .button-container {
            text-align: center;
            margin-top: 30px;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            font-size: 14px;
            color: #777;
        }
        .container {
            display: flex;
            justify-content: center; /* Aligns images to the center */
            gap: 10px; /* Adds space between images */
        }
        [data-testid="stSidebar"] {
            background-color: #77B254; /* Dark green background */
            color: #FFFFFF; /* Text color */
        }
        

        [data-testid="stSidebarNav"] a {
            font-size: 18px;
            color: #FFFFFF; /* White text color */
        }
        [data-testid="stSidebarNav"] a:hover {
            color: #66bb6a;
        }

    
    </style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image("leaf.png", use_container_width=False, width=50)

st.sidebar.title(t("nav.heading"))
st.sidebar.markdown("""
        <style>
        /* Target the radio button labels in the sidebar */
    .stSidebar .stRadio label {
        color: #FFFFFF;  /* Tomato color for the label text */
        font-size: 20px;  /* Larger font size */
        font-weight: bold;  /* Make the text bold */
    }

    /* Change color on hover */
    .stSidebar .st-radio label:hover {
        color: #000000;  /* Green color on hover */
    }

    div[data-testid="stRadio"]
  div[data-testid="stMarkdownContainer"]
    p {
    color: white !important; /* Set the text color to black */
    font-size: 18px !important; /* Adjust the font size */
    font-weight: bold !important; /* Make the text bold */
    padding: 5px !important; /* Optional: Adjust padding for better readability */
}

    div[data-testid="stSelectbox"] label[data-testid="stWidgetLabel"] div[data-testid="stMarkdownContainer"] p {
        color: white; /* Set the text color to black */
        font-size: 18px; /* Adjust the font size */
        font-weight: bold; /* Make the text bold */
        padding: 5px; /* Optional: Adjust padding for better readability */
    }
    
    /* Target the radio button input (circle) */
    .stSidebar .st-radio input[type="radio"] {
        accent-color: #FFFFFF;  /* Change the color of the radio button itself */
        color = #FFFFFF; /* Change the color of the radio button itself */
    }
    .stSidebar .stRadio input[type="radio"]:checked {
        background-color: #FFD700;  /* Yellow background for checked radio button */
    }
    </style>""", unsafe_allow_html=True)
#JSON File Content (Nest whenever '{}' is used):
#Navigation{"Navigation", "Home" ,"Detect Disease", "About Us", "Resources & References"}
st.sidebar.page_link("detect.py", label=t("nav.detectDisease"), icon=":material/image_search:")
st.sidebar.page_link("about.py", label=t("nav.aboutUs"), icon=":material/groups:")
st.sidebar.page_link("resources.py", label=t("nav.resources"), icon=":material/library_books:")
# 3. Language selector in the sidebar
lang_labels = {
    "en": "English",
    "hi": "हिन्दी",
    "mr": "मराठी",
}

st.sidebar.selectbox(
    t("nav.language"),
    options=list(lang_labels.keys()),
    format_func=lambda k: lang_labels[k],
    key="lang",
)

chat = client.chats.create(model="gemini-2.0-flash", config= genai.types.GenerateContentConfig(system_instruction= f"Answer the question about plants and plant diseases in a simple and precise manner. If the question is not about plants, plant diseases or agriculture, say that you are unable to answer that question. Answer in the language {lang_labels[st.session_state.lang]}", max_output_tokens=1000, temperature=0.05))
question = st.text_input(label=t("placeholder.askQuestion"), value="", max_chars=200, key="question", type="default", help="Click to get an answer about questions") 
try:
    if question:
        response = chat.send_message(question)
        st.write(response.text)
except:
    st.write("Server Error")

# Landing Page UI
tagline = t("title.tagline")  # Store the value separately
subtitle = f"<h2 class='subtitle'>{tagline}</h2>"
title = t("title.brand")  # Store the value separately
st.markdown(f"<h1 class='title'>🌿 {title}</h1>", unsafe_allow_html=True)
st.markdown(subtitle, unsafe_allow_html=True)

# Image Display
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("plant_leaf.jpg", use_container_width=True, caption=t("caption.upload"), width=300)

# App Description
description = t("description")  # Store the value separately
st.markdown(f"<p class='description'>{description}</p>", unsafe_allow_html=True)

# "Get Started" Button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
getStarted = t("button.getStarted")
st.page_link("detect.py", label=f"🌱 {getStarted}")  # Assuming there's a Detection page
st.markdown("</div>", unsafe_allow_html=True)

# Footer
#st.markdown("<div class='footer'>Developed by  | Powered by Deep Learning</div>", unsafe_allow_html=True)