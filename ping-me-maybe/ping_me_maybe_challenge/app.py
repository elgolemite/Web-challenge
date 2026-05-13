from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    host = ''

    if request.method == 'POST':
        host = request.form.get('host', '')

        # Intentionally vulnerable for CTF purposes.
        # User input is passed directly into a shell command.
        cmd = f"ping -c 1 {host}"

        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            output = result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            output = "Command timed out."

    return render_template('index.html', output=output, host=host)

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
