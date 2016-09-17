#!/usr/bin/env python
# coding: utf-8
__author__ = "Etanlink (just add your name when you add something)"
__copyright__ = "Copyright 2016, HackingGameProject"
__credits__ = ["Etanlink", "Nopest", "Tellen", "Thomas Bastos", "Jérémy"]
__version__ = "0.0"
__status__ = "Dev"

""" ClientMain.py: client side of HackingGameProject, it implements server connection,
data sending/receiving, contextual map, GUI, etc... """


class Machine:

    name = ""

    ipAddress = [4] # list of 4 elements, each element is in range 0-255

    login = ""

    password = ""

    ports = {"Port SSH": 22, "Port Web": 80, "etc ...": 0} # TODO : complete the ports dictionnary

    # Constructor
    def __init__(self):
        self.name = "Etanlink's Machine" # Example
        self.ipAddress = [255, 255, 255, 255] # Example
        self.login = "EtanlinkLeBG" # Example
        self.password = "32.5cm"  # Example


    # Create a Machine wit random attributes values - same method as constructor but with random values
    def randomMachineGeneration(self):
        return 0

    # Getters and setters to do for each attributes
    def getMachineName(self):
        return self.name

    def setMachineName(self, newName):
        self.name = newName

    # TODO


########################################################################################################
# PC inherits Machine class
class PC(Machine):

    # Attributes to add

    # Constructor
    def __init__(self):
        self.ipAddress = [0, 0, 0, 0] # Example
        self.name = "Etanlink's PC"  # Example
        self.ipAddress = [255, 255, 255, 255]  # Example
        self.login = "EtanlinkLeBG"  # Example
        self.password = "32.5cm"  # Example