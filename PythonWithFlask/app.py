from flask import Flask, render_template

app = Flask('app')

students = ['jatin', 'mandeep', 'harshita']

mydata = {
    "Name": "Umang",
    "Language": "some language"
}

@app.route('/')
def index():
    return render_template('index.html', info = mydata)

@app.route('/profile/')
def profile():
    return "profile data"

@app.route('/students/')
def Students():
    return ''' <h1>Students</h1>
    <ul>
    {}
    </ul>
    '''.format("\n".join(['<li>{}</li>'.format(x) for x in students]))
    #return '''<html><body><h1>Students</h1><ul><li>{}</li>
    #<li>{}</li>
    #<li>{}</li>
    #</ul>
    #</body></html>'''.format(students[0],students[1],students[2])

@app.route('/student/')
def student():
    return render_template('student.html', students = students)

@app.route('/student/<int:id>')
def studt(id):
    return students[id-1]




if __name__ == '__main__':
    app.run(port=8000, debug = True)