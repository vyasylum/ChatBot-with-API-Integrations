#PLEASE KEEP ADDING THE IMPORTED LIBRARIES IN "requirements.txt" for other contributers
import tkinter as tk
from tkinter import scrolledtext
import random
import datetime
import calendar
import os
import webbrowser
import pyjokes
import re

# Create a dictionary of chatbot responses and dynamic functions
responses = {
    "hello": [lambda: random.choice(["Hello!", "Hi there!", "Hey!"])],
    "how are you": [lambda: random.choice(["I'm good, thanks!", "I'm doing well.", "I'm fine."])],
    "date": [lambda: get_today_date()],
    "time": [lambda: get_current_time()],
    "joke": [lambda: pyjokes.get_joke()],
    # Add more responses and features based on user input
}

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

def get_current_time():
    return f"It is {datetime.datetime.now().strftime('%I:%M %p')}."

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

def chatbot_response(input_text):
    input_text = input_text.lower()
    
    matched_keywords = []
    
    # Check for keywords in the user's input
    for keyword in responses.keys():
        if re.search(r'\b' + keyword + r'\b', input_text):
            matched_keywords.append(keyword)
    
    if matched_keywords:
        response_list = [response() for keyword in matched_keywords for response in responses[keyword]]
        response_text = '\n'.join(response_list)
        return response_text
    else:
        return "I'm not sure how to respond to that."

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
