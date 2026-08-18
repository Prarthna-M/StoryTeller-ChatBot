# 📖 StoryTeller AI

An interactive **AI-powered storytelling chatbot** built with **Python, Streamlit, LangChain, and Groq**.

StoryTeller AI turns every user request into a short, creative story. Even when the user asks something unrelated to storytelling—such as a mathematical question, programming question, or general knowledge question—the AI answers it through an engaging story while still providing the correct answer.

## ✨ Features

* 📖 **AI Storytelling** — Generates creative and engaging stories.
* 💬 **Interactive Chatbot** — Chat naturally with the AI through Streamlit's chat interface.
* 🧠 **Conversation Memory** — Maintains previous messages using `st.session_state`.
* 🎭 **Story-Based Answers** — Converts even non-story questions into short stories.
* 🧮 **Accurate Answers** — Provides the actual answer after presenting it creatively.
* 🎨 **Custom UI** — Centered title, custom background, and left/right chat alignment.
* ⚡ **Groq LLM** — Uses Groq for fast AI inference.
* 🔐 **Environment Variables** — API keys are stored securely using Streamlit Secrets / `.env`.

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Programming language            |
| Streamlit     | Web interface                   |
| LangChain     | LLM integration                 |
| ChatGroq      | Groq model integration          |
| Groq          | AI inference                    |
| python-dotenv | Environment variable management |

## 📂 Project Structure

```text
storyteller-chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── chatbot_bg.png
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/storyteller-chatbot.git
cd storyteller-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API Key

Create a `.env` file in the project directory:

```text
GROQ_API_KEY=your_groq_api_key
```

**Never commit your `.env` file to GitHub.**

Add it to `.gitignore`:

```text
.env
venv/
__pycache__/
```

### 5. Run the application

```bash
streamlit run chatbot.py
```

The application will open in your browser.

## 🔑 Streamlit Cloud Deployment

The application can be deployed using Streamlit Community Cloud.

After connecting the GitHub repository:

1. Select `chatbot.py` as the main file.
2. Add the required dependencies from `requirements.txt`.
3. Open **App Settings → Secrets**.
4. Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

5. Save and restart the application.

The API key should **not** be pushed to GitHub.

## 🤖 How It Works

The application uses Streamlit's chat interface and session state to maintain conversations.

### Conversation Flow

```text
User enters a message
        ↓
st.chat_input()
        ↓
Message stored in session_state
        ↓
Previous conversation + new message
        ↓
System storytelling prompt
        ↓
Groq LLM
        ↓
Creative response
        ↓
Response stored in session_state
        ↓
Displayed in chat interface
```

### Chat History

Streamlit reruns the Python script whenever the user interacts with the application.

To preserve the conversation between reruns, the application uses:

```python
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
```

Messages are then stored as:

```python
{
    "role": "user",
    "content": user_input
}
```

and:

```python
{
    "role": "assistant",
    "content": assistant_response
}
```

The previous messages are sent to the LLM using:

```python
*st.session_state.chat_history
```

The `*` operator unpacks the chat history so that each message becomes an individual item in the message list.

## 🎭 Storytelling Behavior

The chatbot is instructed through a system prompt to always answer through a story.

For example, if the user asks:

```text
What is 5 + 5?
```

Instead of simply responding:

```text
10
```

the AI might create a small story involving two groups of five objects and conclude:

```text
Therefore, 5 + 5 = 10.
```

Similarly, programming, factual, or general questions are explained through short stories while still providing the correct information.

## 🎨 User Interface

The application includes custom CSS for:

* Centering the title
* Custom background image
* Left-aligned user messages
* Right-aligned assistant messages
* Chat-focused layout

The UI is implemented using Streamlit's built-in:

```python
st.chat_message()
```

and:

```python
st.chat_input()
```

## 📦 Requirements

Example `requirements.txt`:

```text
streamlit
langchain-groq
python-dotenv
```

Install them using:

```bash
pip install -r requirements.txt
```

## 🔐 Security

Never expose your Groq API key in:

* GitHub repositories
* Python source code
* Screenshots
* README files
* Public Streamlit applications

For local development, use `.env`:

```text
GROQ_API_KEY=your_api_key
```

For Streamlit Cloud, use the application's **Secrets** configuration.

## 🔮 Future Improvements

Some possible enhancements:

* 🎨 Add story genre selection
* 🧙 Add character creation
* 🌍 Add different story worlds
* 🎵 Add background music
* 🖼️ Generate images for story scenes
* 💾 Allow users to save stories
* 📥 Add story download functionality
* 🔊 Add text-to-speech narration
* 👥 Add multiple storytelling personalities
* 🌙 Add light/dark themes

## 👩‍💻 Author

**Prarthna M.**

Built as a GenAI learning project using Python, Streamlit, LangChain, and Groq.

---

⭐ If you enjoyed StoryTeller AI, consider giving the repository a star!
