from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-flash'
)

parser= StrOutputParser()

prompt1 = PromptTemplate(
    template = 'write a full detailed report on the {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='write a short summary on {text}',
    input_variables=['text']
)
# langchain expression language piplelining prompt | model  | parser
joke_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>100 ,prompt2|model|parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(joke_gen_chain,branch_chain)

result = final_chain.invoke({'topic':'ai'})

print(result)