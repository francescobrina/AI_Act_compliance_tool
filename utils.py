from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(file_path, user_info):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Report di Valutazione del Rischio - AI ACT Compliance")

    c.setFont("Helvetica", 12)
    y = height - 80
    c.drawString(50, y, f"Nome del Progetto: {user_info.get('project_name', '')}")
    y -= 20
    c.drawString(50, y, "Descrizione del Progetto:")
    y -= 20
    text = c.beginText(50, y)
    text.setFont("Helvetica", 12)
    text.textLines(user_info.get('project_description', ''))
    c.drawText(text)

    y = text.getY() - 20
    c.drawString(50, y, f"Livello di Rischio: {user_info.get('risk_level', '')}")
    y -= 20
    c.drawString(50, y, f"Criterio: {user_info.get('criteria', '')}")

    y -= 40
    c.drawString(50, y, "Requisiti da soddisfare:")
    y -= 20
    text = c.beginText(50, y)
    text.setFont("Helvetica", 12)
    text.textLines(user_info.get('requirements', '').split('\n'))
    c.drawText(text)

    if 'suggestions' in user_info:
        y = text.getY() - 20
        c.drawString(50, y, "Suggerimenti Personalizzati:")
        y -= 20
        text = c.beginText(50, y)
        text.setFont("Helvetica", 12)
        text.textLines(user_info.get('suggestions', '').split('\n'))
        c.drawText(text)

    c.showPage()
    c.save()
