def individual_data(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["desc"],
        "status": todo["status"]
    }

def all_tasks(todos):
    return [individual_data(todo) for todo in todos]