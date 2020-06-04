from flask import render_template
from app import app

from .logic import first_name as fn
from .logic import last_name as ln


@app.route('/')
def index():
    return render_template('index.html', title='Fake Data', first_names=fn.first_name_function(),
                           last_name=ln.last_name_function())
