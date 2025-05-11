import os 
from typing import List
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator

load_dotenv()

class MCQQuestion(BaseModel):
    question: str = Field(description="The question text")
    option: List[str] = Field(description="list of $ possible answers")
    correct_answer: str = Field(description="The correct answer from the options")

    @validator("question", pre=True)
    def clen_question(cls, v):
        if isinstance(v, dict):
            return v.get("description", str(v))
        return str(v)
      
class QuestionGenerator:
    def __init__(self):
        """
        Initialize question generator with Groq API
        Sets up the language model with specific parameters:
        - Uses llama-3.1-8b-instant model
        - Sets temperature to 0.9 for creative variety
        """
        self.llm = ChatGroq(
            api_key=os.getenv('GROQ_API_KEY'), 
            model="llama-3.1-8b-instant",
            temperature=0.9
        )

        