# AskYourData

AskYourData is an AI-powered data analysis assistant that lets you **chat with your dataset**.  
It executes Python code, performs data analysis, and visualizes insights — all through natural language queries.

---

## 🚀 Features
- Upload datasets (CSV, Excel, etc.).
- Ask questions in plain English.
- Get Python code generated and executed automatically.
- View tabular results directly in the chat.
- Generate and display **visualizations** (bar charts, line plots, etc.).
- Conversational interface powered by **LangChain** and **ChatGroq**.

---

## 🛠️ Tech Stack
- **Backend**: Flask  
- **AI Engine**: LangChain + ChatGroq  
- **Data Handling**: Pandas, Matplotlib  
- **Environment**: Python 3.10+  

---

## 📂 Project Structure
```
project-root/
│── run.py              # Main streamlit app
│── multi_agent.py      # Multi agent 
│── requirements.txt    # Dependencies
│── stats_agent.py      # State agent 
│── supervisor.py       # Supervisor agent who handle every agent
│── README.md           # Documentation
```

---

## ⚙️ Installation

1. Clone the repo:
```bash
git clone https://github.com/AkashSrivastava306/askyourdata.git
cd askyourdata
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your environment variables in `.env`:
```
GROQ_API_KEY=your_groq_api_key
```

5. Run the app:
```bash
streamlit run run.py
```

---

## 💡 Usage
1. Upload your dataset in the app interface.  
2. Ask questions like:  
   - "Show me the top 5 rows."  
   - "Plot a histogram of Age column."  
   - "Find correlation between Sales and Profit."  
3. Get instant answers, code execution, and visualizations.  

---

## 📊 Example Queries
- **"What is the average salary in this dataset?"**  
- **"Show a bar chart of sales by region."**  
- **"Find missing values in the dataset."**  

---

## 🤝 Contribution
Pull requests are welcome! For major changes, open an issue first to discuss your idea.

---

## 📜 License
This project is licensed under the MIT License.
