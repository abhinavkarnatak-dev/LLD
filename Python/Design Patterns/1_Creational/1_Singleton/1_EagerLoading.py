# Thread safe

class Printer:
    def print_documents(self, text):
        print(text)

printer = Printer() # Instance created already, use it whenever you need

# Same printer object is used
printer.print_documents("Text 1")
printer.print_documents("Text 2")