import gzip

import random
import string
from settings import Settings


def generate_random_data(size):
    random_data = "".join(random.choices(string.ascii_letters + string.digits, k=size))
    return "\n".join(random_data[i : i + 50] for i in range(0, len(random_data), 50))


def create_gzip_file(file_path, data_size):
    random_data = generate_random_data(data_size)

    with gzip.open(file_path, "wt") as f:
        f.write(random_data)


if __name__ == "__main__":
    my_settings = Settings()
    file_path = my_settings.zip_file_path
    data_size = my_settings.data_size
    create_gzip_file(file_path, data_size)
    print(f"Gzip file created at {file_path} with {data_size} bytes of random data.")
