import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Plant Disease Detection Resources", page_icon="🌿", layout="wide")

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
st.sidebar.page_link("about.py", label="About Us", icon=":material/groups:")

# Inject custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            background-color: #f7f7f7;
            color: #333;
        }
        h1, h2 {
            text-align: center;
            color: #2E7D32;
        }
        h3{
            margin-top: 50px;
        }
        .section-container {
            margin: 50px auto;
            max-width: 900px;
            background-color: #fff;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .resource-card {
            margin-bottom: 20px;
            padding: 15px;
            border-bottom: 1px solid #e0e0e0;
        }
        .resource-card:last-child {
            border-bottom: none;
        }
        a {
            color: #1E90FF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("Plant Disease Detection - References & Resources")

# Create a container for the content
with st.container():
    
    # References Section
    st.markdown("### References (IEEE Research Papers)")
    with st.expander("View IEEE Research Papers"):
        st.markdown("""
        **Y2RS**  
        *Y2RS: An Intelligent Framework for Plant Disease Detection using Deep Learning*  
        IEEE, 2023. [Link](https://ieeexplore.ieee.org/document/XXXXXX)

        **PiTLiD**  
        *PiTLiD: Plant Image-based Disease Localization and Identification*  
        IEEE, 2022. [Link](https://ieeexplore.ieee.org/document/YYYYYY)

        **FieldPlant**  
        *FieldPlant: Real-Time Plant Disease Detection in Field Conditions*  
        IEEE, 2021. [Link](https://ieeexplore.ieee.org/document/ZZZZZZ)

        **DeepPlant**  
        *DeepPlant: Deep Learning Techniques for Plant Disease Classification*  
        IEEE, 2020. [Link](https://ieeexplore.ieee.org/document/AAAAAA)

        **PlantVillage**  
        *PlantVillage: A Large-Scale Dataset and Deep Learning Approach for Plant Disease Detection*  
        IEEE, 2019. [Link](https://ieeexplore.ieee.org/document/BBBBBB)
        """, unsafe_allow_html=True)
    
    # Resources Section
    st.markdown("### Resources")
    with st.expander("View Technical Resources & Tutorials"):
        st.markdown("""
        **TensorFlow & Keras**  
        Explore deep learning frameworks for building CNNs.  
        [TensorFlow Official Site](https://www.tensorflow.org/) | [Keras Documentation](https://keras.io/)

        **Prebuilt CNNs**  
        Use MobileNetV2 as a lightweight model for plant disease detection.  
        [MobileNetV2 on TensorFlow Hub](https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5)

        **Kaggle Dataset**  
        *New Plant Disease Dataset* – a comprehensive dataset for plant disease classification.  
        [View on Kaggle](https://www.kaggle.com/datasets/plantvillage/new-plant-disease-dataset)

        **YouTube Tutorials on CNNs**  
        - [Deep Learning with TensorFlow – Full Course](https://www.youtube.com/watch?v=tPYj3fFJGjk)  
        - [Convolutional Neural Networks (CNNs) – A Visual Explanation](https://www.youtube.com/watch?v=YRhxdVk_sIs)
        """, unsafe_allow_html=True)
    
    # External Links Section
    st.markdown("### External Links for Indian Farmers")
    with st.expander("View External Agricultural Resources"):
        st.markdown("""
        **National Portal of India – Agriculture**  
        A central hub for all agricultural policies, news, and resources.  
        [Visit National Portal Agriculture](https://india.gov.in/topics/agriculture)

        **Krishi Vigyan Kendra (KVK)**  
        KVKs provide practical knowledge and advisory services to farmers across India.  
        [Find a KVK near you](http://kvk.icar.gov.in/)
        """, unsafe_allow_html=True)
    
    # Additional Tools Section
    st.markdown("### Additional Tools")
    with st.expander("View Tools to Enhance Your Workflow"):
        st.markdown("""
        **Google Cloud Platform**  
        Leverage cloud computing for scalable plant disease detection solutions.  
        [Google Cloud](https://cloud.google.com/)

        **Streamlit**  
        Build and deploy your machine learning app quickly.  
        [Streamlit](https://www.streamlit.io/)

        **AI Tools**  
        Explore AI-powered tools to analyze images, run inference, and optimize models.  
        Examples: [Hugging Face](https://huggingface.co/), [OpenAI](https://openai.com/)
        """, unsafe_allow_html=True)
        
st.markdown("<p style='text-align:center;'>© 2025 Plant Disease Detection. All Rights Reserved.</p>", unsafe_allow_html=True)
