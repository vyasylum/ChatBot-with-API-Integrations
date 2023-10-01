import tkinter as tk
from tkinter import scrolledtext
import random
import datetime
import calendar
import os
import webbrowser
import pyjokes

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good morning, how may I help you?"
    elif 12 <= hour < 16:
        return "Good afternoon, how may I help you?"
    else:
        return "Good evening, how may I help you?"

def get_today_date():
    now = datetime.datetime.now()
    week_day = calendar.day_name[now.weekday()]
    month = now.strftime("%B")
    day = now.day
    return f'Today is {week_day}, {month} {day}.'

def chatbot_response(input_text):
    responses = {
        "hello": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm good, thanks!", "I'm doing well.", "I'm fine."],
        "date": [get_today_date()],
        "time": [f"It is {datetime.datetime.now().strftime('%I:%M %p')}.", "The time is now {datetime.datetime.now().strftime('%I:%M %p')}."],
        "joke": [pyjokes.get_joke()],
        # Add more responses and features based on user input
    }

    input_text = input_text.lower()
    if input_text in responses:
        return random.choice(responses[input_text])
    elif "search" in input_text:
        search_query = input_text.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return f"I've opened a Google search for '{search_query}'."
    elif "email" in input_text:
        # Implement email sending logic here
        return "Sorry, email functionality is not implemented in this version."
    elif "open" in input_text:
        app_mapping = {
            "chrome": "Google Chrome",
            "word": "Microsoft Word",
            "excel": "Microsoft Excel",
            "vs code": "Visual Studio Code",
            "brave": "Brave Browser",
        }
        app_name = input_text.split("open")[1].strip()
        if app_name in app_mapping:
            os.system(f"start {app_mapping[app_name]}")
            return f"Opening {app_name}..."
        else:
            return f"Sorry, I don't know how to open {app_name}."
    else:
        return "I'm not sure how to respond to that."

# Create a function to handle user input and chatbot responses
def send_message():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)
    chat_display.insert(tk.END, f"You: {user_input}\n")
    
    if user_input.lower() in ["exit", "quit"]:
        chat_display.insert(tk.END, "Chatbot: Goodbye!\n")
        chat_display.see(tk.END)
    else:
        response = chatbot_response(user_input)
        chat_display.insert(tk.END, f"Chatbot: {response}\n")
        chat_display.see(tk.END)

# Create the main GUI window
window = tk.Tk()
window.title("Chatbot")

chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=15)
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

user_entry = tk.Entry(window, width=30)
user_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(window, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

greeting = greet()
chat_display.insert(tk.END, f"Chatbot: {greeting}\n")

# Start the GUI main loop
window.mainloop()
