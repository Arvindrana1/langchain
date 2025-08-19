from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

schema = [
    ResponseSchema(name="name", description="The name of the fictional person"),
    ResponseSchema(name="age", description="The age of the fictional person"),  
    ResponseSchema(name="city", description="The city where the fictional person lives"),
]

parser= StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'write a name, age and city of a fictional person. \n {format_instruction}',
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()
})

chain = template|model| parser

final_result = chain.invoke({'topics': 'black hole'})

print(final_result)
