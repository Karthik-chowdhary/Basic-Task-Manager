import json
class TaskManager:
    def __init__(self):
        self.Tasks = []
        self.FileName = "tasks.json"
        self.load_data()
    def load_data(self):
        try:
            with open(self.FileName,"r") as file:
                self.Tasks = json.load(file)
        except Exception as e:
            print(e)  
    def save_data(self):
        try:
            with open(self.FileName,"w"):
                self.json.dump(self.Tasks,file)
        except Exception as e:
            print(e)
    def add_tasks(self):
        task_name = input("Enter the task: ")
        due_date = input("Enter due date {12-Nov}: ")
        new_task = {
            "Task" : task_name,
            "Due-Date" : due_date,
            "complition" : False
        }
        self.Tasks.append(new_task)
        print("new task added successfully")
    def view_tasks(self):
        print("\n----Tasks----\n")
        for index,task in enumerate(self.Tasks):
            status_symbol = "[X]" if task['complition'] else "[ ]"
            print(f"{index+1}. {task['Task']} {task['Due-Date']} {status_symbol}",end="\n")
    def mark_as_done(self):
        try:
            print("enter caomplited task position")
            pos = int(input())
            taskx = self.Tasks[pos-1]
            taskx['complition'] = True
            print("Task marked as done")
        except Exception as e:
            print(e)
    def remove_tasks(self):
        try:
            pos = int(input("enter task position to remove"))
            task = self.Tasks.pop(pos-1)
            print(f"{task['Task']} removed successfully",end="\n")
        except Exception as e:
            print(e)
    def Run(self):
        while True:
            print("\n1. Add  2. View  3. Remove  4. Save & Exit  5. Mark Done")        
            choice = int(input())
            
            if choice == 1:
                self.add_tasks()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.remove_tasks()
            elif choice == 4:
                self.save_data()
                print("Goodbye!")
                break
            elif choice == 5:
                self.mark_as_done()
            else:
                print("Enter a valid nuber!")
if __name__ == "__main__":
    app = TaskManager()
    app.Run()
        