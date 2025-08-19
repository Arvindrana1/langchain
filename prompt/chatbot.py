from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_output_tokens=1024,
)

chat_histroy=[SystemMessage(
    content="You are a helpful assistant that can answer questions.")]

while True:
    user_input = input("You: ")
    chat_histroy.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_histroy)
    chat_histroy.append(AIMessage(content=result))
    print("ai:", result)
print(chat_histroy)
