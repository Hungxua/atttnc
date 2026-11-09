# Ghi chú nghiên cứu TV3

Tài liệu bàn giao để đọc và phản biện, không xác nhận cá nhân đã thực hiện các lượt đo.

**Câu hỏi phụ trách:** cost làm thay đổi gì; so sánh trên nhiều hash khác đối chứng một hash ra sao; khi nào được so tốc độ giữa công cụ.

1. [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html): phân biệt hàm băm nhanh với KDF mật khẩu, salt riêng và work factor. Báo cáo dùng bcrypt làm ví dụ thực nghiệm, Argon2id cho phần đọc thêm về thiết kế mới.
2. [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html): đọc tham số bộ nhớ, số lượt và song song của Argon2. Không biến đề tài thành triển khai Argon2 nếu chưa có thời gian đo và hỗ trợ công cụ.
3. [Hashcat documentation](https://hashcat.net/wiki/doku.php?id=hashcat): đối chiếu mode, thiết bị, runtime, trạng thái và potfile. Xem -I để biết thiết bị thực nhận, không suy CPU/GPU từ thông số máy.
4. [Hashcat example hashes](https://hashcat.net/wiki/doku.php?id=example_hashes): xác minh mã 1400 cho raw SHA-256 ở phiên bản sử dụng; chỉ dùng tệp hash thuần theo chuẩn hỗ trợ.

**Bằng chứng cần tự mở:** log B1–B3 và D1–D3; Hashcat device info; mọi lần thất bại do backend; CSV từng lượt và tổng hợp. Giữ số liệu lỗi môi trường tách khỏi phép đo thành công.

**Phân tích cần có:** median và min–max; đơn vị tốc độ đúng; số salt và số hash hoạt động; wall time có khởi động; giải thích việc G4/G5 không tìm được. Không xếp hạng tốc độ khi backend khác nhau. Đối chứng D có một hash và không chứa đáp án để tránh số mục tiêu giảm trong khi chạy.

**Ba câu tự kiểm tra:** Cost 12 có phải 12 vòng? Vì sao p/s và c/s có thể khác khi có 100 salt? Vì sao kết quả SHA-256 với 4.000 ứng viên chưa đủ làm benchmark ổn định?

Ngày kiểm tra nguồn: 29/10/2026. Nội dung dùng cho kịch bản 2, Chương 4, biểu đồ và demo 2. Các nhận xét chỉ áp dụng cho môi trường, thời gian và dữ liệu đã công bố.
