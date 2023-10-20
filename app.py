from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("lookup.html")

@app.route('/truecaller/', methods=['GET', 'POST'])
def truecaller_info():
    if request.method == "POST":
        phone_numbers = request.form.get("contact")  # Change request.POST to request.form
        phone_numbers_list = phone_numbers.split(',')
        results = {}

        for phone_number in phone_numbers_list:
            command = f"truecallerpy -s {phone_number.strip()} --name"
            try:
                output = subprocess.check_output(command, shell=True, text=True)
            except subprocess.CalledProcessError as e:
                output = f"Error: {e}"
            results[phone_number] = output

        context = {
            'results': results,
        }
        return render_template('result.html', **context)  # Use render_template correctly

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
