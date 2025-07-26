# Makefile for running MCP Chat with Ollama

# Install Python dependencies
install:
	pip install -r requirements.txt

# Download LLaMA 3.1 model using Ollama
pull-model:
	ollama pull llama3.1

# Start the Ollama server (runs in background)
serve:
	ollama serve

# Run the chatbot
run:
	python main3.py

# Clean environment (optional placeholder)
clean:
	echo "Nothing to clean yet."
