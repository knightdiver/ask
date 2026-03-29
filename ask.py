#!/usr/bin/env python3

'''
A simple command-line tool to ask questions to the Ollama LLM server.

Prerequisites:
- ollama server running locally on port 11434
- requests library installed (pip install requests)

Usage:
$ python ask.py "What is the capital of France?"
This will send the prompt to the Ollama server and print the response in real-time as it is generated. 
You can also use it in a shell script or with other command-line tools by piping input to it:
$ echo "What is the capital of France?" | xargs python ask.py   
This will achieve the same result, allowing you to integrate it into larger workflows or scripts.
Note: Make sure to have the Ollama server running and the specified model available for this tool to work correctly.
'''

import sys
import requests
import json

# default Ollama API Enpoint on Jetson
OLLAMA_URL = "http://localhost:11434/api/generate"

# Available models
MODELS = {
    "llama": "llama3.2:3b",
    "gemma": "gemma3:4b"
}

DEFAULT_MODEL = "llama"

def ask(prompt, model):
    #send the prompt to the Ollama server and stream the response
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": True
    })
    
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            print(chunk.get("response", ""), end="", flush=True)
    print()

if __name__ == "__main__":
    args = sys.argv[1:]

    # Default model key
    model_key = DEFAULT_MODEL

    #check for model flag
    if "--model" in args:
        idx = args.index("--model")
        model_key = args[idx + 1]

        #remove the model flag and value from args
        args.pop(idx)  # remove --model
        args.pop(idx)  # remove the model name

        #validate the model
        if model_key not in MODELS:
            print(f"unknown model: '{model_key}' . Available models: {', '.join(MODELS.keys())}")
            sys.exit(1)

    #remainder args are the prompt
    if not args:
        print("Usage: ask [--model llama|gemma] 'your question here'")
        sys.exit(1)
    
    prompt = " ".join(args)
    ask(prompt, MODELS[model_key])