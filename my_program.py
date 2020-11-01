import sys

from FileOperation import JSONWriter
from FileOperation import PDFReader
from Parser import CommandLineParser
from Parser import PDFParser

if __name__ == '__main__':
    parser = CommandLineParser(sys.argv[1:])
    input_file, output_file = parser.parse()

    pdf_reader = PDFReader(input_file)
    pdf_content = pdf_reader.read()

    pdf_parser = PDFParser(pdf_content)

    data_dict = {'name': pdf_parser.parse('name'),
                 'address': pdf_parser.parse('address'),
                 'email': pdf_parser.parse('email'),
                 'Education': pdf_parser.parse('Education', r'Education(.*)Leadership Experience'),
                 'Leadership Experience': pdf_parser.parse('Leadership Experience',
                                                           r'Leadership Experience(.*)Professional Experience'),
                 'Professional Experience': pdf_parser.parse('Professional Experience',
                                                             r'Professional Experience(.*)Additional Projects'),
                 'Additional Projects': pdf_parser.parse('Additional Projects',
                                                         r'Additional Projects(.*)Skills & Interests'),
                 'Skills & Interests': pdf_parser.parse('Skills & Interests',
                                                        r'Skills & Interests(.*)$')}

    json_writer = JSONWriter(output_file)
    json_writer.write(data_dict)
