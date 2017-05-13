# Author: Melissa Melaugh
# Date Created: 11 July 2016
# Date Updated: 10 August 2016
# Description: This class is used to create a single Virtual Machine object.
# File: vm_create
# Status: Complete

# Imports:
import VM_12_pkg.global_functions
import VM_12_pkg.vm_lists
import datetime  # https://docs.python.org/3/library/datetime.html?highlight=time#module-datetime


class VmCreate:
    # Class Variables
    os = ""
    os_min = {}
    ram = {}
    hard_drive = {}
    cpu = {}
    features = []
    date = ""
    start = "start date for VM to run"
    end = "end date for VM to run"
    options = VM_12_pkg.vm_lists.vm_options  # Option lists for: 0-Operating System, 1-Hard Drive, 2-CPU, 3-Ram

    def __int__(self, a_name_str, a_date):
        # Constructor.
        # a_name_str should be a string of the first name from the user object,
        # a_date should be a date object of today's date
        print("Hello, {}, let's create your Virtual Machine.".format(a_name_str))
        self.date = a_date
        self.start = self.create_date("Start", self.date)
        self.end = self.create_date("End", self.start)
        self.os_min = self.make_choice(0, "Operating System")
        self.os = self.os_min["name"]
        self.hard_drive = self.make_choice(1, "Hard Drive")
        self.cpu = self.make_choice(2, "CPU")
        self.ram = self.make_choice(3, "Ram")
        self.add_features()
    # end constructor

    def create_date(self, a_str, date_after):
        # This is used to create a date based on the a_str (which will give instruction to what date is wanted)
        # date_after is used to ensure that the date created is in order.
        while 1:
            # This while loop helps make sure the user enters a valid date object.
            question = "Please input the day you want your virtual machine to " + a_str + ". Format: DD/MM/YYYY \n"
            date = input(question)
            final_date = datetime.date.today()  # Default to today to avoid fails of the if statement further down
            created = False  # Check to see if the user created a date correctly, changes to true when object created

            try:
                # Attempts to split user input into the day, month, year ints for processing
                da, mo, ye = map(int, date.split("/"))
                final_date = datetime.date(int(ye), int(mo), int(da))  # creates a date value using the split date
                created = True
            except ValueError:
                print("Invalid date entry.")

            # checks that the date is after the specified date, and that the object had been created properly
            if final_date >= date_after and created:
                date_str = "{0} date: {1}".format(a_str, final_date.strftime("%d, %B, %Y"))
                if VM_12_pkg.global_functions.is_correct(date_str):
                    return final_date
            elif created:
                # checks that the date was created properly so multiple errors are not needlessly printed
                print("Date is too soon.")
            # end date check if statement
        # end date create while loop
    # end create_date

    def make_choice(self, an_int, a_str):
        # This function allows the user to make a choice from the options provided
        a_list = self.options[an_int]
        if a_str == "Operating System":
            # Because there are no minimums to test against, the OS is checked on its own.
            choice = VM_12_pkg.global_functions.pick_choice_dic(a_str, a_list)
        else:
            while 1:
                # this loop makes sure that the user choice is the correct size for the desired os
                choice = VM_12_pkg.global_functions.pick_choice_dic(a_str, a_list)
                check = self.check_min(self.os_min[a_str], choice)
                if check:
                    break
            # end choice loop
        return choice
    # end make_choice

    def check_min(self, a_min, choice):
        # makes sure that the feature selected can work with the minimum system requirements
        if choice["size"] >= a_min:
            return True
        else:
            return False
    # end check_min

    def add_features(self):
        # This allows the user to add multiple features to their system
        while 1:
            # This allows the user to add multiple features to their system
            choice = VM_12_pkg.global_functions.pick_choice("creating your Virtual Machine", ["Add a feature",
                                                                                              "Save and return to "
                                                                                              "main menu"])
            if choice == 1:
                print("Virtual Machine saved. Returning to main menu.")
                break
            else:
                self.features.append(VM_12_pkg.global_functions.update_str("a feature description and then hit enter"))
    # end add_features

    def display_vm(self):
        message = ""
        message += "\n\tStart Date: {}".format(self.start.strftime("%d, %B, %Y"))
        message += "\n\tEnd Date: {}".format(self.end.strftime("%d, %B, %Y"))
        message += "\n\tOperating system: {}".format(self.os)
        message += "\n\tHard Drive: {}".format(self.hard_drive["name"])
        message += "\n\tRam: {}".format(self.hard_drive["name"])
        message += "\n\tCPU: {}".format(self.cpu["name"])
        count = len(self.features)
        if count > 0:
            for i in range(0, count):
                message += "\n\tFeature {0}: {1}".format((i+1), self.features[i])
        else:
            message += "\n\tNo extra features added."
        return message
# end VmCreate class
