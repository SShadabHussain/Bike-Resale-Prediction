from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/solution')
def solution():
    return render_template('solution.html')


@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/thank_you') 
def thank_you():
    fullname = request.args.get('fullname')
    email = request.args.get('email')
    return render_template('thank_you.html',fullname=fullname,email=email)

# @app.about('/about') 
# def about():
#     return render_template('about.html')

@app.errorhandler(404)
  
def not_found(e):
    return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)
