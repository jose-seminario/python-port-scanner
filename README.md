# Python Port Scanner

A simple TCP Port Scanner built with Python to learn socket programming, modular programming, and basic networking concepts.

---

## Features

- Scan a custom range of TCP ports.
- Scan the full TCP port range (1-65535).
- Detect common services running on open ports.
- Display scan progress in real time.
- Measure total scan execution time.
- Clean and modular project structure.

---

## Project Structure

```
python-port-scanner/
│
├── input_handler.py
├── main.py
├── scanner.py
├── ui.py
└── README.md
```

### File Description

| File | Purpose |
|------|---------|
| `main.py` | Starts the application and coordinates the program flow. |
| `scanner.py` | Performs the TCP port scanning and service detection. |
| `input_handler.py` | Validates and processes user input. |
| `ui.py` | Displays menus, progress, and scan results. |

---

## Requirements

- Python 3.10 or newer

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jose-seminario/python-port-scanner.git
```

Enter the project folder:

```bash
cd python-port-scanner
```

Run the program:

```bash
python main.py
```

---

## Example

```
Enter target IP:
scanme.nmap.org

Enter start port:
20

Enter end port:
100

Scanning... 100.00%

Open Ports

Port: 22 | Service: ssh
Port: 80 | Service: http

Scan completed in 5.81 seconds
```

---

## Concepts Practiced

During this project I practiced:

- Python fundamentals
- Functions
- Modules
- Socket programming
- TCP networking
- Input validation
- Loops
- Exception handling
- Clean code
- Single Responsibility Principle (SRP)

---

## Future Improvements

- Multi-threaded scanning
- Banner grabbing
- Export results to a file
- IPv6 support
- Scan report generation

---

## License

This project is licensed under the MIT License.

---

## Author

**Jose Seminario**

GitHub:
https://github.com/jose-seminario