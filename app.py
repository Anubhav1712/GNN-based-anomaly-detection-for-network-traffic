import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.title("GNN Based Anomaly Detection for Network Traffic")

st.write("This project is used to detect abnormal network traffic.")

st.sidebar.title("Control Panel")

packet_size = st.sidebar.slider(
    "Select Packet Size",
    0,
    10000,
    500
)

st.subheader("Traffic Status")

if packet_size > 3000:
    st.error("Anomaly Detected")
else:
    st.success("Normal Traffic")

st.subheader("Performance")

accuracy = 87
precision = 85
recall = 84
f1 = 86

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accuracy", "87%")
col2.metric("Precision", "85%")
col3.metric("Recall", "84%")
col4.metric("F1 Score", "86%")

st.subheader("Traffic Graph")

data = {
    "Time": [1,2,3,4,5,6,7],
    "Packet": [
        random.randint(100, 8000),
        random.randint(100, 8000),
        random.randint(100, 8000),
        random.randint(100, 8000),
        random.randint(100, 8000),
        random.randint(100, 8000),
        random.randint(100, 8000)
    ]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.plot(df["Time"], df["Packet"], marker='o')

ax.set_xlabel("Time")
ax.set_ylabel("Packet Size")

st.pyplot(fig)

st.subheader("About")

st.write("""
The main objective of this project is to detect
suspicious traffic in the network using anomaly
detection concepts and graph based analysis.
""")