# The code should implement a lightweight port scanning tool that identifies open ports and potential vulnerabilities across a network


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [📋 Table of Contents](#📋-table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation Process](#installation-process)
- [Verification Steps](#verification-steps)
- [Post-Installation Configuration](#post-installation-configuration)
- [Overview](#overview)
- [Basic Usage](#basic-usage)
- [Common Use Cases](#common-use-cases)
- [Command-line Parameters](#command-line-parameters)
- [Expected Output](#expected-output)
- [Advanced Usage Scenarios](#advanced-usage-scenarios)
- [Class Description](#class-description)
- [PortScanner Class Initialization](#portscanner-class-initialization)
- [scan_ports Method](#scan_ports-method)
- [detect_vulnerabilities Method](#detect_vulnerabilities-method)
- [Code Examples](#code-examples)
- [Common Patterns and Best Practices](#common-patterns-and-best-practices)
- [⚙️ Configuration](#⚙️-configuration)
- [🔍 Troubleshooting](#🔍-troubleshooting)
- [🤝 Contributing](#🤝-contributing)
- [📄 License](#📄-license)
- [API Documentation](#api-documentation)
## Project Overview 

The PortScanner project is a lightweight, efficient, and easy-to-use tool written in Python for performing port scanning across a network. The primary aim is to identify open ports and potential vulnerabilities, assisting network administrators and cybersecurity professionals in securing their systems. This tool allows for a broad or targeted search, offering flexibility depending on the user's needs. By identifying open ports and highlighting potential risks, this tool serves as a proactive measure in maintaining network security and stability.

## Features

- **Host Configuration** :house: : This feature allows the user to specify the host to scan. The `__init__` function takes a string argument `host` to set the target for the port scanning.

- **Port Scanning** :satellite: : This tool scans a range of ports on the specified host to check if they are open. The `scan_ports` function takes two integer arguments, `start_port` and `end_port`, which define the range of ports to scan. It creates a socket and attempts to connect to each port in the range. If the connection is successful (result == 0), the port is considered open, and it is added to the `open_ports` list.

- **Open Port Detection** :mag: : The PortScanner class maintains a list of open ports found during the scanning process. This list, `open_ports`, is updated in real-time as the scanner finds open ports.

- **Vulnerability Detection** :shield: : The PortScanner class includes a `detect_vulnerabilities` function. While currently a placeholder, this function will be used to detect potential vulnerabilities in the network based on the open ports found.

- **Flexible Timeouts** :hourglass_flowing_sand: : For efficiency and to prevent hanging, the socket connection has a timeout set. The `scan_ports` function sets a timeout of 1 second for each socket connection attempt. This ensures that the scanner doesn't waste time on ports that are not responding.

- **Clean Resource Management** :recycle: : The PortScanner ensures that all sockets used during the scanning process are properly closed after use. The `scan_ports` function calls `sock.close()` after each port scan, ensuring that no resources are left hanging.

The PortScanner project is a versatile and valuable tool for anyone looking to improve their network security. Its lightweight design and clear output make it a great choice for both professionals and beginners in the field of cybersecurity.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation Instructions

## Prerequisites
To install and run this lightweight port scanning tool, you will need the following software and dependencies:

- Python 3.6 or higher: Python is the programming language used to write the tool. You can download Python from its [official website](https://www.python.org/downloads/).
- Pip: Pip is a package manager for Python, used to install and manage additional packages that aren't included in the standard library. It's typically included with Python.

## Installation Process

1. **Download the Project Files**

   First, you'll need to download the project files from the source. This can typically be done by cloning the repository if it's hosted on a platform like GitHub:
   ```bash
   git clone https://github.com/username/repository.git
   ```
   Replace `https://github.com/username/repository.git` with the URL of the repository you want to clone.

2. **Navigate to the Project Directory**

   Use the command line to navigate into the directory that contains the project files:
   ```bash
   cd repository
   ```
   Replace `repository` with the name of the directory you want to navigate into.

3. **Install the Required Dependencies**

   This project doesn't require any additional Python packages outside of the standard library, so you can skip this step.

## Verification Steps

Once you've installed Python and downloaded the project files, you can check to see if everything is working correctly:

1. **Check Python Version**

   Open a terminal or command prompt and run the following command:
   ```bash
   python --version
   ```
   This should return a version number. If you see a version number (like `Python 3.8.5`), Python is installed correctly.

2. **Run the Script**

   You can also verify the installation by running the script with some test input. Navigate to the folder with the script and run:
   ```bash
   python port_scanner.py
   ```
   Replace `port_scanner.py` with the name of the Python file you want to run.

## Post-Installation Configuration

The `PortScanner` class takes the host as an argument. This host is the IP address or domain name of the machine you want to scan. You will need to provide this when creating a new instance of the `PortScanner` class:

```python
scanner = PortScanner('192.168.1.1')
```

Replace `'192.168.1.1'` with the IP address or domain name you want to scan.

Remember, it's important to use this tool responsibly and only scan networks you have permission to scan. Unauthorized scanning can be illegal and unethical.

# PortScanner Usage Documentation

## Overview
The `PortScanner` is a lightweight port scanning tool. It is designed to scan a specified network host for open ports and potential vulnerabilities.

## Basic Usage

To use the `PortScanner`, follow these steps:

```python
# Import the class
from portscanner import PortScanner

# Initialize the scanner with a host
scanner = PortScanner('127.0.0.1')

# Scan ports from 20 to 80
scanner.scan_ports(20, 80)

# Print the open ports
print(scanner.open_ports)
```

## Common Use Cases

### Scanning a Range of Ports

The `scan_ports` method accepts a start port and an end port as parameters. It scans all the ports in the given range, inclusive.

```python
# Scan ports from 20 to 80
scanner.scan_ports(20, 80)

# Print the open ports
print(scanner.open_ports)
```

### Detecting Potential Vulnerabilities

The `detect_vulnerabilities` method is a placeholder for a vulnerability scanning tool.

```python
# Detect vulnerabilities
scanner.detect_vulnerabilities()

# Print the potential vulnerabilities
print(scanner.vulnerabilities)
```

## Command-line Parameters

This tool does not currently support command-line arguments or parameters.

## Expected Output

The `scan_ports` method populates the `open_ports` list with any open ports it finds.

```python
print(scanner.open_ports)
# Output: [22, 80]
```

## Advanced Usage Scenarios

The `PortScanner` class can be extended to include advanced functionality.

```python
class AdvancedPortScanner(PortScanner):
    def __init__(self, host: str):
        super().__init__(host)

    def scan_ports(self, start_port: int, end_port: int):
        super().scan_ports(start_port, end_port)
        print(f'Scanned ports {start_port} to {end_port} on host {self.host}')

    def detect_vulnerabilities(self):
        super().detect_vulnerabilities()
        print('Vulnerability detection is not yet implemented.')
```

This `AdvancedPortScanner` class inherits from `PortScanner` and adds additional print statements to the `scan_ports` and `detect_vulnerabilities` methods.

```python
# Initialize the advanced scanner with a host
adv_scanner = AdvancedPortScanner('127.0.0.1')

# Scan ports from 20 to 80
adv_scanner.scan_ports(20, 80)

# Detect vulnerabilities
adv_scanner.detect_vulnerabilities()
```

Output:

```bash
Scanned ports 20 to 80 on host 127.0.0.1
Vulnerability detection is not yet implemented.
```

# PortScanner Class API Documentation

## Class Description

The `PortScanner` is a lightweight port scanning tool written in Python that identifies open ports and potential vulnerabilities across a network.

```python
class PortScanner:
    """
    A lightweight port scanning tool that identifies open ports and potential vulnerabilities across a network.
    """
```

## PortScanner Class Initialization

The `PortScanner` class is initialized with a `host` parameter. The `host` parameter is a string that represents the host IP address or hostname.

```python
def __init__(self, host: str):
    self.host = host
    self.open_ports = []
    self.vulnerabilities = []
```

## scan_ports Method

This method scans the ports in the given range and identifies the open ports. It accepts two parameters, `start_port` and `end_port`, which define the range of ports to scan.

```python
def scan_ports(self, start_port: int, end_port: int) -> None:
    """
    Scan the ports in the given range and identify the open ones.
    """
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start_port | int | The start of the port range to scan. |
| end_port | int | The end of the port range to scan. |

### Return Value

This method doesn't return any value. However, it updates the `open_ports` attribute of the `PortScanner` object with the list of open ports.

## detect_vulnerabilities Method

This method is used to detect potential vulnerabilities. This is currently a placeholder method.

```python
def detect_vulnerabilities(self) -> None:
    """
    Detect potential vulnerabilities. This is a placeholder method as actual vulnerabili
    """
```

### Parameters

This method doesn't require any parameters.

### Return Value

This method doesn't return any value. However, it is expected to update the `vulnerabilities` attribute of the `PortScanner` object when implemented.

## Code Examples

```python
# Create an instance of PortScanner for the localhost
scanner = PortScanner('localhost')

# Scan ports 20 to 1024
scanner.scan_ports(20, 1024)

# Print the list of open ports
print(scanner.open_ports)

# Detect vulnerabilities
scanner.detect_vulnerabilities()
```

## Common Patterns and Best Practices

- Always start with a smaller range of ports for scanning to avoid unnecessary load on the network.
- Use the `scan_ports` method before calling the `detect_vulnerabilities` method, as the former updates the `open_ports` attribute which might be used by the latter.
- It's important to handle exceptions and timeouts properly when scanning ports to avoid crashing the program. This is already implemented in the `scan_ports` method.
- Remember that port scanning can be seen as an aggressive act by some systems and may violate some network policies. Always get proper authorization before scanning ports on any network.

## ⚙️ Configuration
Configuration options for customizing the application's behavior.

## 🔍 Troubleshooting
Common issues and their solutions.

## 🤝 Contributing
Guidelines for contributing to the project.

## 📄 License
This project is licensed under the MIT License.

## API Documentation

### Endpoints

#### `GET /api/resource`

Returns a list of resources.

**Parameters:**

- `limit` (optional): Maximum number of resources to return

**Response:**

```json
{
  "resources": [
    {
      "id": 1,
      "name": "Resource 1"
    }
  ]
}
```
