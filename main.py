import sys
import os
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from datetime import datetime


class MyApp(QMainWindow):  # Change QMainWindow to QWidget
    def __init__(self):
        super(MyApp, self).__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(current_dir, 'PKNR.ui')
        loadUi(ui_file, self)

        self.core_state = 0

        for i in range(1, 21):
            setattr(self, f'G{i}_state', 0)

        for i in range(1, 5):
            setattr(self, f'R{i}_state', 0)

        for i in range(1, 5):
            setattr(self, f'B{i}_state', 0)

        for i in range(1, 9):
            setattr(self, f'Y{i}_state', 0)

        self.user = "Mubeen"
        # Connect buttons to methods
        self.UR235.clicked.connect(self.core_control)

        self.R1.clicked.connect(lambda: self.red_em_rods_control(1))
        self.R2.clicked.connect(lambda: self.red_em_rods_control(2))
        self.R3.clicked.connect(lambda: self.red_em_rods_control(3))
        self.R4.clicked.connect(lambda: self.red_em_rods_control(4))

        self.Y1.clicked.connect(lambda: self.yellow_em_rods_control(1))
        self.Y2.clicked.connect(lambda: self.yellow_em_rods_control(2))
        self.Y3.clicked.connect(lambda: self.yellow_em_rods_control(3))
        self.Y4.clicked.connect(lambda: self.yellow_em_rods_control(4))
        self.Y5.clicked.connect(lambda: self.yellow_em_rods_control(5))
        self.Y6.clicked.connect(lambda: self.yellow_em_rods_control(6))
        self.Y7.clicked.connect(lambda: self.yellow_em_rods_control(7))
        self.Y8.clicked.connect(lambda: self.yellow_em_rods_control(8))

        self.B1.clicked.connect(lambda: self.blue_ac_rods_control(1))
        self.B2.clicked.connect(lambda: self.blue_ac_rods_control(2))
        self.B3.clicked.connect(lambda: self.blue_ac_rods_control(3))
        self.B4.clicked.connect(lambda: self.blue_ac_rods_control(4))

        self.G1.clicked.connect(lambda: self.green_control_rods_control(1))
        self.G2.clicked.connect(lambda: self.green_control_rods_control(2))
        self.G3.clicked.connect(lambda: self.green_control_rods_control(3))
        self.G4.clicked.connect(lambda: self.green_control_rods_control(4))
        self.G5.clicked.connect(lambda: self.green_control_rods_control(5))
        self.G6.clicked.connect(lambda: self.green_control_rods_control(6))
        self.G7.clicked.connect(lambda: self.green_control_rods_control(7))
        self.G8.clicked.connect(lambda: self.green_control_rods_control(8))
        self.G9.clicked.connect(lambda: self.green_control_rods_control(9))
        self.G10.clicked.connect(lambda: self.green_control_rods_control(10))
        self.G11.clicked.connect(lambda: self.green_control_rods_control(11))
        self.G12.clicked.connect(lambda: self.green_control_rods_control(12))
        self.G13.clicked.connect(lambda: self.green_control_rods_control(13))
        self.G14.clicked.connect(lambda: self.green_control_rods_control(14))
        self.G15.clicked.connect(lambda: self.green_control_rods_control(15))
        self.G16.clicked.connect(lambda: self.green_control_rods_control(16))
        self.G17.clicked.connect(lambda: self.green_control_rods_control(17))
        self.G18.clicked.connect(lambda: self.green_control_rods_control(18))
        self.G19.clicked.connect(lambda: self.green_control_rods_control(19))
        self.G20.clicked.connect(lambda: self.green_control_rods_control(20))

        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        if self.core_state == 0:
            self.statecore.setText(f"{formatted_datetime}: OFF")
        if self.core_state == 1:
            self.statecore.setText(f"{formatted_datetime}: ON")

    def green_control_rods_control(self, i):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle(f"Change G{i} State?")
        confirmation_box.setText("Are you sure you want to proceed?")
        confirmation_box.setIcon(QMessageBox.Question)

        # Add Yes and No buttons
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Show the confirmation box and capture the response
        response = confirmation_box.exec_()

        self.current_green_control_rod_state = getattr(self, f'G{i}_state')

        if response == QMessageBox.Yes:
            if self.current_green_control_rod_state == 0:
                setattr(self, f'G{i}_state', 1)
                on_message = f"{formatted_datetime}: G{i} Turned On by User: {self.user}"
                self.rodlog.append(on_message)


            elif self.current_green_control_rod_state == 1:
                setattr(self, f'G{i}_state', 0)
                off_message = f"{formatted_datetime}: G{i} Turned Off by User: {self.user}"
                self.rodlog.append(off_message)

        else:
            cancel_message = f"{formatted_datetime}: User {self.user} denied Rod G{i} State Change."
            self.rodlog.append(cancel_message)
            return

    def red_em_rods_control(self, i):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle(f"Change R{i} State?")
        confirmation_box.setText("Are you sure you want to proceed?")
        confirmation_box.setIcon(QMessageBox.Question)

        # Add Yes and No buttons
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Show the confirmation box and capture the response
        response = confirmation_box.exec_()

        self.current_red_em_rod_state = getattr(self, f'R{i}_state')

        if response == QMessageBox.Yes:
            if self.current_red_em_rod_state == 0:
                setattr(self, f'R{i}_state', 1)
                on_message = f"{formatted_datetime}: R{i} Turned On by User: {self.user}"
                self.rodlog.append(on_message)


            elif self.current_red_em_rod_state == 1:
                setattr(self, f'R{i}_state', 0)
                off_message = f"{formatted_datetime}: R{i} Turned Off by User: {self.user}"
                self.rodlog.append(off_message)
        else:
            cancel_message = f"{formatted_datetime}: User {self.user} denied Rod R{i} State Change."
            self.rodlog.append(cancel_message)
            return

    def blue_ac_rods_control(self, i):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle(f"Change B{i} State?")
        confirmation_box.setText("Are you sure you want to proceed?")
        confirmation_box.setIcon(QMessageBox.Question)

        # Add Yes and No buttons
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Show the confirmation box and capture the response
        response = confirmation_box.exec_()

        self.current_blue_ac_rod_state = getattr(self, f'B{i}_state')

        if response == QMessageBox.Yes:
            if self.current_blue_ac_rod_state == 0:
                setattr(self, f'B{i}_state', 1)
                on_message = f"{formatted_datetime}: B{i} Turned On by User: {self.user}"
                self.rodlog.append(on_message)

            elif self.current_blue_ac_rod_state == 1:
                setattr(self, f'B{i}_state', 0)
                off_message = f"{formatted_datetime}: B{i} Turned Off by User: {self.user}"
                self.rodlog.append(off_message)
        else:
            cancel_message = f"{formatted_datetime}: User {self.user} denied Rod B{i} State Change."
            self.rodlog.append(cancel_message)
            return

    def yellow_em_rods_control(self, i):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle(f"Change Y{i} State?")
        confirmation_box.setText("Are you sure you want to proceed?")
        confirmation_box.setIcon(QMessageBox.Question)

        # Add Yes and No buttons
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Show the confirmation box and capture the response
        response = confirmation_box.exec_()

        self.current_yellow_em_rod_state = getattr(self, f'Y{i}_state')

        if response == QMessageBox.Yes:
            if self.current_yellow_em_rod_state == 0:
                setattr(self, f'Y{i}_state', 1)
                on_message = f"{formatted_datetime}: Y{i} Turned On by User: {self.user}"
                self.rodlog.append(on_message)

            elif self.current_yellow_em_rod_state == 1:
                setattr(self, f'Y{i}_state', 0)
                off_message = f"{formatted_datetime}: Y{i} Turned Off by User: {self.user}"
                self.rodlog.append(off_message)
        else:
            cancel_message = f"{formatted_datetime}: User {self.user} denied Rod Y{i} State Change."
            self.rodlog.append(cancel_message)
            return

    def core_control(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle("Change Core State?")
        confirmation_box.setText("Are you sure you want to proceed?")
        confirmation_box.setIcon(QMessageBox.Question)

        # Add Yes and No buttons
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Show the confirmation box and capture the response
        response = confirmation_box.exec_()

        if response == QMessageBox.Yes:
            if self.core_state == 0:
                self.core_state = 1
                on_message = f"{formatted_datetime}: Main Core Turned On by User: {self.user}"
                self.corelog.append(on_message)
                on = f"{formatted_datetime}: ON"
                self.statecore.setText(on)

            elif self.core_state == 1:
                self.core_state = 0
                off_message = f"{formatted_datetime}: Main Core Turned Off by User: {self.user}"
                self.corelog.append(off_message)
                off = f"{formatted_datetime}: OFF"
                self.statecore.setText(off)
        else:
            cancel_message = f"{formatted_datetime}: User {self.user} denied Core State Change."
            self.corelog.append(cancel_message)
            return


app = QApplication(sys.argv)
mainwindow = MyApp()
widget = QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1600)
widget.setFixedHeight(900)
widget.setWindowTitle("PKNR")
widget.show()
app.exec_()
