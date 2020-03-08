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

        # Figure out the start page....
        p = 1
        if page - 4 > 0:
            p = page - 4

        # Output the file
        output_filename = 'Output/{}_page_{}-{}.pdf'.format(
            fname, p, page)
        if (page % n == 0 and page != 0) or page == (num_pages - 1):
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            print('Created: {}'.format(output_filename))
            pdf_writer = PdfFileWriter()


def main():
    i = 0
    directory = r'/Users/heron/PDFS'
    for entry in os.scandir(directory):
        if entry.path.endswith(".pdf"):
            i = i + 1
            pdf_splitter(entry.path, 5)
    print('Processed {} files'.format(i))


if __name__ == '__main__':
    main()
