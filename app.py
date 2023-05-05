from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_lyric', methods=['POST', 'GET'])
def generate_lyric():
    name = request.form['name']
    lyrics = ["I don't know about you, but I'm feeling 22.",
             "Your faithless love's the only hoax I believe in.",
             "You play stupid games, you win stupid prizes",
                "Did you hear about the girl who lives in delusion?",
                "How can a person know everything at eighteen but nothin' at twenty-two?",
                "You drew stars around my scars but now I'm bleeding",
                "I could build a castle out of all the bricks they threw at me",
                "You're on your own, kid, yeah you can face this",
                "Back then I swore I was gonna marry him someday but I realized some bigger dreams of mine",
                "I once believed love would be burning red but it's golden",
                "I think I've seen this film before and I didn't like the ending",
                "I snuck in through the garden gate every night that summer just to seal my fate",
                "She's cheer captain and I'm on the bleachers",
                "And I was never good at telling jokes, but the punchline goes I'll get older, but your lovers stay my age",
                "Just between us, did the love affair maim you too?",
                "I didn't have it in myself to go with grace",
                "It's me. Hi. I'm the problem, it's me.",
                "They say all's well that ends well, but I'm in a new hell.",
                "I'd like to be my old self again, but I'm still trying to find it",
                "They told me all of my cages were mental so I got wasted like all my potential",
                "I'm still a believer but I don't know why. I've never been a natural, all I do is try, try, try.",
                "Wondering if I'd get there quicker if I was a man",
              "We are never ever ever getting back together.",
              "Cause baby now we got bad blood.",
              "All you are is mean, and a liar, and pathetic, and alone in life.",
              "I'm shining like fireworks over your sad empty town."]
    lyric = random.choice(lyrics)
    return render_template('templates/lyric.html', name=name, lyric=lyric)

if __name__ == '__main__':
    app.run(debug=True)
