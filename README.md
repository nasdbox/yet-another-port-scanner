# Simple Python Port Scanner

A lightweight TCP port scanner written in Python that checks for open ports on a target host. 

## Features

* **Hostname Resolution**: Automatically converts web addresses into IP addresses.
* **Timeout Protection**: Stops the script from hanging on unresponsive ports.
* **Graceful Exit**: Stops cleanly if you press `Ctrl+C`.

## Requirements

* Python 3.x

This script only uses standard Python libraries (`socket`, `sys`, `datetime`), so no extra installations are needed.

## Usage

1. Save the code into a file named `scanner.py`.
2. Open your terminal or command prompt.
3. Run the script with Python:
   ```bash
   python scanner.py
   ```
4. Enter the target domain name or IP address when prompted.

### Example Input
```text
Enter target IP or hostname: localhost
```

## Disclaimer

This tool is for educational purposes and authorized security testing only. Only scan devices and networks that you own or have explicit permission to test.
