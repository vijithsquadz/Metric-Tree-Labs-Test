import getopt
import re


class CommandLineParser:

    def __init__(self, argv):
        self.argv = argv

    def parse(self):
        input_file = None
        output_file = None

        try:

            if len(self.argv) != 4:
                raise Exception("Usage: python my_program.py --input  in_file.pdf  --output  out_file.json")

            opts, args = getopt.getopt(self.argv, None, ["input=", "output="])
            for opt, arg in opts:
                if opt == '--input':
                    input_file = arg
                elif opt == '--output':
                    output_file = arg
                else:
                    raise Exception("Usage: python my_program.py --input  in_file.pdf  --output  out_file.json")

            if not (input_file.strip().endswith('.pdf') and output_file.strip().endswith('.json')):
                raise Exception("Usage: python my_program.py --input  in_file.pdf  --output  out_file.json")

            return input_file, output_file

        except getopt.GetoptError:
            raise Exception("Usage: python my_program.py --input  in_file.pdf  --output  out_file.json")


class PDFParser:

    def __init__(self, content):
        self.content = content

    def parse(self, section, pattern=None) -> str:
        if section == "name":
            return re.search(r'^(.*)\n', self.content).group().strip()
        elif section == "address":
            add_1 = re.search(r'(.*?)\|', self.content).groups()[0].strip()
            regex_pattern = re.compile(r'\|(?=.*\|(.*)Education)', re.DOTALL)
            add_2 = regex_pattern.search(self.content).groups()[0].strip()
            return add_1 + ", " + add_2
        elif section == "email":
            return re.search(r'\|(.*)\|', self.content).groups()[0].strip()
        else:
            regex_pattern = re.compile(pattern, re.DOTALL)
            return re.sub(r'_+|\n| {2,}| \n', '', regex_pattern.search(self.content).groups()[0])
