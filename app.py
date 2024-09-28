import logging
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')  # Use environment variable in production

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.info('Rendering home page')
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    app.logger.info('Rendering portfolio page')
    return render_template('portfolio.html')

@app.route('/personal-work')
def personal_work():
    app.logger.info('Rendering personal work page')
    return render_template('personal_work.html')

@app.route('/project')
def project():
    app.logger.info('Rendering project page')
    return render_template('project.html')

@app.route('/about')
def about():
    app.logger.info('Rendering about page')
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    app.logger.info('Handling contact page request')
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('Please fill out all fields.', 'error')
        else:
            # Here you would typically save this information or send an email
            app.logger.info(f'Received contact form submission from {name} ({email})')
            flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)