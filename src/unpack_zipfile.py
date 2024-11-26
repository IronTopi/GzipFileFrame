import gzip

from settings import Settings


def extract_gzip_file(file_path, output_path):
    with gzip.open(file_path, "rt") as f_in:
        with open(output_path, "wt") as f_out:
            f_out.write(f_in.read())


if __name__ == "__main__":
    my_settings = Settings()
    file_path = my_settings.zip_file_path
    output_path = file_path.replace(".gz", "")
    extract_gzip_file(file_path, output_path)
    print(f"Gzip file extracted at {output_path}.")
