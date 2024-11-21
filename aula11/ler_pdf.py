import PyPDF2

with open("aula11/exemplo.pdf", "rb") as pdf:
    leitor = PyPDF2.PdfReader(pdf)
    conteudo = ""
    for pagina in leitor.pages:
        conteudo += pagina.extract_text()
    print(conteudo)
    

