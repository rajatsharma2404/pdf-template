from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")

data = pd.read_csv("topics.csv")



for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="arial", style="B", size=20)
    pdf.cell(w=0, h=10,txt = row['Topic'],ln=1,align="L")
    pdf.line(10,20, 200,20)
    for i in range(int(row['Pages'])-1):
        pdf.add_page()




pdf.output(name="output.pdf")
