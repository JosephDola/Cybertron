from PySide2.QtWidgets import QApplication

from ui.main_window import MainWindow

from brain.wake_word import wake_word
from brain.boot import boot

import threading



class VoiceThread(threading.Thread):


    def run(self):

        wake_word.listen()



class CybertronApp:


    def __init__(self):


        self.app = QApplication([])


        self.window = MainWindow()



        # Start Cybertron boot

        boot.start()



        # Start voice listener

        self.voice_thread = VoiceThread()

        self.voice_thread.daemon = True

        self.voice_thread.start()



    def run(self):

        self.window.show()

        self.app.exec_()
