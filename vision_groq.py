import os
import sys 
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import keys
from groq import Groq

import base64

client = Groq()

def encode_image(img_path):
    with open(img_path,'rb') as img:
        return base64.b64encode(img.read()).decode('utf-8')

img_path  =  os.path.join(os.path.dirname(__file__),"data/images.jpg")

based_image =  encode_image(img_path)

cc =  client.chat.completions.create(
    messages = [
        {"role": "user",
         "content":[
             {"type": "text","text":"What is this image and information present in image?, retreive all the information in JSON "},
             {"type":"image_url","image_url":{
                 "url":f"data:image/jpg;base64,{based_image}"
             }}
              
         ]
        },
    ],
    model =  "llama-3.2-11b-vision-preview",
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    response_format={"type": "json_object"},
)

print(cc.choices[0].message.content)


