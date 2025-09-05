from Shemas import NewsDetails
import json

from article import story_article



details_extarction_message = [
    {
        "role": "system",
        "content": "\n".join([
            "You are an NLP data parser.",
            "You will be provided by an Arabic text associated with a Pydantic scheme.",
            "Generate the ouptut in the same story language.",
            "You have to extract JSON details from text according the Pydantic details.",
            "Extract details as mentioned in text.",
            "Do not generate any introduction or conclusion."
        ])
    },
    {
        "role": "user",
        "content": "\n".join([
            "## Story:",
            story_article.strip(),
            "",
            "## Pydantic details:",
            json.dumps()(
                NewsDetails.model_json_schema(), ensure_ascii = False  # hedhi bech e ytala3ch el ascci code mte3 el 3arbi
            ),
            "",
            "## Story details:",
            "```json"

        ])
    }





]