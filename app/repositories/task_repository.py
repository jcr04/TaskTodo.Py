from app import db
from app.models.task import Task

class TaskRepository:
    
    @staticmethod
    def create(title, description):
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def get_all():
        return Task.query.all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def update(task, title, description, is_complete):
        task.title = title
        task.description = description
        task.is_complete = is_complete
        db.session.commit()
        return task

    @staticmethod
    def delete(task):
        db.session.delete(task)
        db.session.commit()
