import models
import datetime

def convert(date_time):
    format = '%Y-%m-%d'
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str

def end_tasks():
    for project in models.get_all_projects():
        tasks = models.get_all_tasks(project.name)
        for task in tasks:
            deadline = convert(task.deadline)
            if deadline < datetime.datetime.now():
                models.del_task(task.name)