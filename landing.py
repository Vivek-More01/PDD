import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyB1MSHiCCh0G5Nbxk49LQJUWUcaCzVFSE8")

# Set page title and layout
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="wide")
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
        display: None;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image("leaf.png", use_container_width=False, width=50)
st.sidebar.title("Navigation")
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
    /* Change the color of text inside radio buttons */
    div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF; /* Set the color to Tomato (or any color you want) */
        font-weight: bold; /* Optional: Make the text bold */
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
pages = st.sidebar.radio("Select a page from the menu.",["Home","Upload Image", "About", "Resources"], index=0, help="Select a page to navigate to")
if pages == "About":
    st.switch_page("About")
elif pages == "Resources":
    st.switch_page("Resources")
elif pages == "Upload Image":
    st.switch_page("detect")
chat = client.chats.create(model="gemini-2.0-flash", config= genai.types.GenerateContentConfig(system_instruction="Answer the question about plants in a simple and precise manner", max_output_tokens=1000, temperature=0.05))
question = st.text_input(label="Ask a question about plants", value="", max_chars=200, key="question", type="default", help="Click to get an answer about questions") 
try:
    if question:
        response = chat.send_message(question)
        st.write(response.text)
except:
    st.write("Server Error")

# Landing Page UI
st.markdown("<h1 class='title'>🌿 Plant Disease Detection</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Identify plant diseases using deep learning</h2>", unsafe_allow_html=True)

# Image Display
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("plant_leaf.jpg", use_container_width=True, caption="Upload a leaf image to detect diseases", width=300)

# App Description
st.markdown("<p class='description'>This app uses a **CNN model** to analyze leaf images and detect plant diseases with high accuracy. Simply upload an image, and the model will provide insights about the plant's health.</p>", unsafe_allow_html=True)

# "Get Started" Button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
if st.button("🌱 Get Started"):
    st.switch_page("Detection")  # Assuming there's a Detection page
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed by Your Name | Powered by Deep Learning</div>", unsafe_allow_html=True)