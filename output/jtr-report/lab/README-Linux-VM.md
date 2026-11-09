# Tái lập trong máy ảo Linux

Đây là hướng dẫn triển khai tiếp theo cho nhóm. Số liệu trong báo cáo được đo trên Windows, chưa phải số đo từ VM.

1. Tạo VM Ubuntu LTS hoặc Kali Linux bằng hypervisor của nhóm, cấu hình khởi điểm 4 vCPU, 8 GB RAM, 25 GB đĩa. Ghi phiên bản OS/hypervisor và chụp snapshot sau cài. Không ghép số đo VM với số đo Windows vào cùng một phép so sánh tốc độ.
2. Cài dependency build theo `doc/INSTALL-UBUNTU` của đúng commit John. Tham khảo: https://github.com/openwall/john/blob/bleeding-jumbo/doc/INSTALL-UBUNTU
3. Lấy nguồn chính thức, ghi commit rồi build Jumbo:

```bash
git clone https://github.com/openwall/john.git
cd john/src
git rev-parse HEAD
./configure
make -s -j4
../run/john --list=build-info
../run/john --test=0 --format=raw-sha256
../run/john --test=0 --format=bcrypt
```

4. Sao chép lab và dùng nguyên `data`, `ground-truth`, `configs/lab-rules.conf` đã bàn giao. Giữ kết quả Windows trong một bản lưu riêng. Tạo lab mới với `results/` trống cho loạt VM. Không chạy bộ sinh dữ liệu để thay các tệp này.
5. Khai báo đường dẫn binary:

```bash
export JTR_BIN=/duong-dan-tuyet-doi/john/run/john
export HASHCAT_BIN=/usr/bin/hashcat
export OMP_NUM_THREADS=4
python3 scripts/run_lab.py --phase setup
```

6. Với Hashcat, kiểm tra `hashcat -I`. CPU cần OpenCL CPU runtime phù hợp, chẳng hạn PoCL trên distro hỗ trợ. GPU trong VM cần passthrough thực sự; không coi card hiển thị ảo là thiết bị tính khả dụng. Cài Hashcat theo nguồn chính thức và package của distro, lưu version/backend.
7. Chạy loạt đo với ngân sách 60 giây để đối chiếu phương pháp; có thể nâng lên 300 giây như kế hoạch ban đầu, nhưng phải chạy lại toàn bộ cấu hình chính cùng ngân sách. Lưu checksum, cấu hình và phiên bản cho loạt mới.

```bash
python3 scripts/run_lab.py --phase formal --budget 60
```

Runner mặc định thử Hashcat trên CPU. Nếu dùng GPU, cấu hình và lựa chọn device phải được kiểm tra trên máy mới; nhánh GPU trong runner hiện chọn device 1 theo môi trường Windows đã đo. Không sao chép số device sang môi trường khác khi chưa đọc `hashcat -I`.

**Nghiệm thu VM:** tự kiểm tra PASS; checksum dữ liệu khớp; mỗi lượt pot mới; log nêu đúng số hash/salt/cost; kết quả khớp ground truth; ghi lại sai khác so với Windows. Đây là bước nhóm cần hoàn tất nếu giảng viên yêu cầu bằng chứng máy ảo.
