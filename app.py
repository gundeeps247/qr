import qrcode
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     # Return an empty response or a placeholder image
#     return ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    name = request.form['name']
    age = int(request.form['age'])

    data = f"Name: {name}\nAge: {age}"
    img = qrcode.make(data)
    img.save("myqr.png")

    return send_file("myqr.png", mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
