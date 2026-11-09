# Bộ báo cáo John the Ripper

## Mở các tài liệu chính

- `report/Bao-cao-John-the-Ripper.pdf`: báo cáo đã điền kết quả đo thực, giới hạn tối đa 20 trang.
- `report/Bao-cao.md`: bản nguồn để sửa nội dung, họ tên và thông tin lớp.
- `slides/Thuyet-trinh-John-the-Ripper-v2.pptx`: 12 slide với bảng và biểu đồ có thể chỉnh sửa.
- `slides/Thuyet-trinh-John-the-Ripper.pdf`: bản xem/in slide.
- `demo/Kich-ban-thuyet-trinh.md` và `demo/Demo-1.ps1`: hướng dẫn demo và câu hỏi phản biện.
- `lab/results/all-runs.csv`, `analysis.json`, `verification.json`: dữ liệu kết quả và kiểm tra.

## Phạm vi đã triển khai

Dữ liệu tổng hợp gồm 100 mật khẩu thuộc 5 nhóm, 1.000 từ gốc và 4.000 ứng viên. Đã kiểm tra rules xuất từ John trùng cả tập lẫn thứ tự với candidates.txt. Mỗi cấu hình chính chạy ba lần độc lập, pot riêng. Thực nghiệm xử lý trực tiếp bằng John và Hashcat; số liệu không được mô phỏng bằng script thay thế công cụ.

Các lượt John có ngân sách 60 giây thay vì 300 giây của kế hoạch đầu; Windows native thay cho Linux VM vì môi trường hiện có chưa có nền tảng VM. Mỗi thay đổi và giới hạn đều nêu trong báo cáo. Thời gian thực có thể vượt mốc đặt do hoàn tất batch. Các lượt có tập ứng viên nhỏ kết thúc sớm hơn.

Hashcat được kiểm tra thiết bị thật. Máy không có CPU OpenCL backend; các lần thử CPU thất bại được giữ lại. Lượt GPU Intel, nếu thành công, được tách thành C_G, không dùng để xếp hạng tốc độ phần mềm với John CPU. Đọc báo cáo và log để biết trạng thái chính xác.

## Tái lập kết quả

Python 3 dùng cho runner, chỉ cần thư viện chuẩn. Các gói John/Hashcat Windows portable đã có trong `lab/tools/` kèm tài liệu và giấy phép gốc. Dùng binary đúng checksum nếu muốn nhận diện cùng bản đo.

1. Sao chép lab sang thư mục mới. Lưu giữ `data`, `ground-truth`, `configs` và dữ liệu kết quả gốc.
2. Tạo một thư mục `results` mới trong bản lab sao chép trước khi chạy loạt mới. Runner từ chối ghi đè các lượt đã có. Không trộn pot của hai loạt.
3. Tại thư mục lab sao chép, chạy `python scripts/run_lab.py --phase setup`, rồi `python scripts/run_lab.py --phase formal --budget 60`.
4. Chạy `python scripts/analyze.py` sau khi có đủ lượt chính. Phân tích kiểm tra checksum, cặp hash/mật khẩu trong pot và số lần lặp trước khi tổng hợp.
5. GPU trên máy gốc được kiểm tra riêng bằng `python scripts/run_lab.py --phase gpu --budget 60`. Nhánh này chọn Intel OpenCL device 1 ở máy đã đo; máy khác phải kiểm tra lại danh sách thiết bị.

Để dùng Linux VM, xem `lab/README-Linux-VM.md`. Biến `JTR_BIN` và `HASHCAT_BIN` cho phép đổi đường dẫn executable. Loạt VM là loạt mới, cần kết quả riêng và cập nhật phần môi trường trong báo cáo.

## Dữ liệu và mã nguồn

`data/checksums.json` là căn cứ xác nhận dữ liệu đã khóa. Ground truth chỉ chứa mật khẩu tự tạo cho bài này. Các hash bcrypt có salt riêng và đã được bộ sinh xác minh. Khi cần dữ liệu hoàn toàn mới, cài dependency `bcryptjs` theo `lab/scripts/package.json`, rồi gọi bộ sinh với đường dẫn thư mục lab mới. Bộ sinh từ chối thay dữ liệu đã khóa.

Không chạy lại bộ sinh để tái lập chính bộ dữ liệu báo cáo: các mật khẩu ngẫu nhiên và salt mới sẽ khác. Dùng bản tệp đã lưu cùng checksum để tái lập.

Để cập nhật bài PDF: sửa thông tin trong `report/Bao-cao.template.md`, cài các gói ở `lab/scripts/requirements-report.txt`, rồi chạy `python lab/scripts/build_report.py` trên Windows có phông Times New Roman. Script điền số liệu từ analysis.json và xuất lại Markdown, biểu đồ, PDF. Khi sửa nội dung dài, cần kiểm tra lại tổng số trang và các số trang trong mục lục. Bản `Bao-cao.md` là nội dung cuối đã điền số liệu; template chứa các trường thay thế phục vụ xuất lại.

Mỗi thư mục lượt chứa `terminal.log`, `result.json`, pot nếu có kết quả, trạng thái session và quan sát pot theo thời gian. Các timestamp quan sát tệp không phải thời điểm cracking chính xác. Dữ liệu pilot lưu riêng, không gộp thống kê formal.

## Việc nhóm cần tự hoàn tất

- Điền họ tên/mã học viên TV1–TV3, lớp và thông tin nhóm; xác nhận hạn nộp hiện tại.
- Đọc ba ghi chú `references/TV1…TV3`, chạy lại ít nhất một lượt và xác nhận đóng góp thực tế.
- Dựng Linux VM và thu bằng chứng riêng nếu giảng viên giữ yêu cầu thử nghiệm bằng máy ảo. Gói hiện tại chưa có số đo VM.
- Đọc và sửa bản thảo theo mẫu báo cáo của lớp, diễn tập thuyết trình. Bản này có hỗ trợ Codex, không gán công việc cho các cá nhân khi chưa có xác nhận.

## Giấy phép

John và Hashcat giữ nguyên tệp giấy phép trong thư mục công cụ. Binary được lấy từ trang chính thức, checksum được ghi trong environment. Bản John Windows 1.9.0-jumbo-1 là bản portable cũ; bản phát triển mới có thể cho hành vi/hiệu năng khác. Tài liệu lý thuyết tham chiếu nguồn chính thức, nguồn số liệu thực nghiệm là log đi kèm.
