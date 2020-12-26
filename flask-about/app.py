import re
from statistics import mean
from itertools import count


from flask import Flask
from flask import render_template
from flask import url_for
from flask import request


app = Flask(__name__, static_folder='static2')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        grs = request.form['MarksInput']
        grs = [int(i) for i in re.findall('\d', grs)]
        m = mean(grs)
        for i in count():
            if mean(grs) >= 4.5:
                break
            grs.append(5)

        return render_template('index.html', mean=m, count=i)

    return render_template('index.html')    


@app.route('/about')
def about(name=None):
    return render_template('about.html', name=name)    

