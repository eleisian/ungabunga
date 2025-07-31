"""
AI-to-AI Knowledge Transfer Demo

This script demonstrates how two AI systems can exchange knowledge using Ungabunga's compact symbolic language.
"""

from src.tokenizer.ungabunga_tokenizer import UngabungaTokenizer

# Initialize tokenizer
tokenizer = UngabungaTokenizer("src/tokenizer/vocab.json")

# AI1 sends a fact
fact = "cap Fr Par [p0.99]"
encoded = tokenizer.encode(fact)  # Convert to token IDs for transmission
print(f"AI1 sends: {fact}")
print(f"Encoded transmission: {encoded}")

# AI2 receives and processes
decoded = tokenizer.decode(encoded)  # Convert back to Ungabunga syntax
print(f"AI2 received: {decoded}")
