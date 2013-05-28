
<html>
<head>
</head>
<body>
# Table of Contents
[Team Members](#team-members)

[Project Summary](#project-summary)

# <a name="team-members"></a>Team Members
* "Arielle Simmons" <ari.ucb.fire@gmail.com>
	- Planner/GIS Specialist 
	[PVPC](http://www.pvpc.org/ "PVPC")
	
# <a name="project-summary"></a>Project Summary
Create 2 python scripts which search for explicit duplicates in a field called "Address".

The two scripts in this file are:

1)Search_For_Duplicate_Based_on_Address_TABLE_POPULATE_FIELD_csv.py

2)Search_For_Duplicate_Based_on_Address_FeatureClass_POPULATE_FIELD_csv.py

'..TABLE_POPULATE_FIELD_csv.py' looks, flags and prints to csv between different tables (and duplicates within
a table) for a specific file geodatabase.

'..FeatureClass_POPULATE_FIELD_csv.py' looks, flags and prints to csv between different feature classes (and duplicates within
a feature class) for a specific file geodatabase.

Using the [dictionary data structure](http://docs.python.org/2/tutorial/datastructures.html "dictionary data structure") in python I create a dictionary that contains Address count pairs. For the dictionary, the key is the field -- in this case, 'Address' -- and the value is the count of occurrence.

Within the feature classes/tables, I populate a newly created field ('Duplicate') and label it y/n if the tuple is found to be a duplicate. 

The dictionary also exports as .csv file for quick review.

...the Test_Data directory contains two FileGDB's that already have a field called 'Address' with duplicates that can be used to quickly test/review this code.


*THIS PROJECT IS FINISHED as of 4/1/2013*
 
</body>
</html>