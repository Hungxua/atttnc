# An toàn thông tin nâng cao: bài tập và lời giải chi tiết

Đối chiếu bằng **số slide in trong mỗi bộ tài liệu**. Trang PDF=⌈số slide/2⌉. Có cả bài được đặt tên “bài tập” và ví dụ tính toán để không bỏ sót phần cần luyện. Các ví dụ tự luyện CĐ4 nằm ở cuối và được phân biệt rõ với đề gốc.

Ký hiệu: ⌈x⌉ là làm tròn lên; log₂ là log cơ số 2; B=byte, b=bit; 1 B=8b. Khi tính băng thông mạng, dùng 1 Gbps=10⁹bit/s. Dấu chấm trong số như 20.000 dùng để phân cách hàng nghìn; dấu phẩy là phần thập phân.

## 1. Danh mục bài và kết quả nhanh

| Nguồn | Bài/ví dụ | Kết quả chính |
|---|---|---|
| CĐ1, slide 41 | Entropy mật khẩu, ví dụ L=14, R=94 | 91,764 bit dưới giả thiết ngẫu nhiên đều. Slide chỉ ghi “bài tập ví dụ”, không có đề khác với số liệu riêng. |
| CĐ1, 42–45 | Levenshtein kitten/sitting | 3 phép biến đổi. |
| CĐ2, 11 | 2-1: mô hình buffer overflow | P₁=1,5625%; P₂=7,8125%; NOP=256 B; pad=192 B; địa chỉ RET thật thiếu dữ kiện. |
| CĐ2, 44 | 2-2: thử wordlist | 1.000.000 lượt; 55h33m20 s; 1 user: 1h6m40 s. |
| CĐ2, 45 | 2-3: tìm ký tự nhị phân | Tối đa 6 request/ký tự; 48 request; 14,4 s. |
| CĐ2, 46 | 2-4: birthday | Không trùng: 38,170668%; có ít nhất 1 cặp: 61,829332%. |
| CĐ2, 47 | 2-5: băng thông DDoS | 5,12 Gbps; 19.532 máy cho 1 Gbps ở 100 pkt/s; 195.313 máy cho 10 Gbps ở 100 pkt/s. |
| CĐ3, 9 | Đổi chỗ khối 8 ký tự | BANQUYEN SO. |
| CĐ3, 10 | Hoán vị cột khóa MANGIP | HÀ NỘI MÙA NÀY CÓ NHỮNG CƠN MƯA. |
| CĐ3, 11 | XOR với KEY | 03 20 35 27 2A 79 1C 2A 2 B 27 21 (hex). |
| CĐ3, 20 | BLP, ma trận và hai đối tượng thêm | Ma trận ở mục 4.4; S3/O5: W; S3/O6: R. |
| CĐ3, 28 | Henry vân tay | C=9/3=3. |
| CĐ3, 38 | BT1 firewall, xác suất chặn | 25%. |
| CĐ3, 39 | BT2 firewall, mất gói | Cao điểm 28,57%; tổng gói 12,24%; trung bình theo thời gian 8,57%. |
| CĐ3, 40 | BT3 firewall, giữ luồng | Quá tải; tỷ lệ loại 33,33% theo mô hình giản lược. |
| CĐ1, 4–5 | Tiểu luận nhóm | Đề mở; khung thực hiện và báo cáo ở mục 6. |

## 2. Chuyên đề 1

### 2.1. Entropy mật khẩu — slide 41

**Dữ liệu có trong slide:** mật khẩu dài L=14, dùng tập R=94 ký tự, cần tính entropy. Không có đề bài số khác được ghi sau dòng “Bài tập ví dụ”.

**Bước 1 — Đếm không gian lựa chọn.** Mỗi vị trí chọn được 94 ký tự; 14 vị trí độc lập cho:

N=94¹⁴ mật khẩu khả dĩ.

**Bước 2 — Đổi sang bit.** Một không gian 2ᴱ khả năng có E bit, nên:

E=log₂N=log₂(94¹⁴)=14·log₂94≈14·6,55458885=**91,7642439 bit**.

**Hiểu kết quả:** lớn hơn nghĩa không gian tìm kiếm lớn hơn nếu lựa chọn ngẫu nhiên, độc lập và đều. Đây không phải số giây để phá mật khẩu; thời gian còn phụ thuộc tốc độ thử, cơ chế băm, hạn chế đăng nhập và chiến lược đoán.

**Bẫy:** một mật khẩu do người chọn theo ngày sinh/cụm từ/mẫu lặp không đạt entropy này chỉ vì dài 14 và có ký hiệu. R là số ký tự được phép và thực sự có thể được chọn trong mô hình, không phải số loại ký tự.

**Ví dụ tự luyện bổ sung:** nếu dùng 8 chữ số ngẫu nhiên thì R=10, L=8; E=8log₂10≈26,58 bit. Nếu dùng 12 chữ thường ngẫu nhiên thì E=12log₂26≈56,41 bit. Các ví dụ này không phải đề riêng trong slide.

### 2.2. Khoảng cách Levenshtein — slide 42–45

**Đề:** tìm số thao tác tối thiểu biến a=`kitten` thành b=`sitting`, mỗi lần chèn/xóa/thay 1 ký tự có chi phí 1.

**Cách hiểu nhanh:**

1. `kitten`→`sitten`: thay k bằng s.
2. `sitten`→`sittin`: thay e bằng i.
3. `sittin`→`sitting`: thêm g cuối chuỗi.

Có cách làm với 3 phép. Để chứng minh không có cách ít hơn, tính bảng quy hoạch động.

**Bước 1 — Định nghĩa.** D(i, j) là số thao tác tối thiểu biến i ký tự đầu của a thành j ký tự đầu của b.

**Bước 2 — Khởi tạo.** D(i,0)=i vì phải xóa i ký tự; D(0, j)=j vì phải thêm j ký tự.

**Bước 3 — Truy hồi.**

D(i, j)=min{D(i−1, j)+1; D(i, j−1)+1; D(i−1, j−1)+δ},

với δ=0 khi aᵢ=bⱼ, δ=1 khi khác nhau. Ba lựa chọn lần lượt là xóa, thêm, giữ nguyên/thay.

**Bảng đầy đủ:**

| a\b | ∅ | s | i | t | t | i | n | g |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ∅ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| k | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| i | 2 | 2 | 1 | 2 | 3 | 4 | 5 | 6 |
| t | 3 | 3 | 2 | 1 | 2 | 3 | 4 | 5 |
| t | 4 | 4 | 3 | 2 | 1 | 2 | 3 | 4 |
| e | 5 | 5 | 4 | 3 | 2 | 2 | 3 | 4 |
| n | 6 | 6 | 5 | 4 | 3 | 3 | 2 | **3** |

Ví dụ D(1,1)=min(1+1,1+1,0+1)=1. D(2,2) so i với i nên bằng min(2+1,2+1,1+0)=1. Ô cuối D(6,7)=3 là lời giải tối ưu.

**Bẫy:** thứ tự cột/hàng có thể đổi nhưng ô cuối phải đúng; không cộng 1 khi hai ký tự giống. Khoảng cách này đo tương đồng chuỗi, không thay thế phép đánh giá độ mạnh mật khẩu.

## 3. Chuyên đề 2

### 3.1. Bài 2-1 — Buffer overflow, slide 11

**Đề:** buffer 512 B; CPU 16 bit; con trỏ dùng n=12 bit làm địa chỉ; shellcode Sh=64 B. Tính P₁, số NOP để P₂=5P₁, padding, vị trí RET và cấu trúc stack.

**Giả thiết mô hình dùng để giải:** 2¹² địa chỉ được xem như 4.096 vị trí byte có khả năng được đoán đều; vùng trúng là Sh+NOP. Coi mọi địa chỉ của Sh là trúng theo cách tính bài giảng. Trong thực tế không phải nhảy vào mọi byte của mã đều chạy đúng; đây là xác suất lý tưởng của đề, không phải dự đoán khai thác thật.

**1) Xác suất ban đầu:**

S=2¹²=4.096 vị trí byte.

P₁=Sh/S=64/4.096=0,015625=**1,5625%**.

Slide viết 65/4.096 là lỗi đánh máy; dữ kiện phải là 64.

**2) Tăng 5 lần:**

P₂=5P₁=0,078125=**7,8125%**.

Độ dài vùng trúng cần có H=P₂S=0,078125×4.096=320 B.

NOP=H−Sh=320−64=**256 B**.

Nên tính bằng số chính xác đến cuối; không lấy 0,016 rồi 0,078 để tránh sai số trung gian.

**3) Padding:**

Pad=512−(256+64)=**192 B**.

Kiểm tra: 256+64+192=512, vừa đầy buffer trước khi xét dữ liệu điều khiển phía sau.

**4) RET: phải phân biệt offset với địa chỉ thật.** Địa chỉ bắt đầu buffer và bố trí stack frame chưa được cho, nên không thể suy ra địa chỉ tuyệt đối của RET hoặc giá trị địa chỉ mới cần ghi. Có dạng tổng quát:

offset_RET=512+độ dài vùng nằm giữa buffer và RET.

địa_chỉ_RET=địa_chỉ_đầu_buffer+offset_RET (nếu xét chiều địa chỉ tăng trong bố trí minh họa).

Slide lấy 512+4=516 B để gọi “địa chỉ RET”, nhưng lại viết cấu trúc chỉ có 512 B buffer+4 B RET=516 B, bỏ mất vùng SP đã cộng. Hai cách đó không nhất quán.

**5) Hai cách trình bày rõ giả thiết:**

| Giả thiết | Cấu trúc theo chiều vùng ghi | RET bắt đầu ở offset | Độ dài đến hết RET |
|---|---|---:|---:|
| Minh họa near pointer 16 bit: saved frame pointer 2 B, RET 2 B | NOP256 / Sh64 / Pad192 / saved-FP2 / RET2 | 514 B | 516 B |
| Giả sử vùng saved-SP/FP là 4 B và RET cũng 4 B | NOP256 / Sh64 / Pad192 / saved-SP4 / RET4 | 516 B | 520 B |

CPU 16 bit không tự xác định mọi kích thước trường: còn phụ thuộc cơ chế gọi hàm, loại return address và ABI. Nếu chỉ chép **quy ước slide**, cấu trúc được ghi là NOP256/Sh64/Pad192/RET4 và tổng 516 B; trong cấu trúc này RET phải bắt đầu ở offset512, không phải516.

**Khi làm bài:** trình bày chắc chắn P₁, P₂, NOP, Pad như trên; phần địa chỉ ghi rõ giả thiết. Tránh khẳng định “địa chỉ ghi đè RET=516” là địa chỉ tuyệt đối. Giá trị RET mới trỏ vào vùng NOP/mã cũng cần biết địa chỉ vùng đó, đề chưa cho.

### 3.2. Bài 2-2 — Thử wordlist đăng nhập, slide 44

**Đề:** 50 username, mỗi user có 20.000 mật khẩu khả dĩ trong wordlist; server không khóa tài khoản; mỗi request mất 0,2 s. Tính số lượt, tổng thời gian và thời gian cho 1 user.

**Giả thiết:** thử tuần tự, không có chi phí ngoài 0,2 s/request; tính trường hợp thử hết tập. Chính xác hơn đây là dò từ điển trên wordlist, không phải vét cạn mọi chuỗi ký tự.

**1) Số lượt:**

K=N×W=50×20.000=**1.000.000 request**.

**2) Thời gian:**

T=K×t=1.000.000×0,2=200.000 s.

200.000/3.600=55,555…h=**55 giờ 33 phút 20 giây**, khoảng **2,315 ngày**.

**3) Một user:**

K₁=20.000; T₁=20.000×0,2=4.000 s=**1 giờ 6 phút 40 giây**.

**Nếu hỏi trung bình tới lúc tìm đúng:** khi mật khẩu chắc chắn nằm trong wordlist và vị trí đúng phân bố đều, trung bình (W+1)/2=10.000,5 lượt/user, tương ứng 2.000,1 s≈33 phút20,1 s. Đó là bài toán khác với thời gian thử hết trong đề.

**Bẫy:** không chia thời gian cho số user nếu đề nói làm tuần tự; không tự thêm giả thiết song song. Không khóa tài khoản không tự có nghĩa request sẽ luôn nhanh như nhau ngoài mô hình.

### 3.3. Bài 2-3 — Tìm ký tự bằng binary search, slide 45

**Đề:** mật khẩu dài 8, ký tự trong [a–z,0–9]; dò mỗi ký tự bằng binary search; 0,3 s/request. Tính tối đa mỗi ký tự, tổng request và thời gian.

**Giả thiết quan trọng:** đã có cơ chế hỏi nhận kết quả đúng/sai cho một phép chia tập, đã biết chiều dài và dữ liệu cần tìm; không tính request tìm cấu trúc CSDL, độ dài, tên tài khoản hay thử xác nhận ban đầu. Đây là bài tính oracle nhị phân trong bối cảnh SQL injection, không đủ để kết luận bất kỳ URL nào cũng làm được.

**1) Số khả năng:** R=26+10=36.

**2) Số câu hỏi tối đa/ký tự:** một câu hỏi nhị phân chia còn khoảng một nửa, nên q=⌈log₂36⌉=⌈5,1699…⌉=**6**. Cũng thấy 2⁵=32<36≤64=2⁶.

**3) Tổng request:** Q=8×6=**48**.

**4) Thời gian:** T=48×0,3=**14,4 s**.

**Bẫy:** dùng ceiling chứ không làm tròn gần nhất; tối đa 6 không có nghĩa mọi ký tự luôn mất đúng 6. Đề dùng request chia tập theo thứ tự ký tự; nếu chỉ hỏi “có bằng một giá trị không?” thì không còn lợi thế chia đôi tương tự.

### 3.4. Bài 2-4 — Birthday attacks, slide 46

**Đề:** 10 mẫu mã độc có chữ ký độc lập, phân bố đều trong 50 giá trị. Tính xác suất không có cặp trùng và có ít nhất một cặp trùng.

**Cách hiểu:** mẫu đầu chọn gì cũng được; mẫu thứ hai phải né 1 chữ ký; mẫu thứ ba phải né 2… khi các mẫu trước chưa trùng.

**1) Không trùng:**

P₀=(50/50)×(49/50)×(48/50)×…×(41/50).

P₀=∏ᵢ₌₀⁹(1−i/50)=**0,3817066806**, tức **38,170668%**.

**2) Có ít nhất một cặp:** dùng biến cố bù:

P_trùng=1−P₀=**0,6182933194**, tức **61,829332%**.

Không cộng xác suất từng cặp vì các sự kiện có thể chồng nhau.

**Xấp xỉ trong slide:**

P₀≈exp[−k(k−1)/(2m)]=exp[−10×9/(2×50)]=e^(−0,9)≈0,40656966.

P_trùng≈0,59343034. Slide làm tròn thành 0,41 và 0,59. Đây là **xấp xỉ**, không phải phép tính chính xác; ở bộ số này chênh khoảng 2,49 điểm phần trăm.

**Ý nghĩa ATTT:** va chạm giữa bất kỳ hai mẫu dễ xuất hiện hơn việc ép một mẫu trùng đúng một chữ ký mục tiêu. Với không gian b bit, ngưỡng birthday có cỡ 2^(b/2) mẫu; không nhầm với việc tìm preimage cho một giá trị cố định.

### 3.5. Bài 2-5 — Băng thông DDoS, slide 47

**Đề:** 10.000 máy; mỗi gói 64 B; mỗi máy 1.000 pkt/s; đường nạn nhân 1 Gbps. (1) Có quá tải không? (2) Cần bao nhiêu máy nếu mỗi máy 100 pkt/s? (3) Bao nhiêu máy cho mục tiêu 10 Gbps?

**Giả thiết:** tổng lưu lượng đều tới nút thắt nạn nhân; chỉ xét 64 B/gói theo đề, không cộng overhead, lọc hay giới hạn đường trung gian. “Có tấn công xảy ra không” được hiểu là **lưu lượng giả định có đủ vượt băng thông không**, vì ý đồ tấn công đã được đề cho.

Công thức W=N×P×8×R, trong đó P là byte/gói, R là gói/s/máy; W có đơn vị bit/s.

**1) Tổng lưu lượng:**

Một máy: w=64×8×1.000=512.000 bit/s=0,512 Mbps.

10.000 máy: W=10.000×512.000=5.120.000.000 bit/s=**5,12 Gbps**.

5,12>1 nên **đủ gây quá tải băng thông theo mô hình**. Không từ phép tính này suy ra chính xác tỷ lệ mất gói hay dịch vụ nào ngừng.

**2) Nếu 100 pkt/s:**

w=64×8×100=51.200 bit/s.

N≥10⁹/51.200=19.531,25. Số máy nguyên tối thiểu là **19.532 máy**.

Kiểm tra 19.531 máy chỉ tạo 999.987.200 bit/s<1 Gbps nên thiếu. 19.532 máy tạo 1.000.038.400 bit/s.

**3) Mục tiêu 10 Gbps: có hai cách đọc tốc độ.**

| Tốc độ giữ cho câu 3 | Phép tính | Số máy tối thiểu |
|---|---|---:|
| 100 pkt/s như câu 2 và lời giải gốc | ⌈10¹⁰/51.200⌉=⌈195.312,5⌉ | **195.313** |
| 1.000 pkt/s như dữ kiện ban đầu | ⌈10¹⁰/512.000⌉=⌈19.531,25⌉ | **19.532** |

Lời giải gốc dùng 100 pkt/s, vì vậy đáp số theo ý đó là 195.313. Slide ghi 195.310 là sai; câu2 ghi 19.531 cũng thiếu do làm tròn xuống.

**Bẫy:** byte≠bit; Gbps thập phân không phải GiB/s; số máy luôn ceiling khi tìm ngưỡng tối thiểu. Với 10.000 máy ban đầu và tốc độ 1.000 pkt/s, tổng 5,12 Gbps chưa vượt đường10 Gbps trong mô hình băng thông này.

## 4. Chuyên đề 3

### 4.1. Hoán vị khối 8 ký tự — slide 9

**Đề:** bản mã `EQAUNBNY--S---O-`, chia khối 8, đánh số từ phải sang trái; khóa 1→3,2→6,3→8,4→1,5→4,6→7,7→5,8→2. Tìm bản rõ.

**Chú ý quy ước:** với cách dựng bản rõ thể hiện trên slide9, ký tự ở vị trí j của bản mã được đặt vào vị trí f(j) của bản rõ. Không dùng khóa khác ở slide8.

**Bước 1 — Khối đầu:**

| Vị trí trong bản mã, tính từ phải | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Ký tự | E | Q | A | U | N | B | N | Y |
| Chuyển tới vị trí bản rõ | 2 | 5 | 7 | 4 | 1 | 8 | 6 | 3 |

**Bước 2 — Sắp lại theo vị trí bản rõ8→1:**

| Vị trí bản rõ | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Lấy từ vị trí bản mã | 3 | 6 | 2 | 7 | 5 | 1 | 8 | 4 |
| Ký tự | B | A | N | Q | U | Y | E | N |

Khối đầu=`BANQUYEN`.

**Bước 3 — Khối hai:** `--S---O-` cùng phép chuyển cho `-SO-----`. Ghép được `BANQUYEN-SO-----`.

**Bước 4 — Đọc thông điệp:** dấu “-” gồm phần biểu diễn khoảng trống/đệm theo ví dụ. Bỏ đệm cuối và đọc khoảng ngăn từ: **BAN QUYEN SO**, tức **BẢN QUYỀN SỐ**. Slide biểu diễn liền phần đầu là“BANQUYEN SO”.

**Bẫy:** nếu không biết phân biệt dấu ngăn và đệm thì phép hoán vị chỉ cho chính xác chuỗi chứa dấu ở trên, không tự suy ra định dạng khoảng trắng. Cần thống nhất hướng ánh xạ trước khi giải.

### 4.2. Hoán vị cột MANGIP — slide 10

**Đề/ví dụ:** khóa MANGIP, bảng4×6; bản mã `OAUM HUOC IYNU AANO NNHN MCGA`. Giải mã.

**Bước 1 — Xếp hạng chữ khóa theo thứ tự chữ cái:** A, G, I, M, N, P, tương ứng hạng1,2,3,4,5,6. Trên các cột gốc:

| Cột gốc | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Chữ khóa | M | A | N | G | I | P |
| Hạng | 4 | 1 | 5 | 2 | 3 | 6 |

**Bước 2 — Đọc các khối mã theo hạng tăng.** Cột có A là cột2 nên khối1 OAUM vào cột2; G là cột4 nên HUOC vào cột4; I là cột5 nên IYNU vào cột5; M là cột1 nên AANO vào cột1; N là cột3 nên NNHN vào cột3; P là cột6 nên MCGA vào cột6.

| Cột gốc | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Hàng1 | A | O | N | H | I | M |
| Hàng2 | A | A | N | U | Y | C |
| Hàng3 | N | U | H | O | N | G |
| Hàng4 | O | M | N | C | U | A |

**Nhưng bảng này không khớp bản rõ trong slide.** Nguyên nhân: lời giải slide dùng một quy ước khác: lấy danh sách **hạng** [4,1,5,2,3,6] trực tiếp làm **thứ tự cột xuất ra**, thay vì thứ tự vị trí chữ khóa sau khi sắp xếp [2,4,5,1,3,6]. Hai quy ước khác nhau.

**Theo quy ước thực tế của slide**, đặt OAUM vào cột4, HUOC vào cột1, IYNU vào cột5, AANO vào cột2, NNHN vào cột3, MCGA vào cột6:

| Cột | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Hàng1 | H | A | N | O | I | M |
| Hàng2 | U | A | N | A | Y | C |
| Hàng3 | O | N | H | U | N | G |
| Hàng4 | C | O | N | M | U | A |

Đọc từng hàng: `HANOIMUANAYCONHUNGCONMUA` → **HÀ NỘI MÙA NÀY CÓ NHỮNG CƠN MƯA**.

**Cách học:** để khớp ví dụ này, ghi rõ thứ tự cột **4,1,5,2,3,6**. Không ngầm trộn hai cách suy thứ tự từ từ khóa. Hoán vị6 cột có6!=720 cách; bảng giữ số lượng và ký tự, chỉ đổi vị trí. Các ví dụ hoán vị đơn giản phục vụ học nguyên lý, không phải bảo mật mạnh để triển khai.

### 4.3. XOR “Hello World” với “KEY” — slide 11

**Đề/ví dụ:** chuyển từng ký tự sang ASCII rồi XOR với khóa KEY lặp.

**Bước 1 — Lặp khóa:** thông điệp11 ký tự, tính cả dấu cách; khóa là `KEYKEYKEYKE`.

**Bước 2 — XOR từng byte.** Tất cả số trong bảng là **hex**, không phải thập phân.

| Ký tự | ASCII | Khóa | ASCII khóa | XOR |
|---|---|---|---|---|
| H | 48 | K | 4 B | 03 |
| e | 65 | E | 45 | 20 |
| l | 6C | Y | 59 | 35 |
| l | 6C | K | 4 B | 27 |
| o | 6F | E | 45 | 2A |
| dấu cách | 20 | Y | 59 | 79 |
| W | 57 | K | 4 B | 1C |
| o | 6F | E | 45 | 2A |
| r | 72 | Y | 59 | 2 B |
| l | 6C | K | 4 B | 27 |
| d | 64 | E | 45 | 21 |

Ví dụ 0x48=01001000 và 0x4 B=01001011; XOR được00000011=0x03.

Bản mã: **03 20 35 27 2A 79 1C 2A 2 B 27 21**.

**Bước 3 — Giải mã:** C XOR K=(M XOR K) XOR K=M XOR0=M. Ví dụ03 XOR4 B=48→H; làm tương tự thu **Hello World**.

**Bẫy:** giữ dấu cách và đúng vị trí lặp khóa; 20 trong bảng là 0x20, không phải số20 thập phân. XOR khóa ngắn lặp để lộ cấu trúc, không phải one-time pad; không suy từ ví dụ này rằng XOR lặp KEY là mã hóa đủ mạnh.

### 4.4. Ma trận Bell–LaPadula — slide 19–20

**Đề:** S1, S2, S3, S4 có mức3,3,2,1; O1, O2, O3, O4 có mức3,2,2,1. Vẽ ma trận/sơ đồ; xét S3 với O5 mức3 và O6 mức1.

**Bước 1 — Chọn đúng quy tắc:**

- Đọc R nếu L(S)≥L(O): không đọc lên.
- Ghi W nếu L(S)≤L(O): không ghi xuống.
- Cùng mức có R/W, giả sử các quyền cấp khác đều cho phép như bài.

Slide19 in dấu≥cho ghi là lỗi, mâu thuẫn câu “không ghi xuống” và ma trận slide20. Giải theo quy tắc đúng.

**Bước 2 — Tính từng ô:**

| Chủ thể | O1 (3) | O2 (2) | O3 (2) | O4 (1) |
|---|---|---|---|---|
| S1 (3) | R/W | R | R | R |
| S2 (3) | R/W | R | R | R |
| S3 (2) | W | R/W | R/W | R |
| S4 (1) | W | W | W | R/W |

Ví dụ S3/O1:2<3 nên không đọc được, nhưng ghi lên được→W. S1/O4:3>1 nên đọc xuống được, ghi xuống bị cấm→R.

**Sơ đồ phân mức:**

```text
Mức 3: S1, S2                 O1, O5
Mức 2: S3                     O2, O3
Mức 1: S4                     O4, O6

Đọc: chủ thể ở mức cao → đối tượng cùng/thấp.
Ghi: chủ thể ở mức thấp → đối tượng cùng/cao.
Đọc+ghi: cùng mức.
```

**Danh sách cạnh để vẽ đủ sơ đồ truy nhập:**

| Chủ thể | Cạnh đọc R | Cạnh ghi W |
|---|---|---|
| S1 | O1, O2, O3, O4 | O1 |
| S2 | O1, O2, O3, O4 | O1 |
| S3 | O2, O3, O4 | O1, O2, O3 |
| S4 | O4 | O1, O2, O3, O4 |

Nếu vẽ **luồng dữ liệu**, đọc là mũi tên object→subject còn ghi là subject→object. Nếu vẽ **quan hệ được phép thao tác**, có thể dùng subject→object cho cả hai nhưng phải gắn nhãnR/W. Đừng trộn hai ý nghĩa mũi tên.

**Bước 3 — Hai đối tượng thêm:**

- S3 mức2, O5 mức3: R sai vì2≥3 không đúng; W đúng vì2≤3. Kết luận **chỉ ghi**.
- S3 mức2, O6 mức1: R đúng vì2≥1; W sai vì2≤1 không đúng. Kết luận **chỉ đọc**.

**Vì sao:** BLP bảo vệ bí mật, không cho thông tin mức cao rò xuống mức thấp. Nếu riêng bài áp dụng strong-star cho các thao tác thì chỉ cùng mức mới cho phép; các truy nhập khác mức ở đây thuộc quy tắc BLP đọc/ghi thông thường, như ma trận đề gốc.

### 4.5. Hệ số Henry vân tay — slide 28

**Dữ kiện:** chỉ ngón áp út phảiRr và trỏ tráiLi có whorl. Các ngón khác là loop/arch.

R=right, L=left; t=cái, i=trỏ, m=giữa, r=áp út, p=út. Gán w=1 nếu whorl,0 nếu không. Công thức có trọng số trong slide:

C=(16w_Ri+8w_Rr+4w_Lt+2w_Lm+w_Lp+1)/(16w_Rt+8w_Rm+4w_Rp+2w_Li+w_Lr+1).

**Bước 1:** tử chỉ Rr đóng góp8, cộng1→9.

**Bước 2:** mẫu chỉ Li đóng góp2, cộng1→3.

**Bước 3:** C=9/3=**3**.

**Hiểu đúng:** dùng lớp này để thu hẹp danh sách mẫu cần so, rồi còn phải so chi tiết vân tay. C=3 không phải xác suất nhận dạng hay bằng chứng hai mẫu cùng người. Khi triển khai phân loại nên giữ cặp9/3, vì chỉ rút gọn thành số3 có thể gộp các cặp phân loại khác nhau. Dòng công thức slide bỏ hệ số trong ký hiệu rồi thêm qua hàng trọng số; khi tính phải nhân đúng16,8,4,2,1.

### 4.6. BT1 — Xác suất firewall chặn, slide 38

**Đề:** luật theo thứ tự: chặn nguồn192.168.0.0/24; chặn cổng đích23; cho qua còn lại. P(A)=20%, P(B)=10%, P(A∩B)=5%. Tính xác suất chặn một gói.

**Bước 1:** bị chặn nếu thuộc A hoặc B, tứcA∪B.

**Bước 2:** hai tập chồng nhau5%, nếu cộng20%+10% sẽ đếm phần giao hai lần.

P(block)=P(A)+P(B)−P(A∩B)=0,2+0,1−0,05=**0,25=25%**.

**Theo thứ tự luật:** luật1 chặn20%; luật2 chỉ thấy phần chưa bị luật1 chặn, thêm10%−5%=5%; luật3 cho75% còn lại. Các tỷ lệ này tính trên toàn bộ gói ban đầu. Trong số80% tới luật2, tỷ lệ bị luật2 chặn là5/80=6,25%.

**Bẫy:** không giả sử A và B độc lập; nếu độc lập phần giao sẽ2%, trái dữ kiện5%. /24 có nghĩa24 bit đầu là phần mạng trong IPv4; bài xác suất đã cho tỷ lệ nên không phải đếm số IP.

### 4.7. BT2 — Mất gói firewall, slide 39

**Đề:** công suất50.000 gói/s; 70% thời gian đến40.000 gói/s; 30% thời gian đến70.000 gói/s. Tính mất gói cao điểm và trung bình toàn hệ thống.

**Giả thiết:** công suất cố định, khi quá tải phần vượt bị loại; không có hàng đợi đủ lớn để dời xử lý sang thời gian thấp điểm. Với hàng đợi/burst và độ trễ khác, mất gói thực tế có thể khác.

**a) Cao điểm:**

Mất70.000−50.000=20.000 gói/s.

LR_peak=20.000/70.000=2/7=**28,5714%**.

**b) Tỷ lệ trên toàn bộ gói — cách hiểu thông thường của tỷ lệ mất gói toàn hệ thống:** xét100 giây.

| Giai đoạn | Thời gian | Tốc độ đến | Tổng gói đến | Tổng gói mất |
|---|---:|---:|---:|---:|
| Bình thường | 70 s | 40.000/s | 2.800.000 | 0 |
| Cao điểm | 30 s | 70.000/s | 2.100.000 | 600.000 |
| Tổng | 100 s | — | 4.900.000 | 600.000 |

LR_total=600.000/4.900.000=6/49=**12,2449%**.

Cũng tính trực tiếp: tốc độ mất trung bình=0,3×20.000=6.000 gói/s; tốc độ đến trung bình=0,7×40.000+0,3×70.000=49.000 gói/s; 6.000/49.000=12,2449%.

**Một khái niệm khác — trung bình tỷ lệ theo thời gian:**

LR_time=0,7×0+0,3×28,5714%=**8,5714%**.

Hai giá trị khác vì thời gian cao điểm mang nhiều gói mỗi giây hơn. Nếu chọn ngẫu nhiên một gói trong toàn thời gian thì dùng12,24%; nếu chọn ngẫu nhiên một thời điểm rồi lấy tỷ lệ tại thời điểm đó thì dùng8,57%.

**Lỗi slide:** dòng“20×0,2857/100=0,1=10%” không đúng cả tỷ trọng30% lẫn phép nhân. Không có cách hiểu nào ở trên cho10%.

### 4.8. BT3 — Quá tải số luồng firewall, slide 40

**Đề:** giữ/xử lý tối đa10.000 luồng đồng thời; mỗi luồng trung bình30 s; đến500 luồng/s. Quá tải không, tỷ lệ loại là bao nhiêu?

**Giả thiết:**10.000 là số luồng đồng thời, không phải tốc độluồng/s. Dùng mô hình ổn định giản lược, không có hàng đợi thay đổi thời gian phục vụ.

**a) Nhu cầu số luồng:** theo quan hệ L=λT:

L=500×30=**15.000 luồng**.

15.000>10.000 nên **quá tải** nếu muốn nhận mọi luồng.

**b) Tốc độ có thể nhận bền vững:**

λ_max=10.000/30≈333,333 luồng/s.

Loại trung bình500−333,333≈166,667 luồng/s.

Tỷ lệ loại=(500−333,333)/500=1/3=**33,3333%**.

Tương đương(15.000−10.000)/15.000=33,3333%.

**Bẫy:**30 s không phải500 luồng đều xử lý tuần tự từng luồng. Đây là thời gian lưu trú cùng tồn tại. Với quá trình đến ngẫu nhiên và chính sách chặn thực, công thức trung bình này là mô hình bài giảng, chưa là xác suất chặn chính xác của một hệ hàng đợi cụ thể.

## 5. Chuyên đề 4 — Ví dụ tự luyện bổ sung

**Không có bài tập riêng trong bộ CĐ4.** Những bài dưới đây do tôi bổ sung để luyện các công thức/thuật toán mà slide nêu; không phải đề giảng viên.

### 5.1. K-means — liên hệ slide 22–23

**Ví dụ:** dữ liệu1 chiều{1,2,8,9}, k=2, tâm đầuμ₁=1, μ₂=9.

1. So khoảng cách:1,2 gần tâm1; 8,9 gần tâm9.
2. CụmC₁={1,2}, C₂={8,9}.
3. Tâm mớiμ₁=(1+2)/2=1,5; μ₂=(8+9)/2=8,5.
4. Gán lại theo tâm mới, các cụm giữ nguyên→hội tụ.
5. SSE=(1−1,5)²+(2−1,5)²+(8−8,5)²+(9−8,5)²=**1**.

Điều cần nhớ là luân phiên **gán vào tâm gần nhất** và **tính trung bình**, không chỉ một lần chia cụm.

### 5.2. Khoảng cách và cosine — liên hệ slide 25

**Ví dụ:**x=(1,2), y=(4,6).

- Euclidean=√[(1−4)²+(2−6)²]=√25=**5**.
- Manhattan=|1−4|+|2−6|=**7**.
- Maximum=max(3,4)=**4**.
- Cosine=(1×4+2×6)/(√5×√52)=16/√260≈**0,99228**.

Cosine cao vì hai vector gần cùng hướng dù vị trí cách nhau5 đơn vị. Vì vậy“giống nhau” phụ thuộc phép đo, không chỉ một con số duy nhất.

### 5.3. PCA — liên hệ slide 27–31

**Ví dụ:** dữ liệu(1,1),(2,2),(3,3), đã cùng thang đo.

1. Trung bình=(2,2); các điểm sau trừ trung bình:(−1,−1),(0,0),(1,1).
2. Hiệp phương sai mẫuΣ=[[1,1],[1,1]].
3. Trị riêng2 và0; vector riêng tương ứngu₁=(1,1)/√2, u₂=(1,−1)/√2.
4. Chiếu lên u₁ cho{−√2,0,√2}; phương sai giữ lại2/(2+0)=**100%**.
5. Điểm mới(3,1) trừ trung bình thành(1,−1); chiếu lên u₁ được0nhưng lên u₂ được√2. Nó nằm lệch đường dữ liệu cũ, dù điểmPC1=0trông bình thường.

Điều này minh họa vì sao phát hiện PCA có thể cần xét **phần dư tái dựng**, không chỉ điểm số trên các thành phần giữ lại. Ngưỡng cảnh báo phải được chọn/kiểm chứng, ví dụ này chưa tự cho một ngưỡng chuẩn.

### 5.4. Chỉ số phát hiện — liên hệ slide 32

**Ví dụ:**100 mẫu tấn công,900 mẫu bình thường; phát hiện90tấn công và báo nhầm45 mẫu bình thường.

TP=90, FN=10, FP=45, TN=855, tổng1.000.

| Chỉ số | Công thức thay số | Kết quả |
|---|---|---:|
| Recall/sensitivity | 90/(90+10) | 90% |
| Precision | 90/(90+45) | 66,67% |
| FPR | 45/(45+855) | 5% |
| FNR | 10/(10+90) | 10% |
| Specificity | 855/(855+45) | 95% |
| Accuracy | (90+855)/1.000 | 94,5% |
| Youden index | 0,90+0,95−1 | 0,85 |

Trong135 cảnh báo chỉ90 đúng, nên dù recall90%, người xử lý phải xem45 cảnh báo nhầm. FPR dùng tổng **mẫu bình thường** làm mẫu số; precision dùng tổng **cảnh báo**. Nhầm hai mẫu số này rất phổ biến.

### 5.5. Lan truyền logistic — liên hệ slide 33

**Ví dụ:**A₀=0,01, α=0,5/giờ; hỏi bao lâu tỷ lệ nhiễm lên50% trong mô hình không phục hồi.

A(t)=1/[1+((1−A₀)/A₀)e^(−αt)]=1/[1+99e^(−0,5t)].

Cho A(t)=0,5:1+99e^(−0,5t)=2→99e^(−0,5t)=1.

t=ln99/0,5≈**9,19024 giờ**, khoảng9 giờ11 phút25 giây.

Tốc độ lớn nhất tạiA=0,5 vìA(1−A)≤1/4; khi đódA/dt=α/4=0,125/giờ. Mô hình không xét vá, phục hồi, mạng phân nhóm hay thay đổi tốc độ theo thời gian, nên đây là kết quả toán theo giả thiết.

## 6. Tiểu luận nhóm — tổng hợp yêu cầu và cách thực hiện

Nguồn:CĐ1slide4–5. Đây là bài mở cần dữ liệu thử nghiệm; chưa có công cụ được bạn chọn và chưa có kết quả lab nên không thể tạo một“kết quả thực nghiệm” có thật. Phần này đưa khung giải đầy đủ để triển khai và viết báo cáo.

### 6.1. Yêu cầu ghi trong tài liệu

- Nhóm≤4 học viên; trang đầu ghi phân công.
- Báo cáo≤20 trang, có slide và tài liệu tham khảo.
- Giới thiệu công cụ, kiến trúc, nguyên lý.
- Thiết lập máy thử nghiệm, cài/cấu hình.
- Tạo1–2 kịch bản demo.
- Phân tích, đánh giá kết quả.
- So sánh ưu/nhược với1công cụ tương tự.
- Hạn nộp trong tài liệu là14/6/2026; đây là thông tin lịch gốc, không phải hạn mới được suy ra.

Danh mục20chủ đề:

| Nhóm chức năng | Công cụ trong đề |
|---|---|
| Khảo sát/kết nối/tạo gói | Nmap, Netcat, Hping3 |
| Phân tích gói/lưu lượng | Wireshark, Tcpdump |
| Kiểm thử web | Burp Suite, OWASP ZAP, SQLmap, Nikto |
| Quét/đánh giá lỗ hổng và framework | OpenVAS, Metasploit Framework |
| IDS/giám sát mạng | Snort, Suricata, Zeek |
| Giám sát host/log/SIEM | Wazuh, OSSEC, Graylog |
| Kiểm thử mật khẩu | John the Ripper, Hashcat, Hydra |

Cách phân nhóm giúp đọc đề; một công cụ có thể có nhiều khả năng. Đề có dòng“do thầy giao”và dòng“mỗi nhóm chọn1”; khi nộp cần theo phân công đã được lớp chốt.

### 6.2. Cách giải bài mở theo từng bước

1. **Đặt câu hỏi:** ví dụ“Công cụ quan sát được những gì trong một phiên TCP và phát hiện được kết nối chưa hoàn tất ra sao?”. Tránh mục tiêu mơ hồ“tìm hiểu công cụ”.
2. **Vẽ kiến trúc lab:** máy khách, máy chủ, máy quan sát; ghi mạng, địa chỉ, phiên bản, vai trò. Dùng môi trường thử nghiệm thuộc phạm vi được phép, hoặc PCAP mẫu đã có.
3. **Chọn hai kịch bản so sánh được:** một hoạt động bình thường và một tình huống có dấu hiệu lỗi/bất thường; giữ các yếu tố khác ổn định để giải thích được khác biệt.
4. **Định nghĩa đầu vào và kết quả mong đợi:** số phiên/thời gian/gói/mẫu, tiêu chí đúng/sai; lập bảng trước khi chạy.
5. **Lưu bằng chứng:** dữ liệu gốc, cấu hình, ảnh đủ nhãn/thời gian, cách đọc kết quả. Đừng chỉ lấy ảnh có cảnh báo mà không giải thích vì sao.
6. **Đánh giá:** công cụ thấy gì, bỏ sót gì, cảnh báo nhầm gì, chi phí thu/xử lý, hạn chế do vị trí thu hoặc dữ liệu mã hóa.
7. **So sánh cùng dữ liệu:** đối chiếu hai công cụ theo cùng mục tiêu và tiêu chí; không kết luận hơn/kém từ hai kịch bản không tương đương.

### 6.3. Mẫu nội dung cụ thể với Wireshark và Tcpdump

Đây là ví dụ phương pháp theo chủ đề có trong đề, không phải kết quả đã chạy.

**Mục tiêu:** quan sát bắt tay TCP, phân biệt phiên hoàn tất với phiên không hoàn tất, tìm bằng chứng trong PCAP.

**Lab:**1 máy khách,1 máy chủ có dịch vụ TCP,1điểm thu hợp lệ trong mạng lab. Ghi vị trí sensor vì vị trí quyết định nhìn thấy chiều nào của lưu lượng.

**Demo1 — Phiên bình thường:** quan sát SYN→SYN-ACK→ACK, dữ liệu trao đổi, kết thúc phiên. Ghi thời gian phản hồi, cổng, địa chỉ và có retransmission không.

**Demo2 — Phiên không hoàn tất:** dùng PCAP mẫu hoặc tình huống kết nối lỗi trong lab để quan sát thiếu bước hoàn tất. Đếm SYN, SYN-ACK, ACK và trạng thái chờ trong cửa sổ thời gian. Một phiên lỗi chưa đủ chứng minh SYN flood; kết luận tấn công cần thêm quy mô, tần suất và bối cảnh.

| Tiêu chí so sánh | Wireshark | Tcpdump | Bằng chứng cần ghi |
|---|---|---|---|
| Quan sát/thu | Giao diện phân tích tương tác | Thu/đọc qua dòng lệnh | Cùng điểm thu, cùng PCAP |
| Đọc các tầng | Trình bày chi tiết trường | Hiển thị tùy lựa chọn/định dạng | Một gói được đọc ở hai công cụ |
| Làm việc từ xa/tự động | Đánh giá theo cách dùng lab | Đánh giá quy trình CLI | Thao tác thực hiện, số bước |
| Khả năng diễn giải | Đọc phiên và thống kê | Phân tích đầu ra và phối hợp công cụ | Các dấu hiệu thực sự quan sát được |
| Hạn chế | Mã hóa, vị trí thu, tài nguyên | Mã hóa, vị trí thu, tài nguyên | Phần chưa quan sát/đo được |

**Cấu trúc báo cáo gợi ý≤20 trang:**1 trang bìa/phân công; 2 trang mục tiêu/kiến trúc; 3 trang nguyên lý; 3 trang lab/cấu hình; 5 trang demo và bằng chứng; 3 trang phân tích/so sánh; 1 trang kết luận; 1–2 trang tham khảo. Đây là gợi ý tổ chức, không phải quy định phân bổ của giảng viên.

**Cách viết nhận xét:**“Trong dữ liệuX, công cụ quan sátY, với điều kiệnZ; còn Wchưa được kiểm chứng”. Tránh ghi“phát hiện100%” nếu chỉ thử một vài tình huống và không có tập kiểm thử.

## 7. Công thức ôn nhanh

| Dạng | Công thức | Điều kiện quan trọng |
|---|---|---|
| Entropy | E=Llog₂R | Độc lập, đều, ngẫu nhiên |
| Thử wordlist | K=NW, T=Kt | Thử hết, tuần tự |
| Tìm nhị phân | q=⌈log₂R⌉, Q=Lq | Oracle chia tập nhị phân |
| Birthday | P₀=∏ᵢ₌₀ᵏ⁻¹(1−i/m), P_trùng=1−P₀ | Mẫu độc lập, đều; k≤m |
| Lưu lượng | W=NP8R | Pbyte/gói, Rgói/s |
| Máy tối thiểu | N_min=⌈B/(P8R)⌉ | Làm tròn lên |
| Hợp hai sự kiện | P(A∪B)=P(A)+P(B)−P(A∩B) | Không cần độc lập |
| Mất gói tức thời | max(λ−C,0)/λ | λ>0, bỏ qua hàng đợi |
| Mất gói toàn bộ | Σ(thời gian×tốc độ mất)/Σ(thời gian×tốc độ đến) | Trọng số theo gói |
| Luồng đồng thời | L=λT | Ổn định, định nghĩa cùng hệ |
| BLP | R:L(S)≥L(O); W:L(S)≤L(O) | Còn cần quyền khác cho phép |
| Khả dụng | A=uptime/(uptime+downtime) | Cùng kỳ đo |
| Tin cậy | R(t)=e^(−λt), MTTF=1/λ | Tốc độ lỗi không đổi |

## 8. Nguồn và quy ước kiểm chứng

Đề và ví dụ lấy từ4PDF do bạn cung cấp. Các phép tính số được tính lại; những đáp án khác slide đã có giải thích ngay tại bài. Không tạo số liệu lab giả. Những phần tự luyện và khung tiểu luận được đánh dấu là bổ sung.

Với BLP, quy tắc“không đọc lên/không ghi xuống”được đối chiếu với mô tả trong nghiên cứu[Access Control Encryption](https://arxiv.org/abs/1602.03642). Cập nhật chính sách mật khẩu hiện hành trong tài liệu tóm tắt tham khảo[NIST SP800-63 B-4](https://pages.nist.gov/800-63-4/sp800-63b.html).
