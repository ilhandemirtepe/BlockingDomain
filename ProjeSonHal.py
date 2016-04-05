import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPushButton, QDialog, QApplication,QHBoxLayout,QVBoxLayout, QPlainTextEdit


class MainForm(QDialog):

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setWindowTitle("Domain Engelleme Yazılımı")
        # widget olustur  ve butonları ekle
        self.duzenleButton = QPushButton("Domain Adı Gir")
        self.duzenleButton.setStyleSheet("background-color: rgb(200,20,20);")
        self.baslaButton = QPushButton("Başla")
        self.baslaButton.setStyleSheet("background-color: rgb(0,250,0);")
        self.setFixedSize(500, 140)
        # baska bir layout yapalım bizim butonları tutsun
        asagiSatir = QHBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(self.baslaButton, 0, Qt.AlignHCenter)
        asagiSatir.addWidget(self.duzenleButton, 0, Qt.AlignRight)
        layout.addLayout(asagiSatir)
        self.setLayout(layout)
        # butonlara link veriyorum
        self.baslaButton.clicked.connect(backend.engellemeyeBasla)
        self.duzenleButton.clicked.connect(self.listeAc)
    def listeAc(self):
        list.show()


class ListEditor(QDialog):

    def __init__(self, parent=None):
        super(ListEditor, self).__init__(parent)
        self.setWindowTitle("Engellenecek Domain Adı")
        self.tableView = QPlainTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.kaydetButton = QPushButton("Tamam")
        self.kaydetButton.setStyleSheet("background-color: rgb(0,250,0);")
        self.kaydetButton.clicked.connect(self.listeyiKapat)
        layout.addWidget(self.kaydetButton, 0, Qt.AlignRight)
        self.setLayout(layout)

    def listeyiKapat(self):
        """ Engellenecek domain adı adlı pencereyi kapatmaya yarar  """
        list.hide()


class Arkaplan():

    def __init__(self):
        self.initHosts()
    def initHosts(self):
        """ilk önce biz temp dosyasına yazdıracağız hostumuzu..Çünkü üzerinde değişiklik yapabiliriz..O yuzden tempte tuttuk"""

        self.realHostsFile = "/etc/hosts"
        self.tmpHostsFile = "/tmp/etc_hosts.tmp"
        os.system('cp {0} {1}'.format(self.realHostsFile, self.tmpHostsFile))
        self.HostsFile = self.tmpHostsFile

    def engellemeyeBasla(self):
        form.hide()
        list.close()
        hostsFile = open(self.HostsFile, "a")
        blockeEdilecekSiteler = list.tableView.toPlainText()
        # domain başındaki ve sonundaki boşlukları siliyoruz
        blockeEdilecekSiteler = [str(site).strip() for site in blockeEdilecekSiteler.split("\n")]
        for sites in blockeEdilecekSiteler:
            hostsFile.write("0.0.0.0\t" + sites + "\n")
            if sites.startswith('www.'):
                temp = sites.split('www.')[1]
                hostsFile.write("0.0.0.0\t" + temp + "\n")
            else:
                hostsFile.write("0.0.0.0\t" + "www." + sites + "\n")
        hostsFile.close()
        os.system('gksudo cp {0} {1}'.format(self.tmpHostsFile, self.realHostsFile))

if __name__ == '__main__':

    from xdg.BaseDirectory import *
    app = QApplication(sys.argv)
    backend = Arkaplan()
    form = MainForm()
    form.show()
    list = ListEditor()
    sys.exit(app.exec_())