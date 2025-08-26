from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv ()

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

prompt= PromptTemplate(
    template= 'write a summary on the {poem}',
    input_variables=['poem']
)

parser =StrOutputParser()

load_documents=TextLoader('Rag_Document_loader\\cricket.txt',encoding='utf-8')
docs=load_documents.load()

# print(docs[0].page_content)
print(len(docs))


chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})
print(result)

def get_summary(poem):
    prompt=PromptTemplate(
        template= 'write a summary on the {poem}',
        input_variables=['poem']
    )
    return chain.run({'poem': poem})

summary = get_summary(docs[0].page_content)
