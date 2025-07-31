"""
Unit Tests for Ungabunga Tokenizer

This module contains tests to verify the functionality of the UngabungaTokenizer class.
"""

import unittest
from src.tokenizer.ungabunga_tokenizer import UngabungaTokenizer

class TestUngabungaTokenizer(unittest.TestCase):
    def setUp(self):
        """
        Set up the tokenizer instance before each test.
        """
        self.tokenizer = UngabungaTokenizer("src/tokenizer/vocab.json")
    
    def test_encode_decode(self):
        """
        Test encoding and decoding of an Ungabunga statement.
        """
        text = "cap Fr Par [T 987]"
        encoded = self.tokenizer.encode(text)
        decoded = self.tokenizer.decode(encoded)
        
        self.assertIsInstance(encoded, list, "Encoded output should be a list of token IDs")
        self.assertEqual(decoded, text, f"Decoded text should match original input. Expected {text}, got {decoded}")
    
    def test_query_encoding(self):
        """
        Test encoding of a query statement.
        """
        text = "cap? Fr"
        encoded = self.tokenizer.encode(text)
        decoded = self.tokenizer.decode(encoded)
        
        self.assertIsInstance(encoded, list, "Encoded output should be a list of token IDs")
        self.assertEqual(decoded, text, f"Decoded query should match original input. Expected {text}, got {decoded}")
    
    def test_population_fact(self):
        """
        Test encoding and decoding of a population fact.
        """
        text = "Pop C_Tok 37M"
        encoded = self.tokenizer.encode(text)
        decoded = self.tokenizer.decode(encoded)
        
        self.assertIsInstance(encoded, list, "Encoded output should be a list of token IDs")
        self.assertEqual(decoded, text, f"Decoded population fact should match original input. Expected {text}, got {decoded}")

if __name__ == '__main__':
    unittest.main()
