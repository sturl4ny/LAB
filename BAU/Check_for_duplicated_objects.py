import ldif
import json

class MyParser(ldif.LDIFParser):
    def __init__(self, input_file):
        super().__init__(input_file)
        self.results = []

    def handle(self, dn, entry):
        # This function runs for every record found
        clean_entry = {'dn': dn}
        for key, values in entry.items():
            # Decode bytes to strings
            decoded = [v.decode('utf-8', errors='ignore') if isinstance(v, bytes) else v for v in values]
            clean_entry[key] = decoded[0] if len(decoded) == 1 else decoded
        self.results.append(clean_entry)

def convert_ldif_to_json(input_filename):
    with open(r"C:\TMP\users.ldif", 'rb') as f:
        parser = MyParser(f)
        parser.parse() # This triggers the 'handle' function above
        return parser.results