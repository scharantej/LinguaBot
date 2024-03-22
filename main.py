
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def main():
    return render_template('index.html')

# Define the features route
@app.route('/features')
def features():
    return render_template('features.html')

# Define the testimonials route
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

# Define the faq route
@app.route('/faq')
def faq():
    return render_template('faq.html')

# Define the pricing route
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

# Define the signup route
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Define the error route
@app.errorhandler(404)
def error(e):
    return render_template('error.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
