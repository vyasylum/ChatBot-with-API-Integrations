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
import requests
from PIL import Image, ImageTk
import platform

# Create a dictionary of chatbot responses and dynamic functions
responses = {
    "hello": [lambda: random.choice(["Hello!", "Hi there!", "Hey!"])],
    "how are you": [lambda: random.choice(["I'm good, thanks!", "I'm doing well.", "I'm fine."])],
    "date": [lambda: get_today_date()],
    "time": [lambda: get_current_time()],
    "joke": [lambda: pyjokes.get_joke()],
    "astronomy picture of the day": [lambda: get_apod()],
    "apod": [lambda: get_apod()],
    "system": [lambda: get_system_info()],
    # Add more responses and features based on user input
}

#Define functions here, which can be called in responses\
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
        chat_display.insert(tk.END, "{CHATBOT}: Goodbye!\n")
        chat_display.see(tk.END)
    else:
        response = chatbot_response(user_input)
        chat_display.insert(tk.END, f"[CHATBOT]: {response}\n")
        chat_display.see(tk.END)

def get_apod():
    api_key = "DEMO_KEY" 
    url = f"https://api.nasa.gov/planetary/apod?api_key=5uMO7IJLhBQLXSMY4Sgnd4HvWBgsptgYr0NQmluf"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data.get("explanation")
        image_url = data.get("url")
        display_image(image_url)
        chat_display.insert(tk.END, f"Astronomy Picture of the Day:\n{description}\n{image_url}\n")
    else:
        return "Sorry, I couldn't fetch the Astronomy Picture of the Day at the moment."

def get_system_info():
    machine = platform.machine()
    system = platform.system()
    return f'Your operating system is {system}, and your machine architecture is {machine}.'

def display_image(image_url):
    try:
        image = Image.open(requests.get(image_url, stream=True).raw)
        max_width = 1000  # Adjust this value based on your chat display's width
        if image.width > max_width:
            image = image.resize((max_width, int(image.height * (max_width / image.width))))

        photo = ImageTk.PhotoImage(image)
        chat_display.image_create(tk.END, image=photo)
        chat_display.insert(tk.END, "\n", "chatbot")
        label = tk.Label(window, image=photo)
        label.image = photo
        
    except Exception as e:
        print(f"Error displaying image: {e}")

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

# Configure the font and color settings
font = ("Courier New", 21)
chatbot_bg_color = "darkslategray1"
chatbot_fg_color = "black"
user_reply_bg_color = "light blue"
user_reply_fg_color = "black"
send_button_color = "deepskyblue2"

# Chat display with modified settings for chatbot and user
chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=16, font=font, bg=chatbot_bg_color, fg=chatbot_fg_color, padx=20,pady=20)
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# User entry with Enter key binding and modified settings
user_entry = tk.Entry(window, width=60, font=font, bg=user_reply_bg_color, fg=user_reply_fg_color)
user_entry.grid(row=1, column=0, padx=0, pady=5)
# Set a default placeholder text in the user entry
user_entry.insert(0, "Type your message here")

# Create a function to handle the focus event in the user entry
def on_entry_click(event):
    if user_entry.get() == "Type your message here":
        user_entry.delete(0, "end")  # Clear the default text

# Bind the focus event to the function
user_entry.bind("<FocusIn>", on_entry_click)

user_entry.grid(row=1, column=0, padx=10, pady=10)

user_entry.grid(row=1, column=0, padx=10, pady=10)
def send_on_enter(event):
    send_message()
user_entry.bind("<Return>", send_on_enter)

# Send button with modified settings
send_button = tk.Button(window, text="Send", width=10, command=send_message, font=font, bg=send_button_color)
send_button.grid(row=2, column=0, padx=1, pady=10)

greeting = greet()
chat_display.insert(tk.END, f"[CHATBOT]: {greeting}\n")

# Start the GUI main loop
window.mainloop()
