from pydantic import BaseModel, Field
from typing import List, Literal




StoryCategory = Literal[
    "Politics","Technology","Sports",
    "Business","Entertainment","Health",
    "Science","Science Fiction","Economy",
    "Art","not specified"
]
EntityType = Literal["person_male","person_female","location",
"company", "organization","low","event","time","country","disease",
"product","law","money","quantity"]
UrlCategory = Literal["image","video","audio","site","form"]

class Url(BaseModel):
    Url_string: str = Field(..., description="the string of the url written in the story.")
    Url_Type: UrlCategory = Field(..., description="The Type of the url written in the story.")
class Entity(BaseModel):
    entity_value: str = Field(..., description="the actual name or value of the entity.")
    entity_type: EntityType = Field(..., description="the type of the recognized entity.")
class NewsDetails(BaseModel):
    title: str = Field(...,min_length=5,max_length=300, description="A fully informative and SEO optimized title of the story.")
    keywords: List[str] = Field(..., min_items=1,description="Relevant keywords associated with the story.")
    summary: str = Field(...,min_length=5,max_length=450, description="A summary of the story.")
    category: StoryCategory = Field(..., description="category of the news story")
    entities: List[Entity] = Field(...,min_items=1, max_items=10,description="list of identified entities in the story")
    url: List[Url] = Field(...,description="the list of the urls mentioned in the story")