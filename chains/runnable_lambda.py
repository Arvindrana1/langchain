from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel,RunnablePassthrough, RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash"
)
prompt = PromptTemplate(
    template = 'write a joke on {topic}',
    input_variables= ['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt,model, parser)

parellel_chain = RunnableParallel({
        'joke':RunnablePassthrough(),
        'word_count': RunnableLambda(word_count)
    }
)
final_result = RunnableSequence(joke_gen_chain,parellel_chain)

result =final_result.invoke({'topic':'ai in future'})
print(result)
