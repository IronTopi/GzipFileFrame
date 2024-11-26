import gzip

import random
import string
from settings import Settings
from tqdm import tqdm


def generate_random_data(size):
    chars = string.ascii_letters + string.digits
    for _ in range(size):
        yield random.choice(chars)


def create_gzip_file(file_path, data_size):
    chunk_size = 1024 * 1024  # 1 MB
    total_written = 0

    with gzip.open(file_path, "wt") as f:
        with tqdm(
            total=data_size, unit="B", unit_scale=True, desc="Creating Gzip File"
        ) as pbar:
            while total_written < data_size:
                remaining_size = data_size - total_written
                current_chunk_size = min(chunk_size, remaining_size)
                random_data = "".join(
                    next(generate_random_data(current_chunk_size))
                    for _ in range(current_chunk_size)
                )
                f.write(random_data)
                total_written += current_chunk_size
                pbar.update(current_chunk_size)


if __name__ == "__main__":
    my_settings = Settings()
    file_path = my_settings.zip_file_path
    data_size = my_settings.data_size
    create_gzip_file(file_path, data_size)
    print(f"Gzip file created at {file_path} with {data_size} bytes of random data.")
