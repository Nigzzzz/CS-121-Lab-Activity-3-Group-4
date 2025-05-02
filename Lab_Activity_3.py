from abc import ABC, abstractmethod
class Building(ABC):
    def __init__(self, name, location, size, floors):
        self.name = name
        self.location = location
        self.size = size
        self.floors = floors
        self.door_open = False
    
    def open_doors(self):
        if not self.door_open:
            self.door_open = True
            print(f"The door at the {self.name} is now open.")
        else:
            print(f"The door at the {self.name} is already open.")
    
    def close_doors(self):
        if self.door_open:
            self.door_open = False
            print(f"The door at the {self.name} is now closed.")
        else:
            print(f"The door at the {self.name} is already closed.")
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_size(self):
        return self.size
    
    def get_floors(self):
        return self.floors
    
    @abstractmethod
    def building_function(self):
        pass

class Industrial_Building(Building):
    def __init__(self, name, location, size, floors, machinery_list, has_lab, lab_type, equipment_list):
        super().__init__(name, location, size, floors)
        self.machinery_list = machinery_list
        self.lab_type = lab_type
        self.equipment_list = equipment_list
        self.has_lab = has_lab

    def get_lab(self):
        if self.has_lab:
            print(f"{self.name} has a {self.lab_type} lab.")
            print("Equipment(s) in the lab:")
            for equipment in self.equipment_list:
                print(f"- {equipment}")
        else:
            print(f"{self.name} does not have a lab.")

    def get_machinery(self):
        print(f"{self.name} has the following machinery:")
        for machinery in self.machinery_list:
            print(f"- {machinery}")

    def building_function(self):
        machinery_names = ", ".join(self.machinery_list)
        lab = f"It includes a {self.lab_type} lab." if self.has_lab else "It does not include a lab."
        building = (f"{self.name} is an industrial building located at {self.location}. It has a size of {self.size} square meters and consists of {self.floors} floors. It contains the following machinery: \n{machinery_names}. {lab}")
        if self.door_open:
            print(building)
        else:
            print("Open the doors first")
    

industrial_building1 = Industrial_Building("Gabb Building", "Ibaan", "100,000", 5, ["Hydraulic Press", "Forge"], True, "Chemical", ["Spectrometer", "Tensile Tester"])
industrial_building1.building_function()
industrial_building1.open_doors()
industrial_building1.get_machinery()
industrial_building1.get_lab()
industrial_building1.building_function()
industrial_building1.close_doors()


       




