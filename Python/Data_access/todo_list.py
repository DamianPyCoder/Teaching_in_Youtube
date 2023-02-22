#!/usr/bin/python3
#-*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)
pwd = "....."
user = "....."
uri = "mongodb+srv://" + user + ":" + pwd + "....."
client = MongoClient(uri)

database_name = 'todo'

# Obtenir totes les tasques
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = client[database_name].tasks.find()
    response = []
    for task in tasks:
        response.append({
            '_id': str(task['_id']),
            'title': task['title'],
            'description': task['description'],
            'done': task['done']
        })
    return jsonify(response)

# Obtenir una tasca per ID
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = client[database_name].tasks.find_one({'_id': ObjectId(id)})
    if task:
        response = {
            '_id': str(task['_id']),
            'title': task['title'],
            'description': task['description'],
            'done': task['done']
        }
    else:
        response = {'error': 'Task not found'}
    return jsonify(response)

# Afegir una nova tasca
@app.route('/tasks', methods=['POST'])
def add_task():
    # curl -X POST -d '{"title": "novattttedasca", "description": "deprova", "done": "Si"}' -H "Content-type: application/json" localhost:5000/tasks
    title = request.json['title']
    description = request.json['description']
    done = request.json['done']
    task = client[database_name].tasks.find_one({'title': title})
     
    if task:
        response = {'message': 'Title already exists'}
    else:    
        client[database_name].tasks.insert_one({'title': title, 'description': description, 'done': done})
        new_task = client[database_name].tasks.find_one({'title': title})
        response = {
            '_id': str(new_task['_id']),
            'title': new_task['title'],
            'description': new_task['description'],
            'done': new_task['done']
        }
    return jsonify(response)

# Actualitzar una tasca per ID
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = client[database_name].tasks.find_one({'_id': ObjectId(id)})
    if task:
        client[database_name].tasks.update_one({'_id': ObjectId(id)}, {'$set': request.json})
        task = mongo.db.tasks.find_one({'_id': ObjectId(id)})
        response = {
            '_id': str(task['_id']),
            'title': task['title'],
            'description': task['description'],
            'done': task['done']
        }
    else:
        response = {'error': 'Task not found'}
    return jsonify(response)

# Eliminar una tasca per ID
# @app.route('/tasks/<id>', methods=['DELETE'])
# def delete_task(id):
#     task = client[database_name].tasks.find_one({'_id': ObjectId(id)})
#     if task:
#         client[database_name].tasks.delete_one({'_id': ObjectId(id)})
#         response = {'message': 'Task deleted successfully'}
#     else:
#         response = {'error': 'Task not found'}
#     return jsonify(response)



# curl -X DELETE -d -H "Content-type: application/json" localhost:5000/tasks/novattttedasca
# Eliminar una tasca per title
@app.route('/tasks/<title>', methods=['DELETE'])
def delete_task(title):
    task = client[database_name].tasks.find_one({'title': title})
    if task:
        client[database_name].tasks.delete_one({'title': title})
        response = {'message': 'Task deleted successfully'}
    else:
        response = {'error': 'Task not found'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)