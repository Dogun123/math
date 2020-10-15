from flask import Blueprint,render_template

calc = Blueprint('calc',__name__)

@calc.route('/')
def calc_main():
    return render_template('calc_base.html')

@calc.route('/firstgrade')
def firstgrade():
    return render_template('calc_first.html')

@calc.route('/secondgrade')
def secondgrade():
    return render_template('calc_second.html')

@calc.route('/thirdgrade')
def thirdgrade():
    return render_template('calc_third.html')

@calc.route('/fourthgrade')
def fourthgrade():
    return render_template('calc_fourth.html')

@calc.route('/fifthgrade')
def fifthgrade():
    return render_template('calc_fifth.html')

@calc.route('/sixthgrade')
def sixthgrade():
    return render_template('calc_sixth.html')
