# Talent-Scout-Hiring-Assisstant-AI-Chatbot
# 🧠 TalentScout Hiring Assistant

**TalentScout Hiring Assistant** is an AI-powered recruitment chatbot that collects candidate details, generates technical questions based on the candidate's tech stack, and records their responses for review. It’s built using Streamlit and leverages the **Claude Haiku LLM** via OpenRouter for dynamic question generation.

---

## 🔧 Features

- 📋 Collects candidate info: Name, email, phone, experience, desired position, etc.
- 🤖 Uses Claude Haiku (via OpenRouter) to generate relevant technical questions based on the tech stack provided.
- 💬 Asks all questions at once and collects answers.
- 📁 Saves candidate details in a `CSV` file (`candidate_data.csv`).
- 📝 Saves questions and candidate answers in a separate `.txt` file (e.g., `John_Doe_qa.txt`).
- 🎨 Dynamic background from Unsplash to keep the UI fresh and appealing.
- ✅ Session tracking with `st.session_state`.

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| LLM | Claude Haiku via OpenRouter |
| Language | Python 3.11+ |
| Storage | CSV and TXT file system |
| API Client | `openai` (for OpenRouter compatibility) |

---

## 🔗 LLM Integration via OpenRouter

Claude Haiku is accessed using OpenRouter-compatible endpoints.

To configure:
1. Sign up and get your API key from [https://openrouter.ai](https://openrouter.ai).
2. Use the Claude Haiku model endpoint:
   ```python
   client = OpenAI(
       api_key=os.getenv("OPENROUTER_API_KEY") or st.secrets["openai"]["api_key"],
       base_url="https://openrouter.ai/api/v1"
   )


## FILE STRUCTURE
├── app.py                  # Main Streamlit app
├── utils.py                # Question generation logic using Claude Haiku
├── requirements.txt        # Python dependencies
├── candidate_data.csv      # Appends candidate details
├── *_qa.txt                # Saves questions & answers per candidate
├── README.md               # Project documentation

## How to run
```bash
git clone https://github.com/your-username/talent-assistant.git
cd talent-assistant
```

## Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Or venv\Scripts\activate on Windows
```

## Set up your API key
```bash
[openai]
api_key = "your-openrouter-api-key"
```

## Model Info
LLM Used: Claude Haiku
Provider: OpenRouter.ai
Model Endpoint Used: anthropic/claude-3-haiku
API Base URL: https://openrouter.ai/api/v1

