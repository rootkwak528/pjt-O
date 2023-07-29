from datetime import datetime, timedelta
from typing import Callable

from watchdog.events import FileSystemEventHandler


class ExcelFileHandler(FileSystemEventHandler):
    def __init__(self, file_path: str, run: Callable[[], None]):
        self.file_path = file_path
        self.run = run
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.file_path):

            # 중복 수행 방지
            now = datetime.now()
            if now - self.last_modified < timedelta(seconds=3):
                return
            self.last_modified = now

            print('\n원본 엑셀 파일 수정을 감지했어요. 엑셀을 수정할게요.')
            self.run()
