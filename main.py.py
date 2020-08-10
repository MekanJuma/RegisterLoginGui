import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sqlite3


class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setUI()
        self.setGeometry(0, 0, 1350, 690)

    def setUI(self):
        self.setWindowIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\computer.png"))
        self.setWindowTitle("Programming")
        self.setAutoFillBackground(True)
        self.setstyle = "background-color: #292f45;"
        self.setStyleSheet(self.setstyle)

        self.s = QScrollArea()
        self.s.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.s.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget = QWidget(self.s)

        # ========= Menu Area =============
        menu = self.menuBar()
        menu.setObjectName("menu")
        menu.setStyleSheet("""
            background-color: #FF6619; spacing: 3px; color: #ccfff7; font-size: 16px;
        """)

        file = menu.addMenu("File")
        edit = menu.addMenu("Edit")
        view = menu.addMenu("View")
        tool = menu.addMenu("Tools")
        helps = menu.addMenu("Help")

        new_file = QAction("New File", self)
        new_file.setShortcut("Ctrl+N")
        new_file.setIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\new.ico"))

        file.addAction(new_file)

        print = QAction("Print", self)
        print.setShortcut("Ctrl+P")
        print.setIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\print.ico"))

        file.addAction(print)

        settings = file.addMenu("Settings")
        settings.setIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\setting.ico"))

        settings.addAction("Sound set")
        settings.addAction("View set")

        clean = QAction("Clean", self)
        edit.addAction("Cut")
        edit.addAction("Copy")
        edit.addAction("Paste")
        edit.addAction(clean)

        file.triggered[QAction].connect(self.do)

        self.frame = QFrame(self.s)
        # self.frame.setStyleSheet("background-color: yellow;")

        h_box = QHBoxLayout()
        h_box.addWidget(self.frame)
        # self.btn = QPushButton("Mekan", self.frame)
        # self.btn.setStyleSheet("width: 70px; background-color: #ff9900;")

        frame2 = QFrame(self.frame)
        frame2.setFixedWidth(220)

        self.sts = """ 
            QFrame{
                background-color: #292f45;
            }
            QPushButton{
                background-color: #ff9900;
                color: #fff;
                width: 100px;
                border: 1px solid #ff9900;
                border-radius: 12px;
                padding: 6px 4px;
                font-weight: bold;
            }
            QLabel{
                color: white; 
                font-size: 18px; 
                font-family: Impact; 
                background-color: #cc0605; 
                padding-left: 7px;
                margin-top: -5px;
                border-radius: 12px;
            }
            QPushButton::pressed{
                background-color: #fff;
                color: #663300;
            }
            
            QLabel#img{
                background-color: #292f45; 
            }
            
        """
        frame2.setStyleSheet(self.sts)
        image1 = QLabel()
        image1.setObjectName("img")
        imgPix1 = QPixmap("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\pr.png")
        image1.setPixmap(imgPix1.scaled(125, 125, Qt.KeepAspectRatio))
        image1.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        lbl1 = QLabel("Programming Languages")
        lbl1.setFixedHeight(35)
        b1 = QPushButton("Python")
        b1.setCursor(QCursor(Qt.PointingHandCursor))
        b2 = QPushButton("Java")
        b2.setCursor(QCursor(Qt.PointingHandCursor))
        b3 = QPushButton("C++")
        b3.setCursor(QCursor(Qt.PointingHandCursor))

        lbl2 = QLabel("Web Development")
        lbl2.setFixedHeight(35)
        l1 = QPushButton("HTML")
        l1.setCursor(QCursor(Qt.PointingHandCursor))
        l2 = QPushButton("CSS")
        l2.setCursor(QCursor(Qt.PointingHandCursor))
        l3 = QPushButton("Javascript")
        l3.setCursor(QCursor(Qt.PointingHandCursor))
        l4 = QPushButton("Php")
        l4.setCursor(QCursor(Qt.PointingHandCursor))

        lbl3 = QLabel("Python Data Science")
        lbl3.setFixedHeight(35)
        d1 = QPushButton("Data Analyse")
        d1.setCursor(QCursor(Qt.PointingHandCursor))
        d2 = QPushButton("Statistics")
        d2.setCursor(QCursor(Qt.PointingHandCursor))
        d3 = QPushButton("MLE")
        d3.setCursor(QCursor(Qt.PointingHandCursor))
        d4 = QPushButton("Data Visualizer")
        d4.setCursor(QCursor(Qt.PointingHandCursor))

        vb = QVBoxLayout(frame2)
        vb.addWidget(image1)
        vb.addWidget(lbl1)
        vb.addWidget(b1)
        vb.addWidget(b2)
        vb.addWidget(b3)

        vb.addWidget(lbl2)
        vb.addWidget(l1)
        vb.addWidget(l2)
        vb.addWidget(l3)
        vb.addWidget(l4)

        vb.addWidget(lbl3)
        vb.addWidget(d1)
        vb.addWidget(d2)
        vb.addWidget(d3)
        vb.addWidget(d4)

        frame2.setLayout(vb)

        frame3 = QFrame(self.frame)

        image = QLabel()
        imgPix = QPixmap("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\profile.png")
        image.setPixmap(imgPix.scaled(90, 90, Qt.KeepAspectRatio))
        image.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.username_lbl = QLabel("jumayevmekan99@gmail.com")
        # self.username_lbl.setStyleSheet("color: #fff; font-size: 18px; font-family: Impact;")

        lbl_m = QLabel("Software Development")
        lbl_m.setObjectName("m")

        lbl_1 = QLabel("What is Python?")
        lbl_1.setObjectName("big")
        lbl_2 = QLabel("""
        It is used for:
           - web development (server-side),
           - software development,
           - mathematics,
           - system scripting.
        """)
        lbl_3 = QLabel("What can Python do?")
        lbl_3.setObjectName("big")
        lbl_4 = QLabel("""
            - Python can be used on a server to create web applications.
            - Python can be used alongside software to create workflows.
            - Python can connect to database systems. It can also read and modify files.
            - Python can be used to handle big data and perform complex mathematics.
            - Python can be used for rapid prototyping, or for production-ready software development.
        """)
        lbl_5 = QLabel("Why Python?")
        lbl_5.setObjectName("big")
        lbl_6 = QLabel("""
            - Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
            - Python has a simple syntax similar to the English language.
            - Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
            - Python runs on an interpreter system, meaning that code can be executed as soon as it is written.
            - Python can be treated in a procedural way, an object-orientated way or a functional way.
        """)

        self.sts3 = """
            QFrame{
                background-color: #eeff99; 
                height: 70px;
                border-radius: 6px;
            }
            QLabel{
            color: #292f45; 
            font-size: 18px; 
            font-family: Georgia;
            padding-left: 10px;
            }
            QLabel#m{
                font-family: Georgia;
                font-size: 34px;
                color: #7300e6;
                font-weight: bold;
                padding-left: 40px;
            }
            QLabel#big{
                font-weight: bold; 
            }
        """
        frame3.setStyleSheet(self.sts3)
        hb = QHBoxLayout()
        hb.addWidget(lbl_m)
        hb.setAlignment(Qt.AlignTop)

        hb2 = QHBoxLayout()
        hb2.addWidget(self.username_lbl)
        hb2.addWidget(image)
        hb2.setAlignment(Qt.AlignRight | Qt.AlignTop)
        hb.addLayout(hb2)

        vb_m = QVBoxLayout(frame3)
        vb_m.addLayout(hb)
        vb_m.addWidget(lbl_1)
        vb_m.addWidget(lbl_2)
        vb_m.addWidget(lbl_3)
        vb_m.addWidget(lbl_4)
        vb_m.addWidget(lbl_5)
        vb_m.addWidget(lbl_6)

        frame3.setLayout(vb_m)

        # Main HBox
        hb = QHBoxLayout(self.frame)
        hb.addWidget(frame2)
        hb.addWidget(frame3)

        self.frame.setLayout(hb)

        self.s.setLayout(h_box)
        self.setCentralWidget(self.s)

    def do(self, q):
        print(q.text())


# ============ Register Area ====================
class register_window(QMainWindow):
    def __init__(self, parent=None):
        super(register_window, self).__init__(parent)
        self.dialog2 = main_window()
        self.setMaximumSize(QSize(500, 491))
        self.setMinimumSize(QSize(379, 491))
        self.initUI()

    def initUI(self):
        widget = QWidget()

        v_box = QVBoxLayout()

        image = QLabel()
        imgPix = QPixmap("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\register.png")
        image.setPixmap(imgPix.scaled(200, 200, Qt.KeepAspectRatio))
        image.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Username")
        self.name.setAlignment(Qt.AlignTop)

        self.email_r = QLineEdit()
        self.email_r.setPlaceholderText("Email address")
        self.email_r.setAlignment(Qt.AlignTop)

        self.password_r = QLineEdit()
        self.password_r.setEchoMode(QLineEdit.Password)
        self.password_r.setPlaceholderText("Password")
        self.password_r.setAlignment(Qt.AlignTop)

        self.c_password_r = QLineEdit()
        self.c_password_r.setEchoMode(QLineEdit.Password)
        self.c_password_r.setPlaceholderText("Confirm Password")
        self.c_password_r.setAlignment(Qt.AlignTop)

        self.gender = QLabel("Gender")
        self.gender.setStyleSheet("margin: 10px; font-size: 15px;")
        self.rb1 = QRadioButton("Male")
        self.rb1.setCursor(QCursor(Qt.PointingHandCursor))
        # self.rb1.clicked.connect(self.male_clicked)
        self.rb2 = QRadioButton("Female")
        self.rb2.setCursor(QCursor(Qt.PointingHandCursor))
        h_box = QHBoxLayout()
        h_box.addWidget(self.gender)
        h_box.addWidget(self.rb1)
        h_box.addWidget(self.rb2)
        h_box.setAlignment(Qt.AlignTop)

        self.register_r = QPushButton("Register")
        self.register_r.setStyleSheet("margin-bottom: 7px;")
        self.register_r.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_r.clicked.connect(self.Register)

        v_box.addWidget(image)
        v_box.addWidget(self.name)
        v_box.addWidget(self.email_r)
        v_box.addWidget(self.password_r)
        v_box.addWidget(self.c_password_r)
        v_box.addLayout(h_box)
        v_box.addWidget(self.register_r)

        widget.setLayout(v_box)

        self.setCentralWidget(widget)

        return widget

    def Register(self):
        name = self.name.text()
        email = self.email_r.text()
        password = self.c_password_r.text()

        with open("members.txt", "a") as f:
            f.write(f"Username: {name}, Email: {email}, Password: {password}\n")
        msg = QMessageBox.information(self, "Register", "Registered Successfully!")

        self.dialog2.show()
        self.window().destroy()


# ============ Login Area ====================
class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
        self.setWindowIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\lock2.png"))
        self.setWindowTitle("Login")
        self.setStyleSheet(open("main.qss", "r").read())
        self.setMaximumSize(QSize(500, 491))
        self.setMinimumSize(QSize(379, 491))
        self.show()

    def setUI(self):
        m = self.mainWindow()
        self.setCentralWidget(m)

    def connect(self):
        self.email.setText("")
        self.password.setText("")

        self.email1 = str(self.email.text())
        password = str(self.password.text())

        with open("members.txt", "r") as f:
            for i in f:
                if self.email1 in i:
                    ch = 1
                if password in i:
                    ch1 = 1
                if ch == 1 and ch1 == 1:
                    # msg1 = QMessageBox.information(self, "Login", "Logged in Successfully!")
                    self.dialog2.show()
                    self.window().destroy()
                else:
                    msg = QMessageBox.information(self, "Login", "Wrong")

    def connected(self):
        self.dialog.show()
        self.window().destroy()

    def keyPressEvent(self, *args, **kwargs):
        for keys in args:
            if keys.key() == Qt.Key_Return:
                self.login.click()

    def mainWindow(self):
        self.dialog2 = main_window()
        widget = QWidget()

        v_box = QVBoxLayout()

        image = QLabel()
        imgPix = QPixmap("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\lock1.png")
        image.setPixmap(imgPix.scaled(200, 200, Qt.KeepAspectRatio))
        image.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        info = QLabel("ANTONIO BANDERAS LOGIN")
        info.setObjectName("infoArea")
        info.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email address")
        self.email.setAlignment(Qt.AlignTop)

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setAlignment(Qt.AlignTop)

        self.remember_me = QCheckBox("Remember me")
        self.remember_me.setCursor(QCursor(Qt.PointingHandCursor))

        buttons = QHBoxLayout()
        self.login = QPushButton("Login")
        self.login.setCursor(QCursor(Qt.PointingHandCursor))
        self.login.clicked.connect(self.connect)

        self.register = QPushButton("Register")
        self.register.setCursor(QCursor(Qt.PointingHandCursor))
        self.dialog = register_window(self)
        buttons.addWidget(self.register)
        buttons.addWidget(self.login)
        buttons.setAlignment(Qt.AlignRight)

        social_media = QHBoxLayout()
        instagram = QPushButton()
        instagram.setObjectName("ins")
        instagram.setToolTip("Jumayev.Mekan - Instagram!")
        instagram.setCursor(QCursor(Qt.PointingHandCursor))
        instagram.setIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\instagram.png"))
        instagram.clicked.connect(lambda: self.open_social())

        facebook = QPushButton()
        facebook.setObjectName("face")
        facebook.setToolTip("Jumayev.Mekan - Facebook!")
        facebook.setCursor(QCursor(Qt.PointingHandCursor))
        facebook.setIcon(QIcon("C:\\Users\\user\\PycharmProjects\\Programming\\icons\\facebook.png"))
        facebook.clicked.connect(lambda: self.open_social())

        social_media.addWidget(instagram)
        social_media.addWidget(facebook)
        social_media.setStretch(10, 10)
        social_media.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        copyr = QLabel("<u>2020 - Mekan Jumayev </u>")
        copyr.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        v_box.addWidget(image)
        v_box.addWidget(info)
        v_box.addWidget(self.email)
        v_box.addWidget(self.password)
        v_box.addWidget(self.remember_me)
        v_box.addLayout(buttons)
        v_box.addWidget(copyr)
        v_box.addLayout(social_media)

        self.login.clicked.connect(self.connect)
        self.register.clicked.connect(self.connected)

        widget.setLayout(v_box)

        return widget

    def open_social(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = login_window()
    sys.exit(app.exec_())
