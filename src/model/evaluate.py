"""
Evaluation Script for Ungabunga Model

This script evaluates the performance of the fine-tuned Ungabunga model by comparing token count, processing speed, and accuracy against RDF triples and natural language formats.
"""

import os
import argparse
import time
from transformers import LongformerTokenizer, LongformerForSequenceClassification
from datasets import load_dataset
import torch
from tokenizers import Tokenizer

def load_datasets(data_dir):
    """Load datasets for comparison."""
    ungabunga_files = {'test': os.path.join(data_dir, 'ungabunga_facts.txt')}
    rdf_files = {'test': os.path.join(data_dir, 'rdf_facts.txt')}
    natural_files = {'test': os.path.join(data_dir, 'natural_facts.txt')}
    
    ungabunga_dataset = load_dataset('text', data_files=ungabunga_files)
    rdf_dataset = load_dataset('text', data_files=rdf_files)
    natural_dataset = load_dataset('text', data_files=natural_files)
    
    return ungabunga_dataset, rdf_dataset, natural_dataset

def evaluate_token_count(dataset, tokenizer):
    """Evaluate average token count per example."""
    total_tokens = 0
    total_examples = len(dataset['test'])
    for example in dataset['test']:
        if isinstance(tokenizer, LongformerTokenizer):
            tokens = tokenizer(example['text'], return_tensors='pt')
            total_tokens += tokens['input_ids'].shape[1]
        else:
            encoding = tokenizer.encode(example['text'])
            total_tokens += len(encoding.ids)
    return total_tokens / total_examples if total_examples > 0 else 0

def evaluate_processing_speed(dataset, tokenizer):
    """Evaluate processing speed in examples per second."""
    start_time = time.time()
    for example in dataset['test']:
        if isinstance(tokenizer, LongformerTokenizer):
            tokenizer(example['text'], return_tensors='pt')
        else:
            tokenizer.encode(example['text'])
    end_time = time.time()
    total_time = end_time - start_time
    total_examples = len(dataset['test'])
    return total_examples / total_time if total_time > 0 else 0

def evaluate_accuracy(dataset, model, tokenizer):
    """Evaluate accuracy by performing inference on the dataset."""
    model.eval()
    correct = 0
    total = 0
    
    # For simplicity, use a small subset of data for demo (in real implementation, use full dataset or validation set)
    # Assume mock ground truth labels (in real scenario, these would be derived from data)
    for i, example in enumerate(dataset['test']):
        if total >= 10:  # Limit to 10 examples for quick evaluation
            break
        if isinstance(tokenizer, LongformerTokenizer):
            inputs = tokenizer(example['text'], return_tensors='pt', padding='max_length', truncation=True, max_length=4096)
        else:
            encoding = tokenizer.encode(example['text'], return_tensors='pt', padding='max_length', truncation=True, max_length=128)
            inputs = {'input_ids': encoding.ids, 'attention_mask': encoding.attention_mask}
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model(**inputs)
            pred_label = torch.argmax(outputs.logits, dim=1).item()
        
        # Mock ground truth label (replace with actual label logic)
        true_label = 0  # Assuming label 0 for all as placeholder; in real scenario, use actual labels
        if pred_label == true_label:
            correct += 1
        total += 1
    
    return correct / total if total > 0 else 0.0

def main():
    parser = argparse.ArgumentParser(description='Evaluate Ungabunga model performance')
    parser.add_argument('--data_dir', type=str, default='src/dataset', help='Directory containing dataset files')
    parser.add_argument('--model_dir', type=str, default='./output', help='Directory containing trained model')
    args = parser.parse_args()

    # Load datasets
    ungabunga_dataset, rdf_dataset, natural_dataset = load_datasets(args.data_dir)

    # Load tokenizer and model
    tokenizer = LongformerTokenizer.from_pretrained('allenai/longformer-base-4096')
    # Check for custom BPE tokenizer
    custom_tokenizer_path = '../tokenizer/bpe_tokenizer/tokenizer.json'
    if os.path.exists(custom_tokenizer_path):
        print(f'Loading custom BPE tokenizer from {custom_tokenizer_path}')
        tokenizer = Tokenizer.from_file(custom_tokenizer_path)
    model = LongformerForSequenceClassification.from_pretrained(args.model_dir)

    # Evaluate token count
    ungabunga_token_count = evaluate_token_count(ungabunga_dataset, tokenizer)
    rdf_token_count = evaluate_token_count(rdf_dataset, tokenizer)
    natural_token_count = evaluate_token_count(natural_dataset, tokenizer)

    print(f'Average Token Count:\nUngabunga: {ungabunga_token_count:.2f}\nRDF: {rdf_token_count:.2f}\nNatural Language: {natural_token_count:.2f}')

    # Evaluate processing speed
    ungabunga_speed = evaluate_processing_speed(ungabunga_dataset, tokenizer)
    rdf_speed = evaluate_processing_speed(rdf_dataset, tokenizer)
    natural_speed = evaluate_processing_speed(natural_dataset, tokenizer)

    print(f'Processing Speed (examples/sec):\nUngabunga: {ungabunga_speed:.2f}\nRDF: {rdf_speed:.2f}\nNatural Language: {natural_speed:.2f}')

    # Evaluate accuracy
    ungabunga_accuracy = evaluate_accuracy(ungabunga_dataset, model, tokenizer)
    rdf_accuracy = evaluate_accuracy(rdf_dataset, model, tokenizer)
    natural_accuracy = evaluate_accuracy(natural_dataset, model, tokenizer)

    print(f'Accuracy:\nUngabunga: {ungabunga_accuracy:.2f}\nRDF: {rdf_accuracy:.2f}\nNatural Language: {natural_accuracy:.2f}')

if __name__ == '__main__':
    main()
