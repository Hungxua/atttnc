# Ghi chú nghiên cứu TV2

Tài liệu bàn giao cho thành viên phụ trách lab; cần tự kiểm tra trước khi xác nhận đóng góp.

**Câu hỏi phụ trách:** bản cài có Jumbo và format cần thiết không; mask/rules sinh tập ứng viên nào; cách làm các lượt độc lập; cách chạy lại.

1. [John download](https://www.openwall.com/john/): nhận diện gói Windows x64 1.9.0-jumbo-1, ghi việc bản này đã cũ. Binary dùng cho báo cáo phải trùng checksum host.json; không suy phiên bản từ trang tải hiện hành.
2. [MASK](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MASK): kiểm tra ?l và ?d, tính 26² × 10⁴, tạo một mask sai để minh họa phạm vi. Đối chiếu lệnh với bản cài thực tế.
3. [RULES](https://www.openwall.com/john/doc/RULES.shtml): rules Lab giữ nguyên, viết hoa, nối 2026! và nối 123. Xuất 4.000 ứng viên bằng John rồi so cả thứ tự với candidates.txt; không chỉ so số dòng.
4. [OPTIONS](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/OPTIONS): đọc pot, session, format, self-test và max-run-time. Exit code 1 có thể là dừng vì giới hạn thời gian ở bản đã đo; cần đọc log cùng exit code thay vì đánh dấu lỗi chung.

**Các tệp cần nắm:** scripts/run_lab.py, configs/lab-rules.conf, configs/experiment.conf, data/checksums.json và README-Linux-VM.md. Runner dừng khi thấy thư mục lượt đã tồn tại để bảo vệ kết quả. Cấu hình experiment.conf tạo lại khi setup, dùng đường dẫn cục bộ; bản config gốc không bị chỉnh sửa.

**Bằng chứng cần tự mở:** selftest-sha256.txt và selftest-bcrypt.txt; A1–A6; result.json với lệnh đầy đủ; pot của từng lượt. Chạy demo từ thư mục timestamp mới, không dùng pot cũ.

**Ba câu tự kiểm tra:** Vì sao đổi session chưa đủ? Vì sao mask đúng tìm G3 nhưng không tìm G4? Làm sao chứng minh dữ liệu hiện tại là dữ liệu đã đo?

Nguồn và lệnh được kiểm tra ngày 29/10/2026. Nội dung dùng cho Chương 2, kịch bản 1, phụ lục và demo. Linux VM là hạng mục cần nhóm tự triển khai nếu môn yêu cầu bằng chứng máy ảo.
