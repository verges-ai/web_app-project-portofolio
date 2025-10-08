from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

# ===== Flask-Mail Configuration =====
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'stephaneatontsa2014@gmail.com'
app.config['MAIL_PASSWORD'] = 'imdvptpjakkqwxig'  # Your app-specific password (no spaces)
app.config['MAIL_DEFAULT_SENDER'] = 'stephaneatontsa2014@gmail.com'

mail = Mail(app)

# ===== Routes =====

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/resume/download')
def download_resume():
    return redirect(url_for('static', filename='resume/CV_Stephane_Atontsa.pdf'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(
            subject=f'New Contact from {name}',
            sender=app.config['MAIL_USERNAME'],
            recipients=['stephaneatontsa2014@gmail.com'],
            body=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        )
        try:
            mail.send(msg)
            flash('✅ Message sent successfully!', 'success')
        except Exception as e:
            print("❌ Email sending failed:", e)
            flash('❌ Message failed to send. Please try again.', 'danger')

        return redirect('/contact')

    return render_template('contact.html')

# ===== Run App =====
if __name__ == '__main__':
    app.run(debug=True)
