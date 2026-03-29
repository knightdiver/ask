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
#!/usr/bin/env python3
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

def ask(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": True
    })
    
    for line in response.iter_lines():
        if line:
            import json
            chunk = json.loads(line)
            print(chunk.get("response", ""), end="", flush=True)
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ask 'your question here'")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    ask(prompt)