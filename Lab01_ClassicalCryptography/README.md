# Lab01 Classical Cryptography

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

```bash
python task2_1.py
```

**Menu:**
| Lựa chọn | Chức năng |
|-----------|-----------|
| 1 | Mã hóa (Encrypt) — nhập plaintext và khóa k |
| 2 | Giải mã (Decrypt) — nhập ciphertext và khóa k |
| 3 | Brute-force — tự động thử 26 khóa với ciphertext từ `data/task2_1_cipher.txt` |
| 4 | Thoát |

---

### Task 2.3 — Phá mã Monoalphabetic (Simulated Annealing)

**File:** `task2_3.py`  
**Phụ thuộc:** `data/words.txt`, `data/task2_2_cipher.txt`

```bash
python task2_3.py
```

**Menu:**
| Lựa chọn | Chức năng |
|-----------|-----------|
| 1 | Đọc ciphertext từ file `data/task2_2_cipher.txt` |
| 2 | Nhập ciphertext thủ công từ bàn phím |

Chương trình sử dụng thuật toán **Simulated Annealing** kết hợp từ điển `words.txt` để tự động tìm khóa giải mã.

---

### Task 2.4 — Playfair Cipher

**File:** `task2_4.py`

```bash
python task2_4.py
```

Nhập **khóa** trước khi vào menu chính. Chương trình sẽ hiển thị ma trận Playfair 5×5 tương ứng.

**Menu:**
| Lựa chọn | Chức năng |
|-----------|-----------|
| 1 | Mã hóa — nhập plaintext |
| 2 | Giải mã — nhập ciphertext |
| 3 | Giải mã từ file `data/task2_4_cipher.txt` |
| 4 | Thoát |

> **Lưu ý:** Chữ `J` được coi là `I` theo quy tắc Playfair.

---

### Task 2.5 — Vigenère Cipher

**File:** `task2_5.py`

```bash
python task2_5.py
```

Nhập **khóa** trước khi vào menu chính.

**Menu:**
| Lựa chọn | Chức năng |
|-----------|-----------|
| 1 | Mã hóa — nhập plaintext |
| 2 | Giải mã — nhập ciphertext |
| 3 | Giải mã từ file `data/task2_5_cipher.txt` |
| 4 | Thoát |

---

### Task 2.6 — Phá mã Vigenère (Index of Coincidence + Chi-square)

**File:** `task2_6.py`

```bash
python task2_6.py
```

**Menu:**
| Lựa chọn | Chức năng |
|-----------|-----------|
| 1 | Nhập ciphertext từ bàn phím |
| 2 | Đọc ciphertext từ file `data/task2_6_cipher.txt` |

Chương trình tự động:
1. Dự đoán độ dài khóa dựa trên **Index of Coincidence (IC)**
2. Tìm từng ký tự khóa bằng **Chi-square test**
3. In ra khóa ước đoán và plaintext tương ứng

---

### Task 2.7 — Rail Fence Cipher

**File:** `task2_7.py`

```bash
python task2_7.py
```

Chương trình chạy **demo tự động** với chuỗi `"HELLO WORLD"` và 3 rails, in ra:
- Plaintext gốc
- Ciphertext sau khi mã hóa Rail Fence
- Plaintext sau khi giải mã

Để tùy chỉnh, chỉnh sửa biến `plaintext` và `rails` trong file.

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
 
 
 
