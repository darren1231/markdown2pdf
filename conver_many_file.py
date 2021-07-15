# encoding: utf-8
from xhtml2pdf import pisa
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from xhtml2pdf.default import DEFAULT_FONT
import markdown
import os
from tqdm import tqdm

## chinese font
pdfmetrics.registerFont(TTFont('yh', 'font/msyh.ttf'))
DEFAULT_FONT['helvetica'] = 'yh'

def read_md(md_path):
    with open(md_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    sourceHtml = markdown.markdown(text)
    return sourceHtml

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
    mardown_file_path = "D:/backup/where_your_file"
    output_file_path = mardown_file_path+"_pdf"
    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)

    for dirPath, dirNames, fileNames in os.walk(mardown_file_path):    
        for f in tqdm(fileNames):
            # print (os.path.join(dirPath, f))
            file_path = os.path.join(dirPath, f)
            outputFilename = os.path.join(output_file_path,f.replace("md","pdf"))

            try:
                sourceHtml = read_md(file_path)
                convertHtmlToPdf(sourceHtml, outputFilename)
            except Exception:
                print ("error",file_path)