# Simple Rule-Based Chatbot

def get_bot_reply(user_input):
    user_input = user_input.lower().strip()
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

def main():
    print("Welcome to the Rule-Based Chatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        reply = get_bot_reply(user_input)
        print(f"Bot: {reply}")
        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    main()
