from src.excel import PyExcel
from src.input import get_file_names
from src.process import process
from src.watch import ExcelFileHandler, watch


def process_and_reopen_excel(rule_file_name: str, original_file_name: str, output_file_name: str):

    # process 전 파일을 열고 있는 엑셀 종료
    py_excel = PyExcel(file_path=output_file_name)
    py_excel.close()

    # process
    process(
        rule_file_name=rule_file_name,
        original_file_name=original_file_name,
        output_file_name=output_file_name,
    )

    # process 완료 후 엑셀 재실행
    py_excel.open()


def main():

    # 사용자로부터 파일명 입력 받기
    rule_file_name, original_file_name, output_file_name = get_file_names()

    # 규칙 파일 변경 시 마다 process
    watch(
        ExcelFileHandler(
            file_path=f"{rule_file_name}.xlsx",
            run=lambda: process_and_reopen_excel(
                rule_file_name=f"{rule_file_name}.xlsx",
                original_file_name=f"{original_file_name}.xlsx",
                output_file_name=f"{output_file_name}.xlsx",
            )
        )
    )


if __name__ == "__main__":
    main()
