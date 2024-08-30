import cowsay
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pyfiglet
import shutil
import time
from ascii_art import fox_main
import random
from io import BytesIO
from PIL import Image
import numpy as np

# User name input

def cowsay_random(message):
    random_character = random.choice(cowsay.char_names)
    getattr(cowsay, random_character)(message)
def print_slowly(text, delay=0.1):
    for line in text.split('\n'):
        print(line)
        time.sleep(delay)

def get_user_name():
    cowsay.fox("Hello!, Me and my friends will give you advice as you tell us your journey details throughout the week!, first of please tell me your name ?")
    name = input().strip()
    cowsay_random(f"Nice to meet you, {name}!")
    return name

def display_welcome_message():
    terminal_size = shutil.get_terminal_size((80, 20))  # Default size if unable to get terminal size
    terminal_width = terminal_size.columns

    welcome_text = pyfiglet.figlet_format("Hello, I'm EcoPal !", font="slant", width=terminal_width)
    your_pal = pyfiglet.figlet_format("Your pal to help you be more eco-friendly :)", font="slant", width=terminal_width)
    print(welcome_text)
    print_slowly(fox_main, delay=0.05)
    print(your_pal)

# Initial questionnaire
def initial_questionnaire(name):
    works = input(f"{name}, do you work? (yes/no): ").strip().lower()
    if works == 'yes':
        distance_to_work = float(input(f"{name}, distance from work to home (in km): "))
    else:
        distance_to_work = 0
    return works, distance_to_work

# Daily questionnaire
def daily_questionnaire(day, name, works, distance_to_work):
    day_text = pyfiglet.figlet_format(f"Day {day}")
    print(day_text)

    if works == 'yes':
        went_to_work = input(f"{name}, did you go to work today? (yes/no): ").strip().lower()
        if went_to_work == 'yes':
            mode_of_transport = input(f"{name}, how did you travel to work today (walk/cycle/tram/car)?: ").strip().lower()
            if mode_of_transport == 'walk':
                if distance_to_work > 3:
                    cowsay_random("\nGreat job on walking a long distance to work! Keep it up!\n")
                elif distance_to_work > 0:
                    cowsay_random("\nGood effort on walking to work. :) \n")
                else:
                    cowsay_random("\nConsider walking more to improve your health and reduce emissions.\n")
            elif mode_of_transport == 'cycle':
                if distance_to_work > 5:
                    cowsay_random("\nFantastic cycling effort to work! You're doing great for the environment and your fitness.\n")
                elif distance_to_work > 0:
                    cowsay_random("\nNice work on cycling to work. :)\n")
                else:
                    cowsay_random("\nConsider cycling more to stay fit and eco-friendly.\n")
            elif mode_of_transport == 'car':
                if 10 >= distance_to_work > 5:
                    cowsay_random(f"\nYour journey to work is only {distance_to_work} km. Consider cycling or taking the tram instead of driving.\n")
                elif distance_to_work <= 5:
                    cowsay_random(f"\nYour journey to work is only {distance_to_work} km. Consider walking or cycling instead of driving.\n")
                    if distance_to_work < 5:
                        cowsay_random("Maybe try taking the tram or cycling next time.\n")
            elif mode_of_transport == 'tram':
                if distance_to_work <= 5:
                    cowsay_random(f"\nYour journey to work is only {distance_to_work} km. Consider walking or cycling instead of taking the tram.\n")
        else:
            mode_of_transport = 'none'
    else:
        mode_of_transport = 'none'

    other_journeys = []
    num_other_journeys = int(input(f"{name}, how many non-leisure journeys did you make today?: "))
    for i in range(num_other_journeys):
        distance = float(input(f"Distance of journey {i+1} (in km): "))
        transport = input(f"Mode of transport for journey {i+1} (walk/cycle/tram/car): ").strip().lower()
        if transport == 'walk':
            if distance > 3:
                cowsay_random("\nGreat job on walking a long distance! Keep it up!\n")
            elif distance > 0:
                cowsay_random("\nGood effort on walking. :) \n")
            else:
                cowsay_random("\nConsider walking more to improve your health and reduce emissions.\n")
        elif transport == 'cycle':
            if distance > 5:
                cowsay_random("\nFantastic cycling effort! You're doing great for the environment and your fitness.\n")
            elif distance > 0:
                cowsay_random("\nNice work on cycling. :) \n")
            else:
                cowsay_random("\nConsider cycling more to stay fit and eco-friendly.\n")
        elif transport == 'car':
            if 10 >= distance > 5:
                cowsay_random(f"\nYour journey is only {distance} km. Consider cycling or taking tram instead of driving.\n")
            elif distance <= 5:
                cowsay_random(f"\nYour journey is only {distance} km. Consider walking or cycling instead of driving.\n")
                if distance < 5:
                    cowsay_random("Maybe try taking the tram or cycling next time.\n")
        elif transport == 'tram':
            if distance <= 5:
                cowsay_random(f"\nYour journey is only {distance} km. Consider walking or cycling instead of taking the tram.\n")
        other_journeys.append({"distance": distance, "transport": transport})

    return {
        "day": day,
        "went_to_work": went_to_work if works == 'yes' else 'no',
        "mode_of_transport": mode_of_transport,
        "distance_to_work": distance_to_work if went_to_work == 'yes' else 0,
        "other_journeys": other_journeys
    }

def calculate_weekly_scores(daily_data):
    scores = {
        "walking": 0,
        "cycling": 0,
        "tram": 0,
        "car": 0
    }
    for data in daily_data:
        if data["mode_of_transport"] == "walk":
            if data["distance_to_work"] > 3:
                scores["walking"] += 2
            elif data["distance_to_work"] > 0:
                scores["walking"] += 1
            else:
                scores["walking"] -= 1  # Penalize for short journeys
        elif data["mode_of_transport"] == "cycle":
            if data["distance_to_work"] > 5:
                scores["cycling"] += 2
            elif data["distance_to_work"] > 0:
                scores["cycling"] += 1
            else:
                scores["cycling"] -= 1  # Penalize for short journeys

        elif data["mode_of_transport"] == "tram":
            if data["distance_to_work"] > 5:
                scores["tram"] += 1
            else:
                scores["tram"] -= 1
        elif data["mode_of_transport"] == "car":
            if data["distance_to_work"] > 10:
                scores["car"] += 1
            else:
                scores["car"] -= 1

        for journey in data["other_journeys"]:
            if journey["transport"] == "walk":
                if journey["distance"] > 3:
                    scores["walking"] += 2
                elif journey["distance"] > 0:
                    scores["walking"] += 1
                else:
                    scores["walking"] -= 1  # Penalize for short journeys
            elif journey["transport"] == "cycle":
                if journey["distance"] > 5:
                    scores["cycling"] += 2
                elif journey["distance"] > 0:
                    scores["cycling"] += 1
                else:
                    scores["cycling"] -= 1  # Penalize for short journeys
            elif journey["transport"] == "tram":
                if journey["distance"] > 5:
                    scores["tram"] += 1
                else:
                    scores["tram"] -= 1
            elif journey["transport"] == "car":
                if journey["distance"] > 10:
                    scores["car"] += 1
                else:
                    scores["car"] -= 1

    return scores
# Output generation
def calculate_emissions_saved(current_scores, previous_scores):
    # Calculate total carbon emissions saved compared to last week
    pass

def provide_advice(scores):
    advice = []

    # Walking advice
    if scores["walking"] >= 10:
        advice.append("Great job on walking a lot this week! Keep it up!")
    elif scores["walking"] > 0:
        advice.append("Good effort on walking. Try to walk a bit more next week.")
    else:
        advice.append("You didn't walk much this week. Consider walking more to improve your health and reduce emissions.")

    # Cycling advice
    if scores["cycling"] >= 10:
        advice.append("Fantastic cycling effort! You're doing great for the environment and your fitness.")
    elif scores["cycling"] > 0:
        advice.append("Nice work on cycling. Try to cycle a bit more next week.")
    else:
        advice.append("You didn't cycle much this week. Cycling is a great way to stay fit and eco-friendly.")

    # Tram advice
    if scores["tram"] >= 5:
        advice.append("Good use of public transport. Keep using the tram to reduce your carbon footprint.")
    elif scores["tram"] > 0:
        advice.append("You used the tram a few times. Consider using it more often instead of driving.")
    else:
        advice.append("You didn't use the tram this week. Public transport is a great alternative to driving.")

    # Car advice
    if scores["car"] <= 0:
        advice.append("Excellent job avoiding car use! This greatly reduces your carbon footprint.")
    elif scores["car"] <= 5:
        advice.append("You used the car sparingly. Try to reduce car use even further.")
    else:
        advice.append("You used the car quite a bit. Consider alternatives like walking, cycling, or public transport.")

    advice_text = "\n\n".join(advice)
    cowsay_random(advice_text)

if __name__ == "__main__":
    display_welcome_message()
    time.sleep(2)
    name = get_user_name()
    works, distance_to_work = initial_questionnaire(name)
    daily_data = []
    for day in range(1, 8):  # Simulate daily data collection for a week
        daily_data.append(daily_questionnaire(day, name, works, distance_to_work))
        input("Press Enter to continue to the next day...")

    weekly_scores = calculate_weekly_scores(daily_data)
    provide_advice(weekly_scores)
    print("Weekly Scores:", weekly_scores)
    # Further processing and output generation