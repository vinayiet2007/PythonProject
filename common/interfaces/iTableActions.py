from abc import ABC,abstractmethod

class ITableActions(ABC):

    @abstractmethod
    def count_rows(self):
        pass

    @abstractmethod
    def select_row(self,row_num:int):
        pass

    @abstractmethod
    def read_table_row(self,row_num:int):
        pass

    @abstractmethod
    def read_column_data_by_id(self,col_num:int):
        pass

    @abstractmethod
    def read_cell_data_by_id(self,row_num:int,col_num:int):
        pass