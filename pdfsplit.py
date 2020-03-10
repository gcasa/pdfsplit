# pdfsplit.py
import os

from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path, n):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    num_pages = pdf.getNumPages()
    num_files = 0

    for page in range(pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))

        # Output the file
        output_filename = 'Output/{}_page_{}.pdf'.format(
            fname, page + 1)
        if ((page + 1) % n == 0) or page == (num_pages - 1):
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            print('Created: {}'.format(output_filename))
            pdf_writer = PdfFileWriter()
            num_files = num_files + 1

    return num_files


def main():
    i = 0
    files = 0
    directory = r'/Users/heron/PDFS'
    for entry in os.scandir(directory):
        if entry.path.endswith(".pdf"):
            i = i + 1
            files += pdf_splitter(entry.path, 5)
    print('Processed {} files'.format(i))
    print('Created {} files'.format(files))


if __name__ == '__main__':
    main()
