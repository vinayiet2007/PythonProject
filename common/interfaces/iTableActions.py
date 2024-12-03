from abc import ABC,abstractmethod

class TableActions(ABC):

    @abstractmethod
    def countRows(self):
        pass

    @abstractmethod
    def selectRow(self):
        pass

    @abstractmethod
    def readTableRow(self):
        pass

    @abstractmethod
    def readColumnData(self):
        pass

    @abstractmethod
    def readCellData(self):
        pass