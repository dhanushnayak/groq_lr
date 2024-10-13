import os
import sys 
import json
from typing import List,Optional
from pydantic import BaseModel
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import keys
from groq import Groq

client = Groq()
class Ingredient(BaseModel):
    name: str
    quanity: str
    quanity_unit: Optional[str]
    
class Recipe(BaseModel):
    recipe_name: str
    ingredients: List[Ingredient]
    
    
def get_recipe(recipe_name: str) -> Recipe:
    cc =  client.chat.completions.create(
        messages = [
            {"role":"system",'content':"You are food recipe master that outputs in json.\n"
            f"The Json object must use the scheme: {json.dumps(Recipe.model_json_schema(),indent=2)}"},
            {"role": "user", "content": f"Fetch a recipe for {recipe_name}"}
        ],
        model='llama3-8b-8192',
        temperature =  1,
        stream = False,
        response_format= {"type":"json_object"}
    )
    output =  cc.choices[0].message.content
    return output

output_data = get_recipe("mutton briyani")
print(output_data)



