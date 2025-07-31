from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers
import os

# Define paths
data_dir = '../dataset'
output_dir = './bpe_tokenizer'
train_file = os.path.join(data_dir, 'ungabunga_facts.txt')

# Initialize Byte-Pair Encoding tokenizer
tokenizer = Tokenizer(models.BPE())

# Define pre-tokenizer (splits text into words)
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Train the tokenizer on the Ungabunga corpus
trainer = trainers.BpeTrainer(vocab_size=30000, min_frequency=2)
files = [train_file]
tokenizer.train(files, trainer)

# Save the tokenizer
os.makedirs(output_dir, exist_ok=True)
tokenizer.save(os.path.join(output_dir, 'tokenizer.json'))

print(f'BPE tokenizer trained and saved to {output_dir}/tokenizer.json')
