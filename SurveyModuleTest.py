import unittest
from SurveyModule import FixResult, SurveyColumn, GetSurveyData, SurveyDataColumn

def CreateTestResult(email):
    return ["", "", "", "", "", "", email]

def TestSurveyDataItem(self, surveyData, dataColumn, expectedValue):
    self.assertEqual(expectedValue, surveyData[dataColumn.value], "Unexpected value for " + repr(dataColumn))

class Test_SurveyModuleTest(unittest.TestCase):
    def test_FixResult(self):

        result = CreateTestResult("Samhalgren@comcast.com")
        newResult = FixResult(result)
        self.assertEqual("samhalgren@comcast.net", newResult[SurveyColumn.Email.value], 'Email should have been replaced')

    def test_FixResult_NoMatch(self):

        result = CreateTestResult("test@hotmail.com")
        newResult = FixResult(result)
        self.assertEqual("test@hotmail.com", newResult[SurveyColumn.Email.value], 'Email should not have been replaced')

    def test_GetSurveyData(self):

        result = ["", "", "", "", "", "", "test@hotmail.com", "Park;Walking;Golf;Biking;Tennis", "Fees;Property values;Traffic;Privacy", "Agree", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree", "Strongly Agree", "Agree", "Neutral", "", ""]
        surveyData = GetSurveyData(result, [])

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.Id, -1)
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.Email, "test@hotmail.com")

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUseWalking, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUseRunning, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUseBiking, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUseBird, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUseGolf, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUsePreservation, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.PreferUseOther, "Park;Tennis")

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernPropertyValues, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernTraffic, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernNoise, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernFees, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernWildlife, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernViews, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernRecreation, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.ConcernOther, "Fees;Privacy")

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseGolf18Hole_SA, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseGolf18Hole_A, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseGolf18Hole_N, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseGolf18Hole_D, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseGolf18Hole_SD, "N")

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseGolfSmallCourse_SA, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UseOpenSpace_A, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UsePark_N, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.UsePublic_D, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.LimitedDevelopment_SD, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.DevelopmentViewsSpace_SA, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FullDevelopment_A, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.BuyProperty_SA, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.BuyProperty_N, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.BuyProperty_SD, "N")

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUseNone, "Y")

    def test_GetSurveyData2(self):

        result = ["", "", "", "", "", "", "test@hotmail.com", "Park;Walking;Golf;Tennis", "Fees;Property values;Traffic;Privacy", "Agree", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree", "Strongly Agree", "Agree", "Neutral", "Open space (no path);Park", "No comment"]
        surveyData = GetSurveyData(result, [])

        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUse18Hole, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUseNone, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUseNoPath, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUsePark, "Y")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUseSmallGolf, "N")
        TestSurveyDataItem(self, surveyData, SurveyDataColumn.FinanceUseWithPath, "N")


if __name__ == '__main__':
    unittest.main()
