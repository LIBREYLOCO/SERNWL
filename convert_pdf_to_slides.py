#!/usr/bin/env python3
"""
Convert PDF to individual slide images using PyMuPDF
"""
import fitz  # PyMuPDF
import os

# Configuration
pdf_path = "PROGRAMA SER-NWL 2026 PRESENTACION  OK.pdf"
output_dir = "pdf_slides"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

print(f"Converting PDF: {pdf_path}")
print(f"Output directory: {output_dir}")

# Open the PDF
pdf_document = fitz.open(pdf_path)
total_pages = pdf_document.page_count

print(f"Found {total_pages} slides in the PDF")

# Convert each page to an image
for page_num in range(total_pages):
    # Get the page
    page = pdf_document[page_num]
    
    # Render page to an image (matrix for higher resolution)
    # zoom = 2.0 gives 200 DPI (default is 72 DPI)
    mat = fitz.Matrix(2.0, 2.0)
    pix = page.get_pixmap(matrix=mat)
    
    # Save the image
    output_path = os.path.join(output_dir, f"slide_{page_num:02d}.png")
    pix.save(output_path)
    print(f"Saved: {output_path}")

# Close the PDF
pdf_document.close()

print(f"\nConversion complete! {total_pages} slides saved to {output_dir}/")
