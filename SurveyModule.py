import csv
from enum import Enum
from ContactModule import ContactColumn

class SurveyColumn(Enum):
    Timestamp = 0
    Resident = 1
    HomeCount = 2
    Neighborhoods = 3
    OnCourse = 4
    ResideMonths = 5
    Email = 6
    PropertyUses = 7
    Concerns = 8
    UseGolf18Hole = 9
    UseGolfSmallCourse = 10
    UseOpenSpace = 11
    UsePark = 12
    UsePublic = 13
    LimitedDevelopment = 14
    DevelopmentViewsSpace = 15
    FullDevelopment = 16
    BuyProperty = 17
    FinanceUses = 18
    Comments = 19	
    
class SurveyDataColumn(Enum):
    Id = 0
    LastName = 1
    FirstName = 2
    Timestamp = 3
    Resident = 4
    HomeCount = 5
    Neighborhoods = 6
    OnCourse = 7
    ResideMonths = 8
    Email = 9
    PreferUseWalking = 10
    PreferUseRunning = 11
    PreferUseBiking = 12
    PreferUseBird = 13
    PreferUseGolf = 14
    PreferUsePreservation = 15
    PreferUseOther = 16
    ConcernPropertyValues = 17
    ConcernTraffic = 18
    ConcernNoise = 19
    ConcernFees = 20
    ConcernWildlife = 21
    ConcernViews = 22
    ConcernRecreation = 23
    ConcernOther = 24
    UseGolf18Hole_SA = 25
    UseGolf18Hole_A = 26
    UseGolf18Hole_N = 27
    UseGolf18Hole_D = 28
    UseGolf18Hole_SD = 29
    UseGolfSmallCourse_SA = 30
    UseGolfSmallCourse_A = 31
    UseGolfSmallCourse_N = 32
    UseGolfSmallCourse_D = 33
    UseGolfSmallCourse_SD = 34
    UseOpenSpace_SA = 35
    UseOpenSpace_A = 36
    UseOpenSpace_N = 37
    UseOpenSpace_D = 38
    UseOpenSpace_SD = 39
    UsePark_SA = 40
    UsePark_A = 41
    UsePark_N = 42
    UsePark_D = 43
    UsePark_SD = 44
    UsePublic_SA = 45
    UsePublic_A = 46
    UsePublic_N = 47
    UsePublic_D = 48
    UsePublic_SD = 49
    LimitedDevelopment_SA = 50
    LimitedDevelopment_A = 51
    LimitedDevelopment_N = 52
    LimitedDevelopment_D = 53
    LimitedDevelopment_SD = 54
    DevelopmentViewsSpace_SA = 55
    DevelopmentViewsSpace_A = 56
    DevelopmentViewsSpace_N = 57
    DevelopmentViewsSpace_D = 58
    DevelopmentViewsSpace_SD = 59
    FullDevelopment_SA = 60
    FullDevelopment_A = 61
    FullDevelopment_N = 62
    FullDevelopment_D = 63
    FullDevelopment_SD = 64
    BuyProperty_SA = 65
    BuyProperty_A = 66
    BuyProperty_N = 67
    BuyProperty_D = 68
    BuyProperty_SD = 69
    FinanceUse18Hole = 70
    FinanceUseSmallGolf = 71
    FinanceUseNoPath = 72
    FinanceUseWithPath = 73
    FinanceUsePark = 74
    FinanceUseNone = 75
    Comments = 76

#######
correctedEmails = [
    {"ProvidedEmail": "ghansen13@comcast", "ActualEmail": "ghansen13@comcast.net"},
    {"ProvidedEmail": "ridge004@tc.umn.edu", "ActualEmail": "ridge004@umn.edu"},
    {"ProvidedEmail": "Samhalgren@comcast.com", "ActualEmail": "samhalgren@comcast.net"},
    {"ProvidedEmail": "Marialynn48@ Gmail.com", "ActualEmail": "marialynn48@gmail.com"},
    {"ProvidedEmail": "deeemsortega@gmail.com", "ActualEmail": "deemsortega@gmail.com"}
]

def GetCorrectEmail(email):
    for correction in correctedEmails:
        if correction["ProvidedEmail"] == email:
            return correction["ActualEmail"]

    return email

#####
def FixResult(result):
    if result[SurveyColumn.Neighborhoods.value] == "SIENA":
        result[SurveyColumn.Neighborhoods.value] = "Siena"

    if result[SurveyColumn.Neighborhoods.value] == "Fairfield @ Rancho Vistoso" or result[SurveyColumn.Neighborhoods.value] == "yes":
        result[SurveyColumn.Neighborhoods.value] = "Fairfield"

    if result[SurveyColumn.Neighborhoods.value] == "Vistoso Golf Casitas 1" or result[SurveyColumn.Neighborhoods.value] == "Vistoso Golf Casitas 1":
        result[SurveyColumn.Neighborhoods.value] = "Vistoso Golf Casitas"

    result[SurveyColumn.ResideMonths.value] = str.strip(result[SurveyColumn.ResideMonths.value])

    if result[SurveyColumn.ResideMonths.value] == "0":
        result[SurveyColumn.ResideMonths.value] = "Not Provided"

    if result[SurveyColumn.ResideMonths.value] == "":
        result[SurveyColumn.ResideMonths.value] = "Not Provided"

    if result[SurveyColumn.ResideMonths.value] == "0.5":
        result[SurveyColumn.ResideMonths.value] = "1"

    if result[SurveyColumn.ResideMonths.value] == "4.5":
        result[SurveyColumn.ResideMonths.value] = "5"

    if result[SurveyColumn.ResideMonths.value] == "5.5":
        result[SurveyColumn.ResideMonths.value] = "6"

    if result[SurveyColumn.ResideMonths.value] == "13":
        result[SurveyColumn.ResideMonths.value] = "12"

    result[SurveyColumn.Email.value] = GetCorrectEmail(result[SurveyColumn.Email.value])
    
    return result

######
def GetPreferredUses(propertyUses):
    preferences = str.split(result[SurveyColumn.PropertyUses.value], ";")

    valueCounts = {}

    for item in preferences:
        if item in valueCounts:
            valueCounts[item] += 1
        else:
            valueCounts[item] = 1

def AddFlag(surveyData, tag, answer):
    if tag in answer:
        surveyData.append("Y")
        answer.remove(tag)
    else:
        surveyData.append("N")

def AddRankFlags(surveyData, answer):
    if answer == "Strongly Agree":
        surveyData.append("Y")
    else:
        surveyData.append("N")

    if answer == "Agree":
        surveyData.append("Y")
    else:
        surveyData.append("N")

    if answer == "Neutral":
        surveyData.append("Y")
    else:
        surveyData.append("N")

    if answer == "Disagree":
        surveyData.append("Y")
    else:
        surveyData.append("N")

    if answer == "Strongly Disagree":
        surveyData.append("Y")
    else:
        surveyData.append("N")

######
def GetSurveyData(result, contact):
    surveyData = []

    if len(contact) > 0:
        surveyData.append(contact[ContactColumn.Id.value]) # Id
        surveyData.append(contact[ContactColumn.LastName.value]) # LastName
        surveyData.append(contact[ContactColumn.FirstName.value]) # FirstName
    else:
        surveyData.append(-1) # Id
        surveyData.append("Unknown") # LastName
        surveyData.append("Unknown") # FirstName

    surveyData.append(result[SurveyColumn.Timestamp.value]) # Timestamp = 

     # Resident = 4
    if result[SurveyColumn.Resident.value] == "Yes":
        surveyData.append("Y")
    else:
        surveyData.append("N")

    surveyData.append(result[SurveyColumn.HomeCount.value]) # HomeCount = 5
    surveyData.append(result[SurveyColumn.Neighborhoods.value]) # Neighborhoods = 6

     # OnCourse = 7
    if result[SurveyColumn.OnCourse.value] == "Yes":
        surveyData.append("Y")
    else:
        surveyData.append("N")

    surveyData.append(result[SurveyColumn.ResideMonths.value]) # ResideMonths = 8
    surveyData.append(result[SurveyColumn.Email.value]) # Email = 9

    # Split out Property Use Preferences
    preferences = str.split(result[SurveyColumn.PropertyUses.value], ";")
    
    AddFlag(surveyData, "Walking", preferences)
    AddFlag(surveyData, "Running", preferences)
    AddFlag(surveyData, "Biking", preferences)
    AddFlag(surveyData, "Bird Watching", preferences)
    AddFlag(surveyData, "Golf", preferences)
    AddFlag(surveyData, "Nature/Wildlife Preservation", preferences)
    separator = ";"
    surveyData.append(separator.join(preferences))

    # Split out Concerns
    concerns = str.split(result[SurveyColumn.Concerns.value], ";")

    AddFlag(surveyData, "Property values", concerns)
    AddFlag(surveyData, "Traffic", concerns)
    AddFlag(surveyData, "Noise", concerns)

    # Special logic for checking Increased Fees
    if "Increased Fees" in concerns:
        surveyData.append("Y")
        concerns.remove("Increased Fees")
    else:
        if "Increased HOA or Other Fees" in concerns:
            surveyData.append("Y")
            concerns.remove("Increased HOA or Other Fees")
        else:
            surveyData.append("N")

    AddFlag(surveyData, "Impact on Wildlife", concerns)
    AddFlag(surveyData, "Views", concerns)
    AddFlag(surveyData, "Loss of Recreation Opportunities", concerns)
    separator = ";"
    surveyData.append(separator.join(concerns))

    AddRankFlags(surveyData, result[SurveyColumn.UseGolf18Hole.value])
    AddRankFlags(surveyData, result[SurveyColumn.UseGolfSmallCourse.value])
    AddRankFlags(surveyData, result[SurveyColumn.UseOpenSpace.value])
    AddRankFlags(surveyData, result[SurveyColumn.UsePark.value])
    AddRankFlags(surveyData, result[SurveyColumn.UsePublic.value])
    AddRankFlags(surveyData, result[SurveyColumn.LimitedDevelopment.value])
    AddRankFlags(surveyData, result[SurveyColumn.DevelopmentViewsSpace.value])
    AddRankFlags(surveyData, result[SurveyColumn.FullDevelopment.value])
    AddRankFlags(surveyData, result[SurveyColumn.BuyProperty.value])

    # Split out Finance Uses
    financeUses = str.split(result[SurveyColumn.FinanceUses.value], ";")

    AddFlag(surveyData, "18 hole golf course", financeUses)
    AddFlag(surveyData, "Less than 18 hole golf course", financeUses)
    AddFlag(surveyData, "Open space (no path)", financeUses)
    AddFlag(surveyData, "Open space (with path)", financeUses)
    AddFlag(surveyData, "Park", financeUses)
    AddFlag(surveyData, "", financeUses)

    surveyData.append(result[SurveyColumn.Comments.value])

    return surveyData

######
def LoadSurvey(filename):
    allResults = []

    with open(filename, mode='r', encoding='utf8') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                lineCount += 1
            else:
                lineCount += 1
                allResults.append(FixResult(row))

    return allResults

######
def SaveSurvey(filename, allSurveyData):
    columnNames = []
    for column in SurveyDataColumn:
        columnNames.append(column.name)

    with open(filename, mode='w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(columnNames)
        for data in allSurveyData:
            csvWriter.writerow(data)
