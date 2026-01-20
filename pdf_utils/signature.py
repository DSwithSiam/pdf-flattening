import fitz  # PyMuPDF


def add_signature_and_cleanup(input_pdf, output_pdf, signature_img, rect):
    doc = fitz.open(input_pdf)
    page = doc[0]  # Adjust page index if needed

    page.insert_image(rect, filename=signature_img)

    # Remove signature widgets permanently
    for widget in page.widgets():
        if widget.field_type == fitz.PDF_WIDGET_TYPE_SIGNATURE:
            page.delete_widget(widget)

    doc.save(output_pdf)
    doc.close()

    return output_pdf