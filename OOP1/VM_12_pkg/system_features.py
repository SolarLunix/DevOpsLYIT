# Author: Melissa Melaugh
# Description: This code gets information from the PC that it is running on
# Date: 18 July 2016
# Last updated: 11 August 2016
# status: Complete

# Imports
import platform  # https://docs.python.org/3.5/library/platform.html#module-platform
import sys  # https://docs.python.org/3/library/sys.html#module-sys


def print_features():
    system = {}
    system["system"], system["node"], system["release"], \
        system["version"], system["machine"], system["processor"] = platform.uname()
    path = sys.path
    if system["system"] == "Windows":
        service_pack = sys.getwindowsversion().service_pack
    else:
        service_pack = ""

    print("You are running {0} {1} {3} version {2}.".format(system["system"], system["release"], system["version"],
                                                            service_pack), end=" ", flush=True)
    print("Your processor is {0} and is running {1} with the node {2}.".format(system["processor"],
                                                                               system["machine"], system["node"]))
    print("The current path(s) is(are):")
    for i in range(0, len(path)):
        print("\t{}".format(path[i]))
# end print_features
