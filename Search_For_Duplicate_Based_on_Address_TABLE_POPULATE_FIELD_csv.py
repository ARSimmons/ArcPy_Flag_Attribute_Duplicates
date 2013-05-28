###############################################
## Arielle Simmons                           ##
## Planner/GIS Specialist                    ##
## Pioneer Valley Planning Commission        ##
## Date created: November 29, 2010           ##
## Date modified: April 1, 2013              ##
###############################################

## This script searches for duplicates between
## different tables (and duplicates within
## a table) for a specific file geodatabase.

## Currently there are two hardpaths to set:

## 1) You MUST set the workspace (at the moment, this is intended to
## be a file gdb) in order to begin the search.
## 2) set a location for the output csv file (which
## is a print of the dictionary and the count
## of occurance for each duplicate)

## In this example, I am creating a dictionary that contains
## Address count pairs. 
## For the dictionary:
## the key is the field (in this case - Address)
## and the value is the count of occurance
## Within the feature classes, I want to populate a newly created
## field ("Duplicate") and label it yes/no if
## the row is found to be a duplicate.

# Import modules

import arcpy
import os
import sys
import csv
import string

from arcpy import env

# Set the workspace to the geodb with the duplicate feature classes

arcpy.env.workspace = r" "

# Overwrite pre-existing workspace
arcpy.env.overwriteOutput = True



try:
       # open an output csv file, must specify directory!

       f = open("  ", 'w')
       print f

       # pre-define the dictionary (Dictionary is a data structure w/ key value pairs)
       addressDictionary = dict()

       # declare a variable "DuplicateValue"
       # the "yes" statement populates the "Duplicate" field, if a duplicate is found

       DuplicateValue = "Y"

       # declare a variable "NotDuplicate"
       # the "no" statement populates the "Duplicate" field, if NO duplicate is found

       NotDuplicate = "N"

       fcs= arcpy.ListTables()

       # Build a dictionary that stores a count of occurances for each address (dict[address]:count)
       for fc in fcs:
              print fc
              

              rows = arcpy.SearchCursor(fc)

              # Move to the first row
              row = rows.next()

              # Make a list of all the address values in the Address field
              while row <> None:

              # Declare the field to search (i.e. row.___). Ignore any blank Address records
                     addressString = str(row.Address)
                     if addressString != ' ':

                            if addressString in addressDictionary.keys():
                                   addressDictionary[addressString] += 1
                            else:
                                   addressDictionary[addressString] = 1
                     
                     row = rows.next()

       # Delete cursor and row objects to remove locks on data
       del row, rows
                     
       # print the addressDictionary to the shell to verify that it ran okay
       print addressDictionary

       # print the addressDictionary to the csv
       for key in addressDictionary.keys():
              f.write(key + "," + str(addressDictionary[key]) + "\n")       
       f.close()

       
       # Basically repeats the above loop, but does so to populate the geodb
       # is the "yes"/"no" values
       for fc in fcs:

              # In order to flag duplicates, you need to create
              # a field. First, list all the fields in each feature class
              fieldList = arcpy.ListFields(fc)

              # Add the field to the feature class,
              # if it does not already exist
              UpdateField = "Duplicate"
              if not UpdateField in fieldList:
                     arcpy.AddField_management(fc, UpdateField, "text", "1")

              # To populate the field "Duplicate". Use the Update Cursor.
              rows = arcpy.UpdateCursor(fc)

              # Move to the first row
              row = rows.next()

              # Make a list of all the address values in the Address field
              # loop through the list till it reaches an end
              while row <> None:

                     # Declare the field to search (i.e. row.___).
                     addressString = str(row.Address)
                     # Ignore any blank Address record
                     if addressString != ' ' and addressString in addressDictionary.keys():
                            # check if there are duplicates by the dictionary value (aka count)
                            if addressDictionary[addressString] > 1:
                                   print fc + " " + "DUPLICATE" + " " + addressString

                            # Add a 'yes' to the "Duplicate" field in the geodatabase if
                            # the record is a duplicate.
                                   row.setValue(UpdateField,DuplicateValue)
                                   rows.updateRow(row)
                            
                            # Add a 'no' to the "Duplicate" field if it doesn't
                            # exist
                            else:
                                   print fc + " UNIQUE" + " " + addressString
                                   row.setValue(UpdateField,NotDuplicate)
                                   rows.updateRow(row)

                            row = rows.next()

# Delete cursor and row objects to remove locks on data
       del row, rows
                            
except arcpy.ExecuteError:

# get the geoprocessing error messages
       print arcpy.GetMessages(2)


