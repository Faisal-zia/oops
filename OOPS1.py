class University:
    def _init_(self, name):
        self.name = name
        self.departments = []  # Simple list to store departments

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
            print(f"Department '{department}' added successfully.")
        else:
            print(f"Department '{department}' already exists.")

    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            print(f"Department '{department}' removed successfully.")
        else:
            print(f"Department '{department}' not found.")

    def get_departments(self):
        return self.departments

    def search_department(self, department):
        return department in self.departments

    def clear_departments(self):
        self.departments.clear()
        print("All departments cleared.")

    def edit_department(self, department, new_department):
        if department in self.departments:
            index = self.departments.index(department)
            self.departments[index] = new_department
            print(f"Department '{department}' renamed to '{new_department}'.")
        else:
            print(f"Department '{department}' not found.")