# GenAI-3-43 Personalized Q/A chat bot

Project Class 25-26 • Week 3

## Note
This projects relies on these two repos:
- https://github.com/Demid00/GenAI-1-45/
- https://github.com/Demid00/GenAI-2-45/

---

## Description

This project implements a **locally running, document-grounded QA chatbot** with a minimal web interface built using Streamlit.
The system allows a user to upload or paste a text document and ask questions that are answered **strictly based on the provided content**, while maintaining conversational context across multiple turns.

The chatbot supports:

* User profile information (e.g. name) for lightweight personalization
* Context-aware responses that take previous questions into account
* Persistent chat history during a session
* Fully local execution (no external API calls at runtime)

The goal of the project is to demonstrate **context-aware question answering and personalization** in a simple, transparent, and easily inspectable setup.

---

## Model

This project uses the following pretrained QA model from Hugging Face:

**`AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru`**

* Architecture: XLM-RoBERTa Large
* Task: Extractive Question Answering
* Language focus: Multilingual, with fine-tuning on Russian QA data
* Source: Hugging Face Model Hub

The model is loaded locally and used for extractive question answering over user-provided documents.
All credit for the model architecture and fine-tuning belongs to its original author and contributors on Hugging Face.

---


## Setup
<details>
  <summary>Optional best practice</summary>

### Setup a virtual environment
**Linux/macOS:**
```sh
python -m venv venv
source venv/bin/activate
```

**Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

</details>

### Running
```sh
pip install -r requirements.txt
streamlit run ./app.py
```

## Improvements
Add support for using different models (be that local or remote with API keys).