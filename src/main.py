import time
from watchdog.observers import Observer

from src.input import get_file_names
from src.process import process
from src.watch import ExcelFileHandler


def main():
    rule_file_name, original_file_name, output_file_name = get_file_names()

    # 파일 변경 감시
    event_handler = ExcelFileHandler(
        file_path=f"{rule_file_name}.xlsx",
        run=lambda: process(
            rule_file_name=f"{rule_file_name}.xlsx",
            original_file_name=f"{original_file_name}.xlsx",
            output_file_name=f"{output_file_name}.xlsx",
        )
    )

    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
