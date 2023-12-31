# Chatbot Project for MIT-ADT University's Hacktoberfest

Welcome to the Chatbot project for MIT-ADT University's Hacktoberfest! This project allows you to contribute to an interactive chatbot that responds to user input and performs various tasks, such as answering questions, providing information, and more.

## Project Overview

The chatbot is designed to be extensible, and contributors can add new features, responses, and capabilities to make it even more useful and interactive.

## Getting Started

To get started with contributing to the chatbot, follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of this repository to create your own copy.

2. **Clone Your Fork**: Clone the forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/chatbot-project.git


## Install dependencies 
    
    pip install -r requirements.txt


## Add New Features Using an API(s)

Choose an API: Select an external API that you'd like to integrate into the chatbot. Here are some suggested APIs:

- [OpenWeatherMap API](https://openweathermap.org/api): Get real-time weather data.
- [News API](https://newsapi.org/): Retrieve the latest news headlines.
- [NASA API](https://api.nasa.gov/): Access space-related information and images.
- [NASA APOD API](https://apod.nasa.gov/apod/lib/about_apod.html): Display NASA's Astronomy Picture of the Day along with descriptions and explanations.
- [Music Lyrics API](https://lyricsovh.docs.apiary.io/): Retrieve song lyrics based on user queries or display lyrics when the chatbot encounters song-related topics.

**NOTE: These are a few examples, you can add way more!!**
## Create a New Function: Write a Python function that uses the chosen API to fetch data or perform a specific task. For example:

```py
def get_weather(city):
    # Your code to call the weather API and retrieve data
    # Return the weather information as a response
    return "The weather in {} is sunny today.".format(city)
```


**Integrate the Function**: Add your function to the chatbot_response function in main.py. Update the responses dictionary with a keyword that triggers your function.

Test Your Feature: Run the chatbot locally and test your new feature by asking the chatbot about it.

## Submit Your Contribution:

Commit your changes and push them to your forked repository.
Create a pull request to the main repository. Provide a clear description of your contribution.
