# Gzip File Processor

This project provides a set of utilities for creating, extracting, and modifying gzip files. It includes functionalities to generate random or static data, compress it into gzip files, extract gzip files, and add text to existing gzip files.

## Project Structure

```
.gitignore
activate_venv.sh
README.md
requirements.txt
src/
    __pycache__/
    add_frame.py
    create_zipfile.py
    do.py
    settings.py
    unpack_zipfile.py
tmp/
```

## Setup

1. Clone the repository.
2. Create and activate a virtual environment:

    ```sh
    source activate_venv.sh
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Create a Gzip File

To create a gzip file with random or static data, run the following command:

```sh
python src/create_zipfile.py
```

This will generate a gzip file at the path specified in the `Settings` class in

### Extract a Gzip File

To extract a gzip file, run the following command:

```sh
python src/unpack_zipfile.py
```

This will extract the gzip file specified in the `Settings` class in

### Add Text to a Gzip File

To add text to an existing gzip file, run the following command:

```sh
python src/add_frame.py
```

This will add the text "tobi ist toll" to the gzip file specified in the `Settings` class in

## Configuration

The project uses the `pydantic-settings` library for configuration. You can set the configuration values in a `.env` file or directly in the `Settings` class in

## Requirements

- Python 3.x
- `pydantic`
- `pydantic-settings`
- `tqdm`

## License

This project is licensed under the MIT License.
