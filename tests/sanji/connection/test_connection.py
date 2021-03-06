import os
import sys
import unittest

try:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../')
    from sanji.connection.connection import Connection
except ImportError:
    print "Please check the python PATH for import test module."
    exit(1)


class TestConnectionClass(unittest.TestCase):

    def test_init(self):
        conn = Connection()
        with self.assertRaises(NotImplementedError):
            conn.connect()
        with self.assertRaises(NotImplementedError):
            conn.disconnect()
        with self.assertRaises(NotImplementedError):
            conn.set_tunnel(None)
        with self.assertRaises(NotImplementedError):
            conn.set_on_connect(None)
        with self.assertRaises(NotImplementedError):
            conn.set_on_message(None)
        with self.assertRaises(NotImplementedError):
            conn.set_on_publish(None)
        with self.assertRaises(NotImplementedError):
            conn.publish(None)

if __name__ == "__main__":
    unittest.main()
