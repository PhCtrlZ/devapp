from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QThread, pyqtSignal
from QtGui import Ui_Dialog
import sys
import os
import subprocess
from tkinter import messagebox


# Lớp để thực hiện các tác vụ cài đặt trong một thread riêng
class InstallThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, bat_file_path, app_name):
        super().__init__()
        self.bat_file_path = bat_file_path
        self.app_name = app_name

    def run(self):
        subprocess.run([self.bat_file_path], shell=True)
        self.finished.emit(f"{self.app_name} đã được cài đặt!")


# Lớp chính của ứng dụng
class MainApp(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút bấm với các phương thức
        self.ui.pushButton.clicked.connect(self.open_google_chrome)
        self.ui.pushButton_2.clicked.connect(self.open_mozilla_firefox)
        self.ui.pushButton_3.clicked.connect(self.open_brave_browser)
        self.ui.pushButton_4.clicked.connect(self.open_vlc_media_player)
        self.ui.pushButton_5.clicked.connect(self.open_zoom)
        self.ui.pushButton_6.clicked.connect(self.open_microsoft_edge)
        self.ui.pushButton_7.clicked.connect(self.open_opera_browser)
        self.ui.pushButton_8.clicked.connect(self.open_winrar)
        self.ui.pushButton_9.clicked.connect(self.open_vs_code)
        self.ui.pushButton_10.clicked.connect(self.open_adobe_reader)
        self.ui.pushButton_11.clicked.connect(self.open_teamviewer)
        self.ui.pushButton_12.clicked.connect(self.open_obs_studio)
        self.ui.pushButton_13.clicked.connect(self.open_skype)
        self.ui.pushButton_14.clicked.connect(self.open_zalo)
        self.ui.pushButton_15.clicked.connect(self.open_potplayer)
        self.ui.pushButton_16.clicked.connect(self.open_telegram_desktop)
        self.ui.pushButton_17.clicked.connect(self.open_utorrent)
        self.ui.pushButton_18.clicked.connect(self.open_vmware)
        self.ui.pushButton_19.clicked.connect(self.open_k_lite_codec_pack)
        self.ui.pushButton_20.clicked.connect(self.close)  # Đóng ứng dụng
        self.ui.pushButton_21.clicked.connect(self.open_league_of_legends)
        self.ui.pushButton_22.clicked.connect(self.open_python)
        self.ui.pushButton_23.clicked.connect(self.open_unikey)
        self.ui.pushButton_24.clicked.connect(self.setup_to_download)

    # Các phương thức xử lý cho từng nút bấm
    def open_google_chrome(self):
        bat_file_path = os.path.join('command_to_install', 'gg.bat')
        self.run_install_thread(bat_file_path, "Chrome")

    def open_mozilla_firefox(self):
        bat_file_path = os.path.join('command_to_install', 'ff.bat')
        self.run_install_thread(bat_file_path, "Firefox")

    def open_brave_browser(self):
        bat_file_path = os.path.join('command_to_install', 'br.bat')
        self.run_install_thread(bat_file_path, "Brave")

    def open_vlc_media_player(self):
        bat_file_path = os.path.join('command_to_install', 'vlc.bat')
        self.run_install_thread(bat_file_path, "VLC")

    def open_zoom(self):
        bat_file_path = os.path.join('command_to_install', 'z.bat')
        self.run_install_thread(bat_file_path, "Zoom")

    def open_microsoft_edge(self):
        bat_file_path = os.path.join('command_to_install', 'edge.bat')
        self.run_install_thread(bat_file_path, "Edge")

    def open_opera_browser(self):
        bat_file_path = os.path.join('command_to_install', 'op.bat')
        self.run_install_thread(bat_file_path, "Opera")

    def open_winrar(self):
        bat_file_path = os.path.join('command_to_install', 'winrar.bat')
        self.run_install_thread(bat_file_path, "WinRAR")

    def open_vs_code(self):
        bat_file_path = os.path.join('command_to_install', 'vs.bat')
        self.run_install_thread(bat_file_path, "VS Code")

    def open_adobe_reader(self):
        bat_file_path = os.path.join('command_to_install', 'reader.bat')
        self.run_install_thread(bat_file_path, "Adobe Reader")

    def open_teamviewer(self):
        bat_file_path = os.path.join('command_to_install', 'team.bat')
        self.run_install_thread(bat_file_path, "TeamViewer")

    def open_obs_studio(self):
        bat_file_path = os.path.join('command_to_install', 'obs.bat')
        self.run_install_thread(bat_file_path, "OBS Studio")

    def open_skype(self):
        bat_file_path = os.path.join('command_to_install', 'sky.bat')
        self.run_install_thread(bat_file_path, "Skype")

    def open_zalo(self):
        bat_file_path = os.path.join('command_to_install', 'zalo.bat')
        self.run_install_thread(bat_file_path, "Zalo")

    def open_potplayer(self):
        bat_file_path = os.path.join('command_to_install', 'pot.bat')
        self.run_install_thread(bat_file_path, "PotPlayer")

    def open_telegram_desktop(self):
        bat_file_path = os.path.join('command_to_install', 'tele.bat')
        self.run_install_thread(bat_file_path, "Telegram Desktop")

    def open_utorrent(self):
        bat_file_path = os.path.join('command_to_install', 'ur.bat')
        self.run_install_thread(bat_file_path, "uTorrent")

    def open_vmware(self):
        bat_file_path = os.path.join('command_to_install', 'vm.bat')
        self.run_install_thread(bat_file_path, "VMware")

    def open_k_lite_codec_pack(self):
        bat_file_path = os.path.join('command_to_install', 'codecs.bat')
        self.run_install_thread(bat_file_path, "K-Lite Codec Pack")

    def open_league_of_legends(self):
        bat_file_path = os.path.join('command_to_install', 'lm.bat')
        self.run_install_thread(bat_file_path, "League of Legends")

    def open_python(self):
        bat_file_path = os.path.join('command_to_install', 'py.bat')
        self.run_install_thread(bat_file_path, "Python")

    def open_unikey(self):
        bat_file_path = os.path.join('command_to_install', 'uni.bat')
        self.run_install_thread(bat_file_path, "Unikey")

    def setup_to_download(self):
        bat_file_path = os.path.join('command_to_install', 'setup_to_download.bat')
        self.run_install_thread(bat_file_path, "Setup")

    # Phương thức chạy thread cài đặt
    def run_install_thread(self, bat_file_path, app_name):
        self.install_thread = InstallThread(bat_file_path, app_name)
        self.install_thread.finished.connect(self.show_message)
        self.install_thread.start()

    # Hiển thị thông báo sau khi cài đặt xong
    def show_message(self, message):
        messagebox.showinfo("Thông báo", message)

# Hàm khởi chạy ứng dụng
def main():
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())

# Kiểm tra quyền admin và chạy ứng dụng
if __name__ == "__main__":
    main()
