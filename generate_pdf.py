from pdf_utils.fill_pdf import fill_pdf_form
from pdf_utils.signature import add_signature_and_cleanup
from pdf_utils.render import render_pdf_as_image_pdf
import fitz


def generate_final_pdf(template, filled_pdf, final_pdf, data, signature_img):
    fill_pdf_form(template, filled_pdf, data)

    add_signature_and_cleanup(
        filled_pdf,
        filled_pdf,
        signature_img,
        rect=fitz.Rect(100, 500, 300, 580)
    )

    render_pdf_as_image_pdf(filled_pdf, final_pdf)

    return final_pdf