from flask import Flask, jsonify, request
from tasks import tasks_list

app = Flask(__name__)

# Create a route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks_list)

# Create a route to get a single task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks_list if task['id'] == task_id]
    if task:
        return jsonify(task[0])
    else:
        return jsonify({'error': 'Task not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)