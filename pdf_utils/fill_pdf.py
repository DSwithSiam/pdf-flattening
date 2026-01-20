from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, BooleanObject


def fill_pdf_form(input_pdf, output_pdf, field_data):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Critical Fix for Firefox & Safari
    
    if "/AcroForm" in reader.trailer["/Root"]:
        acroform = reader.trailer["/Root"]["/AcroForm"]
        writer._root_object.update({
            NameObject("/AcroForm"): writer._add_object(acroform)
        })
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    for page in writer.pages:
        writer.update_page_form_field_values(page, field_data)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    return output_pdf