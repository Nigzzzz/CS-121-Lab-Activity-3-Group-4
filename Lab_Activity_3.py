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

class Residential_Building(Building):
    def __init__(self, name, location, size, floors, number_of_units, residents, amenities, pet_friendly, has_security, emergency_contacts):
        super().__init__(name, location, size, floors)
        self.number_of_units = number_of_units
        self.residents = residents
        self.amenities = amenities
        self.pet_friendly = pet_friendly
        self.has_security = has_security
        self.emergency_contacts = emergency_contacts

    def get_residents(self):
        print(f"Residents in {self.name}:")
        for resident in self.residents:
            print(f"- {resident}")

    def get_amenities(self):
        print(f"Amenities in {self.name}:")
        for amenity in self.amenities:
            print(f"- {amenity}")

    def get_pet_policy(self):
        if self.pet_friendly:
            print(f"{self.name} is pet-friendly. Pets are allowed, but only common domestic animals like cats or dogs.")
        else:
            print(f"{self.name} is not pet-friendly. Pets are not allowed at all.")

    def get_security_status(self):
        if self.has_security:
            print(f"Security personnel are present in {self.name}.")
        else:
            print(f"No security personnel in {self.name}.")

    def get_emergency_contacts(self):
        print(f"Emergency contacts for {self.name}:")
        for role, number in self.emergency_contacts.items():
            print(f"{role}: {number}")

    def building_function(self):
        if self.door_open:
            print(f"{self.name} is a residential building located in {self.location}.")
            print(f"It has {str(self.floors)} floors, {str(self.number_of_units)} units, and a size of {self.size} square meters.")
        else:
            print("Open the doors first.")

residential_building2 = Residential_Building(
    "Tagaytay Prime Residences", "Tagaytay City", "12,000", 23, 300,
    ["John", "Maria", "Chris", "Sofia", "David", "Emma"],
    ["Outdoor Swimming Pool", "Viewing Deck", "Restaurant", "Coffee House",
     "Minimarket", "Hair/Beauty Salon", "Terrace", "Balcony",
     "Flat-screen TV", "Elevator Access", "Air Conditioning"],
    False,
    True,
    {"Fire Department": "0946-483-1193", "Maintenance": "0927-123-4567"}
)
residential_building2.building_function()
residential_building2.open_doors()
residential_building2.get_residents()
residential_building2.get_pet_policy()
residential_building2.get_emergency_contacts()
residential_building2.get_amenities()
residential_building2.get_security_status()
residential_building2.building_function()
residential_building2.close_doors()

       




