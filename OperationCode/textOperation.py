class Operation:
    # def _init_(self):
    #     self.text = None
    def removePunctuation(self, text):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed+=char 
        return analyzed
    def captalizedFistLetter(self, text):
        return text.capitalize()
    def spaceremover(self, text):
        return " ".join(text.split())
    def charCount(self, text):
        return len(text)
    def removeNewLines(self, text):
        textRes = ""
        for char in text:
            if(char != "\n" and char != "\r"):
                textRes+=char
        return textRes
    def replaceSubstring(self, inputStr, str1, str2):
        if str1.casefold() in inputStr.casefold():
            return inputStr.casefold().replace(str1.casefold(), str2)
        else:
            return "Given string is not present in the text"
    def swapcaseString(self, inputStr):
        return inputStr.swapcase()
    def convertIntoLower(self,inputStr):
        return inputStr.lower()
    def encodeString(self, inputStr):
        return inputStr.encode()
    def splitString(self, inputStr):
        return inputStr.split()
    def removeWhiteSpaceStartEnd(self, inputStr):
        return list(inputStr.split(" "))
    def upperCaseString(self, inputStr):
        return inputStr.upper()
    def splitStringByLines(self, inputStr):
        return list(inputStr.splitlines())
    def checkDiff(self, str1, str2):
        if (str1 == str2):
            return "Both strings are equal"
        elif(str1.casefold() == str2.casefold()):
            return "Bothe strings are equal but ignored case"
        else:
            return "Both strings are not equal"
    def splitbyword(self, str1, str2):
        return str1.partition(str2)
    def findStartIndex(self, str1, str2):
        return str1.find(str2)
