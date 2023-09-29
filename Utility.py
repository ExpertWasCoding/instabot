import instabot as ib
import requests
import random
import time

# Load valid proxies from the file
with open("valid.txt", "r") as f:
    proxies = f.read().split('\n')

# Shuffle the proxies to randomize the rotation
random.shuffle(proxies)

# Instabot setup
bot = ib.Bot()

# Function to rotate proxies
def rotate_proxy():
    proxy = random.choice(proxies)
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    bot.api.session = session
    print(f"Using proxy: {proxy}")

# Login using the first proxy
rotate_proxy()
bot.login(username="enter name", password="enter password")

# Follow a user (replace "elonrmuskk" with the desired username)
bot.follow("elonrmuskk")

# Add a delay between requests to avoid rate limits
time.sleep(10)

# Logout (optional)
bot.logout()
