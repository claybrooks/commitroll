import sys
import os
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "commitroll")))

import commitroll
import commitable
import factory

class TextField:
    def __init__(self):
        self.text = None

    @commitable.Commit
    def setText(self, text):
        self.text = text
        print ("TextField: Set Text to " + (text if text is not None else "None") + "!")

    def print(self):
        print (self.text)

@commitable.CommitAll
class Button:
    def __init__(self):
        self.color = None
        self.text = None

    @commitable.NoCommit
    def print(self):
        print (f"Button: {self.color=}, {self.text=}")

    def setColor(self, color):
        self.color = color
        print ("Button: Set Color to " + (color if color is not None else "None") + "!")

    def setText(self, text):
        self.text = text
        print ("Button: Set Text to " + (text if text is not None else "None") + "!")


def main():

    fact = factory.Factory(commitroll.CommitRoll())
    executor = fact.executor

    textfield = fact.create(TextField)
    button = fact.create(Button)

    textfield.setText("Hello World")
    button.setColor("red")
    textfield.setText("Good Bye World")
    button.setText("fml")
    button.setColor("black")
    button.setColor("green")
    textfield.setText("Ok, done")

    print ("Roll Backward")
    for i in range(7):
        if executor.roll_backward():
            textfield.print()
            button.print()

    print ("Roll Forward")
    for i in range(10):
        if executor.roll_forward():
            textfield.print()
            button.print()


if __name__ == '__main__':
    main()
