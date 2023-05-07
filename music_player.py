import time

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QPushButton, QListWidget, QFileDialog
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QIcon




class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('music_icon.ico'))
        self.setGeometry(0, 0, 550, 300)
        self.setMinimumSize(550, 300)
        self.setMaximumSize(550, 300)
        self.setWindowTitle("MUSIC PLAYER")
        self.setStyleSheet('''font: 75 11pt "Courier"; background-color: rgb(97, 97, 97); color: rgb(255, 216, 124);''')



        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)


        self.track_select_label = QLabel("Выбраный трек для прослушивания: ")
        self.main_layout.addWidget(self.track_select_label)

        self.addButton = QPushButton("Add File")
        self.main_layout.addWidget(self.addButton)

        self.buttons_layout = QHBoxLayout()
        self.main_layout.addLayout(self.buttons_layout)

        self.playButton = QPushButton("PLAY")
        self.pauseButton = QPushButton("PAUSE")
        self.stopButton = QPushButton("STOP")
        self.volume_slider = QSlider()
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)  #Ориентация
        self.volume_slider.setValue(50)               #Значение
        self.volume_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)            #Стиль для "слайдера"
        self.nextButton = QPushButton("NEXT")
        self.prevButton = QPushButton("PREV")

        self.buttons_layout.addWidget(self.playButton)
        self.buttons_layout.addWidget(self.pauseButton)
        self.buttons_layout.addWidget(self.stopButton)
        self.buttons_layout.addWidget(self.volume_slider)
        self.buttons_layout.addWidget(self.nextButton)
        self.buttons_layout.addWidget(self.prevButton)



        self.numbers_layout = QHBoxLayout()
        self.main_layout.addLayout(self.numbers_layout)


        self.position_label = QLabel("0:00")
        self.duration_label = QLabel("99:99")
        self.duration_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.numbers_layout.addWidget(self.position_label)
        self.numbers_layout.addWidget(self.duration_label)

        self.time_line = QSlider()
        self.time_line.setOrientation(Qt.Orientation.Horizontal)     #Ориентация
        self.time_line.setValue(0)
        self.main_layout.addWidget(self.time_line)

        self.list_track = QListWidget()
        self.main_layout.addWidget(self.list_track)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(0.5)
        self.player.setAudioOutput(self.audio_output)
        self.playlist = []
        self.index = 0



        self.playButton.clicked.connect(self.play)
        self.stopButton.clicked.connect(self.stop)
        self.pauseButton.clicked.connect(self.pause)
        self.volume_slider.sliderMoved.connect(self.set_volume)
        self.time_line.sliderMoved.connect(self.change_time)
        self.addButton.clicked.connect(self.add_file)
        self.nextButton.clicked.connect(self.next_play)
        self.prevButton.clicked.connect(self.prev_play)

    def play(self):
        if len(self.playlist) > 0:
            time.sleep(0.5)
            if self.player.source().path() == self.playlist[self.index]:
                self.player.play()
                return
            self.player.stop()


            filename = self.playlist[self.index]
            self.player.setSource(QUrl.fromLocalFile(filename))
            self.player.positionChanged.connect(self.update_time)
            self.player.play()
            filename = filename.split('/')[-1].split(".")[0]
            self.track_select_label.setText(f"Вы слушаете: {filename}")



    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()

    def set_volume(self, position):
        new_volume = position / 100
        self.audio_output.setVolume(new_volume)


    def update_time(self):
        position = self.player.position() / 1000
        duration = self.player.duration() / 1000
        self.time_line.setRange(0, int(self.player.duration()))
        minutes, seconds = divmod(position, 60)
        total_minutes, total_seconds = divmod(duration, 60)
        self.position_label.setText(f"{int(minutes)}:{int(seconds)}")
        self.duration_label.setText(f"{int(total_minutes)}:{int(total_seconds)}")
        self.time_line.setValue(int(self.player.position()))


    def change_time(self, position):
        self.player.setPosition(position)


    def add_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select an audio file", ".", "MP3 Files (*.mp3)")
        if not filename:
            return
        self.playlist.append(filename)
        filename = filename.split('/')[-1].split(".")[0]
        self.list_track.addItem(filename)



    def next_play(self):
        if self.index < len(self.playlist) -1:
            self.stop()
            self.index += 1
            self.play()

    def prev_play(self):
        if self.index > 0:
            self.stop()
            self.index -= 1
            self.play()




if __name__ == "__main__":
    app = QApplication([])
    window = Player()
    window.show()
    app.exec()