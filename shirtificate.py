from fpdf import FPDF



x = input("Name:")
pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', '', 42)
pdf.set_auto_page_break(True)
pdf.cell(0, 40, "CS50 Shirtificate", 0, 1, "C")
pdf.image("shirtificate.png", 10, 50, w=190, h=140)
pdf.cell(0, 120, x, 0, 1, "C")
pdf.output("test.pdf", "F")