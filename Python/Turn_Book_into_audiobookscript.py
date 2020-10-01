import pyttsx3
import PyPDF2
book = open('Django_notes.pdf','rb')
pdfreader =PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7,pages):
    page = pdfreader.getPage(12)
    text =page.extractText()
    speaker.say(text)
    speaker.runAndWait()