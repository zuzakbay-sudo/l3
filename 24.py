class StringHandler:
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())


# Create object
obj = StringHandler()

# Call methods
obj.getString()
obj.printString()
