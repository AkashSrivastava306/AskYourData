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
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("GROQ_API_KEY not found in .env")
    st.stop()

llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")

# Initialize agents
code_agent = CodeAgent(llm)
qa_agent = QAAgent(llm)
intent_agent = IntentAgent(llm)
supervisor = SupervisorAgent(llm, code_agent, qa_agent, intent_agent)

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🧠 Data Analyst AI Agent")

# File upload
uploaded_file = st.file_uploader("Upload your CSV/XLSX file", type=["csv", "xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Clean dataset
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)

    # ------------------------------
    # Fix PyArrow serialization issue
    # ------------------------------
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)

    df.columns = [c.strip().lower() for c in df.columns]

    st.success("✅ Dataset loaded successfully!")

    # ------------------------------
    # Sidebar dropdown for stats
    # ------------------------------
    show_dataset_stats_dropdown(df)
    
    # ------------------------------
    # User query input for AI agents
    # ------------------------------
    # query = st.text_input("Ask me anything about your dataset:")
    # if query:
    #     response = supervisor.run(query, dataset_info, df)

    #     # Display response
    #     if response.get("agent") == "Code Agent":
    #         st.subheader("🖥️ Generated Code")
    #         st.code(response["code"], language="python")

    #         st.subheader("✅ Execution Result")
    #         st.write(response["result"])

    #         if response["fig"] is not None:
    #             st.subheader("📊 Plot Output")
    #             st.pyplot(response["fig"])

    #     elif response.get("agent") == "QA Agent":
    #         st.subheader("💡 Answer from QA Agent")
    #         st.write(response["explanation"])
            
