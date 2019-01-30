import csv
from ContactModule import FindContact, ContactColumn, LoadContacts
from SurveyModule import SurveyColumn, LoadSurvey, GetSurveyData, SaveSurvey
from UtilityMethods import IdentifyDuplicates


##########
print("Loading contacts...")
allContacts = LoadContacts("C:\src\PVData\ContactList.csv")
print(f"Loaded {len(allContacts)} contacts")

#for contact in allContacts:
#    print(f"Notes: {contact[contactColumnIndexes['Notes']]}")

#########
print("Loading survey results...")
allResults = LoadSurvey("C:\src\PVData\SurveyResults.csv")
print(f"Loaded {len(allResults)} survey results")

foundCount = 0
notFoundCount = 0

for result in allResults:
    contactIndex = FindContact(result[SurveyColumn.Email.value], allContacts)
    if (contactIndex >= 0):
        #print(f"{result[SurveyColumn.Email.value]} - Found")
        foundCount += 1
    else:
        print(f"{result[SurveyColumn.Email.value]} - NotFound")
        notFoundCount += 1

print(f"Found: {foundCount}; Not Found: {notFoundCount}")

allSurveyData = []

for result in allResults:
    contactIndex = FindContact(result[SurveyColumn.Email.value], allContacts)

    if contactIndex >= 0:
        matchingContact = allContacts[contactIndex]
    else:
        matchingContact = []

    allSurveyData.append(GetSurveyData(result, matchingContact))

SaveSurvey("C:\src\PVData\SurveyResultsCleaned.csv", allSurveyData)

