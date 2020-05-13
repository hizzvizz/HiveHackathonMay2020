from flask import Flask, render_template #imports Flask and render_template from the flask module
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html') #gets "index.html" from the templates folder and returns it
app.run('0.0.0.0',8080)



# [In a repl](https://repl.it/@mat1/flask-example-2), again

"""

### Make it actually do stuff!
Ok, this may start getting slightly confusing so if you get lost at any point, please refer to [my example repl](https://repl.it/@mat1/flask-example-3)

First, add `request` to your imports from Flask.
Then in your main.py file, add another app route, but this time set the path to '/clicked'. Then after that string, add another argument, but this time set it to `methods = ['POST']`
Now under the app route decorator, define a function. Just like before, the name doesn't matter. After that, inside the function you just created, you can get data sent from the server by using `data = request.data.decode()` You can do whatever you want with that data variable. Now just do `return 'done'` (it won't be shown to the user but it tells the client that the request was successful).
All your Python code is done now, so onto JavaScript!

"""
