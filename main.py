import streamlit

import pandas as pd
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

streamlit.markdown("""
  <div style="background-color:#c5f18a;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
    <center>
      <h5>ข้อมูล iris หรือข้อมูลดอกไม้สำหรับทำนาย</h5>
    </center>
  </div>
""",
unsafe_allow_html=True)


dt = pd.read_csv("public/data/iris-3.csv")

streamlit.subheader("ข้อมูลส่วนแรก 10 แถว")
streamlit.write(dt.head(10))
streamlit.subheader("ข้อมูลส่วนสุดท้าย 10 แถว")
streamlit.write(dt.tail(10))
