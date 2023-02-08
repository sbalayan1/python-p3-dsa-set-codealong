class MySet:
    pass

#what does the __init__ method need? What do we typically initialize a set with?
        #use a dictionary to store the values. 
        #length or size variable
    def __init__(self, values=[]):
        pass
        self.dictionary = {}
        self.length = len(values)
        for value in values:
            if value not in self.dictionary:
                self.dictionary[value] = 1


#what instance methods should a set have?
    #add
    def add(self, value):
        pass
        if not self.has(value): self.dictionary[value] = 1


    #has
    def has(self, value):
        pass
        return True if value in self.dictionary else False


    #delete
    def delete(self, value):
        pass
        if self.has(value): del self.dictionary[value]

    #size
    def size(self):
        pass
        return self.length

