
import os
import csv
import shutil

def merge(file1_path, file2_path, result_path):
    """
    Merges the contents of two text files into one result file.
    The result should contain the contents of file1 followed by file2.
    Handle exceptions gracefully.
    """
    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
        with open(result_path, 'w') as result_file:
            result_file.write(content1 + '\n' + content2)
        print(f"Files merged successfully into '{result_path}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def duplicate(file_path):
    """
    Creates a copy of the file in the same directory with "_copy" added
    to the filename. Handle exceptions gracefully.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        base, ext = os.path.splitext(file_path)
        copy_path = f"{base}_copy{ext}"
        shutil.copy(file_path, copy_path)
        print(f"File duplicated successfully as '{copy_path}'.")
    except Exception as e:
        print(f"Error duplicating file: {e}")

def convert_to_csv(text_file_path, csv_file_path):
    """
    Converts a given text file into a CSV file.
    Each word in the text file should become a cell in the CSV.
    Handle exceptions gracefully.
    """
    try:
        with open(text_file_path, 'r') as f:
            words = f.read().split()
        if not words:
            print(f"Warning: '{text_file_path}' is empty. CSV will be empty.")
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(words)
        print(f"Text file converted to CSV successfully as '{csv_file_path}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def print_file_statistics(file_path):
    """
    Prints the total number of lines and words in the given text file.
    If the file is empty, print "Warning: The file is empty."
    Handle exceptions gracefully.
    """
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        if not lines:
            print("Warning: The file is empty.")
            return
        total_words = sum(len(line.split()) for line in lines)
        print(f"File '{file_path}' has {len(lines)} lines and {total_words} words.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
