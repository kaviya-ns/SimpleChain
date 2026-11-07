# SimpleChain

**A minimal blockchain ledger with a Flask web interface.**

SimpleChain shows the core idea of a blockchain in a few dozen lines: every transaction is a block, every block stores the SHA-256 hash of the block before it, and tampering with any block breaks the chain — which the integrity check catches.

![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)

---

## How it works

```
Block 0 (genesis) ◄── hash ── Block 1 ◄── hash ── Block 2 ◄── ...
```

- Blocks are JSON files stored in `blockchain/` (`0`, `1`, `2`, …).
- Each block holds `holder`, `amount`, `type` and a `prev_block` pointer with the previous block's filename and SHA-256 hash.
- A genesis block is created automatically on first run.
- `check_integrity()` recomputes every previous hash and flags any block whose stored hash no longer matches — i.e. tampered data.

## Project Structure

```
SimpleChain/
├── main.py         # Flask app: form to add transactions
├── block.py        # Block creation, hashing, integrity check
├── index.html      # Web form
└── requirements.txt
```

## Run it

```bash
git clone https://github.com/kaviya-ns/SimpleChain.git
cd SimpleChain
pip install -r requirements.txt
mkdir templates && cp index.html templates/   # Flask looks for templates here
python main.py
```

Open <http://127.0.0.1:5000> and add a few transactions. Then edit a file in `blockchain/` by hand and run the integrity check to watch it detect the tampering:

```bash
python -c "from block import check_integrity; print(check_integrity())"
```
