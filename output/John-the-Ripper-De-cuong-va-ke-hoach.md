# John the Ripper: Password cracking techniques

Đề cương báo cáo và kế hoạch triển khai dành cho nhóm 3 thành viên — môn An toàn thông tin nâng cao.

Ngày lập: 29/10/2026. Trạng thái: kế hoạch nghiên cứu và khung viết báo cáo; chưa có kết quả thực nghiệm. TV1, TV2, TV3 là tên tạm để thay bằng họ tên, mã học viên.

## 1. Căn cứ và phạm vi

Tài liệu môn học `tmp/pdfs/1-CDE1-T5-2026.txt`, trang PDF 2–3, slide 4–5, quy định: nhóm tối đa 4 người; trang đầu có phân công; báo cáo không quá 20 trang; có báo cáo và slide; trình bày công cụ, kiến trúc, nguyên lý; thiết lập lab; xây dựng 1–2 demo; phân tích kết quả; so sánh công cụ tương tự; có tài liệu tham khảo. Dòng “đủ 4 nội dung” trong slide liệt kê thực tế 5 mục, vì vậy kế hoạch bao phủ cả 5.

Mốc nộp 14/06/2026 trong slide đã qua so với ngày lập kế hoạch. Chưa coi đây là hạn nộp hiện tại; dùng lịch D1–D14 tính từ ngày nhóm bắt đầu và xác nhận lại hạn nộp, biểu mẫu, thời lượng thuyết trình với lớp.

**Tên báo cáo đề xuất:** “Nghiên cứu John the Ripper và đánh giá các kỹ thuật dò mật khẩu ngoại tuyến trong môi trường thực nghiệm”.

**Câu chuyện xuyên suốt:** cách chọn ứng viên và cách lưu mật khẩu cùng quyết định hiệu quả dò tìm. Báo cáo cần nối được nguyên lý → giả thuyết → thiết kế đo → dữ liệu → giải thích → khuyến nghị.

Phạm vi thực nghiệm: máy ảo của nhóm; mật khẩu, tài khoản và hash tự tạo; CPU là cấu hình chính để dễ lặp lại. Chọn John the Ripper Jumbo làm công cụ chính và Hashcat làm công cụ so sánh. John Jumbo có hỗ trợ nhiều nền tảng và các định dạng chạy trên CPU/GPU; cần kiểm tra tính năng của đúng bản cài đặt. [Kho mã chính thức John Jumbo](https://github.com/openwall/john).

Hai kịch bản chính:

1. Ảnh hưởng của chiến lược sinh ứng viên: wordlist, rules, mask, incremental giới hạn; single crack là tiểu mục minh họa dùng metadata giả lập.
2. Ảnh hưởng của cơ chế băm và cost: raw SHA-256 so với bcrypt; đối chiếu một phần kết quả với Hashcat trên cùng dữ liệu.

Không mở rộng thành các demo riêng về Wi-Fi, lấy hash hệ thống thật, ZIP/PDF hoặc tấn công đăng nhập mạng; khối lượng này không cần cho mục tiêu và giới hạn 20 trang.

## 2. Mục tiêu, câu hỏi và giả thuyết

| Mã | Câu hỏi nghiên cứu | Giả thuyết để kiểm chứng | Bằng chứng cần thu |
|---|---|---|---|
| RQ1 | Wordlist, rules và mask hiệu quả với nhóm mật khẩu nào? | Rules có lợi với biến thể từ gốc; mask có lợi khi giả định cấu trúc đúng | Tỷ lệ khôi phục theo nhóm và theo thời gian; tập ứng viên |
| RQ2 | Biết cấu trúc mật khẩu giúp giảm công việc tìm kiếm ra sao? | Mask đúng cấu trúc thu hẹp không gian; mask sai sẽ bỏ sót | Kích thước không gian, số tìm được, một trường hợp mask sai |
| RQ3 | Cơ chế băm và cost ảnh hưởng thế nào khi giữ nguyên mật khẩu? | bcrypt làm tăng chi phí mỗi lần thử; cost cao hơn giảm tốc độ thử | Thời gian, throughput với đơn vị rõ ràng, tỷ lệ khôi phục |
| RQ4 | John và Hashcat khác nhau ra sao trong cấu hình nhóm dùng? | Hiệu quả phụ thuộc thuật toán, backend, phần cứng và chiến lược | Cấu hình thiết bị, cùng dữ liệu, cùng tập ứng viên, log gốc |

Đây là giả thuyết, không phải kết luận đã đo. Không đặt trước phần trăm thành công hoặc tuyên bố công cụ nào nhanh hơn.

## 3. Phân công 3 thành viên

Mỗi người có phần tìm hiểu, phần thực nghiệm, phần viết và phần thuyết trình; tỷ trọng dự kiến khoảng một phần ba/người.

| Thành viên | Nội dung tìm hiểu | Công việc thực nghiệm | Nội dung viết chính | Sản phẩm bàn giao | Người phản biện |
|---|---|---|---|---|---|
| TV1 — cơ sở và nguyên lý | Offline/online; hash, salt, cost; cấu trúc xử lý của John; single/wordlist/rules | Xây manifest dữ liệu cùng TV2; thử single với tài khoản giả; kiểm tra ground truth và độ đúng kết quả | Mở đầu, Chương 1; khuyến nghị và kết luận | Sơ đồ nguyên lý; bảng khái niệm; ghi chú nguồn; biên bản kiểm tra dữ liệu | TV3 |
| TV2 — lab và kỹ thuật dò | Cài Jumbo; định dạng hash; mask, incremental; session/pot | Dựng máy ảo; tạo dữ liệu; chạy kịch bản 1 và lưu log; hướng dẫn tái lập | Chương 2 và phần kịch bản 1 của Chương 3 | README lab; cấu hình; script sinh dữ liệu; log; ảnh demo 1 | TV1 |
| TV3 — đánh giá và so sánh | bcrypt/cost; phương pháp đo; Hashcat; sai số và giới hạn | Chạy kịch bản 2; Hashcat; tổng hợp CSV và biểu đồ; kiểm tra điều kiện so sánh | Phần kịch bản 2 của Chương 3; Chương 4 | Log demo 2; bảng số liệu; biểu đồ; bảng đối chiếu công cụ | TV2 |

**Việc chung:** chốt đề cương, duyệt dữ liệu trước khi chạy, kiểm tra nguồn, đọc toàn bộ bản cuối, diễn tập trả lời phản biện. TV1 tích hợp nội dung; TV2 kiểm tra lệnh và khả năng chạy lại; TV3 thống nhất hình, bảng và số liệu. Mỗi người dự kiến 25–30 giờ trong 14 ngày.

Trang đầu báo cáo ghi họ tên, mã học viên, phần việc cụ thể, tỷ lệ đóng góp đã thống nhất sau khi hoàn thành. Không dùng tỷ lệ kế hoạch để thay thế ghi nhận đóng góp thực tế.

## 4. Đề cương báo cáo trong giới hạn 20 trang

Ngân sách dưới đây tính cả bìa, mục lục, tài liệu tham khảo và phụ lục để tránh vượt giới hạn khi chưa có hướng dẫn khác.

| Phần | Số trang dự kiến | Nội dung cần thể hiện | Chủ trì |
|---|---:|---|---|
| Bìa và phân công | 1 | Tên đề tài, môn, giảng viên, nhóm, bảng phân công ngắn | TV1 |
| Tóm tắt và mục lục | 1 | Tóm tắt 150–200 từ sau khi có kết quả; mục lục tự động | TV1 |
| Mở đầu | 1 | Vấn đề, mục tiêu, RQ1–RQ4, phạm vi, phương pháp | TV1 |
| Chương 1. Cơ sở và John the Ripper | 4 | Lưu mật khẩu; offline/online; kiến trúc chức năng; kỹ thuật sinh ứng viên | TV1 |
| Chương 2. Thiết kế và môi trường lab | 3 | Cấu hình, phiên bản, cài đặt, dữ liệu, biến kiểm soát, cách đo | TV2 |
| Chương 3. Thực nghiệm và kết quả | 5 | Hai kịch bản; bảng kết quả; đồ thị; giải thích gắn RQ | TV2 + TV3 |
| Chương 4. So sánh, thảo luận và phòng vệ | 2 | John/Hashcat; giới hạn; khuyến nghị dựa trên kết quả | TV3 |
| Kết luận | 1 | Trả lời RQ, đóng góp, hạn chế, hướng phát triển | TV1 |
| Tài liệu tham khảo | 1 | Nguồn gốc, phiên bản, ngày truy cập; trích dẫn nhất quán | Cả nhóm |
| Phụ lục ngắn | 1 | Lệnh đại diện, manifest và đường dẫn gói tái lập | TV2 |
| **Tổng** | **20** | Code và log đầy đủ để trong gói bàn giao riêng | |

### 4.1. Nội dung Chương 1

- Phân biệt mật khẩu rõ, hàm băm và mã hóa; mô hình xác minh bằng cách tính lại giá trị từ ứng viên.
- Phân biệt offline với online: lab đo việc thử trên hash cục bộ; không suy ra trực tiếp tốc độ gửi yêu cầu đăng nhập.
- Sơ đồ chức năng đề xuất: **hash/metadata → bộ nạp và kiểm tra định dạng → bộ sinh ứng viên → bộ tính hash với salt/cost → so khớp → pot/log/kết quả**. Chú thích đây là sơ đồ khái niệm do nhóm tổng hợp, không phải sơ đồ module mã nguồn chính thức.
- Giới thiệu khác biệt bản core và Jumbo; chỉ liệt kê định dạng và backend có liên quan tới lab.
- Bảng các kỹ thuật: dữ liệu đầu vào, giả định, cách sinh ứng viên, ưu điểm và giới hạn.
- Liên hệ entropy trong bài giảng: N = R^L và H = L·log₂R chỉ áp dụng cho lựa chọn độc lập, đồng đều từ tập ký tự đã xác định. Không gán entropy thực cho một mật khẩu do người chọn chỉ từ độ dài và loại ký tự.

Wordlist thử các mục trong danh sách; rules biến đổi từ gốc; single khai thác metadata tài khoản; incremental ưu tiên tổ hợp dựa trên thống kê ký tự. [Tài liệu các chế độ của Openwall](https://www.openwall.com/john/doc/MODES.shtml). Mask mô tả vị trí ký tự, còn hybrid mask kết hợp từ gốc và mẫu bổ sung. [Tài liệu MASK của Jumbo](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MASK).

### 4.2. Nội dung Chương 2

Ghi được cấu hình máy thật và máy ảo, phiên bản OS, số vCPU, RAM, trạng thái GPU/backend, phiên bản/commit công cụ, số luồng, cách cài đặt và kết quả tự kiểm tra. Lưu cấu hình rules/charset đang dùng; nêu cách sinh salt và cost; bảng mô tả dữ liệu; tiêu chí kết thúc; quy trình chạy lại.

### 4.3. Nội dung Chương 3–4

Với mỗi kịch bản: mục tiêu → giả thuyết → dữ liệu → cấu hình → lệnh đại diện → kết quả → giải thích → giới hạn. Mỗi hình phải có số thứ tự, chú thích, tham chiếu từ nội dung và đường dẫn log tương ứng. Phần so sánh phân biệt năng lực có trong tài liệu với hiệu năng thực sự đo được.

## 5. Kế hoạch tìm kiếm và quản lý tài liệu

### 5.1. Danh mục nguồn ưu tiên

Các nguồn dưới đây đã được kiểm tra khi lập kế hoạch ngày 29/10/2026. Khi thực hiện, nhóm cần lưu bản/commit tương ứng vì tài liệu nhánh phát triển có thể thay đổi.

| Mã | Nguồn chính thức | Mục đích sử dụng | Người đọc |
|---|---|---|---|
| S0 | Tài liệu học phần trong `tmp/pdfs/1-CDE1-T5-2026.txt`, slide 4–5, 41 | Ràng buộc bài làm; liên hệ entropy | TV1 |
| S1 | [Openwall: John documentation](https://www.openwall.com/john/doc/) | Tổng quan và quy trình sử dụng | TV1 |
| S2 | [Openwall: cracking modes](https://www.openwall.com/john/doc/MODES.shtml) | Single, wordlist, incremental | TV1 + TV2 |
| S3 | [Openwall: wordlist rules](https://www.openwall.com/john/doc/RULES.shtml) | Cú pháp rules; minh họa biến đổi | TV1 + TV2 |
| S4 | [John Jumbo: MASK](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MASK) | Mask và hybrid; placeholder | TV2 |
| S5 | [John Jumbo: OPTIONS](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/OPTIONS) | Pot, session, giới hạn thời gian, benchmark | TV2 |
| S6 | [Kho John Jumbo](https://github.com/openwall/john) | Phiên bản, mã nguồn, hướng dẫn build | TV2 |
| S7 | [Hashcat documentation](https://hashcat.net/wiki/doku.php?id=hashcat) và [example hashes](https://hashcat.net/wiki/doku.php?id=example_hashes) | Backend, attack mode, định dạng và mã hash | TV3 |
| S8 | [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | Salt, work factor và lưu mật khẩu | TV3 |
| S9 | [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) | Chính sách mật khẩu và xác thực | TV1 |
| S10 | [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html) | Đọc thêm về Argon2 và chi phí bộ nhớ | TV3 |

### 5.2. Các bước tìm hiểu

1. **D1 — đọc yêu cầu và lập bản đồ câu hỏi.** Mỗi người ghi các khái niệm cần trả lời theo phần phụ trách; đánh dấu nội dung đã có trong slide và nội dung phải kiểm tra nguồn mới.
2. **D1–D2 — đọc nguồn chính.** Truy vấn gợi ý: `site:openwall.com/john cracking modes`, `site:github.com/openwall/john doc MASK`, `site:hashcat.net wiki example hashes`, `site:pages.nist.gov/800-63-4 passwords`, `site:cheatsheetseries.owasp.org Password Storage`. Mục tiêu là tìm đúng mục tài liệu, không thu thập nhiều bài hướng dẫn trùng nhau.
3. **D2–D3 — đối chiếu với bản cài.** Chạy help/list-format trên lab; đối chiếu cú pháp với tài liệu. Blog/video chỉ hỗ trợ thao tác nếu cần; luận điểm kỹ thuật dựa trên tài liệu chính thức hoặc dữ liệu nhóm đo.
4. **D3 — bàn giao bản ghi chú.** Mỗi người nộp 1–2 trang tổng hợp, ít nhất 3 nguồn có ích, 3 câu hỏi phản biện và các điểm chưa xác minh.
5. **D10–D12 — kiểm tra trích dẫn.** Mỗi nhận định quan trọng phải nối được tới nguồn cụ thể hoặc mã lần chạy. Kiểm tra phiên bản và ngày truy cập trước khi chốt bài.

Mẫu ghi chú chung: `source_id, tác giả/tổ chức, tên, URL, phiên bản/commit, ngày truy cập, mục/đoạn, ý diễn giải, dùng ở chương nào, điều cần kiểm chứng`. Trích dẫn theo số [1], [2]… hoặc đúng mẫu giảng viên cung cấp; dùng một cách thống nhất.

## 6. Thiết kế lab và dữ liệu

### 6.1. Cấu hình đề xuất

Một máy ảo Linux, 4 vCPU, 8 GB RAM, khoảng 25 GB đĩa là cấu hình khởi điểm đề xuất, không phải yêu cầu tối thiểu của công cụ. Có thể giảm theo máy thật nhưng phải ghi rõ. Dùng một máy chuẩn để đo; các thành viên còn lại dùng bản sao cấu hình để kiểm tra tái lập. Chụp snapshot sau khi cài và tự kiểm tra thành công.

Cài John Jumbo theo hướng dẫn chính thức hoặc gói phân phối đã xác minh đủ tính năng. Không mặc định gói `john` của mọi distro đều có Jumbo/mask. Kiểm tra `john --list=build-info`, `john --list=formats`, `john --list=inc-modes` nếu bản cài hỗ trợ. Lưu stdout/stderr và bản cấu hình. Hashcat cần backend phù hợp; kiểm tra thiết bị bằng `hashcat -I` trước ngày đo.

Khởi đầu bằng CPU; GPU là phần mở rộng khi có thiết bị, driver và thời gian. Nếu Hashcat không có CPU backend trên lab, chuẩn bị môi trường có backend từ D2. Nếu chỉ đo được GPU, trình bày đó là so sánh hai cấu hình triển khai và ghi rõ hạn chế suy luận về bản thân công cụ.

### 6.2. Bộ dữ liệu chung

Tạo 100 mật khẩu khác nhau, chia 5 nhóm × 20. Đây là bộ dữ liệu có chủ đích để kiểm tra giả thuyết; không đại diện thống kê cho người dùng thực tế.

| Nhóm | Cách xây dựng | Dùng để kiểm tra |
|---|---|---|
| G1 — từ gốc | Chọn 20 từ có mặt trong wordlist cố định | Baseline wordlist |
| G2 — biến thể | Từ gốc khác G1, viết hoa đầu/thêm số/ký hiệu theo quy tắc công bố trước | Rules/hybrid so với wordlist |
| G3 — theo cấu trúc | 20 chuỗi ngẫu nhiên đúng mẫu 2 chữ thường + 4 số | Mask đúng và sai giả định |
| G4 — chuỗi ngẫu nhiên | 20 chuỗi dài 12–16 ký tự, không trùng tập thử đã xác định | Giới hạn của ngân sách thử |
| G5 — cụm từ dài | 20 cụm ghép từ danh sách từ với cách sinh được ghi lại | Phân biệt chiều dài với độ dễ đoán |

Wordlist học thuật tự xây khoảng 1.000 từ, bỏ trùng và giữ thứ tự cố định. Tạo và khóa wordlist/rules trước khi đo; không bổ sung đáp án sau khi xem kết quả. Việc G1 nằm trong danh sách là điều kiện thiết kế, phải nói rõ khi báo cáo. G4/G5 không tìm được chỉ có nghĩa chưa tìm được trong điều kiện đã thử.

Manifest ghi `id, group, generation_method, length, ground_truth_ref`. Lưu mật khẩu gốc trong tệp kiểm chứng riêng để đối chiếu kết quả; các tệp hash dùng cho chạy chỉ chứa dữ liệu cần thiết. Với dữ liệu ngẫu nhiên, lưu nguyên bộ dữ liệu đã tạo và checksum để tái lập; chỉ ghi seed nếu bộ sinh thực sự hỗ trợ tái lập bằng seed.

Băm cùng 100 mật khẩu thành các tập: raw SHA-256; bcrypt cost 10; bcrypt cost 12. Tạo salt riêng từng bản ghi bcrypt và lưu nguyên chuỗi mã hóa. Dùng thư viện chuẩn/phổ biến, ghi phiên bản và tự kiểm tra xác minh hash trước khi đo. Chọn SHA-256 ở đây làm đường cơ sở hàm băm nhanh; không coi đó là phương án lưu mật khẩu phù hợp. [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

Single crack dùng bộ phụ 6–10 tài khoản giả với username/GECOS và mật khẩu liên quan có chủ đích; lưu đúng cấu trúc đầu vào được bản John hỗ trợ. Không đưa số liệu này vào so sánh giữa các chế độ dùng hash thuần vì thông tin đầu vào khác nhau.

## 7. Kịch bản 1 — đánh giá kỹ thuật sinh ứng viên

**Chủ trì:** TV2; TV1 kiểm chứng dữ liệu; TV3 tổng hợp kết quả.

**Câu hỏi:** với cùng 100 hash raw SHA-256, chiến lược nào tìm được nhóm nào trong ngân sách cố định?

| Mã | Phương án | Đầu vào/cấu hình | Mục đích |
|---|---|---|---|
| A1 | Wordlist | Wordlist 1.000 từ, không rules | Baseline |
| A2 | Wordlist + rules | Cùng wordlist; bộ rules nhỏ do nhóm công bố trước | Đo lợi ích biến đổi từ |
| A3 | Mask | `?l?l?d?d?d?d` | Khớp cấu trúc G3; không gian 26² × 10⁴ = 6.760.000 |
| A4 | Incremental có giới hạn | Charset và chiều dài cố định, ví dụ LowerNum 1–6; kiểm tra tồn tại trên bản cài | Quan sát giới hạn không gian rộng |
| A5 | Tiểu thử mask sai | Ví dụ 6 chữ số trên cùng dữ liệu G3 | Chỉ ra ảnh hưởng giả định sai |
| A6 | Minh họa single | Bộ tài khoản giả có metadata riêng | Giải thích vai trò thông tin tài khoản |

A1–A4 chạy độc lập tối đa 300 giây/lần, 3 lần/phương án. Nếu hết ứng viên hoặc tìm hết hash trước thời hạn, ghi đúng nguyên nhân kết thúc. A5–A6 chỉ minh họa, giới hạn tối đa 60 giây; không cần lặp để suy luận hiệu năng.

Quy trình: kiểm tra checksum dữ liệu → tạo mã lần chạy và pot mới → ghi cấu hình → chạy → xuất kết quả → đối chiếu ground truth → ghi số lượng theo nhóm → lưu log và nguyên nhân kết thúc. Lấy tiến độ tại các mốc 10, 30, 60, 120, 300 giây nếu còn chạy; khi đã kết thúc thì ghi trạng thái cuối.

John lưu các mật khẩu đã tìm được trong pot và dùng dữ liệu này để bỏ qua hash đã khôi phục ở lần sau, vì vậy cần pot độc lập cho phép so sánh độc lập. [Hướng dẫn sử dụng John](https://www.openwall.com/john/doc/). Session, pot và giới hạn thời gian phải đặt rõ theo bản Jumbo sử dụng. [Tùy chọn Jumbo](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/OPTIONS).

Lệnh mẫu dự kiến trong Linux/Bash, chạy tại thư mục lab; chỉ dùng sau khi đã tạo các tệp và xác nhận format trên bản cài:

```bash
john --format=raw-sha256 --wordlist=data/wordlist.txt --max-run-time=300 --session=A1_r1 --pot=results/A1_r1.pot data/sha256.txt
john --format=raw-sha256 --wordlist=data/wordlist.txt --rules --max-run-time=300 --session=A2_r1 --pot=results/A2_r1.pot data/sha256.txt
john --format=raw-sha256 --mask='?l?l?d?d?d?d' --max-run-time=300 --session=A3_r1 --pot=results/A3_r1.pot data/sha256.txt
john --format=raw-sha256 --incremental=LowerNum --min-length=1 --max-length=6 --max-run-time=300 --session=A4_r1 --pot=results/A4_r1.pot data/sha256.txt
john --show --format=raw-sha256 --pot=results/A1_r1.pot data/sha256.txt
```

Lệnh A2 trên dùng rules mặc định của bản cài. Trước đo chính thức phải lưu nguyên cấu hình rules đó hoặc đổi sang rules riêng có tên và lưu tệp kèm theo. Không đổi rules giữa các lần lặp. `--session` khác tên chưa đảm bảo pot tách biệt; cần đặt cả `--pot`. Khi lặp r2/r3 đổi cả hai tên; không dùng lại pot chứa kết quả cũ.

**Sản phẩm:** bảng tỷ lệ theo G1–G5; đồ thị số mật khẩu khôi phục theo thời gian; sơ đồ 3–5 ứng viên được rules biến đổi; ảnh lệnh và kết quả tiêu biểu. Giải thích lợi ích của rules/mask kèm điều kiện về tập dữ liệu, không khẳng định một chế độ luôn tốt nhất.

## 8. Kịch bản 2 — ảnh hưởng của hàm băm, cost và đối chiếu Hashcat

**Chủ trì:** TV3; TV2 hỗ trợ môi trường; TV1 kiểm tra cách diễn giải.

### 8.1. Phần B — so sánh cơ chế băm

Xuất trước tập ứng viên hữu hạn từ wordlist + rules đã khóa ở kịch bản 1, bỏ trùng theo cách giữ thứ tự, lưu checksum. Dùng đúng tệp ứng viên đó cho cả raw SHA-256, bcrypt cost 10 và cost 12 để tách ảnh hưởng chiến lược sinh ứng viên khỏi chi phí băm.

- B1: John với raw SHA-256.
- B2: John với bcrypt cost 10.
- B3: John với bcrypt cost 12.

Mỗi cấu hình chạy tối đa 300 giây, lặp 3 lần, pot mới. Dùng đúng format có trong `--list=formats`; tên format bcrypt cần kiểm tra trên bản cài, không suy ra từ tên thuật toán. Ghi tổng thời gian, số khôi phục, số hash còn lại và tốc độ có nhãn đơn vị. Nếu wordlist quá nhỏ khiến cả ba kết thúc gần như tức thời, dùng tập ứng viên lớn hơn đã chốt qua pilot và áp dụng lại cho cả ba trước khi bắt đầu đo chính thức.

**Phép đo bổ sung để giải thích throughput:** chọn một mật khẩu đối chứng chắc chắn nằm ngoài tập ứng viên đã khóa, tạo một hash cho mỗi cơ chế. Chạy cùng tập ứng viên lên từng hash; việc không có kết quả khôi phục giúp giữ số hash hoạt động ổn định. Tách rõ dữ liệu này với số liệu khôi phục trên 100 mật khẩu. Có thể dùng benchmark tích hợp để kiểm tra môi trường, nhưng không thay kết quả chạy trên dữ liệu lab bằng benchmark.

Không gán mọi khác biệt raw SHA-256/bcrypt riêng cho salt: thuật toán và cost cũng thay đổi. Muốn nghiên cứu riêng salt cần thí nghiệm có kiểm soát bổ sung; phần này chỉ giải thích vai trò bằng tài liệu.

### 8.2. Phần C — đối chiếu công cụ

Trước hết so sánh định tính theo tài liệu và bản cài: nền tảng/backend, định dạng liên quan, cách chuẩn bị đầu vào, chế độ sinh ứng viên, quản lý phiên, xuất kết quả, độ dễ tái lập. Không dùng nhận định “John chỉ chạy CPU” hoặc “Hashcat chỉ chạy GPU”.

Thử nghiệm định lượng tối thiểu: raw SHA-256, cùng tập ứng viên đã xuất ở phần B, cùng 100 hash, cùng máy/backend nếu có thể, 300 giây, 3 lần mỗi công cụ. Tệp hash thuần một hash/dòng giúp thống nhất đầu vào; kiểm tra mã hash của Hashcat theo tài liệu đúng phiên bản. Wordlist attack tương ứng chạy trực tiếp tệp ứng viên đã xuất, không áp dụng thêm rules của từng công cụ. [Tài liệu Hashcat](https://hashcat.net/wiki/doku.php?id=hashcat).

Nếu so sánh thêm mask, dùng cùng mẫu và tập ký tự; ghi rõ thứ tự duyệt có thể khác. Đo thời gian khởi động riêng nếu có chênh lệch đáng kể. Không đối chiếu tốc độ từ hai máy khác nhau rồi kết luận ưu thế phần mềm. Nếu chưa có backend thích hợp, vẫn hoàn thành bảng định tính nhưng đánh dấu phần hiệu năng chưa đo và nêu nguyên nhân cụ thể.

### 8.3. Nội dung phòng vệ cần liên hệ

Khuyến nghị lưu mật khẩu dùng KDF chuyên dụng có salt riêng và cost phù hợp; tham khảo Argon2id cho thiết kế mới. Argon2 có chi phí bộ nhớ/thời gian, được mô tả trong [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html). bcrypt trong lab đóng vai trò ví dụ cơ chế có cost, không phải kết luận rằng nó luôn là lựa chọn tốt nhất cho hệ thống mới.

Đối với người dùng và hệ thống xác thực, liên hệ mật khẩu dài, khó đoán, trình quản lý mật khẩu, blocklist và MFA. Rate limiting tác động tới thử đăng nhập online; không trực tiếp làm chậm việc tính hash ngoại tuyến. Đối chiếu chính sách theo [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html); không tự động sao chép yêu cầu thay mật khẩu định kỳ từ tài liệu cũ.

## 9. Phương pháp đo và xử lý kết quả

### 9.1. Biến kiểm soát và số lượt chạy

Giữ cố định dữ liệu, checksum, phiên bản, số luồng, backend, cấu hình VM và giới hạn thời gian. Chạy từng phép đo nối tiếp trên máy chuẩn, tránh tải nền lớn. Luân phiên hoặc xáo trộn thứ tự cấu hình giữa các lần lặp; ghi điều kiện nhiệt độ/tải nếu có biến động rõ. Lượt warm-up hoặc pilot lưu riêng, không gộp vào số liệu chính.

Khối lượng chính: A1–A4 = 12 lượt; B1–B3 = 9 lượt; C = 6 lượt; phép đo đối chứng một hash = 9 lượt. Tổng 36 lượt × tối đa 5 phút ≈ 3 giờ thời gian chạy, chưa gồm chuẩn bị và thu thập dữ liệu. B1 có thể tái sử dụng cho phía John của C nếu mọi điều kiện và tập ứng viên thực sự giống nhau; ghi mã lượt gốc, không coi đó là phép đo độc lập mới.

### 9.2. Chỉ số

- **Tỷ lệ khôi phục theo bản ghi:** số ID xác minh đúng / tổng ID trong tập × 100%; tính riêng từng G1–G5 và toàn bộ. Ghi riêng số hash duy nhất nếu có bản ghi trùng.
- **Số khôi phục theo thời gian:** tại các mốc đã chọn. Nếu không lưu được thời điểm của từng kết quả thì không vẽ đường thời gian chi tiết giả định.
- **Thời gian:** tách thời gian thực tế của tiến trình, thời gian phần dò nếu công cụ báo, và nguyên nhân kết thúc. Chưa tìm được ở 300 giây là quan sát bị giới hạn bởi thời gian, không phải thời gian phá bằng 300 giây.
- **Tốc độ:** lưu đúng nhãn p/s, c/s, C/s, H/s… từ từng công cụ; giải thích theo tài liệu bản cài. Không tự coi tất cả đều là “mật khẩu/giây”; số salt/hash đang hoạt động và cơ chế batch có thể ảnh hưởng.
- **Tóm tắt lặp:** median và min–max của 3 lượt. Ba lượt chỉ giúp quan sát độ ổn định trên lab; không đủ để tuyên bố tính đại diện rộng.

Ước lượng lý tưởng T_toàn_bộ ≈ N/v và T_trung_bình ≈ N/(2v) chỉ dùng khi ứng viên đồng đều, duyệt không lặp và tốc độ xấp xỉ cố định. Với mật khẩu người chọn, phân bố và thứ tự đoán rất quan trọng; không dùng công thức này như dự báo thực tế chắc chắn.

### 9.3. Mẫu dữ liệu kết quả

```text
run_id,scenario,tool,version,device,threads,dataset_sha256,candidates_sha256,format,cost,mode,budget_s,wall_time_s,loaded_hashes,unique_hashes,recovered_ids,recovery_rate,speed_value,speed_unit,stop_reason,log_path,notes
```

Lưu bảng tiến độ riêng: `run_id, elapsed_s, group, recovered_ids`. Nếu chỉ số nào công cụ không cung cấp hoặc không đo được, ghi NA và lý do; không ước lượng rồi ghi như số đo.

| Lượt | Công cụ | Hash/cost | Chiến lược | Thời gian thực | Khôi phục | Đơn vị tốc độ | Kết thúc |
|---|---|---|---|---|---|---|---|
| A1_r1 | John | raw SHA-256 | Wordlist | Chưa đo | Chưa đo | Chưa đo | Chưa đo |
| B2_r1 | John | bcrypt/10 | Tập ứng viên cố định | Chưa đo | Chưa đo | Chưa đo | Chưa đo |
| C_H_r1 | Hashcat | raw SHA-256 | Cùng tập ứng viên | Chưa đo | Chưa đo | Chưa đo | Chưa đo |

## 10. Lịch triển khai 14 ngày

| Ngày | TV1 | TV2 | TV3 | Điều kiện hoàn thành ngày/mốc |
|---|---|---|---|---|
| D1 | Chốt mục tiêu, đọc yêu cầu | Khảo sát máy và VM | Khảo sát Hashcat/backend | Đề cương, phân công, lịch và hạn nộp đã xác nhận |
| D2 | Đọc nguyên lý/modes | Cài Jumbo, tự kiểm tra | Cài Hashcat, kiểm tra thiết bị | M1: môi trường chạy được; ghi phiên bản |
| D3 | Chốt manifest và tiêu chí đúng | Tạo dữ liệu/hash | Chốt ma trận đo/CSV | Bộ dữ liệu và wordlist có checksum |
| D4 | Kiểm tra metadata/single | Pilot A1–A4 | Pilot B/C; ước lượng ngân sách | M2: dữ liệu hợp lệ, chạy thử thành công |
| D5 | Viết Mở đầu/Chương 1 | Khóa rules, dữ liệu; đo A lượt 1 | Khóa tập ứng viên B/C | Không sửa dữ liệu sau khi bắt đầu đo chính thức |
| D6 | Phản biện log A | Đo A lượt 2–3 | Chuẩn bị thu thập tiến độ | Kịch bản 1 đủ log và ground truth |
| D7 | Hoàn thiện lý thuyết | Viết Chương 2 | Đo B và đối chứng một hash | M3: kịch bản 2 phần B đủ dữ liệu |
| D8 | Kiểm tra so sánh công bằng | Kiểm tra tái lập vài lượt | Đo C, tổng hợp CSV | Hai demo và dữ liệu đối chiếu hoàn tất |
| D9 | Đọc giải thích kết quả | Viết kịch bản 1 | Vẽ biểu đồ, viết B/C | M4: bảng/biểu đồ truy được về log |
| D10 | Tích hợp báo cáo | Hoàn thiện README và ảnh | Viết thảo luận/khuyến nghị | Bản nháp đầy đủ, chưa vượt ngân sách trang |
| D11 | Sửa luận điểm và nguồn | Rà lệnh, cấu hình | Kiểm tra tính toán và đơn vị | M5: phản biện chéo xong; RQ đều có trả lời |
| D12 | Rút gọn, viết kết luận | Chuẩn bị demo/video | Làm slide dựa trên số liệu đã chốt | Báo cáo ≤20 trang, slide nhất quán |
| D13 | Diễn tập phần nguyên lý | Diễn tập demo | Diễn tập kết quả/phản biện | M6: chạy thử từ môi trường sạch; sửa lỗi cuối |
| D14 | Kiểm tra thông tin bìa | Kiểm tra gói code/dữ liệu | Kiểm tra PDF và biểu đồ | Gói nộp hoàn chỉnh, cả nhóm duyệt |

Nếu chỉ có 7 ngày: gộp D1–D2, D3–D4, D5–D6, D7–D8, D9–D10, D11–D12, D13–D14; ưu tiên hai kịch bản chính và so sánh wordlist cố định với Hashcat. Lược phần GPU/hybrid mở rộng trước khi giảm chất lượng kiểm chứng.

## 11. Kế hoạch viết bài và slide

Mỗi người viết trực tiếp vào cấu trúc đã chốt, dùng cùng thuật ngữ: “ứng viên mật khẩu”, “khôi phục/dò mật khẩu”, “băm”, “salt”, “cost”, “tấn công ngoại tuyến”. Hạn chế cách nói “giải mã hash” vì hoạt động lab là sinh ứng viên, tính và so khớp.

Mỗi đoạn đánh giá cần chỉ ra: quan sát nào từ bảng/biểu đồ → cơ chế giải thích → điều kiện áp dụng → giới hạn. Khi kết quả trái giả thuyết, kiểm tra dữ liệu/format/pot/backend trước; nếu không có lỗi, giữ kết quả và thảo luận nguyên nhân.

Gợi ý 12 slide cho khoảng 12–15 phút, điều chỉnh theo thời lượng lớp:

1. Chủ đề và phân công — TV1.
2. Vấn đề, mục tiêu, RQ — TV1.
3. Offline cracking và sơ đồ John — TV1.
4. Các chiến lược sinh ứng viên — TV1.
5. Lab, phiên bản, dữ liệu — TV2.
6. Kịch bản 1 và giả thuyết — TV2.
7. Demo 1, biểu đồ và nhận xét — TV2.
8. Kịch bản 2: thuật toán/cost — TV3.
9. Demo 2, kết quả đo — TV3.
10. John–Hashcat và điều kiện so sánh — TV3.
11. Khuyến nghị, giới hạn, trả lời RQ — chia đều.
12. Kết luận và nguồn chính — TV1 kết nối phần trao đổi.

Mỗi demo trực tiếp khoảng 60–90 giây với dữ liệu nhỏ trích từ bộ đã đo; báo cáo dùng kết quả từ đầy đủ lượt đo. Chuẩn bị video và log của chính nhóm làm phương án dự phòng. Ghi rõ nếu trình bày kết quả lưu sẵn. Mỗi thành viên chuẩn bị trả lời ít nhất 3 câu hỏi thuộc phần của người khác.

Câu hỏi phản biện nên luyện: Vì sao hash không được “giải mã”? Vì sao mật khẩu có ký hiệu vẫn dễ đoán? Vì sao salt không làm mật khẩu yếu thành mạnh? Vì sao đổi session vẫn có thể ảnh hưởng kết quả? Vì sao không tìm được trong 5 phút chưa chứng minh an toàn? Điều kiện nào cho phép so sánh tốc độ John với Hashcat?

## 12. Rủi ro, cách xử lý và tiêu chí nghiệm thu

| Rủi ro thực tế | Xử lý |
|---|---|
| Bản John thiếu mask/format | Phát hiện ở D2; chuyển sang bản Jumbo phù hợp, lưu phiên bản mới |
| Hashcat không nhận thiết bị | Kiểm tra backend sớm; chuẩn bị môi trường tương thích, ghi rõ giới hạn nếu chỉ so sánh định tính |
| Các lượt kết thúc quá nhanh | Pilot để chọn tập ứng viên và phép đo đối chứng phù hợp; ghi riêng thời gian khởi động |
| bcrypt quá chậm, không có kết quả | Đây vẫn là quan sát hợp lệ; dùng nhóm đối chứng yếu và throughput để giải thích, không sửa đáp án sau đo |
| Pot cũ làm mất tính độc lập | Pot riêng từng lượt; khởi đầu sạch, xác nhận số hash nạp |
| Kết quả khác máy | Dùng máy chuẩn cho bảng chính; các máy khác chỉ kiểm tra tái lập và ghi riêng |
| Bài vượt 20 trang | Giữ bảng/biểu đồ quan trọng; đưa log/code đầy đủ vào gói kèm, vẫn giữ thông tin phương pháp cần thiết trong bài |

Nghiệm thu trước khi nộp:

- Đủ 5 nhóm nội dung theo slide, đúng chủ đề 17; bìa có phân công; tổng số trang không quá 20.
- Hai kịch bản có mục tiêu, dữ liệu, điều kiện đo, kết quả và phân tích; không chỉ có ảnh terminal.
- Mọi số đo truy được tới mã lượt, log, cấu hình, checksum dữ liệu; không điền số dự kiến thành số thực nghiệm.
- Đã đối chiếu kết quả với ground truth; kiểm tra salt/cost/format và tính độc lập của pot.
- So sánh Hashcat có điều kiện rõ ràng, không lẫn CPU/GPU hoặc tập ứng viên khác nhau mà bỏ qua ảnh hưởng.
- Có giới hạn của dữ liệu tổng hợp, ngân sách thời gian, phần cứng và số lần lặp.
- Các nguồn kỹ thuật chính có trích dẫn; cả 3 người đọc và hiểu toàn bộ bản cuối.
- Người khác trong nhóm chạy lại được một lượt theo README; PDF, slide và CSV thống nhất.

## 13. Cấu trúc gói bàn giao đề xuất

Cây bên dưới là cấu trúc nhóm sẽ tạo trong giai đoạn triển khai; hiện mới có tài liệu kế hoạch này.

```text
jtr-report/
  README.md
  report/              # Bản nguồn, PDF cuối cùng
  slides/              # Slide, PDF, ghi chú thuyết trình
  references/          # Danh mục nguồn và ghi chú
  lab/
    environment/       # Phiên bản, phần cứng, backend
    scripts/           # Sinh dữ liệu, chạy, tổng hợp
    configs/           # Rules và charset/config được sử dụng
    data/              # Manifest, hash, wordlist, checksum
    ground-truth/      # Dữ liệu gốc tổng hợp dùng đối chiếu
    results/           # CSV, pot, log theo run_id
    figures/           # Biểu đồ xuất từ CSV
  demo/                # Kịch bản trình diễn và video dự phòng
```

Việc làm đầu tiên sau khi nhóm thông qua kế hoạch: điền tên TV1–TV3, xác nhận hạn nộp hiện tại, chốt máy chuẩn và thực hiện D1–D2. Chỉ viết phần kết quả và tóm tắt kết luận sau khi có dữ liệu thực nghiệm đã kiểm tra.
