import win32com.client as win32
import pythoncom
import os


class PyExcel:
    excel: win32.dynamic.CDispatch

    def __init__(self, file_path: str):
        pythoncom.CoInitialize()  # COM 라이브러리 초기화
        self.excel = win32.gencache.EnsureDispatch('Excel.Application')
        self.excel.Visible = True  # 엑셀 창을 띄웁니다, False; 백그라운드 실행
        self.file_path = file_path

    def close(self):
        for wb in self.excel.Workbooks:
            if wb.FullName == f"{os.getcwd()}\{self.file_path}":
                wb.Close(SaveChanges=False)  # 변동사항 저장 여부

    def open(self):
        wb = self.excel.Workbooks.Open(f"{os.getcwd()}\{self.file_path}")
        wb.Sheets("비용현황").Activate()
