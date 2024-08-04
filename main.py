import json
import random
import tkinter as tk
from tkinter import scrolledtext

def fetch_intents(file):
    with open(file, 'r') as intent_file:
        outsource = json.load(intent_file)
    return outsource["intents"]

def match_intentions(user_input, intents):
    for intent in intents:
        for pattern in intent["text"]:
            if pattern.lower() in user_input.lower():
                return intent["responses"]
    return ["Sorry! I did not catch that. Can you rephrase that? For reference kindly see the intents.json"]

def chatbot_gui():
    intents = fetch_intents("intents.json")
    
    def get_response(user_input):
        responses = match_intentions(user_input, intents)
        return random.choice(responses)
    
    def send():
        user_input = entry.get()
        if user_input.lower() == "bye":
            chatbox.config(state=tk.NORMAL)
            chatbox.insert(tk.END, f"You: {user_input}\nChatbot: Goodbye! Have a great day!\n")
            chatbox.config(state=tk.DISABLED)
            app.quit()
        else:
            response = get_response(user_input)
            chatbox.config(state=tk.NORMAL)
            chatbox.insert(tk.END, f"You: {user_input}\nChatbot: {response}\n")
            chatbox.config(state=tk.DISABLED)
            entry.delete(0, tk.END)
    
    app = tk.Tk()
    app.title("Chatbot")

    chatbox = scrolledtext.ScrolledText(app, height=15, width=50, state=tk.DISABLED)
    chatbox.pack(padx=10, pady=10)

    entry = tk.Entry(app, width=50)
    entry.pack(padx=10, pady=5)

    send_button = tk.Button(app, text="Send", command=send)
    send_button.pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    chatbot_gui()
