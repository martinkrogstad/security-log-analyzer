# Security Log Analyzer

A Python-based command-line tool that analyzes login records from CSV files and identifies potentially suspicious login activity.

## Features

- Reads login records from a CSV file
- Counts successful and failed login attempts
- Tracks failed login attempts by IP address
- Detects suspicious activity using a configurable threshold
- Displays security warnings for IP addresses exceeding or reaching the threshold
- Handles missing log files gracefully

## Technologies

- Python 3
- CSV module
- pathlib
- Command Line Interface (CLI)

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the program:

   `python main.py`

5. Select option 1 to analyze the sample login data.

## CSV Format

The program reads `login_logs.csv` with the following columns:

`ip,username,status`

Each row represents a login attempt. Status values are `success` or `failed`.

## Security Detection

The analyzer flags IP addresses with three or more failed login attempts by default.

This is a simple threshold-based detection mechanism intended for learning purposes. It does not confirm that an actual brute-force attack has occurred.

## Project Purpose

I developed this project while studying Cyber Security to strengthen my Python programming skills and apply them to a practical security-related scenario.

The project demonstrates file handling, dictionaries, functions, error handling, basic log analysis, and security detection logic.

## Future Improvements

- Support for additional log formats
- Exporting analysis reports
- Automated testing
- More advanced detection rules