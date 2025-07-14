from urllib import response
import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
from googlesearch import search
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
from textwrap import wrap
import os


recognizer = sr.Recognizer()


load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def speak(text):
    ttsx = tts.init()
    voices = ttsx.getProperty('voices')
    ttsx.setProperty('voice', voices[1].id)
    ttsx.say(text)
    ttsx.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open google" in command or "google" in command:
        wb.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command or "youtube" in command:
        wb.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open facebook" in command or "facebook" in command:
        wb.open("https://www.facebook.com")
        speak("Opening Facebook")

    elif "current time" in command or "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"The current time is {current_time}")
        speak(f"The current time is {current_time}")

    elif "search" in command:
        parts = command.split("search", 1)
        if len(parts) > 1 and parts[1].strip() != "":
            query = parts[1].strip()
            speak(f"Searching for {query}")
            for j in search(query, tld="com", num=1, stop=1, pause=2):
                wb.open(j)
                break
        else:
            speak("Sorry, I didn't catch what to search for.")

    elif "exit" in command or "stop" in command or "go offline" in command:
        
        print("Going offline. Goodbye!")
        speak("Going offline. Goodbye!")
        return False

    else:
        speak("AI Mode On")
        try:
            response = model.generate_content(command)
            print("Gemini Response:", response.text)

            # Speak only the first 2 lines or ~300 characters
            short_response = "\n".join(wrap(response.text, 100))[:300]
            speak(short_response)
        except Exception as e:
            print(f"Error generating response: {e}")
            speak("Sorry, I couldn't process that command. Please try again.")
    return True

if __name__ == "__main__":
    print("Initializing Friday....")
    speak("Initializing Friday....")

    while True:
        try:
            with sr.Microphone() as source:
                print("Say 'Friday' to activate...")
                audio_text = recognizer.listen(source, timeout=5)
                activation = recognizer.recognize_google(audio_text).lower()
                print("You said:", activation)

                if "friday" in activation:
                    speak("Voice matched. Activating Friday.")
                    print("Voice matched. Activating Friday.")

                    # Active listening loop
                    while True:
                        try:
                            with sr.Microphone() as source:
                                print("Listening for your command... (say 'exit' to quit)")
                                audio_text = recognizer.listen(source, timeout=5)
                                command = recognizer.recognize_google(audio_text)
                                print("Command:", command)

                                if not processCommand(command):
                                    break  # exit command loop
                        except sr.WaitTimeoutError:
                            print("Timeout: No speech detected. Still waiting...")
                            continue
                        except sr.UnknownValueError:
                            print("Sorry, I couldn't understand. Please try again.")
                            speak("Sorry, I couldn't understand. Please try again.")
                        except Exception as e:
                            print(f"Error: {e}")
                            speak("An error occurred. Please try again.")
                            break

                else:
                    print("Voice not matched. Say 'Friday' to activate.")
                    speak("Voice not matched. Please say Friday to activate.")
        except sr.WaitTimeoutError:
            print("Timeout waiting for 'Friday' activation. Restarting...")
            continue
        except Exception as e:
            print("Something went wrong.")
            speak("Something went wrong.")
