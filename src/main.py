#!/usr/bin/python3

import os
import sys
import argparse

from TaskManager import Task, TaskManager

#----------------------------------------------#

parser = argparse.ArgumentParser(prog = "kyoto", description = "kyoto is tool that allows you to create tasks to easily run sequences of commands.")

parser.add_argument('tasks', nargs = '*')
parser.add_argument('--file', '-f', type = str, help = "specify the tasks file")
parser.add_argument('--list', '-l', action = 'store_true', help = "list all tasks")
parser.add_argument('--hist', '-t', action = 'store_true', help = "show task history")
#parser.add_argument('--supress', '-s', action = 'store_true', help = "supress all text")
#parser.add_argument('--stderr', '-e', type = str, help = "specify the stderr output file")
#parser.add_argument('--stdout', '-o', type = str, help = "specify the stdout output file")

args = parser.parse_args()
vars = vars(args)

#----------------------------------------------#

# Check if input is valid
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Check if file exists
if vars['file']: 
    tasks_file = os.path.expanduser(vars['file'])
    print (tasks_file)
else:
    tasks_file = os.path.expanduser('~/kyoto/tasks.json')

if not os.path.exists(tasks_file):
    exit('Invalid tasks file!')

task_manager = TaskManager(tasks_file)

# List tasks 
if vars['list']:
    task_manager.listTasks()
    exit()

# Print history
if vars['hist']:
    task_manager.printHistory()
    exit()

# Execute tasks
for task in vars['tasks']:
    task_manager.runTask (task)