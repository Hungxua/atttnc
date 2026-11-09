# Kịch bản demo và câu hỏi phản biện

## Demo 1 khoảng 90 giây

TV2 mở manifest, giải thích 5 nhóm dữ liệu và việc G1/G2 được thiết kế phù hợp wordlist/rules. Chạy `Demo-1.ps1` từ thư mục demo bằng PowerShell. Script tạo thư mục mới theo timestamp để không dùng lại pot. Giới thiệu kết quả wordlist, rules, mask đúng và mask sai. Mở log chính thức để chỉ ra số hash nạp, luồng và lý do dừng. TV1 giải thích sơ đồ ứng viên, tính hash và so khớp.

## Demo 2 khoảng 90 giây

TV3 mở các terminal.log B1, B2, B3 và D2, D3 của loạt formal. Trình bày đây là log của phiên đã đo, tránh chờ toàn bộ lượt dài trong giờ thuyết trình. Chỉ rõ: cùng mật khẩu, cùng ứng viên, khác cơ chế băm/cost. Giải thích lý do dùng đối chứng một hash và phân biệt p/s với c/s. Dùng CSV/biểu đồ để trình bày median và min–max.

Nếu cần chạy trực tiếp: dùng tệp control-bcrypt10.txt và control-bcrypt12.txt với `--max-run-time=5`, pot mới. Đây là demo ngắn, không thay thế số liệu của lượt formal 60 giây. Không ghép vào bảng kết quả.

## Phân chia lời trình bày

TV1: vấn đề, cơ sở, nguyên lý và giới hạn entropy. TV2: môi trường, dữ liệu và demo 1. TV3: demo 2, Hashcat và phương pháp đọc kết quả. Cả nhóm chia phần thảo luận và trả lời phản biện theo hiểu biết thực tế.

## Câu hỏi phản biện

1. Vì sao dùng SHA-256 dù không khuyến nghị lưu mật khẩu bằng hàm băm nhanh? — Để có đường cơ sở; mục tiêu là quan sát cơ chế và chi phí, không thiết kế lưu mật khẩu sản xuất.
2. Vì sao rules tìm đúng 40/100? — G1/G2 được thiết kế tương ứng wordlist/rules. Đây không phải ước lượng tỷ lệ mật khẩu yếu trong thực tế.
3. Salt có ngăn hoàn toàn dò mật khẩu không? — Salt phân biệt bản ghi và hạn chế tái sử dụng tính toán; chi phí một lần thử và độ khó đoán vẫn quan trọng.
4. Vì sao khác session vẫn chưa đủ? — Pot chung có thể chứa đáp án cũ khiến John bỏ qua hash đã tìm. Lab dùng cả session và pot riêng.
5. Vì sao chưa tìm được G4/G5 không chứng minh an toàn? — Tập ứng viên và thời gian có giới hạn; kết luận chỉ gắn với điều kiện đã thử.
6. Có kết luận Hashcat nhanh hơn John không? — Chỉ nếu thiết kế đo kiểm soát được backend, phần cứng, ứng viên và trạng thái khởi động. Bài hiện ghi rõ cấu hình khác nhau và giới hạn.
7. Vì sao không lấy 4.000 chia thời gian tiến trình để so tốc độ SHA-256? — Khối lượng nhỏ, phần khởi tạo chi phối và có độ phân giải thời gian hữu hạn.
8. Cost 12 có nghĩa 12 vòng lặp không? — Không; log bcrypt trong lab báo 4.096, so với 1.024 ở cost 10.
9. Ai đã thực hiện phần nào? — Điền và trả lời theo đóng góp thực tế sau khi từng thành viên tiếp nhận, tự chạy lại và kiểm tra bản thảo. Không dùng bảng phân công dự kiến để khẳng định công việc đã làm.

## Trước giờ bảo vệ

Kiểm tra tên nhóm và thành viên, thử mở PDF/PPTX, chạy demo từ thư mục mới, kiểm tra bản công cụ và dữ liệu có sẵn, chuẩn bị log để trình bày nếu máy chiếu hoặc môi trường gặp vấn đề. Nếu dùng video/log lưu sẵn, nói rõ ngay khi trình bày.
