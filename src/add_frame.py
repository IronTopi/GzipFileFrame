import gzip
import shutil
import os
from tempfile import NamedTemporaryFile
from settings import Settings


def add_text_to_zipfile(file_path, text, buffer_size=1024 * 1024):  # 1MB buffer
    temp_file = NamedTemporaryFile(delete=False)
    temp_file_path = temp_file.name

    with gzip.open(file_path, "rb") as original_file, gzip.open(
        temp_file_path, "wb"
    ) as new_file:
        new_file.write(text.encode() + b"\n")

        # Buffered copying
        while True:
            chunk = original_file.read(buffer_size)
            if not chunk:
                break
            new_file.write(chunk)

    os.replace(temp_file_path, file_path)


if __name__ == "__main__":
    my_settings = Settings()
    file_path = my_settings.zip_file_path
    add_text_to_zipfile(file_path, "tobi ist toll")
