import time
#to do list
#testing
class ToDoList:
    def __init__(self):
        self.task_list = []
        
    def add_task(self):
        add = (input("What is your future task? ")).capitalize()
        self.task_list.append(add)
        print("Task added successfully!!")
        time.sleep(1)
        ask = (input("Wanna add another task? (y/n) ")).lower()
        if ask == "y":
            self.add_task()
        else:
            query = (input("Wanna have a look of updated list? (y/n)")).lower()
            if query == "y":
                self.view_task()
            else:
                pass

    def view_task(self):
        if len(self.task_list)>=1:
            print()
            print(*self.task_list, sep="\n")
            print()
        else:
            print("No task found!!")
        query = (input("Ready to go to main page? (y/n) ")).lower()
        if query == 'y':
            pass
        else:
            self.view_task()

    def mark_task(self):
        if len(self.task_list) >= 1:
            print()
            print(*self.task_list, sep="\n")
            print()
            mark = (input("Which task have you completed? ")).capitalize()
            if mark in self.task_list:
                index = self.task_list.index(mark)
                self.task_list.remove(mark)
                self.task_list.insert(index, f"{mark} (completed)")
                print('processing...')
                time.sleep(1)
                print('DONE!!')
            else:
                query = input("Task not found!! Wanna search again? (y/n)")
                if query == "y":
                    self.mark_task()
                else:
                    pass
        else:
            print("Nothing to mark as complete")

    def delete_task(self):
        if len(self.task_list) >= 1:
            print()
            print(*self.task_list, sep="\n")
            print()
            delete = (input("For what task have you made excuses? ")).capitalize()
            if delete in self.task_list:
                self.task_list.remove(delete)
                print("Task removed successfully!!")
                time.sleep(3)
                ask = (input("Wanna have a look of updated list? (y/n)")).lower()
                if ask == "y":
                    self.view_task()
                else:
                    pass
            else:
                query = input("Task not found!! Wanna search again? (y/n)")
                if query == "y":
                    self.delete_task()
                else:
                    pass
        else:
            print("Nothing to remove")

    def main(self):
        running = True
        while running:
            print("**************************")
            print("        To-do-list        ")
            print("**************************")
            print()

            question = ["1. Add a task",
                        "2. See your to_do_list",
                        "3. Mark a task as completed",
                        "4. Remove a task",
                        "5. Exit", ""]
            print(*question, sep="\n")
            choice = input("Choose a number (1-5): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_task()
            elif choice == "3":
                self.mark_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                running = False
                print("Allah Hafiz")
            else:
                print('Invalid Selection!! :(')
                
to_do_list1 = ToDoList()
to_do_list1.main()
