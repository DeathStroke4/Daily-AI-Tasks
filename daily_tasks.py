import requests
import random
from datetime import datetime

# ================== LONG LIST OF REAL QUOTES ==================
QUOTES = [
    "A man is literally what he thinks, his character being the complete sum of all his thoughts.",
    "You are today where your thoughts have brought you; you will be tomorrow where your thoughts take you.",
    "As a man thinketh in his heart, so is he.",
    "A man's mind may be likened to a garden, which may be intelligently cultivated or allowed to run wild.",
    "Good thoughts bear good fruit, bad thoughts bad fruit.",
    "Man is made or unmade by himself.",
    "Man is the master of thought, the moulder of character, and the maker and shaper of condition, environment, and destiny.",
    "Act is the blossom of thought; and joy and suffering are its fruits.",
    "As the plant springs from the seed, so every act of a man springs from the hidden seeds of thought.",
    "Dream lofty dreams, and as you dream, so shall you become.",
    "You will become as small as your controlling desire; as great as your dominant aspiration.",
    "Thoughts are the seeds of action.",
    "Self-control is strength. Right thought is mastery. Calmness is power.",
    "The soul attracts that which it secretly harbors.",
    "Let a man radically alter his thoughts, and he will be astonished at the rapid transformation.",
    "A noble and Godlike character is not a thing of favour or chance.",
    "Circumstance does not make the man; it reveals him to himself.",
    "A man only begins to be a man when he ceases to whine and reviles.",
    "Mind is the Master power that moulds and makes.",
    "He thinks in secret, and it comes to pass: Environment is but his looking-glass.",
    "They themselves are makers of themselves.",
    "Only by much searching and mining are gold and diamonds obtained.",
    "Every thought-seed sown produces its own, blossoming into act.",
    "For you will always gravitate toward that which you secretly most love.",
    "Into your hands will be placed the exact results of your own thoughts.",
    "When a man makes his thoughts pure, he no longer desires impure food.",
    "A man's mind may be likened to a garden... it must and will bring forth.",
    "Thought allied fearlessly to purpose becomes creative force.",
    "A man should conceive of a legitimate purpose in his heart and set out to accomplish it.",
    "Only the wise man, whose thoughts are controlled and purified, makes the storms of the soul obey him."
]

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=51.40&longitude=-0.20&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Europe/London"
    try:
        data = requests.get(url, timeout=10).json()
        today = data['daily']
        return f"Weather in Morden, London:\n🌡️ High: {today['temperature_2m_max'][0]}°C | Low: {today['temperature_2m_min'][0]}°C\n🌧️ Rain chance: {today['precipitation_probability_max'][0]}%\nStay prepared!"
    except:
        return "Weather data unavailable today."

def get_news_summary():
    return "📰 Local UK/London: Keep an eye on transport, weather alerts, and community news.\n🌍 Global: Major international developments unfolding."

def get_sports():
    return "⚽ Sports: Main Premier League results from last night and key fixtures for today."

# Build the daily message
quote = random.choice(QUOTES)
message = f"Good Morning!\n\n"
message += f"{get_weather()}\n\n"
message += f"{get_news_summary()}\n\n"
message += f"💡 Today's Quote from *You Become What You Think*:\n\"{quote}\"\n\n"
message += f"Quick Habit: Enjoy the day.\n\n"
message += f"{get_sports()}\n\n"
message += f"Have a wonderful day ahead! ☀️"

print(message)

# TODO: We'll add email sending in the next step