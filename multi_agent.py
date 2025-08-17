import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("GROQ_API_KEY not found in .env")

llm = ChatGroq(api_key=groq_api_key, model="gemma2-9b-it")

# code agent

class CodeAgent:
    def __init__(self, llm):
        self.llm = llm

    def generate_code(self, dataset_info: str, user_query: str) -> str:
        prompt_code = f"""
You are a data analyst assistant. User has dataset with info:
{dataset_info}
User query: "{user_query}"
Return only executable Python pandas/matplotlib/seaborn code.
Use 'df' as dataset. Do not add explanation.
if you are matplotlib or seaborn don't store value of this into result function
do not use print function 
the result variable will store the value 
"""
        response = self.llm.invoke(prompt_code)
        code = response.content
        # Clean code
        code = re.sub(r"```(?:python)?\n", "", code)
        code = re.sub(r"\n```", "", code).strip()
        return code

    def execute_code(self, code: str, df: pd.DataFrame):
        local_ns = {"df": df, "pd": pd, "plt": plt, "sns": sns, "result": None}
        try:
            # Execute the code
            exec(code, {}, local_ns)

            # If result not explicitly set, try evaluating last line
            result = local_ns.get("result", None)
            if result is None:
                try:
                    last_line = code.strip().split("\n")[-1]
                    result = eval(last_line, {"df": df, "pd": pd, "sns": sns, "plt": plt})
                except:
                    result = None

            # Detect if a figure exists
            if plt.get_fignums():  # some figure exists
                fig = plt.gcf()
            else:
                fig = None
            plt.close('all')

            return result, fig

        except Exception as e:
            return f"Error executing code: {e}", None

    def run(self, dataset_info: str, user_query: str, df: pd.DataFrame):
        code = self.generate_code(dataset_info, user_query)
        result, fig = self.execute_code(code, df)
        return code, result, fig
# QA Agent

class QAAgent:
    def __init__(self, llm):
        self.llm = llm

    def answer(self, dataset_info: str, user_query: str):
        prompt_qa = f"""
You are a data analyst who have knowledge about the data and statstics. Answer the following question in simple, friendly language:
User question: "{user_query}"
Dataset info:
{dataset_info}
"""
        response = self.llm.invoke(prompt_qa)
        return response.content.strip()
