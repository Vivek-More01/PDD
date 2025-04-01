import streamlit as st
from time import sleep

pg = st.navigation([st.Page("landing.py"), st.Page("detect.py"), st.Page("resources.py"), st.Page("about.py")])
pg.run()