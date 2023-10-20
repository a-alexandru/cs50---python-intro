class Add:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        ... 

    def adding(self):
        result = self.a + self.b
        return result

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if a > 10:
            raise ValueError
        self._a = a

    

def main():
    
    tt =  Add()
    tt.a = int(input("A:"))
    tt.b = int(input("B:"))

    print(tt.adding())

    

if __name__ == "__main__":
    main()