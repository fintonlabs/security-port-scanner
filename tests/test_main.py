import unittest
from portscanner import PortScanner

class TestPortScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = PortScanner('localhost')

    def test_scan_ports(self):
        self.scanner.scan_ports(70, 80)
        self.assertTrue(len(self.scanner.open_ports) >= 0)

    def test_detect_vulnerabilities(self):
        self.scanner.scan_ports(70, 80)
        self.scanner.detect_vulnerabilities()
        self.assertTrue(len(self.scanner.vulnerabilities) >= 0)

    def test_generate_report(self):
        report = self.scanner.run(70, 80, 'json')
        self.assertTrue('scan_info' in report)
        self.assertTrue('port_info' in report)
        self.assertTrue('vulnerabilities' in report)

if __name__ == '__main__':
    unittest.main()