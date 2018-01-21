from app import app
from flask import render_template, make_response, request, redirect, url_for
from app.models import rot13alg

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


@app.route('/rot13', methods=('GET', 'POST'))
def rot13():
    textarea_name = 'textarea'
    if request.method == 'POST':
        user_input = request.form.get(textarea_name)
        conversion_result = rot13alg(user_input)
        return redirect(url_for('rot13', conversion_result=conversion_result))
    
    usertext = request.args.get('conversion_result')
    return render_template('rot13.html',
                           input_name=textarea_name,
                           usertext=usertext)

