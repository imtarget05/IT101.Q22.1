# Lab02_Modern_Cryptography

Bài thực hành các thuật toán mã hóa cổ điển bằng Python.

---

## Yêu cầu

- Python 3.x (không cần cài thêm thư viện ngoài)

---

## Cấu trúc thư mục

```
Lab01_ClassicalCryptography/
├── data/
│   ├── task2_1_cipher.txt   # Ciphertext cho Caesar
│   ├── task2_2_cipher.txt   # Ciphertext cho Monoalphabetic
│   ├── task2_4_cipher.txt   # Ciphertext cho Playfair
│   ├── task2_5_cipher.txt   # Ciphertext cho Vigenère
│   ├── task2_6_cipher.txt   # Ciphertext cho phá mã Vigenère
│   └── words.txt            # Từ điển tiếng Anh (dùng cho task2_3)
└── src/
    ├── task2_1.py           # Caesar Cipher
    ├── task2_3.py           # Monoalphabetic Cipher (phá mã)
    ├── task2_4.py           # Playfair Cipher
    ├── task2_5.py           # Vigenère Cipher
    ├── task2_6.py           # Phá mã Vigenère (Index of Coincidence)
    └── task2_7.py           # Rail Fence Cipher
```

---

## Hướng dẫn chạy

Mở terminal, di chuyển vào thư mục `src/`:

```bash
cd src
```

---

### Task 2.1 — Caesar Cipher

**File:** `task2_1.py`

---

### Task 2.3 — Phá mã Monoalphabetic (Simulated Annealing)

**File:** `task2_3.py`  

---

### Task 2.4 — Playfair Cipher

**File:** `task2_4.py`

```bash
python task2_4.py
```

---

### Task 2.5 — Vigenère Cipher

**File:** `task2_5.py`

```bash
python task2_5.py
```
---

### Task 2.6 — Phá mã Vigenère (Index of Coincidence + Chi-square)

**File:** `task2_6.py`
# python -m pip install sympy

```bash
python task2_6.py
```
---

## Ví dụ nhanh

```bash
# Chạy Caesar Cipher
cd src
python task2_1.py

# Chạy Playfair với khóa "SECRET"
python task2_4.py
# Nhập key: SECRET

# Chạy Rail Fence demo
python task2_7.py
```
 
 
 
