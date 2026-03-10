import json

notebook_path = '/Users/white/Desktop/Code/MacCode-master/PYproject/pythonProject/prime/3.weak3/day18/4.subword_embedding_lstm.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Modify ImdbDataset cell
for cell in nb['cells']:
    if cell.get('id') == 'e0f9f4f5':
        # New source code for ImdbDataset class
        new_source = [
            "import torch\n",
            "from torch.utils.data import Dataset, DataLoader\n",
            "\n",
            "# 构建标签词典\n",
            "all_labels = [label.strip() for label in train_labels]\n",
            "unique_labels = sorted(list(set(all_labels)))\n",
            "label2idx = {label: idx for idx, label in enumerate(unique_labels)}\n",
            "idx2label = {idx: label for label, idx in label2idx.items()}\n",
            "print(f\"标签词典大小: {len(label2idx)}\")\n",
            "\n",
            "class ImdbDataset(Dataset):\n",
            "    def __init__(self, texts, labels, label2idx, max_len=None):\n",
            "        self.texts = texts\n",
            "        self.labels = labels\n",
            "        self.label2idx = label2idx\n",
            "        self.max_len = max_len\n",
            "        \n",
            "    def __len__(self):\n",
            "        return len(self.texts)\n",
            "\n",
            "    def __getitem__(self, idx):\n",
            "        text=self.texts[idx]\n",
            "        label=self.labels[idx].strip()\n",
            "        label_id = self.label2idx.get(label, 0)\n",
            "        return {'text':text,'labels':label_id}\n",
            "\n"
        ]
        cell['source'] = new_source

    if cell.get('id') == 'e66abb59':
        # Modify collate_fn and instantiation
        new_source_complete = [
            "def collate_fn(batch):\n",
            "    \"\"\"\n",
            "    DataLoader 的 collate_fn，用于将一个 batch 的样本打包成 Tensor\n",
            "    \"\"\"\n",
            "    '''\n",
            "    不应该exts, labels = zip(*batch)\n",
            "    不应该使用zip(*batch)来解包batch, 因为batch中的每个样本都是一个字典, \n",
            "    而zip(*batch)会将每个字典的键值对解包成一个元组, 而不是一个样本\n",
            "    '''\n",
            "    texts = [item['text'] for item in batch]\n",
            "    labels = [item['labels'] for item in batch]\n",
            "    \n",
            "    # 注意：这里需要在外部访问 tokenizer 对象\n",
            "    batch_token_ids = tokenizer.encode(texts, padding_first=True)\n",
            "    \n",
            "    # 转换为 Tensor\n",
            "    input_ids = torch.tensor(batch_token_ids, dtype=torch.long)\n",
            "    '''张量不可以批量转换为Python标量,需要使用int()来转换每个元素'''\n",
            "    labels=torch.tensor(labels, dtype=torch.long)\n",
            "    # labels = torch.tensor([int(l.strip()) for l in labels], dtype=torch.long)\n",
            "    return {'input_ids': input_ids, 'labels': labels}\n",
            "\n",
            "# 实例化 \n",
            "batch_size = 64\n",
            "\n",
            "train_dataset = ImdbDataset(train_texts,train_labels, label2idx)\n",
            "test_dataset=ImdbDataset(test_texts,test_labels, label2idx)\n",
            "for d in train_dataset:\n",
            "    print(d['text'])\n",
            "    print(d['labels'])\n",
            "    break\n",
            "\n"
        ]
        cell['source'] = new_source_complete

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
