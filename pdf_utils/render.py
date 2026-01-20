import fitz
from PIL import Image
import io


def render_pdf_as_image_pdf(input_pdf, output_pdf, dpi=150, quality=65):
    doc = fitz.open(input_pdf)
    images = []

    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)

    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        img = Image.open(io.BytesIO(pix.tobytes("ppm")))

        if img.mode != "RGB":
            img = img.convert("RGB")

        images.append(img)

    doc.close()

    images[0].save(
        output_pdf,
        "PDF",
        save_all=True,
        append_images=images[1:],
        resolution=dpi,
        optimize=True,
        quality=quality
    )

    return output_pdf