import fitz  # PyMuPDF

# Extracting text from pdf file
def extract_text_from_pdf(file_path):
    try:
        document = fitz.open(file_path)
        text = ""
        for page in document:
            text += page.get_text()
        document.close()
        return text
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return ""
