class WindowsButton:
    def click(self):
        return "windows button clicked"

class MacButton:
    def click(self):
        return "Mac button clicked"

def buttonfactory(op_system):
    if op_system == "Windows":
        return WindowsButton()
    elif op_system == "Mac":
        return MacButton()
b = buttonfactory("Mac")   
print(buttonfactory("Windows").click())