# Ghi chú nghiên cứu TV1

Đây là tài liệu bàn giao để thành viên đọc, kiểm tra và bổ sung; không phải xác nhận cá nhân đã thực hiện nghiên cứu.

**Câu hỏi phụ trách:** mật khẩu được xác minh thế nào; John xử lý hash ra sao; vì sao cách sinh ảnh hưởng độ khó đoán; vì sao metadata có ích với single.

1. Đọc slide 4–5, 41 trong tài liệu học phần. Ràng buộc bài là tối đa 20 trang, có phân công, lab, 1–2 demo, phân tích và so sánh. Entropy lý tưởng yêu cầu mô hình sinh độc lập, đồng đều; không suy trực tiếp từ chuỗi mật khẩu người chọn.
2. Đọc [Openwall documentation](https://www.openwall.com/john/doc/). Ghi sơ đồ nạp dữ liệu, sinh ứng viên, tính, so khớp và lưu pot. Sơ đồ trong báo cáo là tổng hợp chức năng, không khẳng định cấu trúc module mã nguồn.
3. Đọc [cracking modes](https://www.openwall.com/john/doc/MODES.shtml). Đối chiếu single với metadata, wordlist với danh sách ứng viên, incremental với thống kê và giới hạn không gian. Không coi mọi chế độ đều nhận cùng thông tin.
4. Đọc [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html), mục mật khẩu và rate limiting. Phân biệt chính sách trực tuyến với khả năng thử hash ngoại tuyến. Kiểm tra lại các khuyến nghị trong slide cũ trước khi trích.

**Bằng chứng cần tự mở:** ground-truth/passwords.json; manifest.csv; log A6; kết quả A1/A2/A3; tệp checksums. Kiểm tra các mật khẩu G1/G2 xuất phát từ thiết kế có chủ đích, tránh trình bày 40% như tỷ lệ yếu trong thực tế.

**Ba câu tự kiểm tra:** H = L log₂R dùng khi nào? Vì sao single không gộp vào bảng so sánh hash thuần? Vì sao rate limiting không giảm trực tiếp số phép tính hash offline?

Ngày lập ghi chú và kiểm tra nguồn: 29/10/2026. Nội dung dùng cho Mở đầu, Chương 1, Kết luận. Trước nộp: thành viên tự chạy lại, ghi mã lượt xác nhận và sửa bảng đóng góp theo thực tế.
