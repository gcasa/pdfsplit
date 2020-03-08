# pdf_splitter.py
import os

from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path, n):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    num_pages = pdf.getNumPages()

    for page in range(pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}-{}.pdf'.format(
            fname, page - 4, page)
        if (page % n == 0 and page != 0) or page == num_pages:
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            print('Created: {}'.format(output_filename))
            pdf_writer = PdfFileWriter()


def main():
    directory = r'/Users/heron/PDFS'
    for entry in os.scandir(directory):
        if entry.path.endswith(".pdf"):
            pdf_splitter(entry.path, 5)


if __name__ == '__main__':
    main()
