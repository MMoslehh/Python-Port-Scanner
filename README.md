# Python Port Scanner

## About the Project
This is a simple Python program that checks whether TCP ports are open on a local computer.

I created this project to practice Python and learn more about networking and basic cybersecurity concepts.

## Features
- Scans six common TCP ports.
- Uses Python sockets to attempt connections.
- Displays whether each port is open or closed/filtered.
- Uses a timeout to avoid waiting too long for connections.
- Scans the local computer (127.0.0.1).

## Technologies Used
- Python 3
- Python socket library
- Visual Studio Code
- Git and GitHub

## How to Run
1. Download the Python file from this repository.
2. Open the project folder in VS Code.
3. Open the terminal and run:

   `python Port_Scanner.py`

4. View the results in the terminal.

## Testing
I tested the program on my local computer using the loopback address (127.0.0.1).

The program scanned ports 21, 22, 80, 443, 3306, and 8080. All six ports returned "Closed or filtered."

The scan completed successfully without errors.

## What I Learned
- How TCP ports work.
- How to use Python's socket library.
- How to attempt TCP connections.
- How to use loops and conditional statements.
- How to manage projects using GitHub.

## Future Improvements
- Allow users to select which ports to scan.
- Display common services associated with ports.
- Add better error handling.
- Improve the output format.

## Note
This project is for educational purposes and is designed to scan the local computer. It should only be used on systems you own or have permission to test.
