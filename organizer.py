import os
import shutil
import schedule
import time
import logging
from datetime import datetime


# Configure logging
def setup_logging():
    logs_dir = "Logs"
    os.makedirs(logs_dir, exist_ok=True)

    log_filename = datetime.now().strftime("file_organizer_%Y-%m-%d.log")
    log_path = os.path.join(logs_dir, log_filename)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Also log to console for real-time monitoring
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)


def job():
    logging.info("🚀 Starting file organization job")
    start_time = time.time()
    files_processed = 0
    errors_occurred = 0

    # Function to get unique filename
    def get_unique_filename(dest_folder, filename):
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename

        while os.path.exists(os.path.join(dest_folder, new_filename)):
            new_filename = f"{base}_{counter}{ext}"
            counter += 1

        return new_filename

    # Main organization logic
    current_dir = os.path.dirname(os.path.realpath(__file__))
    logs_dir = os.path.join(current_dir, "Logs")

    file_categories = {
        "Code": (".py", ".pyc", ".css", ".html", ".js", ".json", ".md"),
        "Excel": (".xlsx", ".csv", ".xml"),
        "PDFs": (".pdf", ".txt"),
        "Images": (".jpg", ".jpeg", ".png", ".gif"),
        "Database": (".sql", ".db"),
    }

    try:
        for filename in os.listdir(current_dir):
            file_path = os.path.join(current_dir, filename)

            # Skip directories, this script, log files, and Logs directory
            if (
                os.path.isdir(file_path)
                or filename == os.path.basename(__file__)
                or filename.startswith("file_organizer_")
                or file_path.startswith(logs_dir)
            ):
                continue

            moved = False

            for folder, extensions in file_categories.items():
                if filename.endswith(extensions):
                    try:
                        os.makedirs(folder, exist_ok=True)
                        unique_name = get_unique_filename(folder, filename)
                        shutil.move(file_path, os.path.join(folder, unique_name))

                        if filename != unique_name:
                            logging.info(
                                f"Renamed and moved: {filename} → {folder}/{unique_name}"
                            )
                        else:
                            logging.info(f"Moved: {filename} → {folder}")

                        files_processed += 1
                        moved = True
                        break
                    except Exception as e:
                        errors_occurred += 1
                        logging.error(f"Error moving {filename} to {folder}: {str(e)}")
                        break

            if not moved:
                try:
                    os.makedirs("Other", exist_ok=True)
                    unique_name = get_unique_filename("Other", filename)
                    shutil.move(file_path, os.path.join("Other", unique_name))

                    if filename != unique_name:
                        logging.info(
                            f"Renamed and moved: {filename} → Other/{unique_name}"
                        )
                    else:
                        logging.info(f"Moved: {filename} → Other")

                    files_processed += 1
                except Exception as e:
                    errors_occurred += 1
                    logging.error(f"Error moving {filename} to Other: {str(e)}")

        elapsed_time = time.time() - start_time
        status = "✅" if errors_occurred == 0 else "⚠️"
        logging.info(
            f"{status} Job completed: {files_processed} files processed, {errors_occurred} errors, {elapsed_time:.2f} seconds"
        )
        print(
            f"\n{status} Files organized: {files_processed} files | Errors: {errors_occurred} | Time: {elapsed_time:.2f}s"
        )

    except Exception as e:
        logging.exception("🔥 Critical error in organization job: ")
        print(f"Critical error: {str(e)}")


if __name__ == "__main__":
    setup_logging()
    logging.info("=" * 60)
    logging.info("📁 FILE ORGANIZER SERVICE STARTED")
    logging.info("=" * 60)

    print("Starting file organization service...")
    print("Press Ctrl+C to stop the service")

    # Initial run
    job()

    # Schedule subsequent runs
    schedule.every(10).minutes.do(job)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("🛑 Service stopped by user")
        print("\nService stopped. Goodbye!")
    except Exception as e:
        logging.exception("🛑 Unexpected service crash: ")
        print(f"Unexpected error: {str(e)}")
