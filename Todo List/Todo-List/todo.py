import click # to create a cli
import json # to save and load tasks from a file 
import os # to check if a file exists

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task_description")
def add(task_description):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task_description, "done": False})
    save_tasks(tasks)
    click.echo(f"Task Added Successfully: {task_description}")

@click.command(name="list")
def list_tasks():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found")
        return
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed""" 
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else: 
        click.echo(f"Invalid task number: {task_number}")


@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Deleted tasks: {deleted_task['task']}")
    else:
        click.echo(f"Invalid task number")


cli.add_command(add)
cli.add_command(list_tasks)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
