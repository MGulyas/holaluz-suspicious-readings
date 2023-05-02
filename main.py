import sys

from application.use_cases import add_readings_from_file, print_suspicious_readings

if __name__ == '__main__':
    filename = sys.argv[1]
    add_readings_from_file(filename)
    print_suspicious_readings()