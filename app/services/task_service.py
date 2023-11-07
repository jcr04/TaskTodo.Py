from app import db
from app.models.task import Task

class TaskService:
    @staticmethod
    def create_task(title, description):
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def get_all_tasks():
        return Task.query.all()

    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def update_task(task_id, title, description, is_complete):
        task = Task.query.get(task_id)
        if task:
            task.title = title
            task.description = description
            task.is_complete = is_complete
            db.session.commit()
            return task
        return None

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
