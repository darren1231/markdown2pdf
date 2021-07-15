# encoding: utf-8
from xhtml2pdf import pisa
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from xhtml2pdf.default import DEFAULT_FONT

pdfmetrics.registerFont(TTFont('yh', 'font/msyh.ttf'))
DEFAULT_FONT['helvetica'] = 'yh'
sourceHtml = "<html><body><p>To <br>PDF 中文测试</p></body></html>"
outputFilename = "test.pdf"


# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")
    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
        sourceHtml,  # the HTML to convert
        dest=resultFile)  # file handle to recieve result
    # close output file
    resultFile.close()  # close output file
    # return True on success and False on errors
    return pisaStatus.err


# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)