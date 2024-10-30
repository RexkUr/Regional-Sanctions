import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(
    filename='file_changes.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f'Modified: {event.src_path}')

    def on_created(self, event):
        logging.info(f'Created: {event.src_path}')

    def on_deleted(self, event):
        logging.info(f'Deleted: {event.src_path}')

    def on_moved(self, event):
        logging.info(f'Moved: {event.src_path} to {event.dest_path}')
if __name__ == "__main__":
    path = "C:\\Users\\Red RexkUr\\AppData\\Roaming\\ATLauncher\\instances\\lololol\\mods"  
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()