import PyPDF2, os
from pprint import pprint
import pandas as pd

pd.set_option('display.max_columns', None)

def extract_pdf_form(filename):
	with open(filename, "rb") as pdf_obj:
		pdf = PyPDF2.PdfFileReader(pdf_obj)
		return pdf.getFormTextFields()



def find_pdfs():
	for root, dirs, files in os.walk("./POs"):
		for file in files:
			filename, extension = os.path.splitext(file)
			if extension == ".pdf":
				curr_path = f"{root}/{filename}{extension}"
				pdf_data = extract_pdf_form(curr_path)
				pprint(pdf_data)
				df = pd.DataFrame([pdf_data])
				print(df)
				break




extract_pdf_form("./POs/12140(Vital).pdf")

find_pdfs()