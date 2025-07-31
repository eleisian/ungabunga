"""
Entropy Calculation for Ungabunga Tokens

This script calculates the conditional entropy of token sequences in Ungabunga to evaluate predictability and information density.
"""

from scipy.stats import entropy
import numpy as np

# Mock probability distributions for token sequences (to be replaced with real corpus analysis)
# Example: Probabilities of next token after "cap Fr"
mock_probs_after_cap_fr = [0.8, 0.15, 0.05]  # High probability for 'Par', lower for others
mock_labels_after_cap_fr = ["Par", "OtherCity", "Unknown"]

# Calculate entropy in bits
ent_after_cap_fr = entropy(mock_probs_after_cap_fr, base=2)

# Display results
print("Conditional Entropy Calculation")
print("===============================")
print(f"Context: After 'cap Fr'")
print(f"Probabilities: {dict(zip(mock_labels_after_cap_fr, mock_probs_after_cap_fr))}")
print(f"Conditional Entropy: {ent_after_cap_fr:.2f} bits")
print("\nInterpretation: Lower entropy indicates higher predictability. A value close to 0 means the next token is almost certain.")

# Placeholder for future corpus-based calculation
if __name__ == "__main__":
    print("Note: This uses mock data. Future implementation will analyze a real Ungabunga corpus for accurate entropy calculations.")
    print("Goal: Demonstrate that Ungabunga syntax (e.g., 'cap Fr' predicting 'Par') results in lower entropy compared to natural language.")
