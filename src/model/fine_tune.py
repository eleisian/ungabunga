"""
Fine-Tuning Script for Ungabunga LLM

This script fine-tunes a DistilBERT model using Hugging Face's transformers library to process Ungabunga syntax for geography facts.
"""

import os
import argparse
from datasets import load_dataset
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments

def load_ungabunga_dataset(data_dir):
    """Load Ungabunga dataset from text files."""
    ungabunga_files = {
        'train': os.path.join(data_dir, 'ungabunga_facts.txt'),
    }
    dataset = load_dataset('text', data_files=ungabunga_files)
    # Add mock labels for demonstration (in a real scenario, these would be derived from data)
    def add_labels(example):
        example['label'] = 0  # Mock label; replace with actual label logic
        return example
    dataset = dataset.map(add_labels)
    return dataset

def tokenize_function(examples, tokenizer):
    """Tokenize the text data."""
    return tokenizer(examples['text'], padding='max_length', truncation=True, max_length=128)

def main():
    parser = argparse.ArgumentParser(description='Fine-tune DistilBERT on Ungabunga dataset')
    parser.add_argument('--data_dir', type=str, default='src/dataset', help='Directory containing dataset files')
    parser.add_argument('--output_dir', type=str, default='./output', help='Directory to save model outputs')
    parser.add_argument('--num_train_epochs', type=int, default=3, help='Number of training epochs')
    parser.add_argument('--per_device_train_batch_size', type=int, default=8, help='Batch size per device for training')
    args = parser.parse_args()

    # Load dataset
    dataset = load_ungabunga_dataset(args.data_dir)

    # Load tokenizer and model
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

    # Tokenize dataset
    tokenized_dataset = dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)
    tokenized_dataset = tokenized_dataset.remove_columns(['text'])
    tokenized_dataset = tokenized_dataset.rename_column('label', 'labels')
    tokenized_dataset.set_format('torch')

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        save_steps=10_000,
        save_total_limit=2,
    )

    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
    )

    # Train model
    trainer.train()

    # Save model
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

if __name__ == '__main__':
    main()
