# SERENITYWEATHER


## SerenityWeather: Python Weather Information Application

### Overview

SerenityWeather is a Python-based desktop application that provides current weather information for any city worldwide. Built using Tkinter for the graphical user interface (GUI), requests for making HTTP requests to the Weatherbit API, and pyttsx3 for text-to-speech functionality, this application offers users a seamless way to check weather updates while also providing an auditory announcement of the weather conditions.

### Features

- **User-Friendly Interface**: The application features a simple and intuitive GUI where users can enter the name of a city to retrieve weather data.
  
- **Real-Time Data**: Uses the Weatherbit API to fetch real-time weather information including temperature and weather description for the specified city.
  
- **Visual Display**: Displays the retrieved weather information prominently within the application window for easy readability.
  
- **Auditory Feedback**: Utilizes pyttsx3 to convert the weather data into speech, providing an auditory announcement of the current weather conditions.

### Installation and Usage

1. **Installation**:
   - Clone the repository from GitHub or download the source code.
   - Install dependencies listed in `requirements.txt`, particularly `pyttsx3`.

2. **Run the Application**:
   - Execute the Python script `serenity_weather.py`.
   - The application window will open, allowing users to input a city name and fetch weather data.

3. **Getting Weather Data**:
   - Enter the name of a city in the provided input field and click the "Get Weather" button.
   - If the city is found, the application displays the current temperature in Celsius and a brief weather description.
   - Additionally, the application audibly announces the weather information using text-to-speech capabilities.

### Requirements

- **Python 3.x**
- **Tkinter**: Standard GUI toolkit included with Python.
- **pyttsx3**: Python library for text-to-speech conversion.
- **Requests**: Python library for making HTTP requests.

### Code Structure

- **serenity_weather.py**: Main script containing the Tkinter GUI setup, weather data retrieval logic using requests, and text-to-speech functionality with pyttsx3.
- **requirements.txt**: File listing dependencies required for the project.

### Future Enhancements

- **Unit Selection**: Allow users to select temperature units (Celsius, Fahrenheit, etc.).
- **Extended Forecast**: Implement functionality to fetch and display extended weather forecasts.
- **Localization**: Support multiple languages for both visual and auditory weather information.

### Contributions

Contributions to the SerenityWeather project are welcome! If you'd like to contribute, fork the repository, create a new feature branch, make your changes, and submit a pull request.

### License

This project is licensed under the MIT License.
