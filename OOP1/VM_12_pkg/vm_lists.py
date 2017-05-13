# Author: Melissa Melaugh
# Date Created: 11 July 2016
# Date Updated: 10 August 2016
# Description: These lists are created for the VM_CREATE class. This class was called lists in versions 10 and previous
# File: vm_lists
# Status: Complete

# This is the list of Operating system options, ending by combining them into one list. Includes minimum requirements.
# Remember to add any new options to the options list.
windows_10_32 = {"name": "Windows 10 32 bit",
                 "Ram": 1,
                 "Hard Drive": 16,
                 "CPU": 1}
windows_10_64 = {"name": "Windows 10 64 bit",
                 "Ram": 2,
                 "Hard Drive": 16,
                 "CPU": 1}
windows_7_32 = {"name": "Windows 7 32 bit",
                "Ram": 1,
                "Hard Drive": 16,
                "CPU": 1}
windows_7_64 = {"name": "Windows 7 64 bit",
                "Ram": 2,
                "Hard Drive": 16,
                "CPU": 1}
os_min = (windows_10_32, windows_10_64, windows_7_32, windows_7_64)


# This is the list of Ram options, ending by combining them into one list.
# Remember to add any new options to the options list.
ram_1 = {"name": "1 GB", "size": 1}
ram_2 = {"name": "2 GB", "size": 2}
ram_3 = {"name": "4 GB", "size": 4}
ram_4 = {"name": "6 GB", "size": 6}
ram_5 = {"name": "8 GB", "size": 8}
ram_6 = {"name": "16 GB", "size": 16}
ram_7 = {"name": "32 GB", "size": 32}
ram_options = (ram_1, ram_2, ram_3, ram_4, ram_5, ram_6, ram_7)


# This is the list of Hard Drive options, ending by combining them into one list.
# Remember to add any new options to the options list.
disk_1 = {"name": "10 GB Hard Drive", "size": 10}
disk_2 = {"name": "10 GB Solid State Drive", "size": 10}
disk_3 = {"name": "50 GB Hard Drive", "size": 50}
disk_4 = {"name": "50 GB Solid State Drive", "size": 50}
disk_5 = {"name": "100 GB Hard Drive", "size": 100}
disk_6 = {"name": "100 GB Solid State Drive", "size": 100}
disk_7 = {"name": "500 GB Hard Drive", "size": 500}
disk_8 = {"name": "500 GB Solid State Drive", "size": 500}
disk_9 = {"name": "1000 GB Hard Drive", "size": 1000}
disk_10 = {"name": "1000 GB Solid State Drive", "size": 1000}
disk_options = (disk_1, disk_2, disk_3, disk_4, disk_5, disk_6, disk_7, disk_8, disk_9, disk_10)


# This is the list of CPU options, ending by combining them into one list.
# Remember to add any new options to the options list.
cpu_1 = {"name": "1 GHz", "size": 1}
cpu_2 = {"name": "2 GHz", "size": 2}
cpu_3 = {"name": "2.2 GHz", "size": 2.2}
cpu_4 = {"name": "2.4 GHz", "size": 2.4}
cpu_5 = {"name": "3 GHz", "size": 3}
cpu_6 = {"name": "4 GHz", "size": 4}
cpu_options = (cpu_1, cpu_2, cpu_3, cpu_4, cpu_5, cpu_6)


# This list should be updated only if a new list (i.e. Monitor) is created. Then please update comment in vm_create
vm_options = [os_min,
              disk_options,
              cpu_options,
              ram_options]
