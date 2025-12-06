import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from utils.config_loader import load_config



class ConfigLoader:
    def __init__(self):
        print("Loaded cofiguration")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]



class ModelLoader(BaseNode):
    model_provider: Literal["openai",'groq'] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude =True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_model(self):
        """Loads and returns the model based on the provider specified."""
        print("LLM Loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model.provider == "groq":
            print("GROQ Model chosen")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config['llm']['groq']['model_name']
            llm = ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            print("OpenAI Model chosen")
            open_ai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config['llm']['openai']['model_name']
            llm = ChatOpenAI(model=model_name, openai_api_key=open_ai_api_key)

        return llm


