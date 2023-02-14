import json
import os

from dagster import asset
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Task

load_dotenv()


def extract_tasks_list() -> list:
    api = TodoistAPI(os.getenv("TODOIST_API_TOKEN"))
    try:
        tasks_list = api.get_tasks()
        return tasks_list
    except Exception as error:
        print(error)


def transform_todoist_tasks_dict(tasks_list):
    tasks_dict = {}
    for task in tasks_list:
        tasks_dict.update({task.id: task.to_dict()})
    return tasks_dict


def transform_todoist_tasks_json():
    return json.dumps(transform_todoist_tasks_dict(extract_tasks_list()), indent=4)


@asset
def todoist_all_tasks():
    return transform_todoist_tasks_json()


if __name__ == "__main__":
    with open("tasks.json", "w", encoding="utf-8") as file:
        result = json.dump(
            transform_todoist_tasks_dict(extract_tasks_list()), fp=file, indent=4
        )
