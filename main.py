from flask import Flask, request

app = Flask(__name__)

# Endpoint for GET requests
@app.route('/', methods=['GET'])
def get_request():
    return 'This is a GET request.'

# Endpoint for POST requests
@app.route('/', methods=['POST'])
def post_request():
    return 'This is a POST request.'

# Endpoint for PUT requests
@app.route('/', methods=['PUT'])
def put_request():
    return 'This is a PUT request.'

# Endpoint for DELETE requests
@app.route('/', methods=['DELETE'])
def delete_request():
    return 'This is a DELETE request.'

# Endpoint for PATCH requests
@app.route('/', methods=['PATCH'])
def patch_request():
    return 'This is a PATCH request.'

# Endpoint for HEAD requests
@app.route('/', methods=['HEAD'])
def head_request():
    return 'This is a HEAD request.'

if __name__ == '__main__':
    app.run()
