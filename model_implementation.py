import os
from dotenv import load_dotenv
load_dotenv()

from transformers import AutoTokenizer, AutoModelForCausalLM,BitsAndBytesConfig


model = AutoModelForCausalLM.from_pretrained(
    os.getenv("base_model_id"),
    device_map= "auto", # ki tebde te5dem 3el gpu "auto"
    torch_dtype = None   # yloadi el llm model fel gpu memory bech nbedlou 7ajm el volume mte3 el parametres s7i7 rapide eme rahou 3le 7seb el qualité
).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(os.getenv("base_model_id"))