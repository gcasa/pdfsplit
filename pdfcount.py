# pdfcount.py
import os

from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_count(path, n):
    pdf = PdfFileReader(path)
    num_pages = pdf.getNumPages()
    number_dec = (num_pages / n) % 1
    if number_dec > 0.0:
        a = 1
    else:
        a = 0
    num_pdfs = int(num_pages / n) + a
    print('File {} should produce {} files'.format(path, num_pdfs))

    return num_pdfs


def main():
    i = 0
    c = 0
    directory = r'/Users/heron/PDFS'
    for entry in os.scandir(directory):
        if entry.path.endswith(".pdf"):
            i = i + 1
            c += pdf_count(entry.path, 5)
    print('Processed {} files'.format(i))
    print('Result should produce {} files'.format(c))


if __name__ == '__main__':
    main()