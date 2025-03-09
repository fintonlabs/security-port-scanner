import unittest
from main import PortScanner

class TestPortScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = PortScanner('127.0.0.1-127.0.0.1')

    def test_scan(self):
        self.scanner.scan()
        results = self.scanner.get_results()
        self.assertIsInstance(results, str)

    def test_scan_ports(self):
        self.scanner.scan_ports('127.0.0.1')
        self.assertIn('127.0.0.1', self.scanner.results)

if __name__ == '__main__':
    unittest.main()