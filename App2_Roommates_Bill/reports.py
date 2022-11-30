import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about the
    roommates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):

        roommate1_pays = f"${str(round(roommate1.pays(bill, roommate2), 2))}"
        roommate2_pays = f"${str(round(roommate2.pays(bill, roommate1), 2))}"

        pdf = FPDF(orientation="P", unit="pt", format="Letter")
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first roommate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate1_pays, border=0, ln=1)

        # Insert name and due amount of the second roommate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate2_pays, border=0, ln=1)

        os.chdir("files")

        pdf.output(self.filename)

        webbrowser.open(f"file://{os.path.realpath(self.filename)}")
