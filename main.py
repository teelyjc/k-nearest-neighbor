import streamlit

import pandas as pds
import numpy as np

streamlit.title("การจำแนกข้อมูลด้วยเทคนิค Machine Learning")
streamlit.image("public/images/me.jpeg")

col1, col2, col3 = streamlit.columns(3)

with col1:
  streamlit.header("Versicolor")
  streamlit.image("public/images/iris1.jpg")

with col2:
  streamlit.header("Verginiga")
  streamlit.image("public/images/iris2.jpg")

with col3:
  streamlit.header("Setosa")
  streamlit.image("public/images/iris3.jpg")