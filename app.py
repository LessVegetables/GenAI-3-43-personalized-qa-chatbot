import streamlit as st
from GenAI_2_45 import ParagraphQAEvaluator

st.set_page_config(page_title="QA Chatbot", layout="centered")

# -----------------------------
# Session state initialization
# -----------------------------
if "evaluator" not in st.session_state:
    evaluator = ParagraphQAEvaluator()
    evaluator.load_model()
    st.session_state.evaluator = evaluator

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {
        "name": ""
    }

# ----------------
# Helper funcitons
# ----------------
def update_context(document_text: str):
    st.session_state.document_text = document_text
    paragraphs = st.session_state.evaluator.load_text_into_paragraphed_arrays(document_text)
    context, paragraphs = st.session_state.evaluator.create_custom_document(paragraphs)
    pass

def show_chat_history():
    st.session_state.evaluator.logger.info(str("Chat history:\n\n" + str(st.session_state.chat_history) + "\n\n"))

# -----------------------------
# Sidebar: User profile & document
# -----------------------------
with st.sidebar:
    st.header("👤 User Profile")

    st.session_state.user_profile["name"] = st.text_input(
        "Name",
        value=st.session_state.user_profile["name"]
    )

    # st.session_state.user_profile["interests"] = st.text_input(
    #     "Interests",
    #     value=st.session_state.user_profile["interests"]
    # )

    # st.divider()
    st.header("📄 Information")

    uploaded_file = st.file_uploader("Upload pii.txt", type=["txt"])

    if uploaded_file is not None:
        st.session_state.document_text = uploaded_file.read().decode("utf-8")
        update_context(st.session_state.document_text)

    st.text_area(
        "Or paste document text here",
        value=st.session_state.document_text,
        height=250,
        key="document_text_input",
        on_change=lambda: update_context(st.session_state["document_text_input"])
    )

    st.button(
        "Show chat history",
        type="tertiary",
        on_click=show_chat_history
    )

# -----------------------------
# Main chat UI
# -----------------------------
st.title("💬 QA Chatbot")

# Render chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask a question about the document...")

if user_input:
    # Store user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # -----------------------------
    # Build personalized context
    # -----------------------------
    profile = st.session_state.user_profile
    history = st.session_state.chat_history[:-1]  # exclude current question

    context_prompt = f"""
        User profile:
        - Name: {profile['name']}

        Conversation history:
        """

    for msg in history:
        context_prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

    context_prompt += f"\nCurrent question:\n{user_input}"

    # -----------------------------
    # Call QA system
    # -----------------------------
    evaluator = st.session_state.evaluator

    st.session_state.evaluator.logger.info(str("Asking question:\t" + user_input))
    answer = evaluator.answer_question(question=context_prompt)
    st.session_state.evaluator.logger.info(str("Responded:\t\t" + answer))

    # Store assistant response
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)


