class TaskManager:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n📋 MENU:")
        print("1️⃣  Add Task")
        print("2️⃣  Update Task")
        print("3️⃣  Delete Task")
        print("4️⃣  View All Tasks")
        print("5️⃣  Exit")

    def show_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks found.")
        else:
            print("\n📝 Your Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task['name']} (Priority: {task['priority']})")

    def add_task(self):
        name = input("➕ Enter task name: ").strip()
        priority = input("🔢 Enter priority (High/Medium/Low): ").capitalize()
        if priority not in ["High", "Medium", "Low"]:
            print("❌ Invalid priority. Defaulting to 'Medium'.")
            priority = "Medium"
        self.tasks.append({"name": name, "priority": priority})
        print(f"✅ Task '{name}' added with priority '{priority}'.")

    def update_task(self):
        self.show_tasks()
        try:
            idx = int(input("✏️ Enter task number to update: ")) - 1
            if 0 <= idx < len(self.tasks):
                new_name = input("🔁 New task name: ").strip()
                new_priority = input("🔁 New priority (High/Medium/Low): ").capitalize()
                if new_priority not in ["High", "Medium", "Low"]:
                    new_priority = "Medium"
                self.tasks[idx] = {"name": new_name, "priority": new_priority}
                print("✅ Task updated successfully.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def delete_task(self):
        self.show_tasks()
        try:
            idx = int(input("🗑️ Enter task number to delete: ")) - 1
            if 0 <= idx < len(self.tasks):
                removed = self.tasks.pop(idx)
                print(f"🗑️ Task '{removed['name']}' deleted.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def run(self):
        print("👋 Welcome to the Task Manager App")
        while True:
            self.display_menu()
            choice = input("🔘 Select an option (1-5): ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.update_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.show_tasks()
            elif choice == '5':
                print("👋 Exiting Task Manager. Have a productive day!")
                break
            else:
                print("❌ Invalid choice. Please select between 1 to 5.")

# Run the Task Manager
manager = TaskManager()
manager.run()
