import json
try:
    with open('config.json', 'r') as config_file:
        configdata = json.load(config_file)
    with open('emojis.json', 'r') as emoji_file:
        emojidata = json.load(emoji_file)
except:
    print("[ERROR] No config.json file found! Exiting application now.")
    exit()