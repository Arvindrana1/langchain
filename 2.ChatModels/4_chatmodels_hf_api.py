from langchain_huggingface import HuggingFaceEndpoint

# Use text-generation instead of chat
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",  # More reliable model
    task="text-generation",
    huggingfacehub_api_token="your_token_here",
    temperature=0.7,
    max_new_tokens=100
)

response = llm("What is the capital of India?")
print(response)