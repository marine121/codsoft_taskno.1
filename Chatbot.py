import re

# Define questions and their responses
responses = {
    r'hello|hi|hey': "Hola! How can I help you today?",
    r'what is your name\??': "I am Jarvis, your virtual assistant.",
    r'how are you\??': "I'm just a program, but I'm here to help you!",
    r'what can you do\??': "I can answer your questions and have a chat with you. Ask me anything!",
    r'bye|goodbye': "Goodbye! Have a great day!",
}

# Function to get a response based on the user's input
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for consistency
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    return "Sorry, I don't understand that."

# function to interact with the user
def chat():
    print("ChatBot: Hi! Type 'bye' or 'goodbye' to end the chat.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye', user_input.lower()):
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
