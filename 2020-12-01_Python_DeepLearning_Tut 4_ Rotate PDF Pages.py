# install pip-pymuPDF, first, to activate , fitz,

#Python DeepLearning_Tut 4_ Rotating PDF pages

import fitz

pdf = fitz.open("RetireYoungRetireRich.pdf")
numPages = pdf.pageCount   # counts the total number of PDF files pages 

pdf2 = fitz.open()
pdf2.insertPDF(pdf,from_page=385,to_page=numPages-1,rotate=90)
pdf2.save("RetireYoungRetireRich_epilogue_rotated.pdf")

