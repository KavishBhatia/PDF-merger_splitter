from easygui import *
import PyPDF2
import sys

def PDFmerge(pdfs, output): 
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
    
    # appending pdfs one by one
    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)
        
    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)
        msgbox("PDFs Merged")
        sys.exit(0)

def show_pdf(pdfs):
    pdf_list = []
    for pdf in pdfs:
        name = pdf.split("\\")
        pdf_list.append(name[-1])
        
    num = 1
    msg = ""
    for i in range(len(pdf_list)):
        msg += str(num) + ". " + pdf_list[i] + "\n"
        num += 1
    msgbox(msg, "Selected PDFs")

def main():
    # pdf files to merge
    pdfs = []
    while 1:
        msg = "Pick PDF to Merge \t\t\t\t\t\t\t "+ str(len(pdfs)) + " selected"
        title = "PDF Merger"
        choices = ["Pick PDFs","Merge PDFs","Show Selected PDFs","EXIT"]
        choice = indexbox(msg,title,choices)
        
        if choice == 3:
            sys.exit()
            
        elif choice == 0:
            a = fileopenbox()
            if a[-3:] != "pdf": ## or a.endswith('.pdf')
                msgbox("Selected File not PDF")
            else:
                pdfs.append(a)

        elif choice == 1:
            if len(pdfs) <= 1:
                msgbox("Select atleast 2 pdfs, " + str(len(pdfs)) + " selected", " OK")
            elif len(pdfs) >= 2:
                output_filename = enterbox("Enter Output File Name")
                output = output_filename + ".pdf"
                PDFmerge(pdfs = pdfs, output = output)

        elif choice == 2:
            if len(pdfs) < 1:
                msgbox("No Files Selected", "Selected PDFs")
            else:    
                show_pdf(pdfs = pdfs)


if __name__ == "__main__":
	# calling the main function
	main()

