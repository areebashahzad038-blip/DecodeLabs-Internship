# ==========================================
# PROJECT 1: RULE-BASED AI CHATBOT
# DecodeLabs Internship
# ==========================================

print("🤖 CHATBOT: Hello! I'm your AI assistant.")
print("Type 'hello' to chat, or 'bye' to exit.\n")

while True:
    # Get user input and convert to lowercase
    user_input = input("You: ").strip().lower()
    
    # ----- GREETINGS -----
    if user_input in ["hello", "hi", "hey", "hola"]:
        print("Bot: Hey there! How can I help you today?")
    
    # ----- ASK NAME -----
    elif user_input in ["what is your name", "your name", "who are you"]:
        print("Bot: I'm ChatBot 1.0, your rule-based AI friend!")
    
    # ----- ASK HOW ARE YOU -----
    elif user_input in ["how are you", "how's it going", "what's up"]:
        print("Bot: I'm great! Just processing logic all day. How about you?")
    
    # ----- THANK YOU -----
    elif user_input in ["thanks", "thank you", "ty"]:
        print("Bot: You're welcome! 😊")
    
    # ----- EXIT COMMANDS -----
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Goodbye! Thanks for chatting. See you next time! 👋")
        break
    
    # ----- DEFAULT (unknown input) -----
    else:
        print("Bot: Hmm, I don't understand that. Try saying 'hello' or 'bye'.")

print("\n🛑 Chatbot session ended.")
