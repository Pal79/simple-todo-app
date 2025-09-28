from database.todo_db import TodoDatabase
from prettytable import PrettyTable
from colors.textstyle import TextStyle

class TodoService:
    def __init__(self):
        self.db = TodoDatabase()

    def add_task(self, task_name, description, deadline):
        self.db.add_todo(task_name, description, deadline, False)
        print(TextStyle.success("Feladat sikeresen hozzáadva!"))

    def list_tasks(self):
        tasks = self.db.list_todo()
        table = PrettyTable()
        table.field_names = [TextStyle.info(name) for name in ["ID", "Fejléc", "Leírás", "Határidő / DOM", "Státusz"]]

        if not tasks:
            print(TextStyle.warning("Nincs egyetlen feladat sem."))
            return
        else:
            for task in tasks:
                if task.id % 2 == 0:
                    table.add_row([TextStyle.list1(name) for name in [
                        task.id,
                        task.task_name,
                        task.description,
                        f"{task.deadline} / {task.dom}",
                        task.status]
                    ])
                else:
                    table.add_row([TextStyle.list2(name) for name in [
                        task.id,
                        task.task_name,
                        task.description,
                        f"{task.deadline} / {task.dom}",
                        task.status]
                    ])
        print(table)

    def delete_task(self, task_id):
        rows_deleted = self.db.delete_todo(task_id)
        if rows_deleted:
            print(TextStyle.success("Feladat sikeresen törölve."))
        else:
            print(TextStyle.error("Nincs ilyen ID-jű feladat."))

    # majd később ide jöhet az update is
    def update_task(self, task_id, field, new_value):
        success = self.db.update_todo(task_id, field, new_value)
        if success:
            print(TextStyle.success(f"A(z) {task_id}. ID-jű feladat '{field}' mezője módosítva!"))
        else:
            print(TextStyle.error("Hibás mezőnév vagy ID."))


"""
print(f"\n{task.id}. {task.task_name}")
print(f"Leírás: {task.description}")
print(f"Határidő: {task.deadline} (DOM: {task.dom})")
print(f"Státusz: {'Kész' if task.status else 'Nincs kész'}")
"""