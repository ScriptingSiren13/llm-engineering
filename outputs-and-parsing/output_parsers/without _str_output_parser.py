#  IMPORTING THE METHODS AND CLASSES
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


#Loads .env file so that key becomes available
load_dotenv()


#Creates an LLM object
model = ChatOpenAI(model="gpt-4o-mini")  # or whichever model



#TEMPLATE 1
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt1 = template1.invoke({"topic": "black hole"})
result1 = model.invoke(prompt1)





#TEMPLATE 2
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"]
)

prompt2 = template2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)

print(result2.content)
