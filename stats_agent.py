import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from multi_agent import CodeAgent, QAAgent
from supervisor import SupervisorAgent, IntentAgent
from chat_with_data import chat_with_data

def show_dataset_stats_dropdown(df: pd.DataFrame):
    """
    Display dataset stats and plots based on user-selected option from sidebar dropdown.
    """
    st.sidebar.subheader("📊 Dataset Analysis Options")

    # Define available options
    options = [
        "Dataset Info",
        "Missing Values",
        "Descriptive Statistics",
        "Correlation Matrix",
        "Numeric Column Plots",
        "Categorical Column Plots",
        "Chat with Data"
    ]

    choice = st.sidebar.selectbox("Select Analysis", options)

    # ------------------------------ Display results based on selection ------------------------------
    
    if choice == "Dataset Info":
        st.subheader("📁 Dataset Info")
        st.write("**Shape:**", df.shape)
        st.write("**Columns:**", list(df.columns))
        st.write("**Data types:**")
        st.dataframe(df.dtypes)

    elif choice == "Missing Values":
        st.subheader("⚠️ Missing Values")
        null_counts = df.isna().sum()
        st.dataframe(null_counts)

        if null_counts.sum() > 0:
            fig, ax = plt.subplots(figsize=(8,4))
            sns.barplot(x=null_counts.index, y=null_counts.values, palette="salmon", ax=ax)
            plt.title("Missing Values per Column")
            plt.ylabel("Number of Nulls")
            plt.xticks(rotation=45)
            st.pyplot(fig)

    elif choice == "Descriptive Statistics":
        st.subheader("📝 Descriptive Statistics")
        st.dataframe(df.describe(include='all').T)

        # ------------------------------ Numeric Column Plots ------------------------------
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            st.write("### 📊 Numeric Columns Distribution")
            for col in numeric_cols:
                fig, ax = plt.subplots()
                sns.histplot(df[col], kde=True, ax=ax)
                plt.title(f"{col} distribution")
                st.pyplot(fig)

        # ------------------------------ Categorical Column Plots ------------------------------
        categorical_cols = df.select_dtypes(include='object').columns
        if len(categorical_cols) > 0:
            st.write("### 📊 Categorical Columns Distribution")
            for col in categorical_cols:
                fig, ax = plt.subplots()
                df[col].value_counts().plot(kind='bar', ax=ax)
                plt.title(f"{col} counts")
                plt.xticks(rotation=45)
                st.pyplot(fig)

    elif choice == "Correlation Matrix":
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 1:
            st.subheader("📈 Correlation Matrix")
            corr = df[numeric_cols].corr()
            st.dataframe(corr)

            # Plot heatmap
            st.subheader("🌡️ Correlation Heatmap")
            fig, ax = plt.subplots(figsize=(8,6))
            sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.info("Not enough numeric columns for correlation matrix.")

    elif choice == "Numeric Column Plots":
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            selected_col = st.selectbox("Select numeric column", numeric_cols)
            fig, ax = plt.subplots()
            sns.histplot(df[selected_col], kde=True, ax=ax)
            st.pyplot(fig)
        else:
            st.info("No numeric columns found in dataset.")

    elif choice == "Categorical Column Plots":
        categorical_cols = df.select_dtypes(include='object').columns
        if len(categorical_cols) > 0:
            selected_col = st.selectbox("Select categorical column", categorical_cols)
            fig, ax = plt.subplots()
            df[selected_col].value_counts().plot(kind='bar', ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.info("No categorical columns found in dataset.")

    elif choice == "Chat with Data":
        chat_with_data(df)
