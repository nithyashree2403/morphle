from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hi this Nithya Shree V S</p>"

@app.route('/htop')
def htop():
    # Get the server time in IST
    ist_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')

    # Get system username safely
    username = os.getenv('USER', 'codespace')

    # Try running the top command
    try:
        top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True)
        top_output_formatted = top_output.stdout.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")
    except Exception as e:
        top_output_formatted = f"Error running top command: {str(e)}"

    return f"""
    <h1>Server Information</h1>
    <p><strong>Name:</strong>Nithya Shree V S</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <h2>TOP output:</h2>
    <pre>{top_output_formatted}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
