# BTscanner
# Bluetooth Scanner

## Overview
This script scans for nearby Bluetooth devices and categorizes them based on their major, minor, and service classes. It uses Python's `bluetooth` module and provides a clean, tabulated output of discovered devices.

## Features
- Scans for discoverable Bluetooth devices.
- Parses and categorizes devices using Major, Minor, and Service Class information.
- Uses multithreading to prevent UI blocking.
- Implements logging for better error tracking.
- Displays results in a formatted table using `tabulate`.

## Requirements
- Python 3.x
- `pybluez` library (`bluetooth` module)
- `tabulate` for formatted output

## Installation
Ensure you have the required dependencies installed:
```bash
pip install pybluez tabulate
```

## Usage
Run the script using:
```bash
python bluetooth_scanner.py
```

The script will scan for Bluetooth devices and display the results in a structured table.

## Output Example
```
+--------------+-------------------+--------------------------------+
| Device Name  | MAC Address       | Device Class                  |
+--------------+-------------------+--------------------------------+
| Device XYZ   | AA:BB:CC:DD:EE:FF | 236032 (Phone, Smartphone, No Service Class) |
+--------------+-------------------+--------------------------------+
```

## Error Handling
If Bluetooth is disabled or no devices are found, the script will log an appropriate message.

## License
This project is open-source and available under the MIT License.

## Author
Andrea Kang'ethe
