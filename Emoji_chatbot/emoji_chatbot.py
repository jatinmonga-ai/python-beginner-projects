print("🤖 Emoji Chatbot is here! Type 'bye' to exit.\n")
print(" Choose from : hello/hi, happy, sad, angry, love, food , weather and bye \n")

while True:
    user= input("You: ").lower()

    if user == "bye":
        print("Chatbot: 👋 Bye! Have a great day!")
        break

    # Basic responses
    if "hello" in user or "hi" in user:
        print("Chatbot: 😁 Hello! How are you?")
    elif "happy" in user:
        print("Chatbot: 😄 That’s awesome!")
    elif "sad" in user:
        print("Chatbot: 😢 I’m here for you.")
    elif "angry" in user:
        print("Chatbot: 😡 Take a deep breath… it'll be okay.")
    elif "love" in user:
        print("Chatbot: ❤️ Love makes everything better!")
    elif "food" in user:
        print("Chatbot: 🍕 I love pizza! What’s your favorite?")
    elif "weather" in user:
        print("Chatbot: 🌤️ Looks like a nice day today!")
    else:
        print("Chatbot: 🤔 I’m not sure how to respond, but I’m learning!")

print("Press Enter to exit")
