import PyPDF2
import os
import re

def merge_pdfs(paths, output):
    pdf_merger = PyPDF2.PdfMerger()
    for path in paths:
        pdf_merger.append(path)

    with open(output, 'wb') as fileobj:
        pdf_merger.write(fileobj)

def numerical_sort(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

def get_pdf_files(directory):
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    pdf_files.sort(key=numerical_sort)  # Sort files numerically
    return pdf_files

def main(directory, output_file):
    pdf_files = get_pdf_files(directory)
    full_paths = [os.path.join(directory, filename) for filename in pdf_files]

    merge_pdfs(full_paths, output_file)
    print(f"Merged PDF saved as {output_file}")

if __name__ == "__main__":
    directory = os.getcwd()  # Update this path to the directory containing your PDFs
    output_file = 'output.pdf'  # Name of the merged output file
    main(directory, output_file)
