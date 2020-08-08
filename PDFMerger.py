import sys
import PyPDF2

files=sys.argv[1:]
merger=PyPDF2.PdfFileMerger()
for file1 in files:
	merger.append(PyPDF2.PdfFileReader(file1))
merger.write('Merged.pdf')