def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a program, but I'm doing well! How about you?",
        "bye": "Goodbye! Have a great day!",
    }
    user_input = user_input.lower()

    return responses.get(user_input, "Sorry, I don't understand that.")

def chatbox():
    print("Welcome to the chatbox! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbox: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbox: {response}")

if __name__ == "__main__":
    chatbox()
