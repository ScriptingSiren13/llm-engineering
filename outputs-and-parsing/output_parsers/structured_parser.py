from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Facts(BaseModel):
    fact1: str = Field(description="Fact 1 about the topic")
    fact2: str = Field(description="Fact 2 about the topic")
    fact3: str = Field(description="Fact 3 about the topic")

parser = PydanticOutputParser(pydantic_object=Facts)

template = PromptTemplate(
    template="Give 3 facts about {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic": "children"})

print(result)
