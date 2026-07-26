# test_modelsafe.py
"""
Tests for ModelSafe module.
"""

import unittest
from modelsafe import ModelSafe

class TestModelSafe(unittest.TestCase):
    """Test cases for ModelSafe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelSafe()
        self.assertIsInstance(instance, ModelSafe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelSafe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
