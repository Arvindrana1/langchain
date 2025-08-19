from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"],
)

template2= PromptTemplate(
    template="write a 5 line summary on following text. /n {text}. ",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result =chain.invoke({'topic': 'black hole'})

print(result)