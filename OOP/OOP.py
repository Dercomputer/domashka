class Matrix:

    def __init__(self, lines: int = 0, pillars: int = 0, elements: list = [], vid: int = 1):
        self.lines = lines
        self.pillars = pillars
        self.elements = elements
        self.vid = vid

    def __str__(self):
        output = ''
        for j in range(self.lines):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output

    def input_matrix(self):
        self.lines, self.pillars = int(input("Count lines: ")), int(input("Count pillars: "))
        for i in range(self.lines):
            self.elements.append(list(map(int, input(f"string {i + 1}: ").split())))
            print(self.elements)
            if len(self.elements[i]) != self.pillars:
                raise ValueError("НЕКОРРЕКТНЫЙ ВВОД")


n = Matrix()
n.input_matrix()
print(n)
