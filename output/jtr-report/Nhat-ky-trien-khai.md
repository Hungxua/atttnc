# Nhật ký triển khai và bàn giao

Ngày thực hiện 29/10/2026. Người dùng đã yêu cầu triển khai kế hoạch, bộ việc được thực hiện tự động với hỗ trợ Codex. Phân công TV1–TV3 vẫn là đề xuất để nhóm tiếp nhận và xác nhận đóng góp thực tế.

| Hạng mục | Trạng thái và bằng chứng |
|---|---|
| Tìm hiểu tài liệu | Hoàn thành ghi chú cho TV1, TV2, TV3; tham chiếu nguồn chính thức trong bài |
| Cài và kiểm tra John | 1.9.0-jumbo-1 Windows, AVX2, self-test PASS |
| Chuẩn bị dữ liệu | 100 mật khẩu, 5 nhóm, 1.000 từ, 4.000 ứng viên; checksum khóa |
| Kịch bản 1 | A1–A4, mỗi cấu hình 3 lượt; A5/A6 mỗi cấu hình 1 lượt |
| Kịch bản 2 | B1–B3 và D1–D3, mỗi cấu hình 3 lượt |
| Hashcat | 3 thử CPU lỗi backend được giữ; 3 lượt GPU Intel thành công |
| Kiểm tra kết quả | Checksum và mọi cặp hash/mật khẩu trong pot khớp; xem verification.json |
| Báo cáo | 17 trang PDF và bản nguồn Markdown |
| Thuyết trình | 12 slide PPTX, biểu đồ và bảng native; bản xem PDF |
| Demo | Script PowerShell, kịch bản nói và câu hỏi phản biện |
| Máy ảo Linux | Chưa thực hiện; có README-Linux-VM.md để nhóm triển khai theo yêu cầu lớp |
| Thông tin cá nhân | Chờ nhóm điền tên/mã học viên, lớp, xác nhận phân công và hạn nộp |

## Các điều chỉnh trước đo chính thức

- Dùng Windows native thay vì Linux VM vì máy hiện tại chưa có lab Linux.
- Ngân sách chính 60 giây/lượt thay mức dự kiến 300 giây, sau bước pilot. Giữ ngân sách đồng nhất ở cấu hình chính; phần 300 giây có thể chạy lại bằng tham số runner trong loạt mới.
- Không có CPU OpenCL backend cho Hashcat; bổ sung thử GPU Intel và giới hạn kết luận CPU/GPU khác nhau.
- Không vẽ đường thời gian từ thời điểm pot flush vì đó chỉ là thời điểm quan sát tệp. Dùng bảng và biểu đồ kết quả cuối.
- Runtime Windows không có LibreOffice/Word để kiểm tra bố cục DOCX. Bàn giao PDF đã render cùng Markdown chỉnh sửa được, thay vì giao DOCX chưa kiểm tra.

## Kết quả chính

Wordlist 20/100; rules 40/100; mask đúng 20/20 trong G3; incremental 20/100 trong ngân sách 60 giây. Bcrypt cost 10 khôi phục median 1/100 (min–max 1–2); cost 12 là 1/100. Đối chứng một hash có median 114.2 và 28.41 p/s, tỷ số 4.02 lần.

Tổng số lượt formal: 38; 35 lượt có kết quả thực thi hợp lệ và 3 lượt Hashcat CPU lỗi môi trường. Không gộp lỗi backend vào phép đo tốc độ.

## Cách nhóm hoàn tất trước khi nộp

Điền danh tính và lớp; mỗi người đọc ghi chú và tự lặp lại ít nhất một lượt; xác nhận đóng góp; dựng VM nếu giảng viên yêu cầu; cập nhật phiên bản báo cáo nếu dùng số đo mới; diễn tập demo và phản biện. Không coi việc phân công dự kiến là chứng nhận công việc cá nhân đã thực hiện.
