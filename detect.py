import streamlit as st
import tensorflow as tf
import numpy as np
import json as js
from google import genai

client = genai.Client(api_key="AIzaSyB1MSHiCCh0G5Nbxk49LQJUWUcaCzVFSE8")

models = {"MobileNetV2FT": "PPD_MobileNetV2_FT.keras","MNV_Plant_Village":"Plant_Disease_Model_PlantVillageAugmented.keras"}

#Input for model
def model_predictions(test_image, model1):
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
st.sidebar.page_link("about.py", label="About Us", icon=":material/groups:")
st.sidebar.page_link("resources.py", label="Resources & References", icon=":material/library_books:")
chat = client.chats.create(model="gemini-2.0-flash", config= genai.types.GenerateContentConfig(system_instruction="Answer the question about plants in a simple and precise manner", max_output_tokens=1000, temperature=0.05))


#Make an about page that is clickable
class_names_PV =["Apple___Apple_scab","Apple___Black_rot", "Apple___Cedar_apple_rust","Apple___healthy","Blueberry___healthy","Cherry_(including_sour)___Powdery_mildew","Cherry_(including_sour)___healthy",    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot","Corn_(maize)___Common_rust_",  "Corn_(maize)___Northern_Leaf_Blight","Corn_(maize)___healthy",   "Grape___Black_rot","Grape___Esca_(Black_Measles)","Grape___Leaf_blight_(Isariopsis_Leaf_Spot)","Grape___healthy ","Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot","Peach___healthy",    "Pepper,_bell___Bacterial_spot","Pepper,_bell___healthy","Potato___Early_blight",'Potato___Late_blight',  "Potato___healthy","Raspberry___healthy",   "Soybean___healthy","Squash___Powdery_mildew","Strawberry___Leaf_scorch","Strawberry___healthy",  "Tomato___Bacterial_spot","Tomato___Early_blight", "Tomato___Late_blight","Tomato___Leaf_Mold",  "Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite","Tomato___Target_Spot" ,"Tomato___Tomato_Yellow_Leaf_Curl_Virus","Tomato___Tomato_mosaic_virus","Tomato___healthy"] 

question = st.text_input(label="Ask a question about plants", value="", max_chars=200, key="question", type="default", help="Click to get an answer about questions") 
try:
    if question:
        response = chat.send_message(question)
        st.write(response.text)
except:
    st.write("Server Error")
st.title("Plant Disease Detection")
st.write("Capture a clean image for the plant disease detection")

model = st.sidebar.selectbox("Model", ["MobileNetV2FT","MNV_Plant_Village"])
language = st.sidebar.selectbox("Language", ["English", "Hindi", "Marathi"])
image_file = st.file_uploader("Upload a leaf image", type=["jpg", "png"])
if image_file is not None:
    returned = model_predictions(image_file, model)
    col_1, col_2, col_3 = st.columns([1, 1,1])
    with col_2:
        st.image(image_file, caption="Uploaded Image", use_container_width=True)
    
        Plant_Class = class_names_PV[returned].split("_")[0].strip()
        Predicted_Class = (' ').join(class_names_PV[returned].split("_")[1:]).strip()
        st.write(f"{Plant_Class}: {Predicted_Class}")

    if "healthy" in Predicted_Class:
        info_prompt = f"""Give Information about the plant {Plant_Class}"""
    else:
        info_prompt = f"""Give Information about disease {Predicted_Class} and how it affects the plant {Plant_Class}"""
    
    #Loading json file
    with open("Disease_Info_Database.Diseases.json", "r", encoding="utf-8") as f:
        disease_info = js.load(f)
    
    response = disease_info[0][language][Plant_Class][Predicted_Class]
    responses = response.split("/?#")
    if "healthy" in Predicted_Class:
        st.subheader(f"The {Plant_Class} Plant is Healthy")
        st.write(responses[1])
        st.expander("Common Diseases", expanded=False).write(responses[2])
        st.expander("Preventive Measures", expanded=False).write(responses[3])
    else:
        st.subheader(f"The {Plant_Class} Plant is suffering from {Predicted_Class} Diseas")
        st.write(responses[1])
        st.expander("Symptons", expanded=False).write(responses[2])
        st.expander("Causes", expanded=False).write(responses[3])
        st.expander("Solutions", expanded=False).write(responses[4])
else:
    st.write("Upload an image to get started!")