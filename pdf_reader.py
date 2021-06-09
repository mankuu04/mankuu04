import pyttsx3
import PyPDF2
book = open('FundamentalsofComputerStudies.pdf', 'rb')  #enter the pdf file
PdfReader = PyPDF2.PdfFileReader(book)
pages = PdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(5,7): ##enter the page where you want to read
    page = PdfReader.getPage(5)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
