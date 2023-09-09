#!/usr/bin/env python

import os

def write_directory_structure(path, indent="", output_file=None, map_hidden=False):
    if output_file is None:
        output_file = open("directory_structure.txt", "w", encoding="utf-8")

    programming_file_types = (".py", ".html", ".odt", ".js", ".json", ".java", ".cpp", ".c", ".css", ".php",
                              ".rb", ".swift", ".go", ".ts", ".sql", ".pl", ".r", ".sh", ".xml", ".md")

    office_file_types = (".doc", ".docx", ".md", ".ppt", ".pptx", ".xls", ".xlsx", ".txt")

    for item in os.listdir(path):
        if not map_hidden and item.startswith('.'):
            continue  # Skip hidden directories if not mapped
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            output_file.write(f"{indent}./{item}\n")
            write_directory_structure(item_path, indent + "\t", output_file, map_hidden)
        elif os.path.isfile(item_path):
            output_file.write(f"{indent}./{item}\n")
            if item.endswith(programming_file_types + office_file_types):
                output_file.write(f"{indent}\t(source code):\n")
                try:
                    with open(item_path, "r", encoding="utf-8") as source_file:
                        source_lines = source_file.readlines()
                        for line in source_lines:
                            output_file.write(f"{indent}\t\t{line}")
                except UnicodeDecodeError:
                    output_file.write(f"{indent}\t\tCould not read the file content due to encoding issues.\n")

if __name__ == "__main__":
    root_directory = input("Enter the directory path: ")
    output_file_path = input("Enter the full path of the output file: ")
    map_hidden_dirs = input("Do you want to map hidden directories? (y/n): ").lower() == "y"

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        write_directory_structure(root_directory, output_file=output_file, map_hidden=map_hidden_dirs)

    print("Mapping completed successfully.")
