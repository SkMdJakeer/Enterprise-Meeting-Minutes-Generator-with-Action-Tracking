# 📘 Enterprise Meeting Minutes Multi-Agent System
### Automated Meeting Summary • Action Extraction • Decision Detection  
Built with a Planner → Worker → Evaluator AI architecture

## 📌 Overview
This project is an **Enterprise-grade Multi-Agent AI System** that converts raw meeting transcripts into:
- Concise summaries  
- Action items (task, owner, due date)  
- Decisions made  
- Structured JSON minutes  

It uses a **Planner → Worker → Evaluator pipeline**, suitable for Kaggle Capstone submissions and Hugging Face Spaces.

## 🧠 Multi-Agent Architecture

### 1. Planner Agent
- Splits transcript into chunks  
- Creates tasks: `summarize`, `extract_actions`, `extract_decisions`

### 2. Worker Agent
- Executes tasks  
- Runs summarizer and regex-based action/decision extraction  

### 3. Evaluator Agent
- Merges results  
- Removes duplicates  
- Produces final meeting minutes JSON  

## 📂 Project Structure
```
project/
  agents/ (planner, worker, evaluator)
  tools/ (summarizer, regex extractors)
  memory/ (session memory)
  core/ (context, logging, protocol)
  main_agent.py
  app.py
  run_demo.py
  requirements.txt
```

## 🚀 How to Run

### Demo:
```
python project/run_demo.py
```

### Programmatic:
```python
from project.main_agent import run_agent
print(run_agent("Hello!"))
```

## 📦 Install
```
pip install -r project/requirements.txt
```

## 🧾 Example Transcript
```
Tom: I will send the invoice.
```

## ✔ Example Output
```json
{
  "summary": "Tom: I will send the invoice.",
  "actions": [{"text": "Tom: I will send the invoice."}],
  "decisions": []
}
```

## 🎯 Use Cases
- Kaggle Capstone  
- Enterprise AI agents  
- Meeting automation tools  
- Multi-agent experimentation  

## 📄 License
For educational use.
