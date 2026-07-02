from ollama import chat
from prompts import SYSTEM_PROMPT
import sys 

print("Press Ctrl+D (Unix) or Ctrl+Z (Windows) to exit:")

lines = sys.stdin.readlines()

code_snip = '\n'.join(lines)

messages = [

    { 'role': 'system',  'content': SYSTEM_PROMPT },  
    { 'role': 'user',    'content': code_snip     },  
   
]

for part in chat('qwen2.5-coder:7b', messages=messages, stream=True):
  print(part.message.content, end='', flush=True)
