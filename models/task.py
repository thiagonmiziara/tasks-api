class Task:
    def __init__(self, task_id, title, description, completed=False) -> None:
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
