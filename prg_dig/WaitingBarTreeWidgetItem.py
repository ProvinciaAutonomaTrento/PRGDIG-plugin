from qgis.PyQt import QtWidgets

class WaitingBarTreeWidgetItem (QtWidgets.QTreeWidgetItem):
    def __init__( self, parent ):
      
        ## Init super class ( QtGui.QTreeWidgetItem )
        super( WaitingBarTreeWidgetItem, self ).__init__(parent)

        self.progressBar = QtWidgets.QProgressBar()
        
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setStyleSheet('height:15px; margin-right:5px;')

        self.treeWidget().setItemWidget( self, 0, self.progressBar )