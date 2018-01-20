from app import app
from flask import render_template, make_response

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test_response')
def test_response():
    text = '''
<form action="https://google.com/search">
  <input name="q">
  <input type="submit">
</form>
    '''
    headers = {}
    headers['Content-Type'] = 'text/html'
    return make_response((text,
                          200,
                          headers))