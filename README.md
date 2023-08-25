# Directory Structure Mapper

This Python script allows you to map the directory structure of a specified directory and write it to a text file. It provides options to include/exclude hidden directories and includes the source code of specific file types within the structure.

## Features

- Recursively maps the directory structure of a specified directory.
- Includes the source code of `.py`, `.html`, `.odt`, `.js`, `.json`, `.java`, `.cpp`, `.c`, `.css`, `.php`, `.rb`, `.swift`, `.go`, `.ts`, `.sql`, `.pl`, `.r`, `.sh`, `.xml`, `.md`, `.doc`, `.docx`, `.md`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, and `.txt` files within the structure.
- Option to exclude hidden directories (starting with `.`) from the mapping.

## Usage

1. Clone this repository or copy the provided script to your local environment.

2. Make sure you have Python installed.

3. Open a terminal and navigate to the directory containing the script (`dsm.py`).

4. To run the script, use the following command:

   ```bash
   python dsm.py
   ```

5. Follow the prompts:
   - Enter the path of the directory you want to map.
   - Enter the full path (including filename) of the output text file.
   - Choose whether to include hidden directories in the mapping (answer with `y` for yes or `n` for no).

## Example

Here's an example of how the script works:

```bash
python dsm.py
```

```
Enter the directory path: ./example_directory
Enter the full path of the output file: ./output/directory_structure.txt
Do you want to map hidden directories? (y/n): y
Mapping completed successfully.
```

The directory structure and source code (if applicable) will be written to the specified output file.

## Disclaimer

This script is provided as-is and may require modifications to suit your specific use case or directory structure.

## License

This project is licensed under the [MIT License](LICENSE).
