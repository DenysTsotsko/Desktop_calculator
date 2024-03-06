import sys 

from PySide6 import QtCore, QtGui 
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QPushButton, 
    QLineEdit, 
    QWidget, 
    QVBoxLayout
)



colors = {
    "Dark_gray": "#505050",
    "Light_gray": "#D4D4D2", 
    "Orange": "#FF9500", 
    "Black": "#1C1C1C"
}

operations = {
    '+': add,
    '-': sub,
    'x': mul,
    '÷': truediv
}



class ButtonsGrid(QWidget):

    def __init__(self, text):
        super().__init__()

        def creating_orange_button(self):
            self.button 
    def create_buttons_grid(self):

        # fourth row 
        buttonEquality = QPushButton("C", self)
        buttonEquality.setGeometry(300, 600, 100, 100)
        buttonEquality.setStyleSheet(f"background-color: {colors['Orange']};   border-radius: 50")


        buttonDot = QPushButton(".", self)
        buttonDot.setGeometry(200, 600, 100, 100)
        buttonDot.setStyleSheet(f"background-color: {colors['Dark_gray']};   border-radius: 50")

        buttonZero = QPushButton("0", self)
        buttonZero.setGeometry(0, 600, 200, 100)
        buttonZero.setStyleSheet(f"background-color: {colors['Dark_gray']};   border-radius: 50")


    # third row 
        buttonPLus = QPushButton("+", self)
        buttonPLus.setGeometry(300, 500, 100, 100)
        buttonPLus.setStyleSheet(f"background-color: {colors['Orange']}; border-radius: 50")
        
        buttonThree = QPushButton("3", self)
        buttonThree.setGeometry(200, 500, 100, 100)
        buttonThree.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")
            
        buttonTwo = QPushButton("2", self)
        buttonTwo.setGeometry(100, 500, 100, 100)
        buttonTwo.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")

        buttonOne = QPushButton("1", self)
        buttonOne.setGeometry(0, 500, 100, 100)
        buttonOne.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")


    # second row 
        buttonMinus = QPushButton("-", self)
        buttonMinus.setGeometry(300, 400, 100, 100)
        buttonMinus.setStyleSheet(f"background-color: {colors['Orange']};   border-radius: 50")
        
        buttonSix = QPushButton("6", self)
        buttonSix.setGeometry(200, 400, 100, 100)
        buttonSix.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")
            
        buttonFive = QPushButton("5", self)
        buttonFive.setGeometry(100, 400, 100, 100)
        buttonFive.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")

        buttonFour = QPushButton("4", self)
        buttonFour.setGeometry(0, 400, 100, 100)
        buttonFour.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")


    # first row
        buttonX = QPushButton("X", self)
        buttonX.setGeometry(300, 300, 100, 100)
        buttonX.setStyleSheet(f"background-color: {colors['Orange']};   border-radius: 50")
        
        buttonNine = QPushButton("9", self)
        buttonNine.setGeometry(200, 300, 100, 100)
        buttonNine.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")
            
        buttonNine = QPushButton("8", self)
        buttonNine.setGeometry(100, 300, 100, 100)
        buttonNine.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")

        buttonSeven = QPushButton("7", self)
        buttonSeven.setGeometry(0, 300, 100, 100)
        buttonSeven.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")



    # Zeros row 
        buttonDivision = QPushButton("/", self)
        buttonDivision.setGeometry(300, 200, 100, 100)
        buttonDivision.setStyleSheet(f"background-color: {colors['Orange']};   border-radius: 50")
        
        buttonPercent = QPushButton("%", self)
        buttonPercent.setGeometry(200, 200, 100, 100)
        buttonPercent.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")
            
        buttonPlusorMinus = QPushButton("+/-", self)
        buttonPlusorMinus.setGeometry(100, 200, 100, 100)
        buttonPlusorMinus.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")

        buttonAC = QPushButton("AC", self)
        buttonAC.setGeometry(0, 200, 100, 100)
        buttonAC.setStyleSheet(f"background-color:{colors['Dark_gray']};   border-radius: 50")

        return (buttonEquality)




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 60, 400, 700) # setting up the size of the window (left, top, width, height) or (x, y, w, h)
        self.main_layout = QVBoxLayout()

        

        self.create_buttons_grid()


    
        



    def button_click(self):
        pass 


    def add_digits(self):
        pass 


def main() -> None:

    # creating pyqt app
    app = QApplication(sys.argv)
    
    # creating the object from our MainWindow class 
    window = MainWindow()
    window.setStyleSheet(f"background-color: {colors['Black']}")
    window.show()

    # exit after pressing exit button on the application 
    sys.exit(app.exec())



if __name__ == "__main__":
    main()
    