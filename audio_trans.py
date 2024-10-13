import os
import sys 
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import keys
from groq import Groq

client = Groq()

filename = os.path.join(os.path.dirname(__file__),"data/harvard.wav")

with open(filename,'rb') as f:
    trans = client.audio.transcriptions.create(
        model="whisper-large-v3-turbo",
        file=(filename,f.read()),
        response_format='json'
   
    )
    print(trans)