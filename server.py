from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def playground():
    return render_template("index.html", num = 3, background_color = 'lightblue')

@app.route('/play/<int:num>')
def more_boxes(num):
    return render_template("index.html", num = num, background_color = 'lightblue')

@app.route('/play/<int:num>/<background_color>')
def more_color(num, background_color):
    return render_template("index.html", num = num, background_color = background_color)


if __name__=="__main__":
    app.run(debug = True)