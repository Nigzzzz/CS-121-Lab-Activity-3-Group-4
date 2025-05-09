from abc import ABC, abstractmethod
import os

class Building(ABC):

    def __init__ (self):
        os.system('cls')
        print("INPUT THE BASIC BUILDING INFO")
        self.location = input("Enter the Location of the Building: ").capitalize()
        self.size = int_input("Enter the Size of the Building (in square meters): ")
        self.floors = int_input("Enter the Number of Floors: ")
        self.door_open = False

    def __str__(self):
        return ("Building")
 
    def open_doors(self):
        action = "is now open" if not self.door_open else "is already open"
        self.door_open = True
        print(f"The doors of the {self} {action}.")


    def close_doors(self):
        action = "is now closed" if self.door_open else "is already closed"
        self.door_open = False
    

    def get_location(self):
        return self.location

    def get_size(self):
        return self.size

    def get_floors(self):
        return self.floors

    def get_info(self):
        print(f"This {self} is Located at {self.location}, with the size of {self.size} sqm and has {self.floors} floors")

    def add_item(self, item_list, item):
        item_list.append(item)

    def delete_item(self, item_list, item):
        if item in item_list:
            item_list.remove(item)
        else:
            print("Item is not available in {item_list}")
            input("Press Enter to Continue: ")

    def edit_item(self, target_list, item, class_method):
        class_method()
        draw_line()
        draw_menu(["ADD ITEM", "DELETE ITEM"])
        choice = int_input("Enter the Command: ")
        if choice == 1:
            item = input("Enter the Item to Add: ").strip().capitalize()
            self.add_item(target_list, str(item))
        if choice == 2:
            item = input("Enter the Item to Delete: ").strip().capitalize()
            self.delete_item(target_list, str(item))






class Industrial_Building(Building):

    def __init__(self):

        super().__init__()
        os.system('cls')

        print(f"Input the Properties for {self}")

        self.machinery_list = [item.strip().capitalize() for item in input("Enter the list of machinery (comma-separated): ").split(",")]

        self.has_lab = choice_input("Does the building have a lab? (yes/no): ")

        if self.has_lab == True:
            self.lab_type = input("Enter the type of lab: ").capitalize()
            self.equipment_list = [item.strip().capitalize() for item in input("Enter the list of equipments (comma-separated): ").split(",")]    

    def __str__(self):
        return "Industrial Building"
    
    def get_lab(self):
        if self.has_lab == True:
            print(f"{self} has a {self.lab_type}", end = " ")
            print(f"" if "lab" in {self.lab_type} else "lab")
            print("Equipment(s) in the lab:")
            for equipment in self.equipment_list:
                print(f"- {equipment}")

    def get_machinery(self):
        print(f"The {self} has the following machinery:")
        for machinery in self.machinery_list:
            print(f"- {machinery}")

    def get_info(self):
        os.system('cls')
        print(f"This {self} is Located at {self.location}, with the size of {self.size} sqm and has {self.floors} floors.")
        draw_line()
        self.get_machinery()
        draw_line()
        self.get_lab()
        draw_menu(["EDIT MACHINERY", "EDIT EQUIPMENTS", "EXIT"])
        choice = int_input("Enter Command: ")
        if choice == 1:
            os.system('cls')
            self.edit_item(self.machinery_list, None, self.get_machinery)
        elif choice == 2:
            os.system('cls')
            if self.has_lab:
                self.edit_item(self.equipment_list, None, self.get_lab)
            else:
                print(f"This {self} has no Lab Available")
                input("Press Enter to Continue:")
        elif choice == 3:
            return True





        


class Residential_Building(Building):

    def __init__(self):
        super().__init__()
        os.system('cls')

        print(f"Input the Properties for {self}")
        self.total_units = int_input("Enter the number of units in the building: ")
        self.residents_list = [item.strip().capitalize() for item in input("List the name of the residents (comma-separated): ").split(",")]
        self.amenities = [item.strip().capitalize() for item in input("Enter the list of amenities (comma-separated): ").split(",")]
        self.pet_friendly = choice_input("Is the building pet-friendly? (yes/no): ")
        self.has_security =  choice_input("Does the building have security personnel? (yes/no): ")
        self.emergency_contacts = {}

        self.add_contacts()

    def __str__(self):
        return "Residential Building"

    def get_residents(self):
        print(f"Residents in {self}:")
        for resident in self.residents_list:
            print(f"- {resident}")

    def get_amenities(self):
        print(f"Amenities in this {self}:")
        for amenity in self.amenities:
            print(f"- {amenity}")

    def get_pet_policy(self):
        if self.pet_friendly:
            print(f"This {self} is pet-friendly.")
        else:
            print(f"This {self} is not pet-friendly.")

    def get_security_status(self):
        if self.has_security:
            print(f"Security personnel are present in this {self}.")
        else:
            print(f"No security personnel in this {self}.")

    def add_contacts(self):
        while True:
            self.role = input("Enter role for emergency contact (or 'done' to finish): ").capitalize().strip()

            if self.role.lower() == "done" and not self.emergency_contacts:
                print("Emergency contacts cannot be empty, Try Again")
                continue
            
            if self.role.lower() == "done":
                break
            
            self.num_validator()

            self.emergency_contacts[self.role] = self.number
            

    def num_validator(self):
        while True:
            self.number = input(f"Enter the Cellphone Number for {self.role}: ").strip()

            if self.number == "":
                print("Phone number cannot be empty, Try Again!")
                continue

     
            self.number = self.number.replace(" ", "").replace("-","")

      
            if self.number.startswith("+63"):
                self.number = "0" + self.number[3:]
            elif self.number.startswith("9") and len(self.number) < 11:
                self.number = "0" + self.number

        
            if not self.number.isdigit():
                print("Phone number should contain only digits.")
                continue

            if len(self.number) != 11 or not self.number.startswith("09"):
                print("Invalid phone number format. Please enter a valid 11-digit number starting with \"09\".")
                continue
            
            break

    def get_emergency_contacts(self):
        print(f"{'These are ' if len(self.emergency_contacts) > 1 else 'This is '} the emergency contacts for {self}:")
        for role, number in self.emergency_contacts.items():
            print (f"{role}: {number}")

    
    def get_info(self):
        os.system('cls')
        print(f"This {self} is Located at {self.location}, with the size of {self.size} sqm, has {self.floors} floors, and {self.total_units} units,.")
        draw_line()
        self.get_residents()
        draw_line()
        self.get_amenities()
        draw_line()
        self.get_pet_policy()
        draw_line()
        self.get_security_status()
        draw_line()
        self.get_emergency_contacts()
        draw_menu(["EDIT RESIDENTS", "EDIT AMENITIES", "EXIT"])
        choice = int_input("Enter Command: ")
        if choice == 1:
            os.system('cls')
            self.edit_item(self.residents_list, None, self.get_residents)
        elif choice == 2:
            os.system('cls')
            self.edit_item(self.amenities, None, self.get_amenities)
        elif choice == 3:
            return True


class Agricultural_Building(Building):
    def __init__(self):
        super().__init__()
        os.system('cls')
        
        print(f"Input the Properties for {self}")
        self.livestock_facilities = choice_input("Does the building have livestock facilities? (yes/no): ")

        if self.livestock_facilities: 
            self.livestocks = [item.strip().capitalize() for item in input("Enter the list of livestocks (comma-separated): ").split(", ")]
        
        self.equipment_storages = choice_input("Does the building have equipment storages? (yes/no): ")

        if self.equipment_storages:
            self.storage_units = [item.strip().capitalize() for item in input("Enter the list of storage units (comma-separated): ").split(", ")]
            self.equipment_list = [item.strip().capitalize() for item in input("Enter the list of equipment (comma-separated): ").split(", ")]
        
        self.crops = choice_input("Are there crops available? (yes/no): ")

        if self.crops:
            self.crop_list = [item.strip().capitalize() for item in input("Enter the list of crops (comma-separated): ").split(", ")]

    def __str__(self):
        return f"Agricultural Building"

    def get_storage(self):
        if self.livestock_facilities:
            print(f"Livestock facilities are available in {self}")
            print("Livestocks available are:")
            for livestock in self.livestocks:
                print(f"- {livestock}")
        else:
            print(f"Livestock facilities are unavailable in {self}")
    
    def get_crops(self):
        if self.crops:
            print(f"There are crops available in {self}")
            print("Here are the available crops:")
            for crop in self.crop_list:
                print(f"- {crop}")
        else:
            print(f"There are no available crops in {self}")

    def get_equipment_storage(self):
        if self.equipment_storages:
            print(f"Equipment storages are available in {self}")
            print("Here are the equipment storages available:")
            for storage_unit in self.storage_units:
                print(f"- {storage_unit}")
            print("Here are the available equipments:")
            for equipment in self.equipment_list:
                print(f"- {equipment}")
        else:
            print(f"There are no available storages and equipments in {self}")

    def get_info(self):
        os.system('cls')
        print(f"This {self} is Located at {self.location}, with the size of {self.size} sqm and has {self.floors} floors.")
        draw_line()
        print(f"{self} Resources:")
        draw_line()
        self.get_storage()
        draw_line()
        self.get_crops()
        draw_line()
        self.get_equipment_storage()
        draw_line()
        draw_menu(["EDIT LIVESTOCKS", "EDIT STORAGES", "EDIT EQUIPEMENTS", "EDIT CROPS", "EXIT"])
        choice = int_input("Enter Command: ")
        if choice == 1:
            os.system('cls')
            if self.livestock_facilities:
                self.edit_item(self.livestocks, None, self.get_storage)
            else:
                print(f"This {self} has no available Livestock Facilities")
                input("Press Enter to Continue:")
        elif choice == 2:
            os.system('cls')
            if self.equipment_storages:
                self.edit_item(self.storage_units, None, self.get_equipment_storage)
            else:
                print(f"This {self} has no available Equipment Storage")
                input("Press Enter to Continue:")
        elif choice == 3:
            os.system('cls')
            if self.equipment_storages:
                self.edit_item(self.equipment_list, None, self.get_equipment_storage)
            else:
                print(f"This {self} has no available Equipment Storage")
                input("Press Enter to Continue:")
        elif choice == 4:
            os.system('cls')
            if self.crops:
                self.edit_item(self.crop_list, None, self.get_crops)
            else:
                print(f"This {self} has no available Crops")
                input("Press Enter to Continue:")
        elif choice == 5:
            return True



class Warehouse(Building):
    def __init__(self):
        super().__init__()
        self.total_capacity = int(input("Enter the Total Capacity: "))
        self.current_load = 0
        self.storage_type = input("Enter the Type of Items to Store: ")
        self.item_list = {}

    def __str__(self):
        return "Warehouse"

    def add_item(self):
        while True:
            choice = None
            if self.current_load == self.total_capacity:
                draw_line()
                print("Maximum Warehouse Capacity has been Reached!")
                delete = choice_input("Do you wish to Remove some Items in order to proceed?: ")

                if delete:
                    print("Choose which Item/s to Delete:")
                    draw_menu(["Add Items", "Delete Items", "Exit"])
                    self.show_stocks()
                else: 
                    return

            item = input("Enter an Item: ").capitalize().strip()
            quantity = int(input("Enter the Item Quantity: "))

            if self.total_capacity >= (quantity + self.current_load):
                self.current_load += quantity

                if item in self.item_list:
                    self.item_list[item] += quantity
                else:
                    self.item_list[item] = quantity
                print(f"The {item} with the quantity of {quantity} has been added")
                print(f"Current Capacity: ({self.current_load}/{self.total_capacity})")

            else:
                print(f"The Addition of {item} will exceed the Total Capacity, Try Again!")
                print(f"Current Capacity: ({self.current_load})")

            if self.current_load < self.total_capacity:
                choice = choice_input("Add another Item? (yes/no): ") 

            draw_line()

            if not choice:
                return
            
    def get_stocks(self):
        draw_line()
        print(f"The {self} has the following in Stocks:")
        if self.item_list:
            print("Available Items in Stock: ")
            for i, (item, quantity) in enumerate(self.item_list.items(), start=1):
                print(f"[{i}] {item}: {quantity}")
            print(f"Current Capacity: ({self.current_load})")
        else:
            print("No Items Available")


    def remove_item(self):
        choice = int_input("Enter the Item Number to Delelte: ")

        if 1 <= choice <= len(self.item_list):
            item_to_delete = list(self.item_list.keys())[choice - 1]
            quantity_to_delete = int(self.item_list[item_to_delete])

            self.current_load -= quantity_to_delete

            del self.item_list[item_to_delete]
            print(f"{item_to_delete} has been deleted.")
        else:
            print("Invalid choice, try again.")

    def show_stocks(self):
        os.system('cls')
        print("STOCKS:")
        self.get_stocks() 
        draw_menu(["Add Items", "Delete Items", "Exit"])
            

        choice = int_input("Enter the Number of your Choice: ")
        if choice == 1:
            os.system('cls')
            self.add_item()
            return False

        elif choice == 2:
            self.remove_item()
            return False

        elif choice == 3:
            return True
        else:
            print("Enter a valid choice, try again!")

    def get_info(self):
        os.system('cls')
        print(f"This {self} is Located at {self.location}, with the size of {self.size} sqm and has {self.floors} floors")
        print(f"Total Capacity: {self.total_capacity} pcs")
        print(f"Storage Type: {self.storage_type}")
        self.get_stocks()
        draw_menu(["EXIT"])
        choice = input("Enter any key to Exit: ")
        if choice:
            return
               
            

def draw_line():
    print("----------------------------------------------------------------------------------------------------")

def draw_menu(options):
    draw_line()
    print("MENU:")
    for i, option in enumerate(options, start=1):
        print(f"\t\t[{i}] {option.ljust(15)}", end='\t\t')
        if i % 2 == 0:
            print()
    print() 
    draw_line()


def draw_main_screen():
    os.system('cls')
    draw_line()
    print("\t\t\t\t    Building Management System")
    draw_line()
    print("Choose the type of Building: ")
    draw_menu(["Industrial", "Residential", "Agricultural", "Warehouse"])



def choice_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response == "yes"
        elif response == "":
            print("Please choose a decision, Try Again")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def int_input(prompt):
    while True:
        try:
            value = int(input(prompt).replace(",", ""))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    industrial = None
    residential = None
    agricultural = None
    warehouse = None
    while True:
        draw_main_screen()
        choice = int_input("Enter Input: ")

        if choice == 1:
            if industrial is None:
                industrial = Industrial_Building()
            while True:
                exit_industrial_menu = industrial.get_info()
                if exit_industrial_menu:
                    break
            
        elif choice == 2:
            if residential is None:
                residential = Residential_Building()
            while True:
                exit_residential_menu = residential.get_info()
                if exit_residential_menu:
                    break
        elif choice == 3:
            if agricultural is None:
                agricultural = Agricultural_Building()
            while True:
                exit_agricultural_menu = agricultural.get_info()
                if exit_agricultural_menu:
                    break
        elif choice == 4:
            if warehouse is None:
                warehouse = Warehouse()
            while True:
                exit_stock_menu = warehouse.show_stocks()
                if exit_stock_menu:
                    break
            warehouse.get_info()

main()




