from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    todo_item = request.form['todo']
    todo_list.append(todo_item)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    todo_item = request.form['todo']
    todo_list.remove(todo_item)
    return redirect('/')
