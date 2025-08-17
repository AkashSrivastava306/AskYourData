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

---
Screenshot of Project


<img width="1666" height="758" alt="image" src="https://github.com/user-attachments/assets/f03c40c6-07a0-44d2-8d61-ae1736b81c67" />
<img width="1898" height="928" alt="image" src="https://github.com/user-attachments/assets/851b660d-edf2-4099-887f-e973edfa3c16" />
<img width="1889" height="906" alt="image" src="https://github.com/user-attachments/assets/ec954e64-1bb5-46be-86c7-78a21342524d" />
<img width="1865" height="826" alt="image" src="https://github.com/user-attachments/assets/2c12df7f-6c1e-48e6-9ed2-ed3dcdfbe4d9" />
<img width="1911" height="907" alt="image" src="https://github.com/user-attachments/assets/8aaeed10-fda7-4d04-bdf6-aefd5c43010c" />
<img width="1903" height="863" alt="image" src="https://github.com/user-attachments/assets/db1a0bc9-92d1-426d-8e69-17864bb343fd" />
<img width="1911" height="902" alt="image" src="https://github.com/user-attachments/assets/958f75b5-78eb-421f-b22d-0c0d8c89b33e" />
<img width="1864" height="862" alt="image" src="https://github.com/user-attachments/assets/e888f6cc-0882-4792-b436-cebc9f5fe386" />
<img width="1890" height="896" alt="image" src="https://github.com/user-attachments/assets/e4a226c2-954a-4913-943a-3c60fc4189dc" />
<img width="1903" height="834" alt="image" src="https://github.com/user-attachments/assets/b4fd9bed-f889-4e02-b9c9-55e882656c8d" />
<img width="1896" height="813" alt="image" src="https://github.com/user-attachments/assets/c35797d0-31eb-463f-bb38-be56b28462cf" />
<img width="1820" height="671" alt="image" src="https://github.com/user-attachments/assets/83ca5bea-bff0-498a-adda-c229b2fa3088" />
<img width="1840" height="863" alt="image" src="https://github.com/user-attachments/assets/609998c6-b534-4b48-999a-ae40dfee4a15" />
<img width="1909" height="789" alt="image" src="https://github.com/user-attachments/assets/efba61fb-f892-484b-9577-02fbdf287089" />
<img width="1917" height="863" alt="image" src="https://github.com/user-attachments/assets/b619864d-e7f4-4957-989f-e932e179eb28" />
<img width="1904" height="806" alt="image" src="https://github.com/user-attachments/assets/4ba226e9-3dfa-439c-9948-75b8f75d7559" />





## 🤝 Contribution
Pull requests are welcome! For major changes, open an issue first to discuss your idea.

---

## 📜 License
This project is licensed under the MIT License.
