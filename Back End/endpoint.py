import random, feedparser, praw, datetime, json, html, time
from flask import Flask

onion_url = "http://www.theonion.com/rss"
onion_feed = feedparser.parse( onion_url )

headlines = []

for item in onion_feed['items']:
	headlines.append(item.title)

with open(".key") as f:
	user_id = f.readline().strip()
	user_secret = f.readline().strip()

reddit = praw.Reddit(client_id=user_id, client_secret=user_secret, user_agent="Onion or Not")
nottheonion = reddit.subreddit("nottheonion")

last = datetime.datetime.now()

def update_feed():
	headlines = []

	for item in onion_feed['items']:
        	headlines.append(item.title)

	return

def get_onion():
	return random.choice(headlines)
	
def get_fake():
	return nottheonion.random().title

def chal():
	if (datetime.datetime.now() - last).days > 0:
		update_feed()
	
	onion = bool(random.randint(0,1))
	
	if onion:
		title = get_onion()
	else:
		title = get_fake()
	#print(title)
	title = html.unescape(title).encode("ascii", "ignore").decode()
	
	return json.dumps({"headline" : title, "onion" : onion})
	
app = Flask(__name__)

@app.route('/oon/endpoint/')
def endpoint():
	out = chal()
	time.sleep(1)
	return out
	
if __name__ == "__main__":
	app.run(host='127.0.0.1', port=4867)
