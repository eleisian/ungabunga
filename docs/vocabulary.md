# Ungabunga Vocabulary

This document outlines the initial vocabulary for Ungabunga, a dense symbolic language for efficient knowledge transfer. The vocabulary is designed for the Geography domain initially, with plans for expansion.

## Primitive Tokens

These are the base tokens used frequently in Ungabunga, assigned short codes for efficiency (inspired by Huffman coding):

- **C**: City (e.g., `C_Par` for Paris)
- **N**: Nation (e.g., `N_Fr` for France)
- **R**: Relation (generic, e.g., `R_cap` for capital)
- **T**: Time (e.g., `T_987` for year 987)
- **Pop**: Population
- **Bord**: Borders (relation)
- **Loc**: Location (e.g., coordinates)
- **?**: Query marker (e.g., `R_cap? N_Fr` for "What’s France’s capital?")
- **p**: Certainty/probability (e.g., `p0.99` for 99% confidence)

## Entity Abbreviations

Specific entities are abbreviated for compactness:

- **Fr**: France
- **Par**: Paris
- **Tok**: Tokyo
- **Jap**: Japan
- **Ca**: Canada
- **US**: USA

## Compositional Rules

- **Combine Primitives**: Tokens can be combined for complex concepts (e.g., `R_cap` for capital relation, `C_Par` for city Paris).
- **Hierarchy with Underscores**: Use underscores to denote hierarchy (e.g., `C_N_Fr` for capital city of France).
- **Attributes in Brackets**: Add metadata or attributes in brackets (e.g., `[T 987]` for "since 987", `[p0.99]` for certainty).

## Chinese Inspiration

Ungabunga tokens are inspired by the density and compositional nature of Chinese characters, particularly radicals. Just as Chinese characters combine semantic components (e.g., 都 for 'capital' includes elements of 'city' and 'place'), Ungabunga tokens like `C` (City) and `N` (Nation) combine into `C_N` to represent 'capital of a nation'. This approach maximizes information density, allowing complex concepts to be encoded in minimal tokens.

## Vocabulary File

The full vocabulary with token IDs is maintained in `src/tokenizer/vocab.json`. Community contributions to expand this vocabulary (target: ~100 tokens) are welcome.

## Examples

- "Paris is France’s capital since 987": `cap Fr Par [T 987]`
- "Tokyo’s population is 37 million": `Pop C_Tok 37M`
- "Canada borders the USA": `Bord N_Ca N_US`
