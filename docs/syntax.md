# Ungabunga Syntax

This document defines the syntax rules for Ungabunga, a dense symbolic language optimized for AI-to-AI and human-to-AI knowledge transfer. The syntax is inspired by Chinese minimal grammar and focuses on positional structure for efficiency.

## Syntax Structure

### Statements

- **Format**: `[relation] [subject] [object] [attributes]`
- **Example**: `R_cap N_Fr C_Par [T 987]` (Paris is the capital of France since 987)
- **Contextual Omission**: When context is clear (e.g., in Geography domain), tokens can be simplified. For instance, `R_cap N_Fr C_Par` can be written as `cap Fr Par`.

### Queries

- **Format**: `[relation?] [subject]`
- **Example**: `R_cap? N_Fr` or `cap? Fr` (What’s France’s capital?)
- **Response Example**: `cap Fr Par` (Paris is the capital of France)

### Nested Facts

- **Format**: Use brackets to nest related information.
- **Example**: `E [C_Par [R_cap N_Fr] [Pop 2.1M]]` (Paris is France’s capital, population 2.1 million)

## Rules

- **Positional Roles**: The position of a token defines its role in the statement (e.g., first token is typically the relation).
- **Omit Redundant Tokens**: Tokens can be omitted when context is clear (e.g., `R_cap` to `cap` in Geography context).
- **Optional Metadata**: Use brackets for additional information like time or certainty (e.g., `[T 987]`, `[p0.99]`).

## Information Theory Optimization

- **Huffman Coding**: Frequent concepts (e.g., `C`, `N`) are assigned single characters for efficiency, while specific entities (e.g., `C_Par`) use longer codes.
- **Low Entropy**: Token sequences are designed to be predictable (e.g., after `cap Fr`, the next token is likely a city like `Par`).
- **Mutual Information**: Tokens like `R_cap` carry high information about the relation, reducing the need for additional tokens.

## Examples

- **Statement**: "Paris is France’s capital since 987" → `cap Fr Par [T 987]` (4 tokens)
- **Query**: "What’s Japan’s capital?" → `cap? Jap` (2 tokens)
- **Response**: `cap Jap Tok` (3 tokens)
- **Comparison**:
  - RDF: `<Paris, isCapitalOf, France>, <Paris, capitalSince, 987>` (6 tokens)
  - Natural Language: "Paris is the capital of France since 987" (~7–10 tokens)

This syntax minimizes token count while preserving truth, making it ideal for efficient knowledge transfer.
