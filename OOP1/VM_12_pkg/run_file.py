# Author: Melissa Melaugh
# Date Created: 11 July 2016
# Date Updated: 08 August 2016
# Description: The main file to run the VM Package, version 11 - previously called "main" in versions 10 and before
# File: run_file
# Status: Complete

# Imports
import VM_12_pkg.global_functions
import VM_12_pkg.vm_create
import VM_12_pkg.register
import VM_12_pkg.system_features
import VM_12_pkg.server
import VM_12_pkg.dir_control
import copy  # https://docs.python.org/3/library/copy.html?highlight=copy#module-copy
import threading

# Variables
options = ["Quit",
           "Create a virtual machine",
           "Display ordered virtual machines",
           "Read system information",
           "Check the size of a directory",
           "Back up a directory"]

# Code
print("Welcome.")

user = VM_12_pkg.register.Register()
user.__int__()
vms = []
display = "This is a string"

while 1:
    # Have the user chose an option
    run = VM_12_pkg.global_functions.pick_choice("this program", options)

    # run the user option
    if run == 0:
        break
    elif run == 1:
        vm = VM_12_pkg.vm_create.VmCreate()
        vm.__int__(user.first_name, user.date)
        vms.append(copy.deepcopy(vm))
    elif run == 2:
        display = user.user_message()
        num_vms = len(vms)
        if num_vms > 0:
            for i in range(0, num_vms):
                display += "\n\n Virtual Machine number " + str(i+1) + ": " + vms[i].display_vm()
        else:
            display += "\n\nNo Virtual Machines to Display"
        VM_12_pkg.server.web_message = display
        VM_12_pkg.server.run()
    elif run == 3:
        VM_12_pkg.system_features.print_features()
    elif run == 4:
        # ask user for a directory to pass into the function.
        folder = VM_12_pkg.global_functions.update_str("a directory")
        # check if it is a working directory
        direct, check = VM_12_pkg.dir_control.open_dir(folder)
        if check:
            VM_12_pkg.dir_control.check_size(direct, 0)
    elif run == 5:
        # ask user for a directory to back up
        folder = VM_12_pkg.global_functions.update_str("the directory you want to back up")
        # check if it's a working directory
        direct, check = VM_12_pkg.dir_control.open_dir(folder)
        # ask user where to save the back up to
        folder = VM_12_pkg.global_functions.update_str("the directory you want your zip saved to")
        # check if it's a working directory
        save, check2 = VM_12_pkg.dir_control.open_dir(folder)
        # if both are working directories, back up the folder.
        if check and check2:
            a_thread = threading.Thread(target=VM_12_pkg.dir_control.back_up(save, direct), args=(10, 'a_thread'))
            a_thread.start()
            a_thread.join()
    # end running user options

    input("\nHit enter to continue.")
# end main program


print("\nGoodbye, {}.".format(user.first_name))
# end run file
