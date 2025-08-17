from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from multi_agent import CodeAgent ,QAAgent

class IntentAgent:
    def __init__(self, llm):
        self.llm = llm
        self.code_keywords = ["max", "min", "sum", "average", "mean", "plot", "count", "median"]

    def detect(self, query: str) -> str:
        # Force code if keyword present
        if any(k.lower() in query.lower() for k in self.code_keywords):
            return "code"

        # Otherwise, fallback to LLM detection
        prompt = f"""
You are an assistant that detects the intent of user queries about a dataset.
Classify the following query into one of two intents:
- "code" : requires executing pandas/matplotlib/seaborn code to compute a value or generate a plot. This includes max, min, mean, median, sum, std, skewness, correlation, etc.
- "qa" : requires explanation/statistical answer in natural language only.
Query: "{query}"
Return only one word: code or qa
"""
        response = self.llm.invoke(prompt)
        intent = response.content.strip().lower()
        if intent not in ["code", "qa"]:
            intent = "qa"  # default to QA
        return intent

from langchain.memory import ConversationBufferMemory

class SupervisorAgent:
    def __init__(self, llm, CodeAgent, QAAgent, IntentAgent):
        self.llm = llm
        self.code_agent = CodeAgent
        self.qa_agent = QAAgent
        self.intent_agent = IntentAgent
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def run(self, query, dataset_info, df):
        # Store query in memory
        self.memory.chat_memory.add_user_message(query)

        # Detect intent
        intent = self.intent_agent.detect(query)

        if intent == "code":
            code, result, fig = self.code_agent.run(dataset_info, query, df)
            response = {
                "agent": "Code Agent",
                "code": code,
                "result": result,
                "fig": fig
            }
        elif intent == "qa":
            explanation = self.qa_agent.answer(dataset_info, query)
            response = {
                "agent": "QA Agent",
                "explanation": explanation
            }

        # Store agent response in memory
        self.memory.chat_memory.add_ai_message(str(response))
        return response
