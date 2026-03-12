# lab11_test.py
from Shailah_Riddick_Lab11_FileProcessor import merge, duplicate, convert_to_csv, print_file_statistics

def main():
    file1 = "file1.txt"
    file2 = "file2.txt"
    merged_output = "result.txt"
    csv_output = "result.csv"

    print("=== Testing merge() ===")
    merge(file1, file2, merged_output)

    print("\n=== Testing duplicate() ===")
    duplicate(file1)

    print("\n=== Testing convert_to_csv() ===")
    convert_to_csv(file2, csv_output)

    print("\n=== Testing print_file_statistics() ===")
    print_file_statistics(file1)
    print_file_statistics(merged_output)

    # Deliberate error cases
    print("\n=== Testing Error Handling ===")
    merge("missing1.txt", file2, "output.txt")            # merge with missing file
    duplicate("nonexistent.txt")                           # duplicate missing file
    convert_to_csv("missing.txt", "output.csv")           # convert missing text file to CSV
    print_file_statistics("nofile.txt")                  # print statistics of missing file

if __name__ == "__main__":
    main()
