import unittest
from ContactModule import FindContact

def CreateContactList(primaryEmails, secondaryEmails):
    contacts = []
    i = 0
    for email in primaryEmails:
        if i < len(secondaryEmails):
            secondaryEmail = secondaryEmails[i]
        else:
            secondaryEmail = ""

        contacts.append(["","","","","","","","",email,secondaryEmail])
        i += 1

    return contacts

class Test_FindContactTest(unittest.TestCase):

    def test_NotFound(self):
        emails = ['a@gmail.com', 'b@hotmail.com']
        contacts = CreateContactList(emails, [])

        self.assertEqual(-1, FindContact('a@yahoo.com', contacts), 'Should not find a@yahoo.com')
      
    def test_Found(self):
        emails = ['a@gmail.com', 'b@hotmail.com']
        contacts = CreateContactList(emails, [])

        result = FindContact('b@hotmail.com', contacts)
        self.assertEqual(1, result, 'Should find b@hotmail.com')

    def test_Found_DifferentCase(self):
        emails = ['a@gmail.com', 'b@hotmail.com']
        contacts = CreateContactList(emails, [])

        self.assertEqual(0, FindContact('A@Gmail.com', contacts), 'Should find A@Gmail.com')

    def test_Found_SecondaryEmail(self):
        primaryEmails = ['a@gmail.com', 'b@hotmail.com']
        secondaryEmails = ['c@yahoo.com', 'D@Outlook.com']
        contacts = CreateContactList(primaryEmails, secondaryEmails)

        self.assertEqual(1, FindContact('d@outlook.com', contacts), 'Should find d@outlook.com')

    def test_Found_IgnoreTrailingSpaces(self):
        emails = ['A@Gmail.com ', 'b@hotmail.com']
        contacts = CreateContactList(emails, [])

        self.assertEqual(0, FindContact('a@gmail.com', contacts), 'Should find a@gmail.com')

    def test_Found_IgnoreLeadingSpaces(self):
        emails = ['a@gmail.com ', 'b@hotmail.com']
        contacts = CreateContactList(emails, [])

        self.assertEqual(0, FindContact(' A@Gmail.com', contacts), 'Should find A@Gmail.com')


if __name__ == '__main__':
    unittest.main()
