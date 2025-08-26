from langchain.schema.runnable import RunnableLambda

def word_count(text):
    return len(text.split())

runnable_word_count = RunnableLambda(word_count)

print(runnable_word_count.invoke("hi my name is akay !!"))
