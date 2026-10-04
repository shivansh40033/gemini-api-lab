from google import genai
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Send request to the model
response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Explain artificial intelligence in simple terms."
)

# Display the response
print(response.text)