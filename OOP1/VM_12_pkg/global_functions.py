# Author: Melissa Melaugh
# Date Created: 11 July 2016
# Date Updated: 11 August 2016
# Description: The functions contained here are essential for multiple classes, in versions 10 and before this was
#   simply called functions, and included functions that were moved to the VM_CREATE class.
# File: global_functions
# Status: complete


def pick_choice(a_str, a_list):
    # This function displays a list for the user to chose from, and ensures that the option is valid
    while 1:
        print("Your options for {} are as follows:".format(a_str))

        # Print the options
        for i in range(0, len(a_list)):
            print("\t{0}: {1}".format(i, a_list[i]))
        # end for loop for printing options

        # Ask user for their choice
        ans = input("Please input the number of your choice: \n")
        choice = len(a_list) + 1

        # Parse their answer into a numeral
        try:
            choice = int(ans)
        except ValueError:
            print("Invalid choice")
        # end try except statement

        # Return the value of their choice if it is correct
        if (choice >= 0) and (choice < len(a_list)) and (is_correct(a_list[choice])):
            return choice
    # end while loop
# end pick_choice


def pick_choice_dic(a_str, a_list):
    # This function displays a list for the user to chose from, and ensures that the option is valid same as above, but
    # is designed for use with a dictionary
    while 1:
        print("Your options for {} are as follows:".format(a_str))

        # Print the options
        for i in range(0, len(a_list)):
            print("\t{0}: {1}".format(i, a_list[i]["name"]))
        # end for loop for printing options

        # Ask user for their choice
        ans = input("Please input the number of your choice: \n")
        choice = len(a_list) + 1

        # Parse their answer into a numeral
        try:
            choice = int(ans)
        except ValueError:
            print("Invalid choice")
        # end try except statement

        # Return the value of their choice if it is correct
        if (choice >= 0) and (choice < len(a_list)) and (is_correct(a_list[choice]["name"])):
            return a_list[choice]
    # end while loop
# end pick_choice_dic


def is_correct(a_str):
    # Asks a user if the choice they gave is the one they want.
    while 1:
        # This while loop just makes sure that they answer either Y or N to the question
        question = "You input: \n\t" + a_str + "\nIs this correct? Y/N\n"
        ans = input(question)

        if ans.upper() == "Y":
            return True
        elif ans.upper() == "N":
            return False
        else:
            print("Invalid entry, please try again.")
    # end while loop
# end is_correct


def update_str(a_str):
    # This function is to update a string to make sure that
    while 1:
        question = "Please input " + a_str + ".\n"
        ans = input(question)

        # Check if they input it correctly
        if is_correct(ans):
            return ans
        # else return to top of while loop
# end update_str