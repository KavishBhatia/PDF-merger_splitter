import PyPDF2
from easygui import *
import sys

def PDFsplit(pdf, splits):
        # creating input pdf file object
        pdfFileObj = open(pdf, 'rb')
        
        # creating pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        # starting index of first slice
        start = splits[0]-1
        
        # starting index of last slice
        end = splits[1]
        
        
        # creating pdf writer object for (i+1)th split
        pdfWriter = PyPDF2.PdfFileWriter()
        
        # output pdf file name
        output_filename = enterbox("Enter Output File Name")
        output = output_filename + ".pdf"
                
        # adding pages to pdf writer object
        for page in range(start,end):
                pdfWriter.addPage(pdfReader.getPage(page))
                
        # writing split pdf pages to pdf file
        with open(output, "wb") as f:
                pdfWriter.write(f)

                
        # closing the input pdf file object
        pdfFileObj.close()
        msgbox("PDF Split Complete")
        sys.exit(0)
                        
def main():
        pdfs = []
        num = []
        while 1:
                msg = "Pick PDF to Split "
                title = "PDF Splitter"
                choices = ["Pick PDF","Split PDF","EXIT"]
                choice = indexbox(msg,title,choices)

                if choice == 2:
                        sys.exit()
                elif choice == 0:
                        pdf = fileopenbox()
                        if pdf[-3:] != "pdf":
                                msgbox("Selected File not PDF")
                        else:
                                pdfs.append(pdf)
                elif choice == 1:
                        if len(pdfs) < 1:
                                msgbox("Select a PDF, None selected", " OK")
                        elif len(pdfs) == 1:
                                splits = enterbox("Enter Page Numbers to Split (Separated by '-' )")
                                splits = splits.split('-')
                                num.append(int(splits[0]))
                                num.append(int(splits[1]))
                                PDFsplit(pdf, num)
                        elif len(pdfs) > 1:
                                msgbox("Multiple Files selected. Choose 'Split PDF' to Split recent selected file")
                                temp = pdfs[-1]
                                pdfs = []
                                pdfs.append(temp)

if __name__ == "__main__":
        # calling the main function
        main()
