# Task-Tracker

#### This code allows a user to add, delete, view and modify a task they have inputted.

#### This app runs in the terminal with a Command line interface (CLI)

# Code explained

### Add Task 
If the user selects 1 in the main menu function then user can input their task and it will be added to the json file (file.json). 

### Update Task
If the user inputs 2 in the main menu then the user will be able to update the description of a task, also the code will add the time that the task was updated and asign it to the 'updatedat' variable.

### Remove Task
If the user enters 3 within the main menu function then the user can input the ID of the task that they wish to remove, and it will be removed from the json file (file.json).

### Changing the status of a task
If the user inputs 4 in the main menu then the user will be able to update the status of a chosen task, the code does this by asking the user for the id of the task, and then updates it accordingly within the 'status' variable.

### List tasks
If the user enters 5 within the main menu function then the user will be able to input a number between 1-4, depending on whether they want to view everything, all complete tasks, all not complete tasks or all in-progress tasks.

# 🚀 Installation
1. Clone the repository:<br>
```bash
git clone https://github.com/Tazme12/Task-Tracker
cd Task-Tracker
```
2. Install the package:<br>
```bash
pip install .
```
## 📌 Usage

Run the CLI app with:<br>
```bash
task-tracker
```

## RoadMap.sh Project:
https://roadmap.sh/projects/task-tracker
