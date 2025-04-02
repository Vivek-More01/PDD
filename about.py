import streamlit as st
import tensorflow as tf
import numpy as np
import json as js

models = {"MobileNetV2FT": "PPD_MobileNetV2_FT.keras", "MobileNetV2":"Plant_Disease_Model_MobileNetV2_Default.keras", "NPDDCustom":"NPDDCustom_model.keras","ResNet50":"PPD_ResNet50.keras","MNV_Plant_Village":"Plant_Disease_Model_PlantVillageAugmented.keras"}
#Input for model
def model_predictions(test_image, model1 = 'NPDDCustom'):
    model = tf.keras.models.load_model(models[model1])
    input_image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    if model1 in ["MobileNetV2FT", "ResNet50"]:
        #Resizing image to 256x256
        input_image = tf.image.resize(input_image, (256,256))
    elif model1 == "MobileNetV2":
        #Resizing image to 224x224
        input_image = tf.image.resize(input_image, (224,224))
    input_arr = np.array([tf.keras.preprocessing.image.img_to_array(input_image)])
    predictions = model.predict(input_arr)
    return_index =  np.argmax(predictions)
    return return_index

#Changing layout of the page
st.set_page_config(page_title="Plant Disease Detection", page_icon="🌿", layout="wide")
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

st.sidebar.page_link("landing.py", label="Home", icon=":material/home:")
st.sidebar.page_link("detect.py", label="Detect Disease", icon=":material/image_search:")
st.sidebar.page_link("resources.py", label="Resources & References", icon=":material/library_books:")


# Project Overview Statement
st.title("About Us")
st.subheader("Vision & Mission")
st.write("""
Our project aims to leverage deep learning techniques, specifically Convolutional Neural Networks (CNN),
to develop an efficient plant disease detection system. By analyzing leaf images, our system will help
farmers and agriculturists identify diseases early, reducing crop losses and improving yield quality.
""")

# Team Member Details
st.subheader("Meet Our Team")

team_members = [
    {"name": "Swayam Korde", "roll": "25129", "email": "swayamkorde2005@gmail.com", "image": "swayam.png"},
    {"name": "Hrishikesh Mirashe", "roll": "25133", "email": "rushikesh20052@gmail.com", "image": "swayam.png"},
    {"name": "Vivek More", "roll": "25134", "email": "vivekmkmore1605@gmail.com", "image": "swayam.png"},
    {"name": "Nitish Panse", "roll": "25139", "email": "nitishpanse88@gmail.com", "image": "swayam.png"}
]

# Display Team Members
for member in team_members:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(f"{member['image']}", width=150)  # Add profile pictures in "static" folder
    with col2:
        st.write(f"**Name:** {member['name']}")
        st.write(f"**Roll No:** {member['roll']}")
        st.write(f"**Email:** {member['email']}")
    st.markdown("---")  # Separator line

