from flask import make_response
from flask import Flask
from reportlab.pdfgen import canvas
from weasyprint import HTML

# ...

pdf = HTML('http://google.com/').write_pdf()
f =open("data.pdf","w")
f.write(pdf)

