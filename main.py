import socket
import os
import sys
import json
import csv
import datetime
from typing import Dict, List, Any

class PortScanner:
    """
    A lightweight port scanning tool that identifies open ports and potential vulnerabilities across a network.
    """

    def __init__(self, host: str):
        self.host = host
        self.open_ports = []
        self.vulnerabilities = []

    def scan_ports(self, start_port: int, end_port: int) -> None:
        """
        Scan the ports in the given range and identify the open ones.
        """
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.host, port))
            if result == 0:
                self.open_ports.append(port)
            sock.close()

    def detect_vulnerabilities(self) -> None:
        """
        Detect potential vulnerabilities. This is a placeholder method as actual vulnerability detection would require
        a database of known vulnerabilities which is beyond the scope of this task.
        """
        for port in self.open_ports:
            self.vulnerabilities.append({
                'port': port,
                'vulnerability_id': 'VULN001',
                'description': 'Example vulnerability',
                'severity': 'High',
                'remediation': 'Update to the latest version'
            })

    def generate_report(self, format: str) -> Dict[str, Any]:
        """
        Generate a report of the scan in the specified format (JSON or CSV).
        """
        scan_info = {
            'host': self.host,
            'scan_date': str(datetime.datetime.now()),
            'scan_type': 'Port and Vulnerability Scan'
        }

        port_info = [{'port': port, 'state': 'open'} for port in self.open_ports]

        report = {
            'scan_info': scan_info,
            'port_info': port_info,
            'vulnerabilities': self.vulnerabilities
        }

        if format.lower() == 'json':
            with open('report.json', 'w') as f:
                json.dump(report, f, indent=4)
        elif format.lower() == 'csv':
            with open('report.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Scan Information', ''])
                for key, value in scan_info.items():
                    writer.writerow([key, value])
                writer.writerow(['Port Information', ''])
                for info in port_info:
                    writer.writerow([info['port'], info['state']])
                writer.writerow(['Vulnerability Information', ''])
                for vuln in self.vulnerabilities:
                    writer.writerow([vuln['port'], vuln['vulnerability_id'], vuln['description'], vuln['severity'], vuln['remediation']])
        else:
            raise ValueError('Invalid format. Please choose either "json" or "csv".')

        return report

    def run(self, start_port: int, end_port: int, format: str) -> Dict[str, Any]:
        """
        Run the port scanner.
        """
        self.scan_ports(start_port, end_port)
        self.detect_vulnerabilities()
        return self.generate_report(format)


# Example usage
if __name__ == "__main__":
    scanner = PortScanner('localhost')
    report = scanner.run(70, 90, 'json')
    print(json.dumps(report, indent=4))