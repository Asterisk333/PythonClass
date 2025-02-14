import re
import urllib.parse

# Paths to the log files
log_file = r""

# Output files for each log
output_file_access = r""

# Refined SQL injection patterns
sql_patterns = [
    r"union.*select",  # UNION SELECT attack
    r"select.*from",  # Basic SELECT query
    r"drop\s+table",  # Dropping tables
    r"insert\s+into",  # Inserting into tables
    r"update\s+.*set",  # Updating records
    r"sleep\s*\(\d+\)",  # Time-based blind SQLi (SLEEP function)
    r"or\s+1=1",  # Authentication bypass
    r"into\s+outfile",  # SQL Export
    r"order\s+by",  # SQL Order statement
    r"group\s+by",  # SQL Group statement
    r"where\s+.*",  # WHERE clause (matches anything after WHERE)
    r"benchmark\s*\(\d+.*?,.*?\)",  # BENCHMARK function (time-based attacks)
    r"@@[\w]+",  # Global variables in SQL
    r"unhex\s*\(\s*.*?\s*\)"  # UNHEX function
]

# Compile the regex patterns with case-insensitivity
sql_regex = re.compile("|".join(sql_patterns), re.IGNORECASE)


def decode_line(line):
    """
    Decodes URL-encoded characters in a log line.

    :param line: The original log line containing %encoded characters.
    :return: Decoded version of the log line.
    """
    return urllib.parse.unquote(line)


def detect_sql_injection(log_file, output_file):
    """
    Detect potential SQL injection attempts in a log file.
    Decode %encoded characters only if there's a pattern match, and write flagged logs to an output file.

    :param log_file: Path to the log file to scan.
    :param output_file: Path to the file where cleaned and flagged logs will be written.
    """
    try:
        with open(log_file, 'r', encoding='utf-8') as file, open(output_file, 'w', encoding='utf-8') as output:
            print(f"Starting analysis for {log_file}...")
            #line_number = 0  # Counter for log lines processed
            #matched_lines = 0  # Counter for matched log lines

            for line in file:
                #line_number += 1

                # Check the raw line for matching patterns (before decoding)
                match = sql_regex.search(line)

                if match:
                    #matched_lines += 1

                    # Decode the line only if a match is found
                    decoded_line = decode_line(line)

                    # Write the decoded and flagged line to the output file
                    output.write(f"[POTENTIAL SQL INJECTION] - {decoded_line.strip()}\n")
                    output.flush()  # Ensure the data is written immediately

                    print(f"[POTENTIAL SQL INJECTION] - {decoded_line.strip()}")
                    print(f"Matched pattern: {match.group()}\n")

            print(f"\nAnalysis completed for {log_file}.")
            #print(f"Total lines processed: {line_number}")
            #print(f"Total potential SQL injections detected: {matched_lines}")
            print(f"Flagged lines written to {output_file}\n")

    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing the file '{log_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Starting SQL injection detection...")

    # Run detection for the access log
    detect_sql_injection(log_file, output_file_access)

    # Run detection for the error log
    detect_sql_injection(log_file2, output_file_error)

    print("SQL injection detection completed for both log files.")