import argparse
import glob
from PyPDF2 import PdfFileMerger

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str, help="name of the pdf resulting from the merge")
parser.add_argument("-p", "--path", type=str, help="filepath to directory of pdfs to combine")
parser.add_argument("-d", "--dest", action="store_true", help="place the output in the same path")
parser.add_argument("-v", "--verbose", action="store_true", help="print the name of the files merged")
args = parser.parse_args()

if args.path:
    filepath = args.path
    if filepath[-1] != "/":
        filepath += "/"
else:
    filepath = ""

name = "joined"
if args.name:
    name = args.name
if args.dest:
    name = filepath+name

pdfs = glob.glob(filepath+"*.pdf")

if len(pdfs) > 0:
    ordered_pdfs = {}
    for pdf in pdfs:
        pdf_name = pdf.split("/")[-1:][0]
        if pdf_name[0].isnumeric():
            if args.verbose:
                print(pdf_name)
            for i in range(len(pdf_name)):
                c = pdf_name[i]
                if not c.isnumeric():
                    ordered_pdfs[int(pdf_name[:i])] = pdf
                    break
    ordered_pdfs = [pdf[1] for pdf in sorted(ordered_pdfs.items())]
    if len(ordered_pdfs) > 0:
        merger = PdfFileMerger()

        for pdf in ordered_pdfs:
            merger.append(pdf)

        merger.write(name+".pdf")
        merger.close()
