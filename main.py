import tweet_extract as te
import graph_plot as gp
import requests
from PyQt5 import QtWidgets
from ui import Ui_MainWindow #this is your generated .py file 
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import QPixmap
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__() #This is the parent window object
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.checknet()
        self.ui.search_button.clicked.connect(self.search)
        
    def checknet(self):
        url='https://www.google.com/'
        timeout=1
        pixmap = QPixmap("net.png")
        pixmap2 = QPixmap("no_net.png")
        try:
            _ = requests.get(url, timeout=timeout)
            self.ui.netstatus.setText("NET OK")
            self.ui.neticon.setPixmap(pixmap)
            self.ui.neticon.show()
        except requests.ConnectionError:
            self.ui.netstatus.setText("NO NET")
            self.ui.neticon.setPixmap(pixmap2)
            self.ui.neticon.show()
            
    def search(self):
        self.checknet()
        if (self.ui.input_tag.toPlainText()==''):
            QMessageBox.about(self, "ALERT!!", "Empty Keyword /Tag !!")
        else:
            if(self.ui.choice2.isChecked()):
                choice=2
            elif(self.ui.choice3.isChecked()):
                choice=3
            else:
                choice=1
            tags=self.ui.input_tag.toPlainText()
            tags.strip()
            number=self.ui.input_tweet.value()
            self.ui.display_label.setText("LOADING")
            ##-------------BEGIN INVOKING MODULES------------##
            self.ui.progress.setValue(20)
            temp=te.DownloadData(choice,tags,number,self.ui)
            gp.plotPieChart(temp[0],temp[1], temp[2], temp[3],temp[4], temp[5], temp[6], temp[7], temp[8])
            gp.barGraphM(temp[9])
            gp.barGraphD(temp[10])
            gp.cloud(temp[11])
            gp.plotgraph(temp[12], temp[13])
            ##--------------------- END----------------------##
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

