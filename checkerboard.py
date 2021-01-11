from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    print("We are connected to the main page")
    return render_template('checkerboard.html',y=int(1), x=int(1))


@app.route('/4')
def part_2():
    print("made /4")
    return render_template('checkerboard.html',y=int(2), x=int(2))


@app.route('/4/<int:x>/<int:y>')
def part_3(x, y):
    print("adding x & y")
    return render_template('checkerboard.html',y=int(y), x=int(x))


if __name__=="__main__":
    app.run(debug=True)
    