from SurveyModule import SurveyDataColumn

# TODO: Change to actually handle duplicates versus just identifying them
def IdentifyDuplicates(allSurveyData):
    uniqueIds = {}

    for item in allSurveyData:
        if item[SurveyDataColumn.Id.value] in uniqueIds:
            uniqueIds[item[SurveyDataColumn.Id.value]] += 1
        else:
            uniqueIds[item[SurveyDataColumn.Id.value]] = 1

    print("Members with more than one response")
    for k, v in uniqueIds.items():
        if v > 1:
            print(f"Member {k} has {v} responses")