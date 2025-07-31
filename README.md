# Ungabunga

A dense, symbolic language for efficient AI-to-AI and human-to-AI knowledge transfer, minimizing token count while preserving truth.

## Overview

Ungabunga is inspired by Chinese logographic density, compositional symbols, and information theory (e.g., Huffman coding, low entropy). Initially focused on the Geography domain, it aims to represent facts like capitals, populations, and historical events in a compact form for AI processing.

## Goals

- Develop a compact symbolic language for knowledge transfer.
- Optimize for low token count and high information density.
- Focus initially on Geography (e.g., 'Paris is France’s capital since 987' as `cap Fr Par [T 987]`).
- Host as an open-source project on GitHub for community contributions.

## Unique Value Proposition

Ungabunga stands out from existing systems like RDF triples, Lojban, and knowledge graphs by offering:
- **Real-Time AI Optimization**: Designed for transformer-based LLMs and low-bandwidth AI-to-AI transfer, unlike database-oriented RDF or knowledge graphs.
- **Higher Density for Complex Facts**: Uses nested, symbolic syntax (e.g., `cap Fr Par [T 987]` in 4 tokens) compared to RDF’s multiple triples (e.g., 6 tokens).
- **AI-Centric Design**: Prioritizes machine-friendly, ultra-compact tokens over human-centric systems like Lojban.
- **Chinese-Inspired Symbolism**: Leverages compositional tokens (e.g., `C_N` from `C` + `N`) for flexible, dense encoding.
- **Context-Adaptive Syntax**: Reduces token count via information theory principles (e.g., omitting implied entities), unlike static structures in knowledge graphs.

For a detailed comparison, see [docs/comparisons.md](docs/comparisons.md).

## Setup Instructions

1. Clone the repository: `git clone https://github.com/eleisian/ungabunga.git`
2. Navigate to the project directory: `cd ungabunga`
3. Install dependencies (to be updated as project develops).

## Project Structure

- `docs/`: Documentation for vocabulary, syntax, and metrics.
- `src/`: Source code for tokenizer, datasets, models, and metrics.
- `tests/`: Unit tests for tokenizer and model.
- `examples/`: Demos for AI-to-AI and human-to-AI interactions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to vocabulary, syntax, and AI integration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
