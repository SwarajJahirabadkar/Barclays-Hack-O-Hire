from flask import Flask, render_template, request
from passgan import generate_and_analyze_password  # Import the function

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template when the root URL is accessed

@app.route('/check_password', methods=['POST'])
def check_password():
    # Get the password from the form
    user_password = request.form['password']
    
    # Call the password generation and analysis function
    strength, reasons, suggestions, crack_time = generate_and_analyze_password(user_password)
    
    # Return the results back to the front-end (index.html)
    return render_template('index.html', 
                           strength=strength, 
                           reasons=reasons, 
                           suggestions=suggestions, 
                           crack_time=crack_time)

if _name_ == '_main_':
    app.run(debug=True)
