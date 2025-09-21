import hashlib
import json
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

FOLDERS_TO_MONITOR = config["folders_to_monitor"]
HASH_ALGO = config["hash_algorithm"].lower()
LOG_FILE = config["log_file"]

# Function to calculate file hash
def calculate_hash(filepath, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

# Custom event handler
class IntegrityHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_hash = calculate_hash(event.src_path, HASH_ALGO)
            self.log_event("NEW", event.src_path, file_hash)

    def on_modified(self, event):
        if not event.is_directory:
            file_hash = calculate_hash(event.src_path, HASH_ALGO)
            self.log_event("MODIFIED", event.src_path, file_hash)

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_event("DELETED", event.src_path, None)

    def log_event(self, action, filepath, file_hash):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{action}] {filepath}"
        if file_hash:
            log_entry += f" | Hash ({HASH_ALGO}): {file_hash}"

        print(log_entry)
        with open(LOG_FILE, "a") as log:
            log.write(log_entry + "\n")

# Main execution
if __name__ == "__main__":
    event_handler = IntegrityHandler()
    observer = Observer()

    for folder in FOLDERS_TO_MONITOR:
        os.makedirs(folder, exist_ok=True)  # create if not exists
        observer.schedule(event_handler, folder, recursive=True)

    print(f"Monitoring folders: {FOLDERS_TO_MONITOR}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

