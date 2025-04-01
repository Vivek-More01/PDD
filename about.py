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
st.markdown(
    """
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    """,
    unsafe_allow_html=True
)
#Make an about page that is clickable
class_names_NPDD = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
class_names_PV =["Apple___Apple_scab","Apple___Black_rot", "Apple___Cedar_apple_rust","Apple___healthy","Blueberry___healthy","Cherry_(including_sour)___Powdery_mildew","Cherry_(including_sour)___healthy",    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot","Corn_(maize)___Common_rust_",  "Corn_(maize)___Northern_Leaf_Blight","Corn_(maize)___healthy",   "Grape___Black_rot","Grape___Esca_(Black_Measles)","Grape___Leaf_blight_(Isariopsis_Leaf_Spot)","Grape___healthy ","Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot","Peach___healthy",    "Pepper,_bell___Bacterial_spot","Pepper,_bell___healthy","Potato___Early_blight",'Potato___Late_blight',  "Potato___healthy","Raspberry___healthy",   "Soybean___healthy","Squash___Powdery_mildew","Strawberry___Leaf_scorch","Strawberry___healthy",  "Tomato___Bacterial_spot","Tomato___Early_blight", "Tomato___Late_blight","Tomato___Leaf_Mold",  "Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite","Tomato___Target_Spot" ,"Tomato___Tomato_Yellow_Leaf_Curl_Virus","Tomato___Tomato_mosaic_virus","Tomato___healthy"] 

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Resources"])

if page == "Home":
    st.title("Plant Disease Detection")
    st.write("Welcome to the Home Page!")
    
    model = st.sidebar.selectbox("Model", ["MobileNetV2FT", "NPDDCustom","MNV_Plant_Village"])
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
elif page == "About":

# Vision and Mission Statement
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
        {"name": "Swayam Korde", "roll": "25129", "email": "swayamkorde2005@gmail.com", "image": "swayam.jpg"},
        {"name": "Hrishikesh Mirashe", "roll": "25133", "email": "rushikesh20052@gmail.com", "image": "hrishikesh.jpg"},
        {"name": "Vivek More", "roll": "25134", "email": "vivekmkmore1605@gmail.com", "image": "vivek.jpg"},
        {"name": "Nitish Panse", "roll": "25139", "email": "nitishpanse88@gmail.com", "image": "nitish.jpg"}
    ]

    # Display Team Members
    for member in team_members:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(f"static/{member['image']}", width=150)  # Add profile pictures in "static" folder
        with col2:
            st.write(f"**Name:** {member['name']}")
            st.write(f"**Roll No:** {member['roll']}")
            st.write(f"**Email:** {member['email']}")
        st.markdown("---")  # Separator line


elif page == "Resources":
    st.title("Resources")
    st.markdown("Resources for Plant Disease Detection")
    st.markdown(f"""<h6>PlantVillage Dataset {class_names_PV}</h6>""")
