from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    name = request.form['name']
    file = open("names.txt", 'a')
    file.write(name + '\n') # appends the [name] to the file extra/next line
    file.close()
    infile = open("names.txt",'r') # can omit 'r'
    lines = infile.readlines()
    infile.close()
    return render_template('index.html',name=name,lines=lines)
  return render_template('index.html')


app.run(host='0.0.0.0', port=81)
