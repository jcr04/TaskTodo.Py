from flask import request, jsonify, Blueprint
from app.services.task_service import TaskService

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = TaskService.create_task(data['title'], data['description'])
    return jsonify(task), 201

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks]), 200

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TaskService.get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({"error": "Task not found"}), 404

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = TaskService.update_task(task_id, data['title'], data['description'], data['is_complete'])
    if task:
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({"error": "Task not found"}), 404

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if TaskService.delete_task(task_id):
        return jsonify({"success": "Task deleted"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

def init_app(app):
    app.register_blueprint(task_bp)
