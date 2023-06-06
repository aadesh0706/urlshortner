from flask import Flask, render_template,request, redirect, url_for
import string
import random

mappings = {}  # Temporary dictionary to store URL mappings
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_short_url()
        mappings[short_url] = original_url
        return render_template('index.html', shortened_url=request.host_url + short_url)
    return render_template('index.html')

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    if short_url in mappings:
        original_url = mappings[short_url]
        return redirect(original_url)
    return "URL not found!"
if __name__ == '__main__':
    app.run(debug=True)
