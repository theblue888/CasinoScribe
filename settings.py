import json, pymongo

try:
    with open('config.json', 'r') as config_file:
        configdata = json.load(config_file)
    with open('emojis.json', 'r') as emoji_file:
        emojidata = json.load(emoji_file)
except:
    print("[ERROR] No config.json file found! Exiting application now.")
    exit()

try:
    # Connect to MongoDB server
    myclient = pymongo.MongoClient(configdata["mongo"]["url"])
except:
    print("[ERROR] There was an error connecting to MongoDB. Invalid URL in config.json maybe? Exiting now.")
    exit()
# Define the main database and collections as variables
db = myclient["casinoscribe"]
bank = db["bank"]

print("[Start] Database and collections defined")