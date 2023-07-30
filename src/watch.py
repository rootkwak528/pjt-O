import time
from datetime import datetime, timedelta
from typing import Callable
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


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

            print('\n규칙 저장 엑셀 파일의 수정을 감지했어요. 비용 현황 엑셀을 수정할게요.')
            self.run()


def watch(event_handler: ExcelFileHandler):

    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
