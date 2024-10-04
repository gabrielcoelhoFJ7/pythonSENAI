from flask import Flask, jsonify
app = Flask(__name__)

# Defina a lista de usuários
users = [
    {'id': 1, 'name': 'John', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Jane', 'email': 'jane@example.com'}
]

# Defina a rota /users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)