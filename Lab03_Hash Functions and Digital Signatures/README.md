# Lab03 Hash Functions and Digital Signatures

Bài thực hành về hàm băm mật mã, va chạm (collision), và xác minh chữ ký số/chứng chỉ X.509.

---

## Yêu cầu

- Python 3.x
- OpenSSL (dùng cho các bước phân tích chứng chỉ và hash)
- Công cụ hash dòng lệnh: `md5sum`, `sha1sum`, `sha256sum`
- (Tùy chọn cho Task 2.3) `md5collgen`

---

## Cấu trúc thư mục

```
Lab03_Hash Functions and Digital Signatures/
├── NT101_Lab03__Hash_Functions_and_Digital_Signatures.pdf
├── README.md
└── src/
    ├── task2_1.py                    # RSA: tạo khóa, mã hóa/giải mã, giải bản mã mẫu
    ├── task2_2/
    │   ├── hello                     # File thực thi mẫu cho quan sát hash/collision
    │   ├── erase                     # File thực thi mẫu cho quan sát hash/collision
    │   ├── msg1.bin                  # Message 1 (binary)
    │   ├── msg2.bin                  # Message 2 (binary)
    │   ├── shattered-1.pdf           # Cặp PDF SHA-1 collision
    │   └── shattered-2.pdf
    └── task2_4/
        ├── c0.pem                    # Chứng chỉ server
        ├── c1.pem                    # Chứng chỉ issuer (CA trung gian)
        └── c0_body.bin               # Phần thân chứng chỉ đã tách bằng ASN.1
```

---

## Hướng dẫn chạy

Mở terminal, di chuyển vào thư mục `src/`:

```bash
cd src
```

---

### Task 2.1 — Mã hóa khóa công khai RSA

**File:** `task2_1.py`

```bash
python task2_1.py
```

**Nội dung chính chương trình:**
- Tạo khóa công khai/riêng tư từ các bộ tham số `p, q, e` đề bài cho trước
- Thực hiện mã hóa/giải mã với `M = 5` cho 2 mục tiêu:
	- **Confidentiality:** $C = M^e \bmod n$, giải mã bằng $d$
	- **Authentication:** $C = M^d \bmod n$, xác minh bằng $e$
- Mã hóa chuỗi `"The University of Information Technology"` và in bản mã Base64
- Giải mã các bản mã mẫu (Base64/Hex/Binary) trong đề bài

---

### Task 2.2 — Đặc tính của hàm băm (MD5, SHA-1)

**Thư mục dữ liệu:** `task2_2/`

Thực hiện lần lượt các kiểm tra hash theo đề bài:

```bash
# So sánh hash của 2 message nhị phân
md5sum task2_2/msg1.bin task2_2/msg2.bin

# Quan sát với SHA-1/SHA-256
sha1sum task2_2/msg1.bin task2_2/msg2.bin
sha256sum task2_2/msg1.bin task2_2/msg2.bin

# So sánh 2 file thực thi
md5sum task2_2/hello task2_2/erase

# So sánh cặp PDF SHAttered
sha1sum task2_2/shattered-1.pdf task2_2/shattered-2.pdf
sha256sum task2_2/shattered-1.pdf task2_2/shattered-2.pdf
```

**Gợi ý báo cáo quan sát:**
- Các file khác nội dung nhưng có thể trùng hash ở thuật toán yếu (MD5/SHA-1)
- Thuật toán mạnh hơn (ví dụ SHA-256) cho hash khác nhau rõ ràng

---

### Task 2.3 (*) — Tạo MD5 collision với cùng prefix

**Công cụ:** `md5collgen`

Ví dụ lệnh theo tài liệu lab:

```bash
md5collgen -p prefix.txt -o out1.bin out2.bin
diff out1.bin out2.bin
md5sum out1.bin out2.bin
xxd out1.bin | head
```

**Mục tiêu:**
- Tạo 2 file khác nhau nhưng có cùng MD5
- Kiểm tra ảnh hưởng khi độ dài `prefix` không là bội số của 64 byte

---

### Task 2.4 — Xác minh thủ công X.509 Certificate (RSA)

**Thư mục dữ liệu:** `task2_4/`

Các bước thao tác OpenSSL theo lab:

```bash
# 1) Trích modulus (n) từ chứng chỉ issuer (CA)
openssl x509 -in task2_4/c1.pem -noout -modulus

# 2) In toàn bộ trường để lấy exponent (e)
openssl x509 -in task2_4/c1.pem -text -noout

# 3) Xem chữ ký từ chứng chỉ server
openssl x509 -in task2_4/c0.pem -text -noout

# 4) Phân tích ASN.1 và trích phần thân chứng chỉ (TBS)
openssl asn1parse -i -in task2_4/c0.pem
openssl asn1parse -i -in task2_4/c0.pem -strparse 4 -out task2_4/c0_body.bin -noout

# 5) Tính hash phần thân
sha256sum task2_4/c0_body.bin
```

Sau đó viết chương trình Python để xác minh chữ ký theo công thức RSA:

$$
EM' = S^e \bmod n
$$

So sánh hash trích xuất từ `EM'` với `SHA-256(TBS)` để kết luận chứng chỉ hợp lệ hay không.

---

## Ghi chú

- Task 2.2 và 2.3 là các task có dấu (*) trong tài liệu
- Nếu chạy file thực thi `hello`/`erase` bị từ chối quyền, thêm quyền trước khi chạy:

```bash
chmod +x task2_2/hello task2_2/erase
./task2_2/hello
./task2_2/erase
```

- Nên giữ nguyên dữ liệu mẫu trong `task2_2/` và `task2_4/` để tái hiện kết quả như lab
