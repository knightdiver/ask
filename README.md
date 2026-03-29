# ask

A simple command-line tool to query local LLMs via Ollama on a Jetson Orin Nano.

## Prerequisites
- Ollama running locally on port 11434
- Python 3
- requests library (`pip install requests`)

## Usage
```bash
ask "what is the capital of France?"
ask --model gemma "explain CUDA in one sentence"
```

## Models
- `llama` — llama3.2:3b (default)
- `gemma` — gemma3:4b

## Install
```bash
chmod +x ask.py
sudo cp ask.py /usr/local/bin/ask
```