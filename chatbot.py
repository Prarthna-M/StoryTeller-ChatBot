from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="StoryTeller AI",
    page_icon="📖",
    layout="centered"
)

# ---------- Simple styling ----------
st.markdown("""
<style>
/* Cute background */
.stApp {
    background-image: url("https://img.magnific.com/premium-photo/black-white-floral-design-white-background_960396-362158.jpg?semt=ais_test_b&w=740&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Center title */
h1 {
    text-align: center;
}

/* User message → left */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    flex-direction: row;
    justify-content: flex-start;
}

/* Assistant message → right */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    flex-direction: row-reverse;
    justify-content: flex-end;
}
</style>
""", unsafe_allow_html=True)

st.title("📖 StoryTeller AI")

# saves chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history for each re-render
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# LLM connection
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1.8
)

# get user input
user_input = st.chat_input("✨ Give me a character, place, or story idea...")

if user_input:
    st.chat_message("user").markdown(user_input)

    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    response = llm.invoke(
        input=[
            {
                "role": "system",
                "content": """You are StoryTeller AI, a creative and playful storytelling assistant.

            Your special rule is: ALWAYS answer the user's request as a short story.

            Even if the user asks something that is not related to stories, turn the answer into a story first.

            For example:
            - If the user asks "What is 5 + 5?", create a tiny story involving 5 + 5, then clearly state that the answer is 10.
            - If the user asks a factual question, explain the fact through a short story and then give the direct answer.
            - If the user asks a coding question, create a small story involving the coding problem, then explain the solution clearly.
            - If the user asks for a definition, explain the concept through a story and then provide the definition.

            Keep stories short, fun, imaginative and relevant to the question.
            Always make sure the actual answer is correct and easy to identify.

            Do not refuse a question just because it is not related to storytelling.
            """
            },
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.content

    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_response)