import pdfplumber
import sys
import os

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n\n"
            return full_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        pdf_path = sys.argv[1]
    else:
        pdf_path = '/Users/white/Desktop/Taylor Algorithm13.pdf'
    text = extract_text_from_pdf(pdf_path)
    if text:
        out_dir = "/Users/white/Desktop/Code/MacCode-master/create"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "extracted_text.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Text extracted successfully to {out_path}")
    else:
        print("Failed to extract text.")
