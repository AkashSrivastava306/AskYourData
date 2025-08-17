import streamlit as st
from supervisor import SupervisorAgent, IntentAgent
from multi_agent import CodeAgent, QAAgent
import os 
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("GROQ_API_KEY not found in .env")

llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")

def sanitize_dataframe(df):
    """Convert problematic object columns to strings so Streamlit can handle them."""
    for col in df.columns:
        if df[col].dtype == "O":
            df[col] = df[col].apply(lambda x: str(x) if x is not None else "")
    return df


def chat_with_data(df, llm=llm):
    st.subheader("💬 Chat with your Dataset")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ------------------ Display messages first ------------------
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            # Show code / text
            if "```python" in msg["content"]:
                code_block = msg["content"].split("```python")[1].split("```")[0]
                st.code(code_block, language="python")
                if "**Result:**" in msg["content"]:
                    result_text = msg["content"].split("**Result:**")[1].strip()
                    st.write(f"**Result:** {result_text}")
            else:
                st.write(msg["content"])

            # Show figure if exists
            if msg.get("fig"):
                st.pyplot(msg["fig"])

    # ------------------ User input at the bottom ------------------
    def submit():
        user_input = st.session_state.chat_input
        if not user_input:
            return

        # Agents
        code_agent = CodeAgent(llm)
        qa_agent = QAAgent(llm)
        intent_agent = IntentAgent(llm)
        supervisor = SupervisorAgent(llm, code_agent, qa_agent, intent_agent)

        # Run supervisor
        response = supervisor.run(
            query=user_input,
            dataset_info=f"Columns: {list(df.columns)}, Shape: {df.shape}",
            df=df
        )

        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Append AI message
        agent_type = response.get("agent", "")
        msg_content = ""
        fig = None

        if agent_type == "QA Agent":
            msg_content = response.get("explanation", "")
        elif agent_type == "Code Agent":
            code = response.get("code", "")
            msg_content = f"```python\n{code}\n```"
            result = response.get("result")
            if result is not None:
                msg_content += f"\n**Result:** {result}"
            fig = response.get("fig")

        st.session_state.messages.append({"role": "assistant", "content": msg_content, "fig": fig})

        # Clear input
        st.session_state.chat_input = ""

    st.text_input("Type your question here:", key="chat_input", on_change=submit)