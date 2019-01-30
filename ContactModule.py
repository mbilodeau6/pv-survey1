import csv
from enum import Enum

##########
class ContactColumn(Enum):
    Id = 0
    LastName = 1
    FirstName = 2
    PrimaryContact = 3
    Neighborhood = 4
    Address = 5
    Phone1 = 6 
    Phone2 = 7
    Email1 = 8
    Email2 = 9
    OnCourse = 10
    Own = 11
    Fulltime = 12
    Funding = 13
    Volunteer = 14
    Board = 15
    Officer = 16
    Committee = 17
    DateAdded = 18
    Notes = 19

##########
def LoadContacts(filename):
    allContacts = []

    with open(filename, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                lineCount += 1
            else:
                lineCount += 1
                allContacts.append(row)

    return allContacts

##########
def FindContact(email, contacts):
    i = 0;
    email = str.strip(str.lower(email))
    for contact in contacts:
        contactEmail1 = str.strip(str.lower(contact[ContactColumn.Email1.value]))
        contactEmail2 = str.strip(str.lower(contact[ContactColumn.Email2.value]))
        if (contactEmail1 == email or  contactEmail2 == email):
            return i;
        i += 1

    return -1

