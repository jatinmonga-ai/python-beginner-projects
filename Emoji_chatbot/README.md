Emoji Chatbot 

A super simple and fun "Python emoji chatbot" for beginners. This chatbot responds to emotions like happy, sad, angry, love, weather, and more.

Quick tip: "I used NOTEPAD to insert emojis, and then copy paste the code in IDLE."

##  What This Chatbot Does

* Greets the user.
* Responds with different emojis based on mood or keywords.
* Ends when the user types bye.

##  How to Run This Project

### 1. Open IDLE (Python)
* Search for IDLE on your computer
* Click **File → New File**
* Copy & paste the full code below
* Save the file as **emoji_chatbot.py**

##  Copy This Code
```
print("🤖 Emoji Chatbot is here! Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: 👋 Bye! Have a great day!")
        break

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
```

##  Running the Program
* After pasting the code, press F5 or go to Run → Run Module**
* A new window will open
* Type something and the chatbot will reply with emojis!

## Why Emojis Don’t Show in CMD/Terminal
Some Windows terminals don’t support emojis, so they might appear as boxes.
But IDLE always shows emojis correctly, so use IDLE to run this project.
