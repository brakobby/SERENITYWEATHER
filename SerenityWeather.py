import tkinter as tk
from tkinter import messagebox
import requests
import pyttsx3

class SerenityWeather:
    def __init__(self, app):
        self.app = app
        self.app.geometry("400x600+400+100")
        self.app.config(bg='lightblue')
        self.app.title("VartsyLabs")

        self.city = tk.StringVar()
        self.api_key = 'c4f3b54b36b44fae9eb2d7913741e686'

        self.nav_bar = tk.Frame(self.app, width=400, height=50, bg="blue")
        self.nav_bar.place(relx=0, rely=0)
        self.navlabel = tk.Label(self.nav_bar, text="SerenityWeather", font=("Montserrat", 16, "bold"), bg="blue", fg="white")
        self.navlabel.place(relx=0.01, rely=0.2)

        self.citydesc = tk.Label(self.app, text="Enter Name Of city", font=("Montserrat", 16), bg='lightblue', fg='black')
        self.citydesc.place(relx=0.3, rely=0.2)
        self.cityentry = tk.Entry(self.app, width=25, font=("Montserrat", 16), bg='lightblue', fg='black', textvariable=self.city)
        self.cityentry.place(relx=0.14, rely=0.3)

        self.datalabel = tk.Label(self.app, text="", bg='lightblue', fg='black', font=("Montserrat", 16))
        self.datalabel.place(relx=0.1, rely=0.5)

        self.btn = tk.Button(self.app, width=25, text="Get Weather", font=("Montserrat", 16, "bold"), bg="blue", fg='white', command=self.get_weather_data)
        self.btn.place(relx=0.1, rely=0.4)

    def get_weather_data(self):
        city = self.city.get()
        if not city:
            messagebox.showwarning("Missing Parameter", "Enter the name of the city")
            return
        url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={self.api_key}&units=M"
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()

            if weather_data['count'] == 0:
                messagebox.showerror("Error", "City not found")
                return
            self.temp = weather_data["data"][0]["temp"]
            self.weather_desc = weather_data["data"][0]["weather"]["description"]
            self.result_text = f"Temperature: {self.temp}°C\nDescription: {self.weather_desc}"
            self.datalabel.config(text=self.result_text)

            # Update the UI before calling text-to-speech
            self.app.update_idletasks()
            
            # Initialize pyttsx3 engine
            self.voice = pyttsx3.init()
            self.voice.setProperty('rate', 150)  
            self.voice.setProperty('volume', 0.5)  
            # Say and run the text
            self.voice.say(self.result_text)
            self.voice.runAndWait()

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error fetching weather data: {e}")

if __name__ == "__main__":
    window = tk.Tk()
    app = SerenityWeather(window)
    window.mainloop()
