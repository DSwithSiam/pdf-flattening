# PDF Form Filler with Signature

A Python library for filling PDF forms, adding signatures, and converting PDFs to image-based PDFs. Perfect for document automation workflows.

## Features

- ✅ Fill PDF form fields with data
- ✅ Add signature images to PDFs
- ✅ Convert PDFs to image-based format (fixes browser compatibility)
- ✅ Remove signature widgets
- ✅ Firefox & Safari compatibility fixes

## Installation

```bash
pip install PyPDF2 PyMuPDF Pillow
```

### Required Dependencies
- `PyPDF2` - PDF manipulation
- `PyMuPDF` (fitz) - PDF rendering and image conversion
- `Pillow` - Image processing

## Project Structure

```
pdf_problem solve/
├── generate_pdf.py          # Main entry point
├── pdf_utils/
│   ├── fill_pdf.py          # PDF form filling
│   ├── signature.py         # Signature handling
│   └── render.py            # PDF to image conversion
└── README.md
```

## Usage

### Basic Example

```python
from generate_pdf import generate_final_pdf

# Prepare your data
template_pdf = "template.pdf"
output_pdf = "filled_output.pdf"
final_pdf = "final_document.pdf"
signature_image = "signature.png"

# Form field data to fill
form_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "date": "2024-01-15",
    "amount": "$1000"
}

# Generate complete PDF
generate_final_pdf(
    template=template_pdf,
    filled_pdf=output_pdf,
    final_pdf=final_pdf,
    data=form_data,
    signature_img=signature_image
)

print(f"PDF generated: {final_pdf}")
```

### Step-by-Step Usage

#### 1. Fill PDF Form

```python
from pdf_utils.fill_pdf import fill_pdf_form

form_data = {
    "field_name_1": "Value 1",
    "field_name_2": "Value 2",
    "checkbox_field": "Yes"
}

filled_pdf = fill_pdf_form(
    input_pdf="template.pdf",
    output_pdf="filled.pdf",
    field_data=form_data
)
```

#### 2. Add Signature

```python
from pdf_utils.signature import add_signature_and_cleanup
import fitz

# Define signature position (left, bottom, right, top)
signature_rect = fitz.Rect(100, 500, 300, 580)

signed_pdf = add_signature_and_cleanup(
    input_pdf="filled.pdf",
    output_pdf="signed.pdf",
    signature_img="signature.png",
    rect=signature_rect
)
```

#### 3. Convert to Image PDF

```python
from pdf_utils.render import render_pdf_as_image_pdf

final_pdf = render_pdf_as_image_pdf(
    input_pdf="signed.pdf",
    output_pdf="final.pdf",
    dpi=150,           # Resolution (72-300 recommended)
    quality=65         # JPEG quality (0-95)
)
```

## Advanced Examples

### Multi-Page Form Filling

```python
from pdf_utils.fill_pdf import fill_pdf_form
from pdf_utils.render import render_pdf_as_image_pdf

# Works with multi-page PDFs
form_data = {
    "page1_field1": "Data 1",
    "page2_field2": "Data 2",
    "page3_signature_date": "2024-01-15"
}

fill_pdf_form("multi_page.pdf", "output.pdf", form_data)
render_pdf_as_image_pdf("output.pdf", "final_output.pdf")
```

### Custom Signature Position

```python
from pdf_utils.signature import add_signature_and_cleanup
import fitz

# Signature at different positions
# Format: Rect(x_min, y_min, x_max, y_max)
# Bottom right corner
bottom_right = fitz.Rect(450, 700, 550, 800)

# Top right corner
top_right = fitz.Rect(450, 50, 550, 150)

# Middle of page
middle = fitz.Rect(200, 350, 400, 450)

add_signature_and_cleanup(
    "filled.pdf",
    "signed.pdf",
    "signature.png",
    rect=bottom_right
)
```

### High Quality Output

```python
from pdf_utils.render import render_pdf_as_image_pdf

# High quality (for printing)
render_pdf_as_image_pdf(
    input_pdf="signed.pdf",
    output_pdf="final_hq.pdf",
    dpi=300,        # High resolution
    quality=85      # Better quality
)

# Web quality (smaller file size)
render_pdf_as_image_pdf(
    input_pdf="signed.pdf",
    output_pdf="final_web.pdf",
    dpi=72,         # Screen resolution
    quality=50      # Lower quality for web
)
```

### Browser Compatibility

The `render_pdf_as_image_pdf` function converts PDFs to image-based format, which ensures compatibility with:
- Firefox
- Safari
- Chrome
- Edge
- Mobile browsers

```python
# Ensures compatibility across all browsers
from generate_pdf import generate_final_pdf

generate_final_pdf(
    template="form.pdf",
    filled_pdf="temp.pdf",
    final_pdf="browser_compatible.pdf",
    data={"name": "Jane Doe"},
    signature_img="sig.png"
)
```

## Common Use Cases

### 1. Invoice Generation

```python
invoice_data = {
    "invoice_number": "INV-001",
    "date": "2024-01-15",
    "customer_name": "ABC Company",
    "amount": "$5,000",
    "authorized_by": "Manager"
}

generate_final_pdf(
    template="invoice_template.pdf",
    filled_pdf="temp.pdf",
    final_pdf="invoice.pdf",
    data=invoice_data,
    signature_img="authorized_signature.png"
)
```

### 2. Contract Signing

```python
contract_data = {
    "party1_name": "John Doe",
    "party2_name": "Jane Smith",
    "date": "2024-01-15",
    "terms": "As agreed"
}

generate_final_pdf(
    template="contract.pdf",
    filled_pdf="temp.pdf",
    final_pdf="signed_contract.pdf",
    data=contract_data,
    signature_img="john_signature.png"
)
```

### 3. Certificate Generation

```python
certificate_data = {
    "recipient_name": "John Doe",
    "course": "Advanced Python",
    "completion_date": "2024-01-15",
    "instructor": "Expert"
}

generate_final_pdf(
    template="certificate_template.pdf",
    filled_pdf="temp.pdf",
    final_pdf="certificate_john_doe.pdf",
    data=certificate_data,
    signature_img="instructor_signature.png"
)
```

## Parameters Reference

### `fill_pdf_form()`
- `input_pdf` (str): Path to template PDF
- `output_pdf` (str): Path for output PDF
- `field_data` (dict): Dictionary of field names and values

### `add_signature_and_cleanup()`
- `input_pdf` (str): Path to input PDF
- `output_pdf` (str): Path for output PDF
- `signature_img` (str): Path to signature image file
- `rect` (fitz.Rect): Signature position as Rect(x_min, y_min, x_max, y_max)

### `render_pdf_as_image_pdf()`
- `input_pdf` (str): Path to input PDF
- `output_pdf` (str): Path for output PDF
- `dpi` (int): Resolution in DPI (default: 150)
- `quality` (int): JPEG quality 0-95 (default: 65)

### `generate_final_pdf()`
- `template` (str): Path to template PDF
- `filled_pdf` (str): Path for intermediate filled PDF
- `final_pdf` (str): Path for final output PDF
- `data` (dict): Form field data
- `signature_img` (str): Path to signature image

## Tips & Best Practices

1. **PDF Form Fields**: Ensure your template PDF has properly named form fields
2. **Signature Images**: Use PNG or JPG with transparent background for best results
3. **DPI Settings**: Use 150 for screen viewing, 300 for printing
4. **Quality**: Higher quality = larger file size. Balance based on use case
5. **Cleanup**: Remove temporary files after generation for disk space

## Troubleshooting

### Form Fields Not Filling
- Verify field names in PDF template match your `form_data` keys
- Check PDF has AcroForm objects

### Signature Not Appearing
- Ensure signature image file exists
- Adjust `rect` coordinates to visible area of page
- Verify first page exists if adjusting page index in `signature.py`

### Browser Display Issues
- Use `render_pdf_as_image_pdf()` to convert to image format
- This ensures maximum compatibility

## License

MIT

## Support

For issues or questions, please check the code comments for detailed implementation notes.
