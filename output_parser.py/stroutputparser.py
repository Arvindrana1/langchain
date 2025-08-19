from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

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
prompt1=template1.invoke({'topic': 'black'})

response1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': response1.content})

response2 = model.invoke(prompt2)

print(response2.content)
