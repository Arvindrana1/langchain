from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

class Person(BaseModel):
    name:str  =Field(description = 'the name of the fictional person')
    age:int = Field(description = 'the age of the fictional person')
    city:str = Field(description='the city of the fictional person lives')

parser = PydanticOutputParser(pydantic_object=Person)
    
template = PromptTemplate(
    template = 'write a name, age and city of a fictonal person from {name}./n {format_instructions}',
    input_variables=['name'],
    partial_variables= {'format_instructions': parser.get_format_instructions()}
)

chain= template | model  |parser

result = chain.invoke({'name':'australian'})

print(result)