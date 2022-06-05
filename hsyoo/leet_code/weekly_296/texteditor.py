class TextEditor:

    def __init__(self):
        self.s = ''
        self.cursor = 0

    def addText(self, text):
        self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k):
        new_cursor = max(0, self.cursor - k)
        delete_s = k if self.cursor - k >= 0 else self.cursor
        self.s = self.s[:new_cursor] + self.s[self.cursor:]
        self.cursor = new_cursor
        return delete_s

    def cursorLeft(self, k):
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor-10)
        return self.s[start:self.cursor]
    
    def cursorRight(self, k):
        self.cursor = min(len(self.s), self.cursor + k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]

obj = TextEditor()
obj.addText('leetcode')
# print(obj.s)
print(obj.deleteText(4))
print(obj.s)
print(obj.)