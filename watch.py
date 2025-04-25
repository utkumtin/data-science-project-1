import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys

class TestRunnerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'\n🌀 Change detected in {event.src_path}, running tests...\n')
            subprocess.run([sys.executable, 'tests/test_question.py'])

if __name__ == "__main__":
    path = "."  # izlenen klasör
    event_handler = TestRunnerHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print("👀 Watching for changes... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
