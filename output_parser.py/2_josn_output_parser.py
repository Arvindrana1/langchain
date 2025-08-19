from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

parser = JsonOutputParser()

template= PromptTemplate(
    template='write a name, age and city of a fictional person. \n {format_instructions}',
    input_variables=["format_instructions"],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({})

print(result)