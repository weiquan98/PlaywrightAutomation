# test_playwrightautomation.py
"""
Tests for PlaywrightAutomation module.
"""

import unittest
from playwrightautomation import PlaywrightAutomation

class TestPlaywrightAutomation(unittest.TestCase):
    """Test cases for PlaywrightAutomation class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PlaywrightAutomation()
        self.assertIsInstance(instance, PlaywrightAutomation)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PlaywrightAutomation()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
