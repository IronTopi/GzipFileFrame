import gzip

import random
from settings import Settings
from tqdm import tqdm

my_settings = Settings()


def generate_random_data(size):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    chunk_size = 1024  # 1 KB
    for _ in range(0, size, chunk_size):
        yield "".join(random.choice(chars) for _ in range(chunk_size))


def generate_static_data(size):
    static_string = "a" * 1024  # 1 KB of 'a'
    chunk_size = 1024  # 1 KB

    loop = 0
    for _ in range(0, size, chunk_size):
        loop += 1
        yield static_string

    # print(loop)


def create_gzip_file(file_path, data_size):
    chunk_size = 1024 * 1024  # 1 MB
    total_written = 0

    with gzip.open(file_path, "wt") as f:
        with tqdm(
            total=data_size, unit="B", unit_scale=True, desc="Creating Gzip File"
        ) as pbar:
            data_generator = (
                generate_random_data
                if my_settings.use_random_data
                else generate_static_data
            )
            while total_written < data_size:
                remaining_size = data_size - total_written
                current_chunk_size = min(chunk_size, remaining_size)
                data = "".join(data_generator(current_chunk_size))
                f.write(data)
                total_written += current_chunk_size
                pbar.update(current_chunk_size)


if __name__ == "__main__":
    file_path = my_settings.zip_file_path
    data_size = my_settings.data_size
    create_gzip_file(file_path, data_size)
    print(f"Gzip file created at {file_path} with {data_size} bytes of random data.")
