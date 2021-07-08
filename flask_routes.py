from flask import Flask, render_template, request, redirect

# create a flask object
app = Flask(__name__)

# define a url / routing: ex of return HTML
@app.route('/home')
def home():
    return "<h1>hello world<h1>"

# define a url / routing: ex of template rendering
@app.route('/')
def index():
    return render_template('index.html')

# unique route with string parameter
@app.route('/<string:name>')
def hello(name): 
    return "hello, " + name

# unique route with integer parameter
@app.route('/<int:id>')
def numbers(id): 
    return "hello, " + str(id)

# unique route with multiple parameters
@app.route('/users/<string:name>/posts/<int:id>')
def profile(name, id): 
    return "hello, " + name + ", your id is:" + str(id)

# only allow get requests: does not allow put post etc
@app.route('/onlyget', methods=['GET'])
def get_only(): 
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)