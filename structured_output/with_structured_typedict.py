from google import genai
from pydantic import BaseModel,Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()   

# Define the schema for structured output
class Review(BaseModel):
    summary: str = Field(description="A brief summary of the review")
    sentiment: str

# Initialize the GenAI client
client = genai.Client()

# Generate content with structured response
response = client.models.generate_content(
    model="gemini-2.5-flash",   # switched to latest
    contents="""I’ve been using these headphones for the past 3 months, mostly for work calls and travel. 
    The noise cancellation is absolutely top-notch—I can barely hear the metro announcements when I’m commuting. 
    The sound quality is balanced with good bass, not overpowering like some other brands. 
    Battery life is excellent, lasting me about 3-4 days with 6–7 hours daily use. 
    The only downside is that they feel a bit bulky after wearing for long hours. 
    Overall, worth the price if you need premium noise-canceling headphones.""",
    config={
        "response_mime_type": "application/json",
        "response_schema": Review,
    },
)

# Use the response as a JSON string
print(response.text)

# Use instantiated object
my_review: Review = response.parsed
print(my_review.summary)
print(my_review.sentiment)
