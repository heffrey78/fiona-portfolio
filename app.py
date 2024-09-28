import logging
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')  # Use environment variable in production

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.info('Rendering home page')
    return render_template('home.html')

@app.route('/about')
def about():
    app.logger.info('Rendering about page')
    return render_template('about.html')

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    app.logger.info('Handling contact page request')
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if not name or not email or not subject or not message:
            flash('Please fill out all fields.', 'error')
        else:
            # Here you would typically save this information or send an email
            app.logger.info(f'Received contact form submission from {name} ({email})')
            flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    app.logger.info('Handling AJAX contact form submission')
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    if not name or not email or not subject or not message:
        return jsonify({'success': False, 'message': 'Please fill out all fields.'})
    else:
        # Here you would typically save this information or send an email
        app.logger.info(f'Received contact form submission from {name} ({email})')
        return jsonify({'success': True, 'message': 'Thank you for your message! I will get back to you soon.'})

@app.route('/portfolio/<string:project_id>')
def portfolio_detail(project_id):
    app.logger.info(f'Rendering portfolio detail page for project {project_id}')
    # Here you would typically fetch the project details based on the project_id
    # For now, we'll just pass the project_id to the template
    return render_template('project.html', project_id=project_id)

@app.route('/liveness_check')
def liveness_check():
    return 'OK', 200

@app.route('/readiness_check')
def readiness_check():
    return 'OK', 200

@app.errorhandler(404)
def page_not_found(e):
    app.logger.error('404 error occurred')
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error('500 error occurred', exc_info=True)
    return render_template('500.html'), 500

# Context processor to make the current year available in all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.utcnow().year}

if __name__ == '__main__':
    app.run(debug=True)