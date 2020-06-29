from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='/css')

@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/subjects')
def subjects_page():
    return render_template('subjects.html')

if __name__ == '__main__':
    app.run()    
