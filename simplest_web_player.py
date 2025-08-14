''' example ported from qt C++ docs: https://doc.qt.io/qt-6/videooverview.html '''

# this is because python linters and Qt don't play nice:
#pylint: disable=E0611

from PySide6.QtCore import (
    QUrl, )

from PySide6.QtMultimedia import (
    QMediaPlayer, )

from PySide6.QtMultimediaWidgets import (
    QVideoWidget, )

from PySide6.QtWidgets import (
    QApplication, )


def main():
    ''' to run as example script '''
    app = QApplication([])
    player = QMediaPlayer()
    player.setSource(
        QUrl(  # any url of a video file type that QMediaPlayer can handle, including local
           # INTERNET:
            "https://videos.pexels.com/video-files/4459705/4459705-hd_1920_1080_24fps.mp4"))
           # LOCAL RELATIVE:
           # "zarove_platter.mp4"))
    video_widget = QVideoWidget()
    player.setVideoOutput(video_widget)
    video_widget.show()
    player.play()
    app.exec()

if __name__ == "__main__":
    main()
