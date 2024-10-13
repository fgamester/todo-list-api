from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {'label': 'My first task', 'done': False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    resquest_body = request.get_json(force=True)
    print('Incoming request with the following body', resquest_body)
    todos.append(resquest_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('This is the position to delete', position)
    if len(todos) == 0:
        return jsonify({'message':'the todo list is empty'})
    
    if len(todos) < (position):
        return jsonify({'message':'there is no task in that position'})
    
    if len(todos) >= position:
        del todos[(position-1)]
        if len(todos) == 0:
            return jsonify({'message':'the list is empty now'})

    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)