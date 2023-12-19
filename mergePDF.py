from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = os.listdir("ToEditFolder")

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()