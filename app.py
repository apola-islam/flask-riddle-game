import secrets
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Uncomment the line below and set your own secret key when running the app
#app.secret_key = secrets.token_hex(32) 

def load_riddles():
    riddles = []
    try:
        with open("riddles.txt", "r") as file:
            for line in file:
                if "," in line and line.strip():
                    riddle=line.strip().split(',')
                    if len(riddle) == 2:
                        riddles.append({"question":riddle[0],"answer":riddle[1]})
    except Exception as e:
        print(f"Error loading riddles: {e}")
        return []
    return riddles


@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/game')
def index():
    riddles = load_riddles()
    if len(riddles) < 1:
        return "Error with riddles.txt file."
    length = len(riddles)
    score = session.get('score',0)
    index = session.get('riddle_index',0)
    if index >= length:
        return f"Game Over! Your final score is {score}."
    
    riddle = riddles[index]
    result = request.args.get('result', "")

    return render_template('index.html',riddle=riddle, score=score, index=index,length=length,result=result)

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the user's answer and current score/riddle_index
    user_answer = request.form['answer'].strip().lower()
    riddle_index = session.get('riddle_index', 0)
    score = session.get('score', 0)
    
    # Load riddles and check the user's answer
    riddles = load_riddles()
    if riddle_index >= len(riddles):  # Ensure no out-of-bounds error
        return redirect(url_for('index'))
    correct_answer = riddles[riddle_index]["answer"].lower()
    # Update score if correct
    if user_answer == correct_answer:
        score += 1
        result = "Correct!"
    else:
        result = "Incorrect..."
    # Update session with new score and increment riddle index
    session['score'] = score
    session['riddle_index'] = riddle_index + 1

    return redirect(url_for('index',result=result))

if __name__=="__main__":
    app.run(debug=True)