from abc import ABC, abstractmethod

class Building(ABC):
    def __init__(self, location, size, floors):
        self.location = location
        self.size = size
        self.floors = floors
        self.door_open = False

    def open_doors(self):
        if not self.door_open:
            self.door_open = True
            print(f"The door at the {self} is now open.")
        else:
            print(f"The door at the {self} is already open.")

    def close_doors(self):
        if self.door_open:
            self.door_open = False
            print(f"The door at the {self} is now closed.")
        else:
            print(f"The door at the {self} is already closed.")

    def get_location(self):
        return self.location

    def get_size(self):
        return self.size

    def get_floors(self):
        return self.floors

    @abstractmethod
    def building_function(self):
        pass

    def __str__(self):
        pass


class Industrial_Building(Building):
    def __init__(self, location, size, floors, machinery_list, has_lab, lab_type, equipment_list):
        super().__init__(location, size, floors)
        self.machinery_list = machinery_list
        self.has_lab = has_lab
        self.lab_type = lab_type
        self.equipment_list = equipment_list 

    def __str__(self):
        return f"Industrial Building"

    def get_lab(self):
        if self.has_lab:
            print(f"{self} has a {self.lab_type} lab.")
            print("Equipment(s) in the lab:")
            for equipment in self.equipment_list:
                print(f"- {equipment}")
        else:
            print(f"{self} does not have a lab.")

    def get_machinery(self):
        print(f"{self} has the following machinery:")
        for machinery in self.machinery_list:
            print(f"- {machinery}")

    def building_function(self):
        if self.door_open:
            machinery_names = ", ".join(self.machinery_list)
            equipment_names = ", ".join(self.equipment_list) if self.has_lab else ""
            lab = (f"It includes a {self.lab_type} lab, and contains the following equipment: {equipment_names}."
                   if self.has_lab else "It does not include a lab.")
            print(f"{self} is located at {self.location}. Size: {self.size} sqm, Floors: {self.floors}")
            print(f"Machinery: {machinery_names}. {lab}")
        else:
            print("Open the doors first.")

class Residential_Building(Building):
    def __init__(self, location, size, floors, number_of_units, residents, amenities, pet_friendly, has_security, emergency_contacts):
        super().__init__(location, size, floors)
        self.number_of_units = number_of_units
        self.residents = residents
        self.amenities = amenities
        self.pet_friendly = pet_friendly
        self.has_security = has_security
        self.emergency_contacts = emergency_contacts

    def __str__(self):
        return f"Residential Building"

    def get_residents(self):
        print(f"Residents in {self}:")
        for resident in self.residents:
            print(f"- {resident}")

    def get_amenities(self):
        print(f"Amenities in {self}:")
        for amenity in self.amenities:
            print(f"- {amenity}")

    def get_pet_policy(self):
        if self.pet_friendly:
            print(f"{self} is pet-friendly.")
        else:
            print(f"{self} is not pet-friendly.")

    def get_security_status(self):
        if self.has_security:
            print(f"Security personnel are present in {self}.")
        else:
            print(f"No security personnel in {self}.")

    def get_emergency_contacts(self):
        print(f"Emergency contacts for {self}:")
        for role, number in self.emergency_contacts():
            print(f"{role}: {number}")

    def building_function(self):
        if self.door_open:
            print(f"{self} is located at {self.location}.")
            print(f"It has {self.floors} floors, {self.number_of_units} units, and is {self.size} sqm.")
        else:
            print("Open the doors first.")


print("******************************************")
print("\n        Building Management System        \n")
print("******************************************\n")
print("Welcome to the Building Management System!\n")
print("Choose the type of Building: ")
print("1. Industrial Building")
print("2. Residential Building\n")

while True:
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        if input("Do you want to open the doors of the building? (yes/no): ").lower() == "yes":
            location = input("Enter the location of the building: ")
            size = int(input("Enter the size of the building (in square meters): "))
            floors = int(input("Enter the number of floors in the building: "))
            machinery_list = input("Enter the list of machinery (comma-separated): ").split(", ")
            has_lab_input = input("Does the building have a lab? (yes/no): ").lower()
            has_lab = has_lab_input == "yes"
            if has_lab:
                lab_type = input("Enter the type of lab: ")
                equipment_list = input("Enter the list of equipment (comma-separated): ").split(", ")
            else:
                lab_type = None
                equipment_list = None
            building = Industrial_Building(location, size, floors, machinery_list, has_lab, lab_type, equipment_list)
            print()
            building.open_doors()
            building.get_machinery()
            building.get_lab()
            print()
            building.building_function()
            print()
            if input("Do you want to close the doors of the building? (yes/no): ").lower() == "yes":
                building.close_doors()
            else:
                print(f"The doors of {building} are still open.")
        else:
            print("\nDoors remain closed. Goodbye!")

    elif choice == "2":
        if input("Do you want to open the doors of the building? (yes/no): ").lower() == "yes":
            location = input("Enter the location of the building: ").strip()
            size = int(input("Enter the size of the building (in square meters): "))
            floors = int(input("Enter the number of floors in the building: "))
            number_of_units = int(input("Enter the number of units in the building: "))
            residents = input("Enter the list of residents (comma-separated): ").split(", ")
            amenities = input("Enter the list of amenities (comma-separated): ").split(", ")
            pet_friendly = input("Is the building pet-friendly? (yes/no): ").lower() == "yes"
            has_security = input("Does the building have security personnel? (yes/no): ").lower() == "yes"
            emergency_contacts = {}
            while True:
                role = input("Enter role for emergency contact (or 'done' to finish): ")
                if role.lower() == "done":
                    break
                number = input(f"Enter phone number for {role}: ")
                emergency_contacts[role] = number
            building = Residential_Building(location, size, floors, number_of_units, residents, amenities, pet_friendly, has_security, emergency_contacts)
            print()
            building.open_doors()
            building.get_residents()
            building.get_amenities()
            building.get_pet_policy()
            building.get_security_status()
            building.get_emergency_contacts()
            print()
            building.building_function()
            print()
            if input("Do you want to close the doors of the building? (yes/no): ").lower() == "yes":
                building.close_doors()
            else:
                print(f"The doors of {building} are still open.")
        else:
            print("\nDoors remain closed. Goodbye!")

    else:
        print("Invalid choice.\n")
        continue
    break
