from app import app
from flask import render_template, make_response, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/test_response', methods=('GET', 'POST'))
def test_response():
    text = '''
<form action="post">
  What is your birthday?
  <br>
  <label> Month
  <input type="text" name="month">
  </label>
  <label> Day
  <input type="text" name="day">
  </label>
  <label> Year
  <input type="text" name="year">
  </label>
  <br>
  <br>
  <input type="submit">
</form>
    '''
    headers = {}
    headers['Content-Type'] = 'text/html'
    return make_response((text,
                          200,
                          headers))


@app.route('/testform', methods=('GET', 'POST'))
def testform():
    headers = {}
    headers['Content-Type'] = 'text/plain'
    q = request.args.get('q')
    print(str(request))
    return make_response((request.get_data(),
                          200,
                          headers))

