from flask import Flask, render_template
import game_of_life

app = Flask(__name__)

c = 0


@app.route("/")
def index():
    game_of_life.GameOfLife(20, 13)
    return render_template("index.html")


@app.route("/live")
def live():
    global c
    gol = game_of_life.GameOfLife(20, 13)
    if c > 0:
        gol.form_new_generation()
    gol.new_life(c)
    c += 1
    return render_template("live.html", life=gol)


if __name__ == "__main__":
    app.run(host="localhost", port=5555)
