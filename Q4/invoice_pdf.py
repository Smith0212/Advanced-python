import pandas as pd
from fpdf import FPDF
import os
from PyPDF2 import PdfFileMerger
from datetime import date

def create_pdf_invoice(order):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(0, 10, f"Invoice Number: {order['Order ID']}", ln=True)
    pdf.cell(0, 10, f"Date of Purchase: {date.today()}", ln=True)
    pdf.cell(0, 10, f"Customer Name: {order['Customer Name']}", ln=True)
    pdf.cell(0, 10, f"Product Name: {order['Product Name']}", ln=True)
    pdf.cell(0, 10, f"Quantity: {order['Quantity']}", ln=True)
    pdf.cell(0, 10, f"Unit Price: ${order['Unit Price']:.2f}", ln=True)
    
    total_amount = order['Quantity'] * order['Unit Price']
    pdf.cell(0, 10, f"Total Amount: ${total_amount:.2f}", ln=True)
    
    pdf_file_name = f"invoice_{order['Order ID']}.pdf"
    pdf.output(pdf_file_name)
    return pdf_file_name

order_data = pd.read_csv('orders.csv')

pdf_invoice_files = []
for _, order in order_data.iterrows():
    pdf_invoice_file = create_pdf_invoice(order)
    pdf_invoice_files.append(pdf_invoice_file)

pdf_merger = PdfFileMerger()
for pdf_file in pdf_invoice_files:
    pdf_merger.append(pdf_file)

pdf_merger.write('merged_invoices.pdf')
pdf_merger.close()

for pdf_file in pdf_invoice_files:
    os.remove(pdf_file)

print("PDF invoices generated and merged successfully.")
