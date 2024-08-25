from transformers import pipeline

# Create a conversational pipeline
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Test the chatbot with a simple conversation
from transformers import Conversation

conversation = Conversation("Hello! How are you?")
response = chatbot([conversation])

print(response)
