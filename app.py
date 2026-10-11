
from flask import Flask, jsonify, request, render_template

from pymongo import MongoClient

import json

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.todo_db

@app.route('/api')

def api():

    with open('data.json') as f:

        data = json.load(f)

    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])

def submit_todo_item():

    item_name = request.form.get('itemName')

    item_description = request.form.get('itemDescription')

    db.todos.insert_one({'itemName': item_name, 'itemDescription': item_description})

    return "Item added successfully!"

if __name__ == '__main__':

    app.run(debug=True)

