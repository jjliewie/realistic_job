from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request
from actual import calculate, euclidean_distance, cosine_similarity

app = Flask(__name__)

@app.route('/')
def my_form():
  return render_template('index.html', PageTitle = "Landing page")

@app.route('/', methods=['POST'])
def my_form_post():
  text1 = request.form['text1']
  if text1!='':
    return "<h1>hello</h1>"

  # uploaded_file = request.files['txt_file']
  # if uploaded_file.filename != '':
  #   text = uploaded_file.read()
  #   text = str(text)
  #   return calculate(text)

  else:
    return render_template('index.html', PageTitle = "Landing page")

if __name__ == '__main__':
  app.run(debug = True)
