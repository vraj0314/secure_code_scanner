from ollama import chat
from prompts import SYSTEM_PROMPT
import sys
def scan_code(code_snip):
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user',   'content': code_snip},
    ]
    result = ""                        # start with empty string
    for part in chat('qwen2.5-coder:7b', messages=messages, stream=True):
        result += part.message.content  # add each piece to result
        print(part.message.content, end='', flush=True)  # optional: live output
    return result                      # send it back to app.py