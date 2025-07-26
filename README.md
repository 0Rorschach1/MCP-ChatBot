

````markdown
# 🧠 MCP Chatbot with Ollama + LangChain

This is a simple interactive chatbot with memory using:

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com) for local LLMs (e.g. LLaMA 3.1)
- [MCP (Model Context Protocol)](https://github.com/microsoft/playwright-mcp) for external tool integration

---

## 🚀 Features

- ✅ Built-in conversation memory
- ✅ Interactive terminal chat
- ✅ Uses local model (`llama3.1`) via Ollama
- ✅ Accesses external tools (filesystem, time, Airbnb, etc.)

---

## ⚙️ Setup Instructions

### 1. Install Ollama

Download and install Ollama from [https://ollama.com](https://ollama.com)  
Or on Unix systems:

```bash
curl -fsSL https://ollama.com/install.sh | sh
````

---

### 2. Pull the LLaMA model

```bash
ollama pull llama3.1
```

> 📦 This will download \~3–4GB

---

### 3. Clone and install project dependencies

```bash
git clone https://github.com/0Rorschach1/MCP-ChatBot.git
cd MCP-ChatBot
make install
```

---

### 4. Start the Ollama server

```bash
make serve
```

> This runs `ollama serve` in the background

---

### 5. Run the chatbot!

```bash
make run
```

You’ll now be in an interactive terminal chat.

---

### 💬 Commands in Chat

* Type any question to ask the model.
* Type `clear` to reset conversation memory.
* Type `exit` or `quit` to end the chat.

---

## 🧠 About MCP

Model Context Protocol (MCP) allows LLMs to interact with external tools like:

* Local files
* Time zones
* Search engines
* Airbnb APIs
* Databases

It acts like a plugin system for language models.

---

## 📁 Filesystem Setup

The `main3.py` uses a config that connects to:

```json
"C:/Users/V.V/Desktop/" and "C:/Users/V.V/Desktop/WWW"
```

You can change that in the script if needed.

---

## 📝 License

MIT

---

## 📬 Contact

Made with ❤️ by \[Your Name or Handle]

```

---

Let me know your GitHub username and repo name if you’d like me to generate the full folder layout or upload-ready files. I can also help package `mcp_use` if you want others to run it easily.
```
