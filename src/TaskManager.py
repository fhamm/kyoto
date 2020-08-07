import os
import sys
import json
import subprocess
from datetime import datetime

class Task:

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.directory = os.path.expanduser (attributes['cwd'])
        self.commands = attributes['cmd']

    def run(self):
        
        return_codes = []

        for command in self.commands:
            return_code = subprocess.call(command.split(), cwd=self.directory)
            return_codes.append(return_code)

        return return_codes

class TaskManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.data = self.getData() 
        self.tasks = self.getTasks()
        self.history_file = '.KYOTOHIST'
    
    def getData(self):
        with open(self.filename) as file:
            return json.load(file)

    def getTasks(self):
        
        tasks = {}
        
        for key, value in self.data.items():
            new_task = Task(key, value)
            tasks[key] = new_task
            
        return tasks

    def listTasks(self):
        for key, value in self.data.items():
            print(key)

    def writeToHistory(self, task_name, return_code):
        history = open(self.history_file, "a+")
        
        if return_code == 0:
            return_string = 'Success (' + str(return_code) + ')'
        else:
            return_string = 'Error (' + str(return_code) + ')'
        
        info = '[ ' + str(datetime.now()) + ' | ' + str(task_name) + ' ]' + ' : ' + return_string + '\n'
        history.write(info)
        history.close()
    
    def printHistory(self):
        if os.path.isfile(self.history_file):
            history = open(self.history_file, 'r')
            for line in history.readlines():
                print (line.rstrip('\n'))
        else:
            print('History does not exist!')

    def runTask(self, task_name):
        if task_name in self.tasks:
            return_codes = self.tasks[task_name].run()
           
            for return_code in return_codes:
                self.writeToHistory (task_name, return_code)
        else:
            print('Task', task_name, 'does not exist!')