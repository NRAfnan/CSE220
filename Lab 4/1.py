# Assignment Part 1

# class Node:
#     def __init__(self, data, nxt, prev):
#         self.data = data


class Patient:

    def __init__(self, id=None, name=None, age=None, bloodgroup=None, nxt=None, prev=None, ):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
        self.next = nxt
        self.prev = prev


class WRM:

    def __init__(self):
        self.dummy_head = Patient(name="Dummy Head", nxt=None, prev=None)
        self.dummy_head.next = self.dummy_head
        self.dummy_head.prev = self.dummy_head
        self.tail = self.dummy_head

    def registerPatient(self, id, name, age, bloodgroup):
        patient_node = Patient(id, name, age, bloodgroup, nxt=self.dummy_head, prev=self.tail)

        self.tail.next = patient_node
        self.tail = self.tail.next
        self.dummy_head.prev = self.tail

        print("Success registering patient.")

    def servePatient(self):
        if self.dummy_head.next != self.dummy_head:
            patient_to_be_served = self.dummy_head.next
            next_patient = patient_to_be_served.next

            self.dummy_head.next = next_patient
            next_patient.prev = self.dummy_head

            print(f"{patient_to_be_served.name} is served.")
            patient_to_be_served.next = None
            patient_to_be_served.prev = None
            patient_to_be_served.id = None
            patient_to_be_served.name = None
            patient_to_be_served.age = None
            patient_to_be_served.bloodgroup = None

            if self.dummy_head.next == self.dummy_head:
                self.tail = self.dummy_head
        else:
            print("No patient to serve.")

    def showAllPatient(self):
        n = self.dummy_head.next
        if n != self.dummy_head:
            while n != self.dummy_head:
                if n.next != self.dummy_head:
                    print(n.id, end=" ")
                else:
                    print(n.id)
                n = n.next
        else:
            print("No patient remaining.")

    def canDoctorGoHome(self):
        if self.dummy_head.next != self.dummy_head:
            return "No."
        else:
            return "Yes."

    def cancelAll(self):
        if self.dummy_head.next != self.dummy_head:
            next_patient = self.dummy_head.next

            self.dummy_head.next = self.dummy_head
            self.dummy_head.prev = self.dummy_head

            while next_patient != self.dummy_head:
                temp = next_patient.next

                # Removing link
                next_patient.next = None
                next_patient.prev = None
                # Clear the data in the current node
                next_patient.id = None
                next_patient.name = None
                next_patient.age = None
                next_patient.bloodgroup = None

                # Move to the next node
                next_patient = temp

            self.tail = self.dummy_head
            print("All appointments are cancelled.")
        else:
            print("No patient appointments to cancel.")

    def ReverseTheLine(self):
        if self.dummy_head.next == self.dummy_head or self.dummy_head.next.next == self.dummy_head:
            print("No need to reverse.")
        else:
            count = self.countNode()
            current_node = self.dummy_head.next
            original_tail = current_node.prev.prev
            for i in range(count - 1):
                current_node = self.dummy_head.next
                next_node = current_node.next
                # tail = tail.prev

                original_tail.next = current_node
                current_node.prev = original_tail

                if i == 0:
                    current_node.next = self.dummy_head

                if i > 0:
                    tail.prev = current_node
                    current_node.next = tail

                tail = current_node

                if i == 0:
                    self.dummy_head.prev = tail

                self.dummy_head.next = next_node
                next_node.prev = self.dummy_head
            self.tail = self.dummy_head.prev

            print("Reversed the line.")

    # Counts the number of Nodes in the list and return the number
    def countNode(self):
        dummy_head = self.dummy_head
        count = 0
        temp = self.dummy_head.next
        while temp != dummy_head:
            count += 1
            temp = temp.next
        return count


# Write a Tester Code in this cell
# wrm1 = WRM()
# print("**Welcome to Waiting Room Management System**")
# while True:
#     print("==Choose an Option==")
#     print("1. RegisterPatient()")
#     print("2. ServePatient()")
#     print("3. ShowAllPatient()")
#     print("4. CanDoctorGoHome()")
#     print("5. CancelAll()")
#     print("6. ReverseTheLine()")
#     print("7. Exit")
#     print("=====================")
#     user_input = int(input("Enter your choice: "))
#     if user_input == 1:
#         print("Executing RegisterPatient()...")
#         up_id = input("Enter ID: ")
#         up_name = input("Enter Name: ")
#         up_age = int(input("Enter Age: "))
#         up_bloodgroup = input("Enter Blood group: ")
#         wrm1.registerPatient(up_id, up_name, up_age, up_bloodgroup)
#     elif user_input == 2:
#         wrm1.servePatient()
#     elif user_input == 3:
#         wrm1.showAllPatient()
#     elif user_input == 4:
#         print(wrm1.canDoctorGoHome())
#     elif user_input == 5:
#         wrm1.cancelAll()
#     elif user_input == 6:
#         wrm1.ReverseTheLine()
#     elif user_input == 7:
#         print("Thank you for using Waiting Room Management system.")
#         print("Exiting...")
#         break
#     else:
#         print("No such option.")


# Write a Tester Code in this cell
patients1 = {"Patient 1": [1, "abc", 34, "B+"],
             "Patient 2": [2, "Gojo", 54, "A+"],
             "Patient 3": [3, "Geto", 24, "B-"]}

patients2 = {"Patient 4": [4, "Tanjiro", 94, "AB+"],
             "Patient 5": [5, "Eren", 14, "A-"],
             "Patient 6": [6, "Naruto", 104, "0-"]}

print("**Welcome to Waiting Room Management System**")
print("==========Case 1==========")
wr = WRM()
wr.servePatient()
wr.showAllPatient()
print(wr.canDoctorGoHome())
wr.cancelAll()
wr.ReverseTheLine()
print("==========Case 2==========")
wr1 = WRM()
wr1.registerPatient(patients1["Patient 1"][0], patients1["Patient 1"][1], patients1["Patient 1"][2], patients1["Patient 1"][3])
wr1.showAllPatient()
print(wr1.canDoctorGoHome())
wr1.ReverseTheLine()
wr1.servePatient()
wr1.showAllPatient()
print(wr1.canDoctorGoHome())
wr1.cancelAll()
print("==========Case 3==========")
wr1 = WRM()
wr1.registerPatient(patients1["Patient 1"][0], patients1["Patient 1"][1], patients1["Patient 1"][2], patients1["Patient 1"][3])
wr1.registerPatient(patients1["Patient 2"][0], patients1["Patient 2"][1], patients1["Patient 2"][2], patients1["Patient 2"][3])
wr1.registerPatient(patients1["Patient 3"][0], patients1["Patient 3"][1], patients1["Patient 3"][2], patients1["Patient 3"][3])
wr1.showAllPatient()
print(wr1.canDoctorGoHome())
wr1.ReverseTheLine()
wr1.servePatient()
wr1.showAllPatient()
print(wr1.canDoctorGoHome())
wr1.cancelAll()
print(wr1.canDoctorGoHome())
print("==========Case 4==========")
wr1 = WRM()
wr1.registerPatient(patients1["Patient 1"][0], patients1["Patient 1"][1], patients1["Patient 1"][2], patients1["Patient 1"][3])
wr1.registerPatient(patients1["Patient 2"][0], patients1["Patient 2"][1], patients1["Patient 2"][2], patients1["Patient 2"][3])
wr1.registerPatient(patients1["Patient 3"][0], patients1["Patient 3"][1], patients1["Patient 3"][2], patients1["Patient 3"][3])
wr1.showAllPatient()
wr1.ReverseTheLine()
wr1.registerPatient(patients2["Patient 4"][0], patients2["Patient 4"][1], patients2["Patient 4"][2], patients2["Patient 4"][3])
wr1.registerPatient(patients2["Patient 5"][0], patients2["Patient 5"][1], patients2["Patient 5"][2], patients2["Patient 5"][3])
wr1.registerPatient(patients2["Patient 6"][0], patients2["Patient 6"][1], patients2["Patient 6"][2], patients2["Patient 6"][3])
wr1.showAllPatient()
wr1.ReverseTheLine()
wr1.showAllPatient()
wr1.servePatient()
print(wr1.canDoctorGoHome())
wr1.cancelAll()
wr1.showAllPatient()
print(wr1.canDoctorGoHome())