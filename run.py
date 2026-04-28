# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from multi_agent import CodeAgent, QAAgent
from supervisor import SupervisorAgent, IntentAgent
from stats_agent import show_dataset_stats_dropdown
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# ------------------------------
# Load environment & initialize LLM
# ------------------------------
import streamlit as st
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

llm = ChatGroq(api_key=GROQ_API_KEY, model="gemma2-9b-it")

# Initialize agents
code_agent = CodeAgent(llm)
qa_agent = QAAgent(llm)
intent_agent = IntentAgent(llm)
supervisor = SupervisorAgent(llm, code_agent, qa_agent, intent_agent)

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("Ask Your Data")

# File upload
uploaded_file = st.file_uploader("Upload your CSV/XLSX file", type=["csv", "xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)

    df.columns = [c.strip().lower() for c in df.columns]

    st.success("✅ Dataset loaded successfully!")

    # ------------------------------
    # Sidebar dropdown for stats
    # ------------------------------
    show_dataset_stats_dropdown(df)
    

            


