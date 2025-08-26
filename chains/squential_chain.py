from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt1 = PromptTemplate(
    template= ' write a detailed report on the following topic. \n {topic}. ',
    input_variables=["topic"]   
)

prompt2 = PromptTemplate(
    template='write a 5 line summary on the following text line by line \n {text}. ',
    input_variables=["text"]    
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'unemployment in India'})

print(result)
