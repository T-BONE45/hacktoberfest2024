class Patient:
    def __init__(self, patient_id, name, age, contact_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.contact_number = contact_number

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient_id, name, age, contact_number):
        patient = Patient(patient_id, name, age, contact_number)
        self.patients.append(patient)
        print(f"Patient {name} added successfully.")

    def add_doctor(self, doctor_id, name, specialty):
        doctor = Doctor(doctor_id, name, specialty)
        self.doctors.append(doctor)
        print(f"Doctor {name} added successfully.")

    def add_appointment(self, appointment_id, patient_id, doctor_id, date, time):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)
        if patient and doctor:
            appointment = Appointment(appointment_id, patient, doctor, date, time)
            self.appointments.append(appointment)
            print(f"Appointment for {patient.name} with {doctor.name} added successfully.")
        else:
            print("Invalid patient or doctor ID.")

    def display_patients(self):
        print("List of Patients:")
        for patient in self.patients:
            print(f"Patient ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Contact Number: {patient.contact_number}")

    def display_doctors(self):
        print("List of Doctors:")
        for doctor in self.doctors:
            print(f"Doctor ID: {doctor.doctor_id}, Name: {doctor.name}, Specialty: {doctor.specialty}")

    def display_appointments(self):
        print("List of Appointments:")
        for appointment in self.appointments:
            print(f"Appointment ID: {appointment.appointment_id}, Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date}, Time: {appointment.time}")


def main():
    hospital = HospitalManagementSystem()

    while True:
        print("\nHospital Management System Menu:")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Add Appointment")
        print("4. Display Patients")
        print("5. Display Doctors")
        print("6. Display Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            contact_number = input("Enter patient contact number: ")
            hospital.add_patient(patient_id, name, age, contact_number)
        elif choice == "2":
            doctor_id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            specialty = input("Enter doctor specialty: ")
            hospital.add_doctor(doctor_id, name, specialty)
        elif choice == "3":
            appointment_id = input("Enter appointment ID: ")
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date: ")
            time = input("Enter appointment time: ")
            hospital.add_appointment(appointment_id, patient_id, doctor_id, date, time)
        elif choice == "4":
            hospital.display_patients()
        elif choice == "5":
            hospital.display_doctors()
        elif choice == "6":
            hospital.display_appointments()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
