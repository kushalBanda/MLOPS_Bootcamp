from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data in my to do list
items = [
    {'id': 1, "name": "Item 1", "description": "This is item 1"},
    {'id': 2, "name": "Item 2", "description": "This is item 2"},
    {'id': 3, "name": "Item 3", "description": "This is item 3"}
]


@app.route('/')
def home():
    return "Welcome to the Sampel To DO List APP"

# Get: Retreive all the items

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get: Retreive specific items by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'})
    else:
        return jsonify(item)
    
## Post: Create a new task
@app.route('/items', methods = ['POST'])
def create_item():
    if not request.method or not 'name' in request.json:
        return jsonify({'error': 'item not found'}), 400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json(items[-1]['name']),
        "description": request.json(items[-1]['description']),
    }
    items.append(new_item)
    return jsonify(new_item)

# Put: Update an existing item
@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = request.json.get("name", item['name'])
    item['description'] = request.json.get("description", item['description'])
    
    return jsonify(item)

# Delete: Delete an existing item
@app.route("/items/<int:item_id>", methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug = True)