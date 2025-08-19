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
template = PromptTemplate(
    template='write a 5 line summary on the following text. /n {text}. ',
    input_variables=["text"]   
)

paresr = StrOutputParser()

chain = template | model| paresr

result =chain.invoke({'text':'lion'})

print(result)