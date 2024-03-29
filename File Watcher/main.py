import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"deleted: {event.src_path}")

if __name__ == "__main__":
    paths = sys.argv[1:]
    if not paths:
        print("Please specify at least one path to monitor.")
        sys.exit(1)

    event_handler = MyHandler()
    observer = Observer()
    for path in paths:
        observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
