import sys
import os

from sort import Sort
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QProgressBar,
    QToolBar,
    QLineEdit,
    QVBoxLayout, 
    QFileDialog,
    QWidget,
    QHBoxLayout,
    QMessageBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Strength Test")

        global dataToBeSorted
        dataToBeSorted = []
        global requirements
        requirements = [False, False, [False, False, False, False]]

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimumWidth(500)
        self.progressBar.setMaximumWidth(500)
        self.progressBar.setValue(0)
        
        button_action = QAction(QIcon("folder-open.png"), "Open Folder", self)
        button_action.setStatusTip("Open Directory")
        button_action.triggered.connect(self.openFileDialog)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        toolbar.addSeparator()
        
        button_action1 = QAction(QIcon("sort.png"), "&Sort", self)
        button_action1.setStatusTip("Sort Data in Dictionary")
        button_action1.triggered.connect(self.sortTheData)
        button_action1.setCheckable(True)
        toolbar.addAction(button_action1)
        
        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon("question.png"), "&Help", self)
        button_action2.setStatusTip("Help with this Program")
        button_action2.triggered.connect(self.helpMessage)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        
        toolbar.addSeparator()
        
        button_action3 = QAction(QIcon("cross.png"), "&Exit", self)
        button_action3.setStatusTip("Quit program")
        button_action3.triggered.connect(QApplication.instance().quit)
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)

        self.label = QLabel("Password Strength Checker")
        labelFont = self.label.font()
        labelFont.setPointSize(20)
        labelFont.setBold(True)
        self.label.setFont(labelFont)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label2 = QLabel("Password Minimum Requirement")
        labelFont2 = self.label2.font()
        labelFont2.setPointSize(16)
        self.label2.setFont(labelFont2)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label3 = QLabel("• At least 10 characters in length")
        labelFont3 = self.label3.font()
        labelFont3.setPointSize(14)
        self.label3.setFont(labelFont3)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label4 = QLabel("• Contains 3/4 of following items")
        labelFont4 = self.label4.font()
        labelFont4.setPointSize(14)
        self.label4.setFont(labelFont4)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label5 = QLabel("  -- Uppercase letters")
        labelFont5 = self.label5.font()
        labelFont5.setPointSize(14)
        self.label5.setFont(labelFont5)
        
        self.label6 = QLabel("  -- Lowercase letters")
        labelFont6 = self.label6.font()
        labelFont6.setPointSize(14)
        self.label6.setFont(labelFont6)
        
        self.label7 = QLabel("  -- Digits")
        labelFont7 = self.label7.font()
        labelFont7.setPointSize(14)
        self.label7.setFont(labelFont7)
        
        self.label8 = QLabel("  -- Special Characters")
        labelFont8 = self.label8.font()
        labelFont8.setPointSize(14)
        self.label8.setFont(labelFont8)
        
        self.label9 = QLabel("• Not a composition of one or two dictionary words")
        labelFont9 = self.label9.font()
        labelFont9.setPointSize(14)
        self.label9.setFont(labelFont8)
        self.label9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.userChangedText)
        self.input.setMaximumWidth(400)
        
        
        layout = QVBoxLayout()
        inputLayout = QHBoxLayout()
        horiHelper = QHBoxLayout()
        horiHelper1 = QHBoxLayout()
        horiHelper2 = QHBoxLayout()
        horiHelper3 = QHBoxLayout()

        hori = QWidget()
        hori1 = QWidget()
        hori2 = QWidget()
        hori3 = QWidget()
        criteriaLayout = QVBoxLayout()
        criteriaItem1 = QHBoxLayout()
        Item1 = QWidget()
        criteriaItem2 = QHBoxLayout()
        Item2 = QWidget()
        criteriaItem3 = QHBoxLayout()
        Item3 = QWidget()
        criteriaItem4 = QHBoxLayout()
        Item4 = QWidget()
        
        
        
        criteriaItem1.addWidget(self.label5)
        self.checkMark2 = QLabel("✓")
        self.checkMark2.hide()
        criteriaItem1.addWidget(self.checkMark2)
        criteriaItem1.addStretch()
        Item1 = QWidget()
        Item1.setLayout(criteriaItem1)
        
        criteriaItem2.addWidget(self.label6)
        self.checkMark3 = QLabel("✓")
        self.checkMark3.hide()
        criteriaItem2.addWidget(self.checkMark3)
        criteriaItem2.addStretch()
        Item2 = QWidget()
        Item2.setLayout(criteriaItem2)
        
        criteriaItem3.addWidget(self.label7)
        self.checkMark4 = QLabel("✓")
        self.checkMark4.hide()
        criteriaItem3.addWidget(self.checkMark4)
        criteriaItem3.addStretch()
        Item3 = QWidget()
        Item3.setLayout(criteriaItem3)
        
        criteriaItem4.addWidget(self.label8)
        self.checkMark5 = QLabel("✓")
        self.checkMark5.hide()
        criteriaItem4.addWidget(self.checkMark5)
        criteriaItem4.addStretch()
        Item4 = QWidget()
        Item4.setLayout(criteriaItem4)
        
        criteriaLayout.addWidget(Item1)
        criteriaLayout.addWidget(Item2)
        criteriaLayout.addWidget(Item3)
        criteriaLayout.addWidget(Item4)
        criteria = QWidget()
        criteria.setMaximumWidth(300)
        criteria.setLayout(criteriaLayout)
        
        horiHelper.addStretch()
        horiHelper.addWidget(criteria)
        horiHelper.addStretch()
        hori.setLayout(horiHelper)
        
        inputLayout.addStretch
        inputLayout.addWidget(self.input)
        inputLayout.addStretch
        inputContainer = QWidget()
        inputContainer.setLayout(inputLayout)
        
        horiHelper3.addStretch()
        horiHelper3.addWidget(self.progressBar)
        horiHelper3.addStretch()
        hori3.setLayout(horiHelper3)
        
        horiHelper1.addStretch()
        horiHelper1.addWidget(self.label3)
        self.checkMark1 = QLabel("✓")
        self.checkMark1.hide()
        horiHelper1.addWidget(self.checkMark1)
        horiHelper1.addStretch()
        hori1.setLayout(horiHelper1)
        
        horiHelper2.addStretch()
        horiHelper2.addWidget(self.label9)
        self.checkMark8 = QLabel("✓")
        self.checkMark8.hide()
        horiHelper2.addWidget(self.checkMark8)
        horiHelper2.addStretch()
        hori2.setLayout(horiHelper2)
        
        
        
        layout.addWidget(self.label)
        layout.addWidget(inputContainer)
        layout.addWidget(hori3)
        layout.addWidget(self.label2)
        layout.addWidget(hori1)
        layout.addWidget(self.label4)
        layout.addWidget(hori)
        layout.addWidget(hori2)
        layout.addStretch()

        container = QWidget()
        
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setStatusBar(QStatusBar(self))
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File")
        
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action1)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        exit_menu = menu.addMenu("&Exit")
        exit_menu.addAction(button_action3)
        

    def openFileDialog(self):
        dataToBeSorted.clear()
        fileName = QFileDialog.getOpenFileName(self, str("Open Text File"), os.getcwd(), str("Text Files (*.txt)"))
        if fileName[0]:
            with open(fileName[0], 'r') as file:
                for line in file:
                    dataToBeSorted.append(line.strip())
        
    
    def sortTheData(self):
        Sort.mergeSort(dataToBeSorted, 0, len(dataToBeSorted)-1)

    def helpMessage(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Help")
        dialog.setText("""
To properly use test password strength, you must compare the password to the common password text files.

1. Open the file directory in the program.

2. Select a text file to use from the `text_files` directory.

3. Sort the text file by pressing the sort button in the program (found next to the folder icon in the program).

4. That's all. Happy testing!

                       """)
        button = dialog.exec()

    def userChangedText(self):
        input_text = self.input.text()
        value = self.progressBar.value()
        
        if any(char.isupper() for char in input_text):
            value = self.progressBar.value()
            self.checkMark2.show()
            if(requirements[2][0] != True):
                if not(requirements[2][1] and requirements[2][2] and requirements[2][3]):
                    self.progressBar.setValue(value + 20)
            requirements[2][0] = True
        else:
            value = self.progressBar.value()
            self.checkMark2.hide()
            if requirements[2][0] == True and (value - 20) <= 0:
                self.progressBar.setValue(0)
            else:
                if(requirements[2][0] == True):
                    if not(requirements[2][1] and requirements[2][2] and requirements[2][3]):
                        self.progressBar.setValue(value - 20)
            requirements[2][0] = False
        
        if any(char.islower() for char in input_text):
            value = self.progressBar.value()
            self.checkMark3.show()
            if(requirements[2][1] != True):
                if not(requirements[2][0] and requirements[2][2] and requirements[2][3]):
                    self.progressBar.setValue(value + 20)
            requirements[2][1] = True
        else:
            value = self.progressBar.value()
            self.checkMark3.hide()
            if requirements[2][1] == True and (value - 20) <= 0:
                self.progressBar.setValue(0)
            else:
                if(requirements[2][1] == True):
                    if not(requirements[2][0] and requirements[2][2] and requirements[2][3]):
                        self.progressBar.setValue(value - 20)
            requirements[2][1] = False
        
        # Check for digits and show checkMark4
        if any(char.isdigit() for char in input_text):
            value = self.progressBar.value()
            self.checkMark4.show()
            if(requirements[2][2] != True):
                if not(requirements[2][0] and requirements[2][1] and requirements[2][3]):
                    self.progressBar.setValue(value + 20)
            requirements[2][2] = True
        else:
            value = self.progressBar.value()
            self.checkMark4.hide()
            if requirements[2][2] == True and (value - 20) <= 0:
                self.progressBar.setValue(0)
            else:
                if requirements[2][2] == True:
                    if not (requirements[2][0] and requirements[2][1] and requirements[2][3]):
                        self.progressBar.setValue(value - 20)
            requirements[2][2] = False
        
        # Check for special characters and show checkMark5
        if any(not char.isalnum() for char in input_text):
            value = self.progressBar.value()
            self.checkMark5.show()
            if(requirements[2][3] != True):
                if not(requirements[2][0] and requirements[2][1] and requirements[2][2]):
                    self.progressBar.setValue(value + 20)
            requirements[2][3] = True
        else:
            value = self.progressBar.value()
            self.checkMark5.hide()
            if requirements[2][3] == True and (value - 20) <= 0:
                self.progressBar.setValue(0)
            else:
                if requirements[2][3] == True:
                    if not(requirements[2][0] and requirements[2][1] and requirements[2][2]):
                        self.progressBar.setValue(value - 20)
            requirements[2][3] = False
        
        # Check for length of input text and show checkMark1
        if len(input_text) >= 10:
            value = self.progressBar.value()
            self.checkMark1.show()
            if(requirements[0] != True):
                self.progressBar.setValue(value + 20)
            requirements[0] = True
        else:
            value = self.progressBar.value()
            self.checkMark1.hide()
            if requirements[0] == True and (value - 20) <= 0:
                self.progressBar.setValue(0)
            else:
                if requirements[0] == True:
                    self.progressBar.setValue(value - 20)
            requirements[0] = False
        
        # Check if current input is a composition of one-two dictionary words or not.
        if(len(dataToBeSorted) != 0):
            is_composed_of_words = self.is_composed_of_dictionary_words(self.getLinearSubstrings(input_text))
            if (is_composed_of_words == False) and (len(input_text) > 0) :
                value = self.progressBar.value()
                self.checkMark8.show()
                if(requirements[1] != True):
                    self.progressBar.setValue(value + 20)
                requirements[1] = True
            else:
                value = self.progressBar.value()
                if requirements[1] == True and (value - 20) <= 0:
                    self.progressBar.setValue(0)
                else:
                    if requirements[1] == True:
                        self.progressBar.setValue(value - 20)
                self.checkMark8.hide()
                requirements[1] = False
                
            if len(input_text) == 0:
                self.progressBar.setValue(0)
    
    def is_composed_of_dictionary_words(self, substrings):
        wordFoundCount = 0
        for word in substrings:
            if(self.binarySearch(word) != -1):
                wordFoundCount += 1
        return wordFoundCount > 0
    
    def getLinearSubstrings(self, text):
        substrings = []
        text_length = len(text)

        for start in range(text_length):
            for end in range(start + 1, text_length + 1):
                substring = text[start:end]
                if len(substring) >= 3:
                    substrings.append(substring)

        return substrings
    
    def binarySearch(self, target):
        low = 0
        high = len(dataToBeSorted) - 1
        while low <= high:
            mid = (low+high) // 2
            if dataToBeSorted[mid].lower() < target.lower():
                low = mid + 1
            elif dataToBeSorted[mid].lower() > target.lower():
                high = mid - 1
            else:
                #print(dataToBeSorted[mid])
                return mid
        return -1
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()