import os
from huggingface_hub import login
from dotenv import load_dotenv
import json_repair
from os.path import join

load_dotenv()


login(token=os.getenv('hf_token'))

def parse_json(text):
    try:
        return json_repair.loads(text)
    except:
        return None

