import datetime, json, oniony, random, time
from flask import Flask

onion = oniony.onion()
onion.populate(1000)

notonion = oniony.notonion()
notonion.populate()

update = time.time()

def reload():
    onion.refresh()
    notonion.refresh()
    update = time.time()
	

def chal():
    if time.time() >= update + 86400:
        reload()
    
    real = bool(random.randint(0,1))
	
    if real:
        title = onion.random_hl()
    else:
        title = notonion.random_hl()

    title = title.encode("ascii", "ignore").decode()
	
    return json.dumps({"headline" : title, "onion" : real})
	
app = Flask(__name__)

@app.route('/oon/endpoint/')
def endpoint():
    out = chal()
    return out
	
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4867)
