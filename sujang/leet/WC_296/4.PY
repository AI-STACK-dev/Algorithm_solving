class TextEditor:

    def __init__(self):
       self.text = ""
       self.cursorIndex = 0

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursorIndex] + text + self.text[self.cursorIndex:]
        self.cursorIndex += len(text)
        
    def deleteText(self, k: int) -> int:
        snapshotIndex = self.cursorIndex
        tempCusorIndex = max(0, self.cursorIndex-k)
        self.text = self.text[:tempCusorIndex] + self.text[self.cursorIndex:]
        self.cursorIndex = tempCusorIndex
        return min(k, snapshotIndex)

    def cursorLeft(self, k: int) -> str:
        self.cursorIndex = max(0, self.cursorIndex - k)
        return self.text[max(self.cursorIndex-10,0):self.cursorIndex]
        

    def cursorRight(self, k: int) -> str:
        self.cursorIndex = min(len(self.text), self.cursorIndex + k)
        return self.text[max(self.cursorIndex-10,0):self.cursorIndex]



textEditor = TextEditor()
print(textEditor.addText("leetcode"))
print(textEditor.text)
print(textEditor.cursorIndex)
print(textEditor.deleteText(4)); 
print(textEditor.text)
print(textEditor.cursorIndex)
print(textEditor.addText("practice")); 
print(textEditor.text)
print(textEditor.cursorIndex)
print(textEditor.cursorRight(3));
print(textEditor.text)
print(textEditor.cursorIndex)
print(textEditor.cursorLeft(8));
print(textEditor.text)
print(textEditor.cursorIndex)
print("-------")
print(textEditor.deleteText(10));
print(textEditor.text)
print(textEditor.cursorIndex)
print("-------")
print(textEditor.cursorLeft(2));
print(textEditor.text)
print(textEditor.cursorIndex)
print(textEditor.cursorRight(6));


