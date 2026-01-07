# %% [markdown]
# # OpenAI Tutorial - Setup and Configuration
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Verify the API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("✓ OpenAI API key loaded successfully!")
else:
    print("✗ OpenAI API key not found! Check your .env file")

# %% [markdown]
# # Create OpenAI Client and Test

# Create the OpenAI client
client = OpenAI()

print(client)

# Create a chat completion
response = client.chat.completions.create(
    model="gpt-4o",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?"
        }
    ]
)

print(response.choices[0].message.content)
# %%
