import socket
import threading
import unittest
from check import check

class Checks(unittest.TestCase):
    def test_listener_is_reachable(self):
        with socket.socket() as server:
            server.bind(("127.0.0.1", 0))
            server.listen()
            def accept():
                connection, _ = server.accept()
                connection.close()
            worker = threading.Thread(target=accept)
            worker.start()
            result = check("127.0.0.1", server.getsockname()[1])
            worker.join(timeout=2)
            self.assertTrue(result["ok"])
    def test_refused_connection(self):
        with socket.socket() as server:
            server.bind(("127.0.0.1", 0))
            result = check("127.0.0.1", server.getsockname()[1], 0.2)
            self.assertFalse(result["ok"])
            self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
