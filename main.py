from services.todo_servce import TodoService
from colors.textstyle import TextStyle

service = TodoService()

is_on = True
while is_on:
    print(TextStyle.info("-----  MENU  -----"))
    print(TextStyle.text("Új feladat létrehozása (1)"))
    print(TextStyle.text("Feladatok kiíratása (2)"))
    print(TextStyle.text("Feladat módosítása (ID alapján) (3)"))
    print(TextStyle.text("Feladat törlése (ID alapján) (4)"))
    print()
    print(TextStyle.error2("Kilépés (0)"))
    print()
    choise = int(input(TextStyle.warning("Válassz a menüből: ")))

    if choise == 1:
        task_name = input("Feladat megnevezése: ")
        description = input("Feladat leírása: ")
        deadline = input("Határidő (YYYY-mm-dd): ")
        service.add_task(task_name=task_name, description=description, deadline=deadline)

    elif choise == 2:
        service.list_tasks()
    elif choise == 3:
        service.list_tasks()
        task_id = int(input(TextStyle.warning("Melyik feladatot módosítod? (ID): ")))
        print(TextStyle.info("Mit szeretnél módosítani?"))
        print(TextStyle.text("1 - Megnevezés"))
        print(TextStyle.text("2 - Leírás"))
        print(TextStyle.text("3 - Határidő"))
        print(TextStyle.text("4 - Státusz (True/False)"))
        
        field_choice = int(input(TextStyle.warning("Válassz mezőt: ")))
        field_map = {
            1: "task_name",
            2: "description",
            3: "deadline",
            4: "status"
        }

        if field_choice not in field_map:
            print(TextStyle.error("Érvénytelen választás."))
            continue

        new_value = input("Új érték: ")
        if field_map[field_choice] == "status":  # Boolean konverzió
            new_value = new_value.lower() in ("true", "1", "igen")

        service.update_task(task_id, field_map[field_choice], new_value)


    elif choise == 4:
        service.list_tasks()
        task_id = int(input(TextStyle.warning("Melyik feladatot törlöd? (ID): ")))
        service.delete_task(task_id=task_id)
    else:
        is_on = False