from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()


model=ChatOpenAI()


parser=JsonOutputParser()


template=PromptTemplate(
    template="Give me five facts about the {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


chain=template | model | parser

result=chain.invoke({'topic':'children'})

print(result)