from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    name = request.form['name']
    file = open("names.txt", 'a')
    file.write(name + '\n')
    file.close()
    return render_template('index.html', name=name)
  return render_template('index.html') # for get method


app.run(host='0.0.0.0', port=81)

