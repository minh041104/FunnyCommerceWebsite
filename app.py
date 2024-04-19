from flask import Flask, jsonify, request
app = Flask(__name__)

user_list = [
    {'id': 1, 'name': "Khong Ngoc Anh", 'age': 20},
    {'id': 2, 'name': "Nguyen Binh Minh", 'age': 20}
]

@app.route('/')
def hello_world():
    return 'Hello World!!!'

@app.route('/user', methods=['GET'])
def get_user():
    return jsonify(user_list)

@app.route('/user', methods=['POST'])
def add_user():
    new_users = []
    new_users = request.json
    for u in new_users:
        user_list.append(u)
    return jsonify({'message': 'User added'})

@app.route('/user', methods=['PUT'])
def update_user():
    user_new = request.json
    for i, u in enumerate(user_list):
        if u['id'] == user_new['id']:
            user_list[i] = user_new
            break
    return jsonify({'message': "User updated"})

@app.route('/user', methods=['DELETE'])
def delete_user():
    user_delete = request.json
    id_delete = user_delete['id']
    for i, u in enumerate(user_list):
        if u['id'] == id_delete:
            user_list.pop(i)
            break
    return jsonify({'message': "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)