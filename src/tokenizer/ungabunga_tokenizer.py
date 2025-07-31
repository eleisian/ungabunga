"""
Ungabunga Tokenizer

This module provides a custom tokenizer for the Ungabunga language, designed to parse its dense symbolic syntax into token IDs for AI processing.
"""

from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
import json

class UngabungaTokenizer:
    def __init__(self, vocab_file):
        """
        Initialize the Ungabunga tokenizer with a vocabulary file.
        
        Args:
            vocab_file (str): Path to the vocabulary JSON file (e.g., vocab.json).
        """
        self.tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
        self.tokenizer.enable_padding()
        
        # Load vocabulary from JSON file
        with open(vocab_file, 'r') as f:
            self.vocab = json.load(f)
        
        # Add special tokens
        special_tokens = ["[UNK]", "[T", "[p"]
        
        # Train tokenizer with vocabulary
        trainer = WordLevelTrainer(vocab_size=1000, special_tokens=special_tokens)
        vocab_list = list(self.vocab.keys())
        self.tokenizer.train_from_iterator(vocab_list, trainer)
    
    def encode(self, text):
        """
        Encode Ungabunga text into token IDs.
        
        Args:
            text (str): Ungabunga text to encode (e.g., "cap Fr Par [T 987]").
        
        Returns:
            list: List of token IDs.
        """
        encoded = self.tokenizer.encode(text)
        return encoded.ids
    
    def decode(self, token_ids):
        """
        Decode token IDs back into Ungabunga text.
        
        Args:
            token_ids (list): List of token IDs to decode.
        
        Returns:
            str: Decoded Ungabunga text.
        """
        decoded = self.tokenizer.decode(token_ids)
        return decoded

if __name__ == "__main__":
    # Example usage
    tokenizer = UngabungaTokenizer("vocab.json")
    
    # Test encoding and decoding
    example_text = "cap Fr Par [T 987]"
    encoded_ids = tokenizer.encode(example_text)
    print(f"Encoded: {encoded_ids}")
    
    decoded_text = tokenizer.decode(encoded_ids)
    print(f"Decoded: {decoded_text}")
