#!/usr/bin/python3
"""Exports list of dictionaries of TODOs"""
import json
import requests


if __name__ == '__main__':
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    to_dos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    with open("todo_all_employees.json", 'w') as file:
        todo_dict = {employee.get('id'): [{
                'task': task.get('title'),
                'username': employee.get('username'),
                'completed': task.get('completed')
            } for task in to_dos if employee.get('id') == task.get('userId')
            ] for employee in users}
        json.dump(todo_dict, file)