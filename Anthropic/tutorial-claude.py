from dotenv import load_dotenv
import os
import anthropic

# Load environment variables from .env file
load_dotenv()

# Verify the API key is loaded
api_key = os.getenv("ANTHROPIC_API_KEY")
if api_key:
    print("✓ API key loaded successfully!")
else:
    print("✗ API key not found! Check your .env file")

# Create the Anthropic client (it will automatically use ANTHROPIC_API_KEY from environment)
client = anthropic.Anthropic()

print(client)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?"
        }
    ]
)

print(message.content)