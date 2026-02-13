from abc import abstractmethod

class Printer:
    @abstractmethod
    def print_document(self, document): 
        pass
class Scanner:
    @abstractmethod
    def scan_document(self, document): 
        pass
class Fax:
    @abstractmethod
    def fax_document(self, document): 
        pass

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print("Printing document...")
    def scan(self, document):
        print("Scanning document...")
    def fax(self, document):
        print("Faxing document...")