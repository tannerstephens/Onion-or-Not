import requests, html, random, praw, pickle
import os

class onion:
    def __init__(self):
        self.url = "https://www.theonion.com/"
        self.add = ""
        self.headlines = []
        self.blacklist = ["episode", "onion", "horoscope", "report", "this week in"]
	
    def populate(self,amount=None):
        if os.path.isfile("./onion.pickle"):
            with open("./onion.pickle", "rb") as f:
                self.headlines = pickle.load(f)

        
        if amount == None:
            amount = 1

        while len(self.headlines) < amount:
            r = requests.get(self.url + self.add)
            text = html.unescape(r.text).split('post-list--pe js_post-list hfeed">')[1].replace("\n", "")
            work = text.split('class="js_entry-link">')
            work = [j.split("</a")[0].replace("<em>", "").replace("</em>", "").strip() for j in work][1:]
            for hl in work:
                if hl.lower() not in self.blacklist:
                    self.headlines.append(hl)

            self.add = text.split('class="load-more__button">')[1].split('href="')[1].split('">')[0]

        with open("./onion.pickle", "wb") as f:
            pickle.dump(self.headlines, f)
        
    def refresh(self):
        r = requests.get(self.url)
        text = html.unescape(r.text).split('post-list--pe js_post-list hfeed">')[1].replace("\n", "")
        work = text.split('class="js_entry-link">')
        work = [j.split("</a")[0] for j in work][1:]
        for hl in work:
            if hl in self.headlines:
                continue
            elif hl.lower() not in self.blacklist:
                self.headlines.append(hl)

        with open("./onion.pickle", "wb") as f:
            pickle.dump(self.headlines, f)

    def random_hl(self):
        return random.choice(self.headlines)

class notonion:
    def __init__(self):
        with open(".key") as f:
            user_id = f.readline().strip()
            user_secret = f.readline().strip()

        reddit = praw.Reddit(client_id=user_id, client_secret=user_secret, user_agent="Onion or Not")
        self.nottheonion = reddit.subreddit("nottheonion")
        self.headlines = []
        self.blacklist = ["onion"]

    def populate(self):
        if os.path.isfile("./notonion.pickle"):
            with open("./notonion.pickle", "rb") as f:
                self.headlines = pickle.load(f)

        self.clean()
        
        for post in self.nottheonion.new(limit=1000):
            if not post.stickied:
                if post.title not in self.headlines:
                    if True not in [word in post.title.lower() for word in self.blacklist]:
                        self.headlines.append(post.title)

        with open("./notonion.pickle", "wb") as f:
            pickle.dump(self.headlines, f)

    def refresh(self):
        for post in self.nottheonion.new(limit=1000):
            if not post.stickied:
                if post.title not in self.headlines:
                    self.headlines.append(post.title)

        with open("./notonion.pickle", "wb") as f:
            pickle.dump(self.headlines, f)

    def clean(self):
        new = []
        for hl in self.headlines:
            if True not in [word in hl for word in self.blacklist]:
                new.append(hl)
        self.headlines = new[:]

    def random_hl(self):
        return random.choice(self.headlines)
    
	
