class Patient(object):
    Patient.id_number = 0
    def __init__(self, name, allergies):
        self.id_number = Patient.id_number
        self.name = name
        self.allergies = allergies
        self.bed = bed
        Patient.id_number += 1

class Hospital(object):
    def __init__(self, patients, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, patient):
        if self.patients <= self.capacity:
            patients.append(patient)
    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds
    def discharge(self, id_number):
        for patient in self.patients:
            if patient.id_number == id_number:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_number:
                        bed["Available"] = True
                        break
                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged. Bed #{} now available.".format(patient.id, patient.bed_num)
        return "Patient not found."