from flask import render_template
from app import app

from .logic import first_name as fn
from .logic import last_name as ln
from .logic import gender as gn
from .logic import password as pass_
from .logic import bio
from .logic import email
from .logic import address


@app.route('/')
def index():
    return render_template('index.html', title='Fake Data', first_names=fn.first_name_function(),
                           last_name=ln.last_name_function(),
                           gender=gn.random_gender(),
                           email=email.send_email(),
                           spare_email=email.send_email(),
                           address=address.fake_address(),
                           spare_address=address.fake_address(),
                           password=pass_.randomString(),
                           bio=bio.fake_bio())
