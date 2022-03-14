from flask import Flask, render_template, session, redirect, request, url_for
from random import randint, randrange
from datetime import datetime
app = Flask(__name__)
app.secret_key = "skdflaiudbvlialvsdfvb82772fr982h89yfrh"

@app.route('/')
def index():
    if "playerGold" not in session:
        playerGold = session["playerGold"] = 0
        activities = session["activities"] = []
        round = session["round"] = 0
        return render_template('index.html', playerGold=playerGold,activities=activities,round=round)
    else:
        playerGold = session["playerGold"]
        activities = session["activities"]
        round = session["round"]
        return render_template('index.html', playerGold=playerGold,activities=activities,round=round)

@app.route('/process_money', methods=["POST"])
def process_money(): 
    activities = session["activities"]
    locations = { #dict of locations with start and end nums
        "farm":[10,20],
        "cave":[5,10],
        "house":[2,5],
        "casino":[-50,50]
    }
    
    session["round"] += 1
    round = str(session["round"])
    location = locations[request.form["location"]] #extracts location from POST
    
    change = randint(location[0],location[1]) #Calculates change in player gold
    
    session['playerGold'] += change
    
    if change > 0:
        activities.insert(0, "<p style='color: green'>Round: " + round + " --- You gained " + str(change) + " gold --- " + str(datetime.now().strftime("%A, %d. %B %Y %I:%M %p")) + "</p>")
    elif change < 0:
        activities.insert(0, "<p style='color: red'>Round: " + round + " --- You lost " + str(abs(change)) + " gold --- " + str(datetime.now().strftime("%A, %d. %B %Y %I:%M %p")) + "</p>")
    else:
        activities.insert(0, "<p>Round: " + round +" --- You got " + str(change) + " gold --- " + str(datetime.now()) + "</p>")
    
    if len(activities) > 10: activities.pop() 

    return redirect('/')

@app.route('/newGame')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)