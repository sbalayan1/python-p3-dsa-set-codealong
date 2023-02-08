class MySet:
    pass

#what does the __init__ method need? What do we typically initialize a set with?
        #use a dictionary to store the values. 
        #length or size variable
    def __init__(self, values=[]):
        pass
        self.dictionary = {}
        for value in values:
            if value not in self.dictionary:
                self.dictionary[value] = 1


#what instance methods should a set have?
    #add
    def add(self, value):
        pass
        if not self.has(value): self.dictionary[value] = 1
        return self


    #has
    def has(self, value):
        pass
        return value in self.dictionary


    #delete
    def delete(self, value):
        pass
        if self.has(value): del self.dictionary[value]
        return self

    #size
    def size(self):
        pass
        return len(self.dictionary)

    def clear(self):
        self.dictionary = {}
        return self

    def __str__(self):
        pass
        values = ",".join([str(val) for val in self.dictionary.keys()])
        return f"MySet: {{{values}}}"

