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