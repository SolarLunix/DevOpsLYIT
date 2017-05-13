# Author: Melissa Melaugh
# Date Created: 10 August 2016
# Date Updated: 10 August 2016
# Description: This class is to register the user so that they can use the program.
# File: register
# Status: Completed

# Imports:
import datetime  # https://docs.python.org/3/library/datetime.html?highlight=time#module-datetime
import VM_12_pkg.global_functions


class Register:
    # Class Variables
    first_name = "Melissa"
    last_name = "Melaugh"
    company_name = "LYIT"
    date = ""

    def __int__(self):
        # Constructor
        self.date = datetime.date.today()
        # The following can be disabled for testing purposes:
        self.first_name = self.input_name("first")
        self.last_name = self.input_name("last")
        self.company_name = self.input_name("company")
    # End Constructor

    def input_name(self, a_str):
        # This asks a user to input a name based on a_str and returns the name if it is correct.
        while 1:
            # This while loop is here to ensure that the name is not left blank.
            # Further checks of the name can then be added here to make sure the name works, but is not required
            question = "Please enter your " + a_str + " name:\n"
            name = input(question)
            if len(name) >= 1 and VM_12_pkg.global_functions.is_correct(name):
                return name
            else:
                print("Error, no name entered.")
        # end name-check while loop
    # end input_name

    def user_message(self):
        message = "Today's date is {0}.\n\n Name: {1} {2} \nCompany name: {3}".format(self.date.strftime("%d, %B, %Y"),
                                                                                      self.first_name, self.last_name,
                                                                                      self.company_name)
        return message
# end Register Class
