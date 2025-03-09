import os
import socket
import json
import concurrent.futures

class PortScanner:
    """
    A class used to represent a Port Scanner

    ...

    Attributes
    ----------
    ip_range : str
        a string representing the range of IP addresses to scan
    results : dict
        a dictionary to store the results of the scan

    Methods
    -------
    scan_ports(ip_address):
        Scans all ports for a given IP address and stores the results in the results dictionary.
    scan():
        Initiates the port scan for all IP addresses in the ip_range.
    get_results():
        Returns the results of the scan in a structured JSON format.
    """

    def __init__(self, ip_range: str):
        """
        Constructs all the necessary attributes for the Port Scanner object.

        Parameters
        ----------
            ip_range : str
                a string representing the range of IP addresses to scan
        """

        self.ip_range = ip_range
        self.results = {}

    def scan_ports(self, ip_address: str):
        """
        Scans all ports for a given IP address and stores the results in the results dictionary.

        Parameters
        ----------
            ip_address : str
                a string representing the IP address to scan
        """

        self.results[ip_address] = {}

        for port in range(0, 65536):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    self.results[ip_address][port] = 'Open'
                else:
                    self.results[ip_address][port] = 'Closed'
                sock.close()
            except Exception as e:
                self.results[ip_address][port] = 'Error: ' + str(e)

    def scan(self):
        """
        Initiates the port scan for all IP addresses in the ip_range.
        """

        ip_addresses = self.ip_range.split('-')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.scan_ports, ip_addresses)

    def get_results(self) -> str:
        """
        Returns the results of the scan in a structured JSON format.

        Returns
        -------
        str
            a string representing the results of the scan in a structured JSON format
        """

        return json.dumps(self.results, indent=4)


# Example usage
scanner = PortScanner('192.168.1.1-192.168.1.5')
scanner.scan()
print(scanner.get_results())