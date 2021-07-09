from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import prosodic
prosodic.config['print_to_screen']=0 


class Poem():
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def parse(self):
        text = prosodic.Text(self.text)
        text.parse() # must parse text before most methods are available
        stanzas = []
        for i, stanza in enumerate(text.children):
            i = {}
            for line in stanza.descendants():
                line = prosodic.Text(str(line)) # make each line a text object to access text properties (like syllables) PROBS a better way, idk
                line.parse()
                i[str(line.bestParses())] = len(line.syllables()) #bestParse returns list of lines with caps/lower emphasis
            stanzas.append(i)
        return stanzas

# create a flask object
app = Flask(__name__)
#config method that tells Flask where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialize db
db = SQLAlchemy(app)


# define a url / routing: ex of template rendering
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        # try: 
            poem = Poem(title=request.form['title'], text=request.form['poem'], author=request.form['author'])
            print('RESQUEST', request.form['poem'])
            scansion = poem.parse()
            # return redirect('/')
            return render_template('index.html', scansion=scansion, title=poem.title)
        # except: 
        #     return 'There was an error parsing your text'
    else: 
        scansion = []
        return render_template('index.html', scansion=scansion)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')
    
@app.route('/contact')
def hello(): 
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)