# TalkWithChatGPT Python Client

This repository originally contains Keyboard Maestro macros to interact with ChatGPT. It now also includes a simple Python script that lets you chat with ChatGPT from the command line.

## Requirements
- Python 3
- `requests` library (`pip install requests`)
- An OpenAI API key set in the environment variable `OPENAI_API_KEY`

## Usage
Run the script from a terminal:
```bash
python chat.py
```

Type your message and press enter. Type `exit` or `quit` to end the conversation.

## Keyboard Maestro Macros
The file "🎙️Talk with ChatGPT 1.0 Macros.kmmacros" contains a collection of macros for interacting with ChatGPT on macOS.
A helper macro in `chat_cli.kmmacros` launches the Python chat client via a hotkey (Ctrl+Option+K by default). Import the macro set into Keyboard Maestro to use it.
