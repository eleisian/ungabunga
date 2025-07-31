# Information Theory Metrics for Ungabunga

Ungabunga is designed to maximize information density and minimize token count for efficient AI-to-AI and human-to-AI knowledge transfer. This document outlines the information theory metrics used to evaluate Ungabunga's efficiency compared to RDF triples and natural language.

## Metrics

### Average Bits per Token

- **Definition**: Estimate the average number of bits required to represent each token based on frequency. Frequent tokens (e.g., `C` for City) are assigned fewer bits, similar to Huffman coding.
- **Example**: 
  - Ungabunga: `cap Fr Par [T 987]` ≈ 5 bytes (assuming single-byte tokens)
  - Natural Language: "Paris is the capital of France since 987" ≈ 20–30 bytes
- **Implementation**: See `src/metrics/bits_per_token.py` for calculation scripts.

### Entropy

- **Definition**: Measure the conditional entropy of tokens to evaluate predictability. Low entropy indicates that the next token is highly predictable given the previous tokens.
- **Example**: After `cap Fr`, the next token is likely a city like `Par`, resulting in low entropy (H(next_token | cap Fr) ≈ low).
- **Implementation**: Use Python’s `scipy.stats.entropy` in `src/metrics/entropy.py` to calculate entropy in bits.
- **Code Snippet**:
  ```python
  from scipy.stats import entropy
  import numpy as np

  # Token probabilities (example)
  probs = [0.5, 0.3, 0.2]  # Probabilities of next tokens after "cap Fr"
  ent = entropy(probs, base=2)  # Entropy in bits
  print(f"Conditional Entropy: {ent} bits")
  ```

### Mutual Information

- **Definition**: Quantify how much information one token provides about another. High mutual information indicates strong predictive power between tokens.
- **Example**: `cap Fr` strongly predicts `Par`, resulting in high mutual information.
- **Implementation**: Planned for future metric scripts in `src/metrics/`.

## Comparison and Benchmarking

Ungabunga is benchmarked against RDF triples and natural language for efficiency:

- **Token Count**:
  - Ungabunga: `cap Fr Par` (3 tokens)
  - RDF: `<Paris, isCapitalOf, France>` (6 tokens)
  - Natural Language: "Paris is the capital of France" (~7–10 tokens)
- **Estimated Bits**:
  - Ungabunga: Low entropy, ~5 bits for `cap Fr Par`
  - RDF: ~10–15 bits
  - Natural Language: ~20–30 bits

## Goals

- **Quantify Efficiency**: Use these metrics to prove Ungabunga’s compactness and low entropy design.
- **Continuous Evaluation**: Automate metric calculations via GitHub Actions to validate improvements.
- **Community Input**: Encourage contributions to refine entropy calculations and mutual information estimates.

See `src/metrics/` for implementation details and `examples/` for practical demos of efficiency.
