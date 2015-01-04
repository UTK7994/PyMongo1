import time
import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from datetime import datetime

try:
    c = Connection(host="localhost", port=27017)
except ConnectionFailure,e:
	print "\t\t\t\t\t======================================"
	print "\t\t\t\t\t       NO CONNECTION!!! :-(           "
	print "\t\t\t\t\t======================================"
	sys.exit(1)

db=Connection().buga
collection=db.Student_information


print "\t\t\t\t=========================================================================="
print "\t\t\t\t||WELOCOME TO CONSOLE CONTROLLED STUDENT INFORMATION SYSTEM OF BIG-DATA ||"
print "\t\t\t\t=========================================================================="
print "\t\t\t\t\t\t\tCONNECTED SUCCESSFULLY"
if (input("Drop the existing database 1/0\n")):
    collection.drop()

print "====================WELCOME TO THE MONGO-----CRUD================================="

print "MENU\n1   Insert a record\n2   Read a record\n3   Update a record\n4   Delete a record\n5   EXIT"
choice=input("Choice.... ");

while(choice!=5):
	if(choice==1):
	    collection.insert({"fn":raw_input("enter First name>>??  "),"mn":raw_input("Enter the middle name  "),"ln":raw_input("enter last name>>??  "),"rn":raw_input("enter ur roll_no>>??  "),"Semester":raw_input("enter semester  "),"Branch":raw_input("Branch CSE EE ME  ")})
	if(choice==2):
		results = db.Student_information.find()
		print()
		print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
		for record in results:
			print "FisrtName:  "+record['fn']+"\n"+"MiddleName: "+record['mn']+"\n"+"LastName:   "+record['ln']+"\n"+"RollCall:   "+record['rn']+"\n"+"Semester:   "+record['Semester']+"\n"+"Branch:     "+record['Branch']+"\n"
	if(choice==3):
		roll=raw_input("Enter the RollCall of the stud!! ")
		results=db.Student_information.find({'rn':roll})
		if(results!=None):
			print "INITIAL RECORD"
			for record in results:
				print "FisrtName:  "+record['fn']+"\n"+"MiddleName: "+record['mn']+"\n"+"LastName:   "+record['ln']+"\n"+"RollCall:   "+record['rn']+"\n"+"Semester:   "+record['Semester']+"\n"+"Branch:     "+record['Branch']+"\n"
			choice=input("Enter the options you wanna update \n1-> FisrtName  2-> MiddleName  3->LastName  4->roll_no   5->Semester    6->Branch")
			if(choice==1):
				db.Student_information.update( { 'rn':roll},{'$set': {'fn':raw_input("Enter the updated First name ")}})
			if(choice==2):
				db.Student_information.update( { 'rn':roll},{'$set': {'mn':raw_input("Enter the updated Middle name ")}})
			if(choice==3):
				db.Student_information.update( { 'rn':roll},{'$set': {'ln':raw_input("Enter the updated Last name ")}})
			if(choice==4):
				db.Student_information.update( { 'rn':roll},{'$set': {'rn':raw_input("Enter the updated Roll number ")}})
			if(choice==5):
				db.Student_information.update( { 'rn':roll},{'$set': {'Semester':raw_input("Enter the updated Semester ")}})
			if(choice==6):
				db.Student_information.update( { 'rn':roll},{'$set': {'Branch':raw_input("Enter the updated Branch ")}})
			results=db.Student_information.find({'rn':roll})
			print "UPDATED RECORD"
			for record in results:
				print "FisrtName:  "+record['fn']+"\n"+"MiddleName: "+record['mn']+"\n"+"LastName:   "+record['ln']+"\n"+"RollCall:   "+record['rn']+"\n"+"Semester:   "+record['Semester']+"\n"+"Branch:     "+record['Branch']+"\n"
	if(choice==4):
		roll=raw_input("Enter the RollCall of the stud!! ")
		db.Student_information.remove({'rn':roll})
	print "MENU\n1   Insert a record\n2   Read a record\n3   Update a record\n4   Delete a record\n5   EXIT"
	choice=input("Choice.... ");

print "\t\t\t\t\t====================================================="
print "\t\t\t\t\t||Good Bye!!!! and THANKS FOR USING THE SIS ver--1.0||"
print "\t\t\t\t\t====================================================="
