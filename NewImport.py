#!/usr/bin/python

import ExampleImport
import imp

print ("This is from the python file and not the module")

import ExampleImport
# NOTE that this import of the module will have
# no effect


# To reload a module in the same program
# we use the imp module reload method

imp.reload(ExampleImport)

# By virtue of this import
# this will again execute the print statement 
# that was a part of the ExampleImport Module



