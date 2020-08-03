import sys
import PyPDF2

files=sys.argv[1:]
for file in files:
	merger=PyPDF2.PdfFileMerger()
	merger.append(file)
merger.write('Merged.pdf')