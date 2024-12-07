import unittest

if __name__ == "__main__":
    # Discover and run all tests in the current directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=".", pattern="*_test.py")

    runner = unittest.TextTestRunner()
    runner.run(suite)