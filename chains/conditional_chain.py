from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Initialize Google Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Define output schema  
class SentimentAnalysisOutput(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="The sentiment of the text, can be positive or negative."
    )

# Create parser
parser = PydanticOutputParser(pydantic_object=SentimentAnalysisOutput)

# Prompt with format instructions
prompt = PromptTemplate(

    template="Analyze the sentiment of the following text:\n{text}\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Classify text into sentiment (returns dict instead of Pydantic object for branching)
classified_chain = (prompt | model | parser | (lambda x: {"sentiment": x.sentiment, "feedback": x}))

# Response prompts
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback in 2 lines:\n{feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback in 2 lines:\n{feedback}",
    input_variables=["feedback"]
)

# Branch logic
branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", prompt2 | model | StrOutputParser()),
    (lambda x: x["sentiment"] == "negative", prompt3 | model | StrOutputParser()),
    RunnableLambda(lambda x: "Could not determine sentiment.")
)

# Final chain
chain = classified_chain | branch_chain

# Test
result = chain.invoke({"text": "This is a  terrible phone"})
print(result)
