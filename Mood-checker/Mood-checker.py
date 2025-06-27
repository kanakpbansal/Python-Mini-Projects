"""Mood Checker"""
import time
from colorama import Fore, Style,Back
print(Fore.CYAN+ Back.RED + Style.BRIGHT + "Hi there 👋 I'm your mood buddy." + Style.RESET_ALL)

time.sleep(1)
mood=input("How are you feeling today? (happy, sad, tired, anxious, excited) : ").lower()
responses = {
    "happy": "That's amazing! Keep spreading that sunshine ☀️",
    "sad": "I'm sorry you're feeling that way. You're not alone 💙",
    "tired": "Please rest if you can. You're doing your best 🛌",
    "anxious": "Breathe in... breathe out... you're safe right now 🌿",
    "excited": "Yay! Ride that wave and do something fun 🚀"
}
default = "Whatever you're feeling is valid. I'm here with you 🌻"
print("\n" + Fore.YELLOW + Style.BRIGHT + responses.get(mood, default) + Style.RESET_ALL)
print("\n"+"-"*50)
print("\nThanks for checking in with me today 💛")