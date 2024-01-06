#!/usr/bin/python3
'''A script that gathers data from an API.
'''
from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = get(url)
    name = response.json().get('name')

    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = get(url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print(f"Employee {name} is done with tasks({done}/{len(tasks)}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
