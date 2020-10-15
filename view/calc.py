from flask import Blueprint
from flask import Blueprint,render_template

calc = Blueprint('calc',__name__)

@calc.route('/')
def calc_main():
    

