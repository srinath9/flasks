from flask import render_template, flash, redirect, request, jsonify
from app import app
import task_db 

@app.route('/events', methods=['GET'])
def get_all_tasks():
    return jsonify(task_db.fetch_all_tasks())

@app.route('/events', methods=['POST'])
def create_task():
    task_string = request.form['task']
    task_db.create_task(task_string)
    return task_string

@app.route('/events/<id>', methods=['GET'])
def get_task(id):
    return task_db.fetch_task(id)





