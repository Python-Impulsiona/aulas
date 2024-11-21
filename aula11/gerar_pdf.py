# pip = python install package
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

pdf = canvas.Canvas("aula11/exemplo.pdf", pagesize=letter)

pdf.setTitle("teste")
pdf.drawString(100, 750, "Olá, mundo")
pdf.drawRightString(100, 725, "teste")

pdf.save()
print("PDF gerado")
