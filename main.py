import bluetooth
import threading
import logging
from tabulate import tabulate

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Major and Minor Device Class definitions
MAJOR_CLASSES = { ... }  # Same as your existing major classes
MINOR_CLASSES = { ... }  # Same as your existing minor classes

SERVICE_CLASSES = {
    0x00: "No Service Class Information",
    0x01: "Limited Discoverable Mode",
    0x02: "Reserved",
    0x04: "Networking",
    0x08: "Rendering",
    0x10: "Capturing",
    0x20: "Object Transfer",
    0x40: "Audio",
    0x80: "Telephony",
    0x100: "Information"
}

def parse_device_class(device_class):
    service_class = (device_class >> 13) & 0x7FF  # Extract service class (upper 11 bits)
    major = (device_class >> 8) & 0x1F  # Major class (5 bits)
    minor = (device_class >> 2) & 0x3F  # Minor class (6 bits)
    
    major_class_name = MAJOR_CLASSES.get(major, "Unknown Major Class")
    minor_class_name = MINOR_CLASSES.get((major, minor), "Unknown Minor Class")
    service_class_name = SERVICE_CLASSES.get(service_class, "Unknown Service Class")
    
    return major_class_name, minor_class_name, service_class_name

def scan_bluetooth_devices():
    try:
        logging.info("[!] Scanning for Bluetooth devices...")
        discovered_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True)
        
        if not discovered_devices:
            logging.info("[-] No devices found.")
            return
        
        devices_table = []
        for addr, name, device_class in discovered_devices:
            major_class, minor_class, service_class = parse_device_class(device_class)
            devices_table.append([name, addr, f"{device_class} ({major_class}, {minor_class}, {service_class})"])
        
        print(tabulate(devices_table, headers=["Device Name", "MAC Address", "Device Class"], tablefmt="grid"))
    except bluetooth.BluetoothError as e:
        logging.error("[ERROR] Bluetooth error: %s", e)
    except Exception as e:
        logging.error("[ERROR] An unexpected error occurred: %s", e)

def run_scan_in_thread():
    scan_thread = threading.Thread(target=scan_bluetooth_devices)
    scan_thread.start()
    scan_thread.join()

if __name__ == "__main__":
    run_scan_in_thread()
