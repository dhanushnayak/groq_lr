import os
import sys 
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import keys
from groq import Groq

client = Groq()

cc = client.chat.completions.create(
    messages = [
        {"role":"system","content":"you are a science master assistance"},
        {"role":"user","content":"What is the definition of a black hole?"}
    ],
    model='llama3-8b-8192',
    temperature =  0.5,
    max_tokens =  1024,
    top_p=1,

    stream= False
)

print(cc.to_json())