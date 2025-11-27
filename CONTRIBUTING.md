# Contributing to the Enterprise Meeting Minutes Multi‑Agent System

Thank you for your interest in contributing!  
This project implements a **Planner → Worker → Evaluator** AI architecture designed for meeting summarization, action extraction, and decision detection.

This `CONTRIBUTING.md` outlines how to contribute code, documentation, tests, or feature improvements to the repository.

---

# 📌 How You Can Contribute

### ✅ 1. Report Issues
Use GitHub Issues to report:
- Bugs
- Incorrect outputs
- Missing or duplicated actions
- Unexpected agent behavior
- UI / API issues

Please include:
- Your transcript input
- Steps to reproduce
- Expected vs actual output
- Logs (if available)

---

### ✅ 2. Suggest Improvements
You can propose:
- Better regex patterns for action/decision extraction  
- Improved summarization logic  
- New tools (date parser, entity resolver, etc.)  
- Additional test scenarios  
- Memory system upgrades  
- Evaluation logic improvements  

---

### ✅ 3. Contribute Code (Pull Requests)
Follow these steps:

#### Step 1 — Fork the repository
```
https://github.com/<your-username>/<repo-name>
```

#### Step 2 — Clone your fork
```
git clone https://github.com/<your-username>/<repo-name>
cd <repo-name>
```

#### Step 3 — Create a feature branch
```
git checkout -b feature/<short-description>
```

#### Step 4 — Install dependencies
```
pip install -r project/requirements.txt
```

#### Step 5 — Make your changes  
Keep your code consistent with the existing architecture:
- **Planner**: Creates tasks  
- **Worker**: Executes tasks using tools  
- **Evaluator**: Validates and merges  

#### Step 6 — Run tests
```
pytest -q
```

#### Step 7 — Commit & Push
```
git add .
git commit -m "feat: <short description>"
git push origin feature/<short-description>
```

#### Step 8 — Open Pull Request  
Provide:
- Description of the change  
- Why it is needed  
- How it was tested  
- Screenshots or logs (optional)

---

# 📁 Project Structure Guidelines

Please keep all contributions aligned with the existing folder structure:

```
project/
  agents/          # Planner, Worker, Evaluator
  tools/           # Summarizer, regex tools, extractors
  memory/          # Session memory
  core/            # Context engineering, logging, protocol
  main_agent.py    # Orchestrator
  app.py           # FastAPI app
  run_demo.py
```

Avoid placing Python files outside these folders unless necessary.

---

# 🧪 Testing Guidelines

### ✔ Write tests for:
- Planner logic  
- Worker task execution  
- Evaluator merging  
- Tool functions (summarizer, extraction, normalization)

### ✔ Tests should go in:
```
project/tests/
```

Example:
```
test_worker.py
test_planner.py
test_evaluator.py
```

---

# 🧹 Coding Standards

- Follow **PEP8** formatting  
- Use clear variable names  
- Add docstrings to all functions  
- Use **absolute imports**, e.g.:

```
from project.agents.planner import Planner
```

- Avoid unused code or commented blocks  
- Keep components modular and small  

---

# 🛡 Code of Conduct
Be respectful, collaborative, and constructive.  
Harassment, discrimination, or disrespectful behavior is not tolerated in issues or PR discussions.

---

# 📄 License
By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing — your help improves the system for everyone! 🚀
