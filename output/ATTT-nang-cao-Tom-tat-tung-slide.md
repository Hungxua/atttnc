# An toàn thông tin nâng cao: tóm tắt từng slide

Tài liệu học từ 4 bộ slide của GVCC. PGS. TSKH. Hoàng Đăng Hải. Mục tiêu là bao quát phần lớn kiến thức cốt lõi, giúp hiểu bản chất và làm bài; không thể bảo đảm một tỷ lệ hiểu cố định cho mọi người.

**Cách đối chiếu:** dùng số slide in trong tài liệu, không dùng số trang của trình đọc PDF. Mỗi trang PDF có tối đa 2 slide: slide s nằm ở trang PDF ⌈s/2⌉. CĐ1 có 45 slide; CĐ2 có 47; CĐ3 có 40; CĐ4 có 33, tổng cộng **165 slide**.

**Cách đọc:** đọc bản đồ kiến thức → bảng từng slide → phần giải thích sâu của chuyên đề → tài liệu [Bài tập và lời giải](ATTT-nang-cao-Bai-tap-loi-giai.md). Các giải thích và ví dụ bổ sung được viết để làm rõ bài giảng; những lỗi hoặc cách diễn đạt dễ gây nhầm được chỉ rõ.

Thông tin lịch học, hạn nộp, email và lệnh cài đặt xuất hiện trong slide được ghi nhận như nội dung tài liệu, không phải yêu cầu thực hiện của bạn. Tôi không gửi email, cài công cụ hay chạy thử tấn công.

## 1. Bản đồ kiến thức của toàn môn

| Chuyên đề | Câu hỏi trung tâm | Điều cần nắm |
|---|---|---|
| 1. Tổng quan | Bảo vệ cái gì, tại sao và theo nguyên tắc nào? | Chuỗi giá trị thông tin; bảo vệ toàn hệ thống; CIA, xác thực, chống chối bỏ; khả dụng/tin cậy; kiểm soát truy nhập; mật khẩu. |
| 2. Điểm yếu và tấn công | Hệ thống bị phá vỡ bằng cách nào? | Điểm yếu → lỗ hổng → khai thác → hậu quả; tràn bộ đệm; mã độc; nghe lén, giả mạo, DoS, MITM, DNS; các bước tấn công. |
| 3. Bảo vệ | Chọn và kết hợp biện pháp nào? | Mã hóa/giấu tin; phân vùng/DMZ; xác thực; BLP; OTP/MFA/sinh trắc; firewall; IDS/IPS. |
| 4. Nghiên cứu | Thu thập và phân tích bằng chứng như thế nào? | PCAP/log/web → tiền xử lý → đặc trưng → mô hình → phát hiện/cảnh báo → đánh giá. |

Một ví dụ nối cả môn: website bị nghẽn bởi hàng loạt kết nối chưa hoàn tất. Thuộc tính bị ảnh hưởng là **khả dụng** (CĐ1); cơ chế có thể là **SYN flood** (CĐ2); dùng lọc, giới hạn tốc độ, cơ chế chống SYN và giám sát (CĐ3); thu PCAP/log, tính tỷ lệ SYN/lỗi và đánh giá khả năng phát hiện (CĐ4).

## 2. Chuyên đề 1 — Tổng quan và cách tiếp cận

Nguồn: `1-CDE1-T5-2026.pdf`, 23 trang PDF, 45 slide.

### Tóm tắt từng slide

| Slide | Nội dung chính và cách hiểu |
|---:|---|
| 1 | Trang giới thiệu môn và giảng viên. Chưa có kiến thức chuyên môn. |
| 2 | Lịch học và đánh giá: chuyên cần, kiểm tra cá nhân giữa kỳ, tiểu luận nhóm cuối kỳ. Những ngày ghi ở đây là lịch trong tài liệu. |
| 3 | Giữa kỳ gồm 1 câu lý thuyết và 3 bài tập nhỏ. Trả lời lý thuyết cần đúng bản chất, ngắn gọn, có ví dụ. |
| 4 | Tiểu luận nhóm ≤4 người, báo cáo ≤20 trang, có phân công và tham khảo. Cần giới thiệu công cụ, dựng lab, demo, phân tích và so sánh. Slide ghi “4 nội dung” nhưng liệt kê **5 mục**; nên hiểu theo đủ 5 mục. Hạn nộp ghi trong tài liệu: 14/6/2026. |
| 5 | Danh sách 20 công cụ/chủ đề tiểu luận, từ quét mạng đến IDS/SIEM và kiểm tra mật khẩu. Cần hiểu kiến trúc, thử nghiệm và đánh giá, không chỉ chụp giao diện. Bản hướng dẫn tiểu luận nằm trong tài liệu bài tập. |
| 6 | Phạm vi CĐ1: cách tiếp cận, tổng quan, điểm yếu/nguy cơ, bảo vệ và nghiên cứu. Đây là bản đồ của môn. |
| 7 | Ba bước tư duy: nhận biết vấn đề → hình thành ý tưởng → tìm cách giải quyết. Học công cụ phải xuất phát từ một vấn đề cụ thể. |
| 8 | Tri thức và kỹ năng tạo nền cho đổi mới. Vấn đề thực tế thường liên ngành; kết hợp kiến thức có thể tạo cách giải mới. |
| 9 | Chuỗi giá trị từ tín hiệu/số liệu đến dữ liệu, thông tin và tri thức. Ý tưởng xuất phát từ vấn đề thực tiễn, có thể là cải tiến hoặc phát minh; cần kiểm chứng thay vì mặc nhiên cho rằng hệ thống đã hoàn hảo. |
| 10 | Phân biệt các tầng: tín hiệu là sóng/đại lượng vật lý; số liệu là giá trị; dữ liệu là cấu trúc; thông tin có ý nghĩa; tri thức là quan hệ và hiểu biết. Ví dụ số điện thoại chỉ trở thành thông tin khi gắn với một người. |
| 11 | Thông tin đi qua tạo lập, số hóa, tiền xử lý, chuyển tiếp, truyền tải, xử lý và kết xuất. ATTT liên quan mọi công nghệ trong chuỗi, từ cảm biến đến AI và hiển thị. |
| 12 | Bổ sung **lưu trữ** ở nhiều công đoạn: cơ sở dữ liệu, backup, RAID, trung tâm dữ liệu. Thông tin nằm yên cũng phải bảo vệ; RAID và backup có vai trò khác nhau. |
| 13 | Bảo mật cần phủ xuyên suốt đầu cuối, thu thập, liên kết, truyền, lưu, xử lý và điều khiển. Một mắt xích yếu có thể làm hỏng bảo vệ toàn chuỗi. |
| 14 | Kiến trúc edge–fog–cloud: xử lý ở thiết bị/gần thiết bị/trung tâm. Slide nêu mô hình private, public, hybrid và các dịch vụ cloud; cần hiểu trách nhiệm bảo vệ phân bố theo từng nơi. |
| 15 | An ninh tầng vật lý: tín hiệu điện từ, âm thanh, nhiệt hoặc sóng vô tuyến có thể làm lộ dữ liệu; gây nhiễu cũng ảnh hưởng hoạt động. Đây là nguy cơ ngoài lớp phần mềm thông thường. |
| 16 | ARROW được dùng như ví dụ hệ thống đánh chặn/tác chiến điện tử. Ý cần nhớ là liên lạc di động có nguy cơ bị theo dõi ở tầng vô tuyến; không cần ghi nhớ chi tiết thiết bị từ ảnh. |
| 17 | Trạm gốc giả có thể khiến máy di động kết nối tới một điểm không đáng tin. Bài học: phải xem xét xác thực hạ tầng, không chỉ xác thực người dùng. |
| 18 | An ninh chip/chipset: phần tử phần cứng cũng có thể chứa chức năng độc hại. Chuỗi cung ứng và gốc tin cậy của thiết bị là một phần của ATTT. |
| 19 | Nguy cơ ở linh kiện/khối hệ thống: ổ đĩa, điện thoại, USB keylogger, thiết bị IoT. Cổng vật lý và thiết bị ngoại vi là đường vào cần kiểm soát. |
| 20 | Hệ điều hành và công cụ nền tảng có thể có backdoor/trapdoor, kể cả trình biên dịch. Không thể kết luận an toàn chỉ vì ứng dụng bên trên có mật khẩu. |
| 21 | Khởi động là nền của chuỗi tin cậy. Secure Boot kiểm tra thành phần được phép khởi động; TPM có thể hỗ trợ đo lường và bảo vệ khóa; PUF khai thác đặc tính vật lý riêng của chip. Các công nghệ này không đồng nghĩa với nhau. |
| 22 | Khi nhiều hệ thống thông minh kết nối, nguy cơ mở rộng sang liên kết và dữ liệu trao đổi. Cần bảo vệ cả điểm cuối lẫn kênh truyền. |
| 23 | Xe và xe tự hành minh họa hệ thống nhiều bộ điều khiển. Thông tin giả hoặc điều khiển sai có thể ảnh hưởng hành vi vật lý, vì vậy security có thể tác động đến safety. |
| 24 | Haptic kết hợp VR minh họa thông tin gắn với cảm giác/điều khiển. Tính đúng, độ trễ và khả dụng của luồng tương tác đều quan trọng. |
| 25 | Hình robot/cảnh sát robot minh họa xã hội sử dụng hệ thống tự động. Tin trong ảnh là ví dụ của slide, không phải dự báo đã được xác minh ở thời điểm hiện tại. |
| 26 | Hình AI, phương tiện tự hành và hệ thống điều khiển minh họa phạm vi ATTT mở rộng ra thế giới vật lý. Cảm biến, liên lạc và quyết định tự động đều cần bảo vệ. |
| 27 | Phân biệt **safety**: tránh tổn hại/sự cố do lỗi; **security**: chống hành vi trái phép/có chủ đích. Hai mặt giao nhau ở thiết kế, vận hành, vá lỗi và phục hồi. |
| 28 | Thông tin là dữ liệu có ngữ nghĩa; HTTT tích hợp thiết bị, phần mềm, CSDL và mạng. ATTT bảo vệ khỏi truy cập, sử dụng, tiết lộ, sửa đổi hoặc phá hủy trái phép. |
| 29 | **Bí mật — Confidentiality:** chỉ chủ thể được phép được biết thông tin. Bảo vệ dữ liệu cá nhân, tài sản trí tuệ và bí mật tổ chức/quốc gia. Slide dùng “Confidence”; thuật ngữ đúng trong CIA là “Confidentiality”. |
| 30 | **Toàn vẹn — Integrity:** ngăn sửa/xóa/thêm trái phép, duy trì tính đúng của dữ liệu. Ví dụ điểm thi không bị sửa bởi người không có quyền. |
| 31 | **Khả dụng — Availability:** người hợp pháp sử dụng được dịch vụ khi cần. Quan tâm thời gian phục vụ, gián đoạn và phục hồi; không chỉ việc máy đang bật. |
| 32 | **Xác thực:** kiểm tra đúng chủ thể/nguồn tin. **Chống chối bỏ:** có bằng chứng về hành động để khó phủ nhận; không chỉ ghi một tên vào log. |
| 33 | Khả dụng đo bằng tỷ lệ thời gian hoạt động: A = uptime/(uptime+downtime). Mô hình chu kỳ trong slide: A = MTTF/(MTTF+MTTR). Muốn tăng A thì giảm thời gian sửa hoặc tăng thời gian hoạt động trước lỗi. |
| 34 | Tin cậy là xác suất không hỏng trong khoảng thời gian xét: R(t)=1−F(t). Nếu tốc độ lỗi λ không đổi: R(t)=e^(−λt), MTTF=1/λ. Điều kiện λ không đổi rất quan trọng. |
| 35 | **Defense in depth:** nhiều biện pháp bổ trợ nhau, để một lớp bị vượt qua vẫn còn lớp khác. Ví dụ mạng, máy chủ, ứng dụng, dữ liệu và giám sát. |
| 36 | Mô hình củ hành minh họa phân lớp bảo vệ. Mỗi lớp cần nhiệm vụ riêng; nhiều lớp giống hệt nhau có thể cùng thất bại vì một lỗi chung. |
| 37 | Cân bằng chi phí, bảo vệ và khả dụng; không có an toàn tuyệt đối. Bảo vệ trước–trong–sau sự cố. Cách viết “obsecurity” hướng tới phân biệt bảo mật thực chất với chỉ che giấu cách làm. |
| 38 | Kiểm soát truy nhập phải có ở thiết bị, mạng, ứng dụng, dữ liệu và cloud; bảo vệ kênh truyền là phần bổ trợ. Một lần đăng nhập không thay thế mọi kiểm tra quyền phía sau. |
| 39 | Quyền gắn với đối tượng và hành động: máy chủ, file, thư mục, vùng CSDL; đọc/ghi/sửa/chạy/tải/in. Quyền cần đủ cụ thể để hạn chế hành vi ngoài nhu cầu. |
| 40 | Vòng đời quyền: nhận dạng → xác thực → cấp quyền → sử dụng → kiểm tra/thu hồi/điều chỉnh. Các chức năng cùng hỗ trợ CIA; không nên gán máy móc mỗi chức năng chỉ tương ứng một thuộc tính. |
| 41 | Mật khẩu xét chiều dài, tập ký tự và khả năng đoán. Mô hình lý tưởng E=L·log₂R, ví dụ L=14,R=94 cho 91,76 bit. Chỉ đúng cho lựa chọn độc lập, đều; chính sách NIST trong slide cần cập nhật. |
| 42 | Khoảng cách Levenshtein: số phép chèn/xóa/thay tối thiểu để biến một chuỗi thành chuỗi khác. Giá trị thấp nghĩa là hai chuỗi gần nhau; không tự nó đo đầy đủ độ mạnh mật khẩu. |
| 43 | Minh họa ô đầu D(1,1) khi so “kitten” với “sitting”: khác k/s nên chi phí thay bằng 1. Dùng ba ô trước để tính tối ưu. |
| 44 | Tính tiếp D(2,1)=2, D(3,1)=3. Điền bảng từ các tiền tố ngắn đến dài; mỗi ô là một bài toán con. |
| 45 | Bảng đầy đủ cho khoảng cách **3**: kitten → sitten → sittin → sitting. Cần hiểu truy hồi và thao tác, không chỉ nhớ kết quả. |

### Những ý phải hiểu sâu

**CIA và hai thuộc tính bổ sung.** C là “ai được biết?”, I là “ai được thay đổi, dữ liệu có đúng không?”, A là “người hợp pháp có dùng được lúc cần không?”. Xác thực trả lời “có đúng người/nguồn tuyên bố không?”. Chống chối bỏ cần bằng chứng gắn với hành động, ví dụ chữ ký số cùng quy trình bảo vệ khóa và kiểm chứng. Mã hóa có thể giữ bí mật nhưng nếu không kèm cơ chế kiểm tra toàn vẹn/xác thực, nó chưa giải quyết mọi thuộc tính.

**Phân biệt nhận dạng, xác thực và cấp quyền.** Gõ username là nhận dạng; chứng minh sở hữu yếu tố đăng nhập là xác thực; được đọc một file cụ thể là cấp quyền. Người đăng nhập đúng vẫn có thể bị cấm sửa file. IP, MAC hay tên tài khoản là định danh trong một phạm vi, không tự chứng minh ai đang sử dụng chúng.

**Khả dụng khác tin cậy.** Một hệ thống hay lỗi nhưng sửa rất nhanh có thể đạt khả dụng cao. Hệ thống rất ít lỗi nhưng mỗi lần lỗi nằm lâu vẫn có thể có khả dụng thấp. Với thiết bị sửa chữa được, MTBF thường được dùng trong công thức A=MTBF/(MTBF+MTTR); khi làm bài cần giữ đúng định nghĩa thời gian mà đề cho.

**Bảo vệ toàn chuỗi.** Cảm biến thu sai → phân tích dù rất tốt vẫn cho kết luận sai. Đường truyền bị giả mạo → máy xử lý nhận dữ liệu không đúng. Dữ liệu lưu bị lộ → TLS trên đường truyền không cứu được bản đã lưu. Đó là lý do các slide nói ATTT xuyên suốt nhiều tầng và ngành.

**Mật khẩu và entropy.** 94 ký tự là 26 chữ hoa +26 chữ thường +10 chữ số +32 ký hiệu theo tập slide; không bao gồm dấu cách trong cách đếm này. Tăng một ký tự ngẫu nhiên bổ sung log₂94≈6,55 bit. Tuy nhiên mật khẩu có mẫu dễ đoán không đạt entropy lý tưởng, dù đủ các loại ký tự.

**Cập nhật NIST:** SP 800-63B-4 yêu cầu tối thiểu 15 ký tự khi mật khẩu là yếu tố duy nhất; có thể cho phép tối thiểu 8 khi dùng trong MFA. Không yêu cầu đổi định kỳ khi chưa có dấu hiệu lộ lọt, không áp đặt quy tắc bắt buộc pha trộn loại ký tự; cần kiểm tra danh sách mật khẩu phổ biến/bị lộ và giới hạn lần thử. Vì vậy không học dòng “NIST tối thiểu 8 + đổi định kỳ” như một quy tắc hiện hành cho mọi trường hợp. Nguồn: [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html).

## 3. Chuyên đề 2 — Điểm yếu, nguy cơ và cách thức tấn công

Nguồn: `2-CDE2-T5-2026.pdf`, 24 trang PDF, 47 slide.

### Tóm tắt từng slide

| Slide | Nội dung chính và cách hiểu |
|---:|---|
| 1 | Trang giới thiệu chuyên đề về điểm yếu và tấn công. |
| 2 | Năm phần: điểm yếu/lỗ hổng, nguy cơ, phân loại, cách thức và các bước tấn công. |
| 3 | Điểm yếu là lỗi/khiếm khuyết của hệ thống; lỗ hổng là điểm yếu có thể bị khai thác làm vi phạm an ninh. Điểm yếu đã biết nhưng chưa khắc phục vẫn là nguy cơ. |
| 4 | Lỗ hổng bí mật cho phép đọc thông tin ngoài thẩm quyền, ví dụ người dùng thường đọc báo cáo mật. |
| 5 | Lỗ hổng toàn vẹn cho phép thay đổi dữ liệu/quyền trái phép, ví dụ nhân viên tự sửa quyền như admin. |
| 6 | Lỗ hổng khả dụng cho phép làm dịch vụ ngừng hoặc cạn tài nguyên, khiến người hợp pháp không truy cập được. |
| 7 | Nhóm điểm yếu: kiểm tra đầu vào, tràn bộ đệm, kiểm soát truy nhập, xác thực/cấp quyền, con trỏ, giao thức và race condition. Cần liên hệ mỗi lỗi với khả năng bị khai thác. |
| 8 | Tràn bộ đệm là ghi ngoài ranh giới vùng nhớ cấp cho bộ đệm. Có thể gây crash, mất dữ liệu hoặc chiếm quyền; không phải mọi lỗi tràn đều khai thác được. |
| 9 | Stack có tính LIFO; gọi hàm thêm ngữ cảnh/biến và khi trả về khôi phục ngữ cảnh. Mã ví dụ tăng 5 thành 6 minh họa stack frame, địa chỉ trở về và con trỏ. Bố trí thực tế phụ thuộc kiến trúc/ABI. |
| 10 | Mô hình cổ điển: ghi tràn từ buffer làm hỏng dữ liệu điều khiển, đặc biệt địa chỉ trở về. NOP sled tạo vùng đáp rộng hơn, shellcode là mã minh họa, padding lấp khoảng trống. Đây là mô hình học, không áp dụng nguyên xi cho mọi hệ thống hiện đại. |
| 11 | Bài 2-1 tính xác suất mô hình BO, NOP, padding và vị trí RET. Có lỗi 65/64, làm tròn và bố trí stack thiếu nhất quán; lời giải riêng phân biệt đáp số mô hình với địa chỉ thật. |
| 12 | Tổng quan: đánh cắp mật khẩu, tấn công đăng nhập bằng giả mạo/chèn mã, lấy file rồi chuyển ra ngoài. Phải quan tâm cả truy nhập và đường thất thoát dữ liệu. |
| 13 | Link trong email/tin nhắn có thể dẫn tới trang giả hoặc nội dung độc hại. Người dùng tin ngữ cảnh/thông điệp là điểm bị khai thác. |
| 14 | File/ảnh có thể làm phương tiện mang mã độc. Cần phân biệt việc chứa dữ liệu độc hại với việc một chương trình thực sự chạy/khai thác nó. |
| 15 | Hình minh họa giấu/gắn mã trong ảnh. Việc xem ảnh không đương nhiên thực thi mã; thường cần lỗi ở bộ đọc, bước tải tiếp hoặc cơ chế khác. |
| 16 | Word/PDF và file khác có thể là đường phát tán: tính năng chủ động, liên kết hoặc lỗi trình đọc. Bài học là kiểm soát file và ứng dụng mở file. |
| 17 | Keylogger phần cứng/phần mềm ghi lại thao tác bàn phím. Spyware theo dõi; adware liên quan quảng cáo. Mật khẩu mạnh vẫn có thể bị lấy trước khi được mã hóa truyền đi. |
| 18 | Ransomware mã hóa dữ liệu để đòi tiền. Hậu quả chính là mất khả dụng; có thể kèm lấy cắp dữ liệu làm ảnh hưởng bí mật. |
| 19 | Phần mềm giả như antivirus/game/tiện ích dụ người dùng cài và cấp quyền. Cần xác minh nguồn và quyền thực tế. |
| 20 | Thụ động: quan sát/thu thông tin, thường tác động bí mật. Chủ động: gửi, sửa, giả mạo hoặc cản trở dữ liệu/dịch vụ. Tiêu chí là mức can thiệp hoạt động. |
| 21 | Bốn dạng: interruption→khả dụng; interception→bí mật; modification→toàn vẹn; fabrication/masquerade→xác thực. Một cuộc tấn công có thể thuộc nhiều dạng. |
| 22 | Phân loại mã độc theo cần vật chủ và tự lây. Virus thường gắn vật chủ; worm tự lan; Trojan ngụy trang; logic bomb chờ điều kiện. Fileless dùng bộ nhớ/công cụ sẵn có, không có nghĩa là tuyệt đối không để lại dấu vết hay không bao giờ chạm đĩa. |
| 23 | Chuỗi minh họa: xác định mục tiêu → trinh sát → cài cắm/ẩn → khai thác/củng cố → gây tác động. Đây không phải một thứ tự bắt buộc cho mọi cuộc tấn công. |
| 24 | Xác định mục tiêu gồm rà phạm vi hoặc chọn một đối tượng có chủ đích. Góc nhìn phòng thủ: biết tài sản nào hấp dẫn và phải ưu tiên bảo vệ. |
| 25 | Reconnaissance thu thông tin host, mạng, cổng, phiên bản, dịch vụ. Chủ động tương tác trực tiếp; thụ động thu gián tiếp. Các hoạt động scanning/crawling/enumeration có mức tương tác khác nhau. |
| 26 | Nmap minh họa thu thông tin kết nối, cổng, giao thức và miền. Cổng mở cho biết dịch vụ có thể tiếp cận; chưa tự chứng minh có lỗ hổng. |
| 27 | Ảnh Nmap minh họa khảo sát hệ thống. Cần đọc kết quả theo host, trạng thái cổng, dịch vụ và giả thiết xác định phiên bản. |
| 28 | Ảnh tiếp tục minh họa thông tin Nmap. Kết quả nhận dạng là bằng chứng khảo sát cần kiểm chứng, không phải kết luận tuyệt đối. |
| 29 | Sniffing bắt gói mạng. Hub chia sẻ lưu lượng; switch chuyển theo MAC nên không mặc nhiên nhìn thấy mọi gói. ARP spoofing và CAM flooding là hai cơ chế khác nhau, không nên gom thành “switch luôn thành hub”. |
| 30 | Nơi lưu trú: file, rootkit, thiết bị, chip/bo mạch; cơ chế như backdoor, trapdoor, logic bomb và zombie chờ lệnh. Ý chính: khả năng tồn tại lâu và né quan sát. |
| 31 | Che giấu qua mã hóa/đóng gói, ngụy trang và giả phần mềm/website. Sơ đồ bỏ qua kiểm tra khóa minh họa sửa luồng điều khiển; cần hiểu nguy cơ kiểm tra bảo vệ chỉ nằm ở phía dễ sửa. |
| 32 | ARP ánh xạ IP sang MAC trong mạng cục bộ. Phản hồi ARP giả có thể làm thiết bị tin sai ánh xạ, chuyển lưu lượng qua kẻ trung gian. Đây là đầu độc ARP cache, khác việc làm đầy bảng MAC của switch. |
| 33 | SYN flood tạo nhiều kết nối TCP chưa hoàn tất, làm đầy trạng thái hoặc cạn tài nguyên. IP giả có thể làm phản hồi không quay lại bên gửi; không phải mọi SYN flood đều cần giả IP. |
| 34 | TCP bình thường: SYN→SYN-ACK→ACK; SYN flood thiếu bước hoàn tất khiến nhiều trạng thái chờ tồn tại. Cần hiểu tài nguyên bị giữ, không chỉ đếm gói SYN. |
| 35 | Smurf minh họa phản xạ/khuếch đại ICMP: yêu cầu dùng IP nguồn của nạn nhân gửi tới broadcast, nhiều máy phản hồi về nạn nhân. Phụ thuộc cấu hình cho phép cơ chế đó. |
| 36 | DDoS dùng nhiều nguồn, ví dụ botnet dưới điều khiển chung. DoS có thể một nguồn; DDoS phân tán khiến lọc theo một địa chỉ khó hơn. |
| 37 | IP spoofing sửa địa chỉ nguồn trong gói. ACL tin IP có thể bị lợi dụng; giả địa chỉ không tự tạo được phiên TCP hai chiều hay vượt mọi firewall. |
| 38 | MITM chèn vào giữa A và B, giả danh mỗi bên để đọc/sửa trao đổi. Mã hóa vẫn có thể thất bại nếu trao đổi khóa không xác thực đúng đối tác. |
| 39 | DNS giả/đầu độc ánh xạ tên miền có thể đưa người dùng tới máy chủ sai. Phải phân biệt chuyển hướng tên với việc vượt xác thực chứng chỉ của HTTPS. |
| 40 | Sửa file hosts thay ánh xạ tên miền ngay trên máy. Thường cần quyền thay đổi file/cấu hình; tác động tương tự DNS sai từ góc nhìn người dùng. |
| 41 | Web không kiểm tra đầu vào URL có thể xử lý tham số độc hại. Nguyên tắc: dữ liệu bên ngoài không đáng tin; kiểm tra, xử lý đúng ngữ cảnh và kiểm tra quyền phía server. |
| 42 | Bẫy và ngụy trang trong tự nhiên minh họa lừa đối tượng tương tác. Honeypot trong phòng thủ là tài nguyên nhử để quan sát; không nên đồng nhất mọi honeypot với hành vi tấn công. |
| 43 | Camouflage/đa hình: thay biểu hiện hoặc hình thức để khó nhận dạng. Phòng thủ dựa một mẫu cố định có thể bỏ sót biến thể. |
| 44 | Bài 2-2: 50 user×20.000 mật khẩu×0,2s. Tính số lượt và thời gian tuần tự khi thử hết; không nhầm với thời gian trung bình tới lần thành công. |
| 45 | Bài 2-3: 36 ký tự, mật khẩu dài 8, tìm nhị phân từng ký tự. Tối đa 6 request/ký tự, 48 request và 14,4s trong giả thiết oracle nhị phân có sẵn. |
| 46 | Bài 2-4: 10 mẫu trong 50 chữ ký. Tính không va chạm bằng tích, có va chạm bằng biến cố bù; xấp xỉ birthday khác kết quả chính xác. |
| 47 | Bài 2-5: tính tổng lưu lượng botnet bằng N×bytes/gói×8×gói/s. Đổi đơn vị bit/byte và làm tròn số máy lên; đáp án slide làm tròn thiếu. |

### Những ý phải hiểu sâu

**Chuỗi điểm yếu–lỗ hổng–tấn công–rủi ro.** Điểm yếu là khiếm khuyết; lỗ hổng là khiếm khuyết có thể khai thác; mối đe dọa là nguồn/tình huống có thể gây hại; khai thác là cách tận dụng lỗ hổng; tác động là thiệt hại. Rủi ro phụ thuộc khả năng xảy ra và mức tác động, nên không phải mọi lỗi có ưu tiên xử lý giống nhau.

**Tràn bộ đệm.** Một vùng nhớ chỉ được cấp B byte nhưng chương trình ghi quá B byte có thể làm hỏng vùng bên cạnh. Trong ví dụ cổ điển, vùng đó chứa địa chỉ trở về nên việc điều khiển chương trình bị thay đổi. Các cơ chế như kiểm tra biên, canary, bộ nhớ không thực thi và ngẫu nhiên hóa địa chỉ tác động vào những mắt xích khác nhau của cơ chế này. Không có một công thức xác suất chung dự đoán mọi khai thác BO; bài 2-1 là mô hình đơn giản.

**Nghe lén, giả mạo và MITM.** Nghe lén chỉ thu; giả mạo làm bên nhận tin sai danh tính; MITM có thể đồng thời thu và sửa. ARP giả xử lý ánh xạ cục bộ, DNS giả xử lý tên miền, IP spoofing sửa nguồn gói. Các cơ chế này khác nhau về tầng và điều kiện thành công.

**Mã độc không phải một loại duy nhất.** Virus thường cần vật chủ và cơ chế chạy; worm tập trung tự lan; Trojan tạo vẻ hợp pháp; ransomware gây khóa dữ liệu; rootkit che giấu sự hiện diện; bot/zombie chờ điều khiển. Một mẫu mã độc có thể mang nhiều chức năng cùng lúc.

**DoS không chỉ là vượt băng thông.** Có thể cạn bộ nhớ/trạng thái, CPU, luồng xử lý hoặc năng lực ứng dụng khi băng thông chưa đầy. Bài DDoS chỉ xét nút thắt băng thông, còn SYN flood minh họa cạn trạng thái. Khi diễn giải phải nói rõ tài nguyên nào bị quá tải.

**Biện pháp gắn đúng cơ chế:** SQL injection → truy vấn tham số hóa; lỗi quyền → kiểm tra quyền ở server; lấy mật khẩu → MFA và bảo vệ điểm cuối; ransomware → phân quyền, phát hiện và bản sao có thể khôi phục; MITM → xác thực đúng đối tác và bảo vệ kênh; DoS → kiểm soát tải và năng lực xử lý. Đây là giải thích liên hệ với CĐ3, không phải một công cụ duy nhất giải quyết tất cả.

## 4. Chuyên đề 3 — Kỹ thuật, công nghệ bảo vệ

Nguồn: `3-CDE3-T9-2026.pdf`, 20 trang PDF, 40 slide.

### Tóm tắt từng slide

| Slide | Nội dung chính và cách hiểu |
|---:|---|
| 1 | Trang giới thiệu chuyên đề kỹ thuật bảo vệ chống tấn công. |
| 2 | Ba nhóm mở đầu: khái quát công nghệ, che giấu thông tin và vành đai bảo vệ. |
| 3 | Công nghệ chia thành bảo vệ dữ liệu, bảo vệ HTTT và hoạt động chung như giám sát, điều tra, threat hunting, honeypot, quét/vá lỗi. Cần phối hợp phòng ngừa, phát hiện và xử lý. |
| 4 | Tunnel đóng gói luồng trong kênh khác; VPN tạo kết nối riêng theo cơ chế cụ thể; giấu/nhúng tin đặt nội dung trong vật mang. Tunnel không tự đồng nghĩa mã hóa. |
| 5 | Phân biệt giấu kênh, giấu định danh, steganography, embedding, watermark và fingerprint. Watermark phục vụ đánh dấu/quyền sở hữu; fingerprint có thể phân biệt bản phân phối; mã hóa biến dữ liệu sang bản mã. |
| 6 | Mô hình nhúng: vật mang+tin+thuật toán/khóa→vật mang có tin; bộ dò/trích xuất lấy lại nội dung. Có thể mã hóa tin trước khi nhúng, dung lượng file có thể tăng hoặc không. |
| 7 | Đối xứng dùng cùng bí mật cho mã hóa/giải mã. Bất đối xứng dùng cặp khóa công khai–bí mật của từng chủ thể. Cách gọi “mã hóa 3 khóa” trong slide dễ gây nhầm, không phải định nghĩa chuẩn của mật mã công khai. |
| 8 | Hoán vị đổi vị trí bit/ký tự mà giữ các giá trị. Phải biết kích thước khối, quy ước đánh số từ trái/phải và hướng ánh xạ khóa. Khóa minh họa ở slide 8 khác khóa bài slide 9. |
| 9 | Bài đổi chỗ khối 8 ký tự, bản mã `EQAUNBNY--S---O-`. Giải bằng hoán vị ngược cho `BANQUYEN SO` sau xử lý dấu đệm. |
| 10 | Hoán vị cột với khóa MANGIP và bảng 4×6. Slide dùng trực tiếp dãy hạng [4,1,5,2,3,6] làm thứ tự cột; cần giữ quy ước đó để dựng lại câu “HÀ NỘI MÙA NÀY CÓ NHỮNG CƠN MƯA”. Đây khác thứ tự vị trí cột khi sắp chữ khóa theo alphabet. |
| 11 | XOR “Hello World” với khóa KEY lặp: C=M XOR K; giải bằng C XOR K vì XOR hai lần cùng khóa triệt tiêu. Đây là ví dụ đại số, không phải thiết kế mã hóa mạnh để triển khai. |
| 12 | Firewall, bastion host và DMZ tạo vành đai. DMZ chứa dịch vụ công khai, giúp hạn chế đường trực tiếp vào mạng nội bộ. Bastion host là điểm được gia cố. |
| 13 | Sensor và IDS/IPS được ví như hàng rào điện tử: thu dữ liệu, giám sát và cảnh báo/ngăn chặn. Chỉ xây rào mà không quan sát thì khó phát hiện việc rào bị vượt. |
| 14 | Phạm vi bảo vệ gồm phần cứng, OS, ứng dụng, web, CSDL, server, mạng và cloud ở cả hai đầu lẫn trung gian. Quyền ở từng lớp phải nhất quán. |
| 15 | Định danh hệ thống/thiết bị/user/thông tin và xác thực tương ứng. Định danh có phạm vi và có thể giả mạo; cần bằng chứng. Ẩn danh và định danh có thể cùng tồn tại ở các cấp khác nhau. |
| 16 | Tổng quan mô hình: BLP/bí mật, Biba/toàn vẹn, HRU/quyền trong ma trận; lattice/luồng; Clark–Wilson/giao dịch hợp lệ; Chinese Wall/xung đột lợi ích; DAC/MAC/RBAC/rule-based theo cách cấp quyền. Không phải tất cả là biến thể đơn giản của BLP. |
| 17 | Chính sách phân loại chủ thể và đối tượng thành mức an ninh. Ví dụ nhân viên thường không đọc tài liệu mật, tài liệu tối mật không được ghi ra nơi không kiểm soát. |
| 18 | BLP là mô hình bảo vệ **bí mật**, dựa mức nhạy cảm và quyền chủ thể. Các mức “top secret”, “unclassified”, “public” minh họa phân lớp; mức cụ thể phụ thuộc chính sách. |
| 19 | BLP: đọc khi L(S)≥L(O), ghi lên/cùng mức khi L(S)≤L(O). Không đọc lên, không ghi xuống. **Dấu ≥ trong điều kiện ghi của slide là lỗi**; strong-star hạn chế đọc/ghi ở cùng mức. |
| 20 | Bài BLP với S=(3,3,2,1), O=(3,2,2,1). Cùng mức R/W; chủ thể cao hơn chỉ R; thấp hơn chỉ W theo mô hình giản lược. S3 với O5 mức3: chỉ W; O6 mức1: chỉ R. |
| 21 | OTP dùng một lần, chuyển qua kênh/thiết bị hoặc sinh trên thiết bị. Mục đích là giảm dùng lại mật khẩu lấy được. Không nên hiểu mọi OTP đều sinh ngẫu nhiên độc lập; có loại dựa bộ đếm/thời gian và bí mật chung. |
| 22 | Minh họa OTP: người dùng nhận/sinh mã, gửi để hệ thống kiểm tra và tiêu thụ mã. Tính một lần và hạn hiệu lực cần được thực thi phía xác minh. |
| 23 | 2FA minh họa password+OTP. Phải là hai nhóm yếu tố độc lập, không chỉ hai câu hỏi cùng thuộc “điều bạn biết”. |
| 24 | MFA kết hợp điều biết, điều sở hữu và đặc điểm sinh trắc. Cần tính cả khâu đăng ký, phục hồi và thay thiết bị; nhiều bước không tự bảo đảm nhiều yếu tố. |
| 25 | Sinh trắc dùng vân tay, mống mắt, mặt, giọng… Có sai số, nhiễu và chi phí; “gắn với chủ thể” không đồng nghĩa không thể giả mạo. |
| 26 | Minutiae vân tay: điểm kết thúc, rẽ nhánh, hồ, đoạn độc lập, đảo, móc, giao cắt. Nhận dạng dựa cấu trúc/quan hệ, không chỉ số lượng điểm. |
| 27 | So khớp cần trích đặc trưng, căn chỉnh vị trí/hướng và so độ tương đồng. Hai ảnh cùng người có thể khác do góc, lực ép và chất lượng. |
| 28 | Phân loại Henry: arch, loop, whorl; dùng hệ số có trọng số ngón để thu hẹp tìm kiếm. Ví dụ Rr và Li có whorl cho C=9/3=3. C giống nhau chưa chứng minh cùng người. |
| 29 | Gatekeeper là thành phần kiểm soát tiếp cận tài nguyên/tính năng. “Chỉ admin” là trường hợp trong slide; bản chất là thực thi chính sách quyền, không bắt buộc mọi đối tượng chỉ admin được dùng. |
| 30 | Filter chọn cho qua/chặn theo tiêu chí IP, dịch vụ, giao thức… Quy tắc phải phân biệt lưu lượng hợp pháp với trái phép. |
| 31 | Firewall kiểm soát lưu lượng qua ranh giới tin cậy, hạn chế dịch vụ và hỗ trợ log/giám sát. Firewall biên không quan sát được lưu lượng nội bộ không qua nó; firewall nội bộ/host có thể kiểm soát các luồng đó. NAT không tự là bảo mật toàn diện. |
| 32 | Bốn nhóm: packet filter đọc tiêu đề; stateful theo trạng thái phiên; circuit-level proxy theo kết nối; application-level hiểu giao thức/nội dung ứng dụng. Kiểm tra sâu thường tăng chi phí, mức cụ thể phụ thuộc triển khai. |
| 33 | Hai chính sách mặc định: deny trừ khi cho phép, hoặc allow trừ khi cấm. Bảng SMTP minh họa luật IP/cổng/chiều/ACK; cờ ACK đơn lẻ không chứng minh phiên đã được xác thực. |
| 34 | Luật theo giao diện, nguồn/đích, giao thức, cổng và nội dung. Cần đúng thứ tự, chiều và hành động; bảng trên slide không đủ mọi hành động để tự suy ra một cấu hình hoàn chỉnh. NetFlow mô tả thông tin luồng, không tự là cơ chế chặn. |
| 35 | NIDS/NIDPS phân tích gói/lưu lượng mạng qua sensor. IDS có thể nghe thụ động; IPS muốn chặn thường phải có vị trí inline hoặc cơ chế thực thi phản ứng. |
| 36 | HIDS dùng agent trên máy, quan sát tiến trình và log; agent gửi về trung tâm. Nó nhìn hoạt động máy mà giám sát mạng có thể không thấy, nhưng cần bảo vệ agent. |
| 37 | Phát hiện theo chữ ký dùng mẫu đã biết; bất thường dùng baseline/thống kê/ML; mạng neuron/học sâu học đặc trưng. Có đánh đổi bỏ sót/cảnh báo nhầm và thay đổi hành vi theo thời gian. |
| 38 | BT1 firewall: hợp hai sự kiện bị chặn, trừ giao để tránh đếm đôi. P=20%+10%−5%=25%. |
| 39 | BT2 công suất 50.000 gói/s: cao điểm mất 28,57%; tỷ lệ trên toàn bộ gói là 12,24%, còn trung bình tỷ lệ theo thời gian là 8,57%. Đáp số 10% trong slide sai. |
| 40 | BT3 giữ tối đa 10.000 luồng, mỗi luồng 30s, đến 500/s: nhu cầu 15.000 luồng nên quá tải; mô hình ổn định giản lược loại 33,33%. |

### Những ý phải hiểu sâu

**Mã hóa, giấu tin và watermark khác mục đích.** Mã hóa che nội dung; người quan sát vẫn có thể biết có bản mã. Giấu tin cố che sự tồn tại của thông điệp. Watermark đánh dấu nguồn/quyền sở hữu, có thể nổi hoặc chìm. Có thể phối hợp: mã hóa thông điệp trước rồi nhúng vào ảnh. Chúng không mặc nhiên thay thế xác thực và kiểm soát quyền.

**Mật mã đối xứng và công khai.** Đối xứng hiệu quả cho dữ liệu nhưng cần chia sẻ bí mật đúng cách. Với mã hóa công khai, A gửi bí mật cho B thì dùng public key của B, B dùng private key tương ứng. Với chữ ký, người ký dùng private key, người kiểm tra dùng public key. Phải xác thực khóa công khai thuộc đúng chủ thể; nếu không vẫn có thể bị MITM. “Một khóa công khai chung + hai khóa riêng” không phải mô tả tổng quát đúng của hệ này.

**BLP dễ nhớ bằng luồng bí mật.** Chủ thể mức thấp không được đọc bí mật cao; chủ thể mức cao không được ghi dữ liệu xuống thấp vì có thể làm rò rỉ. Do đó **đọc xuống, ghi lên**. Cùng mức có thể đọc và ghi nếu các quyền khác cũng cho phép. Quy tắc mức là điều kiện chính sách, không tự cấp mọi quyền thực tế. Tham khảo nghiên cứu về luồng thông tin và BLP: [Access Control Encryption](https://arxiv.org/abs/1602.03642).

**BLP và Biba:** BLP giữ bí mật; Biba dạng nghiêm ngặt giữ toàn vẹn, thường mô tả “không đọc xuống, không ghi lên” để tránh dữ liệu ít tin cậy làm bẩn mức tin cậy cao. RBAC gắn quyền với vai trò công việc; DAC để chủ sở hữu có quyền quyết định trong chính sách; MAC thực thi nhãn/chính sách bắt buộc. Các mục tiêu này có thể kết hợp.

**OTP và MFA.** OTP dùng một lần giúp chống replay sau khi mã đã dùng/hết hạn, nhưng kẻ trung gian có thể lừa lấy mã rồi sử dụng ngay. Password và PIN đều thuộc nhóm điều biết; không thành 2FA chỉ vì nhập hai bí mật. Sinh trắc cần bảo vệ mẫu và xem xét sai nhận/sai từ chối.

**Firewall, IDS và IPS.** Firewall trả lời “luồng nào được qua theo luật?”. IDS trả lời “có dấu hiệu đáng nghi để cảnh báo không?”. IPS có thể chủ động chặn. IDS thấy bất thường chưa chứng minh có tấn công; IPS chặn sai có thể làm giảm khả dụng. Ghép log mạng, host và ứng dụng giúp có bối cảnh hơn.

**DMZ và phân vùng.** Máy web công khai nằm ở vùng riêng; truy cập tới CSDL nội bộ chỉ mở đúng luồng cần thiết. Nếu máy web bị chiếm, phân vùng giúp giảm khả năng lan tiếp. Cần luật giữa Internet–DMZ, DMZ–nội bộ và chiều đi ra, không chỉ một đường vào.

## 5. Chuyên đề 4 — Hướng nghiên cứu, thu thập và phát hiện

Nguồn: `4-CDE4-T9-2026.pdf`, 17 trang PDF, 33 slide. **Không có slide ghi bài tập riêng**; có ví dụ/thuật toán minh họa.

### Tóm tắt từng slide

| Slide | Nội dung chính và cách hiểu |
|---:|---|
| 1 | Trang giới thiệu hướng nghiên cứu trong ATTT. |
| 2 | Ba phần: phân tích hệ thống, thu thông tin, xử lý/phân tích/phát hiện. |
| 3 | Hệ thống có đầu vào, xử lý, đầu ra, nhiễu và phản hồi. Nhiễu có thể tự nhiên hoặc có chủ đích; đầu vào giả có thể làm đầu ra sai. |
| 4 | Cả nghiên cứu tấn công và phòng thủ đều có pipeline dữ liệu→lọc/phân lớp/phân cụm/tương quan→kết quả. Đầu ra phòng thủ là dấu hiệu, mẫu, lỗ hổng và cảnh báo; cần định nghĩa mục tiêu trước khi chọn thuật toán. |
| 5 | Ba nguồn dữ liệu: giao diện mạng, file/log hệ thống, lớp ứng dụng. Mỗi nguồn nhìn một mặt nên có thể bổ sung nhau. |
| 6 | Bắt gói qua driver/thư viện PCAP, đi từ NIC/kernel tới ứng dụng và file `.pcap`. Slide dùng tên WinPcap theo minh họa; cần hiểu vị trí tầng và cấu trúc dữ liệu, không coi đây là yêu cầu cài đặt hiện hành. |
| 7 | Wireshark phân tích gói đã thu hoặc đang thu; giải mã các trường của Ethernet/IP/TCP/UDP/ứng dụng khi có dữ liệu phù hợp. |
| 8 | Giao diện Wireshark minh họa danh sách gói, cấu trúc tầng và dữ liệu byte. Cần đọc thời gian, nguồn/đích, giao thức rồi mở chi tiết để kiểm chứng. |
| 9 | DPI kiểm tra sâu hơn header, có thể tới nội dung ứng dụng; shallow inspection chỉ xét các tầng thấp hơn. Payload mã hóa giới hạn điều có thể thấy nếu không có cơ chế giải mã hợp lệ. |
| 10 | Filebeat đọc/thu log qua các harvester, gom dữ liệu rồi chuyển tới hệ thống nhận. Hình thể hiện các đích như Elasticsearch/Logstash/Kafka/Redis trong kiến trúc minh họa. |
| 11 | Pipeline: Beats/Syslog/ứng dụng→Logstash tiền xử lý→Elasticsearch lập chỉ mục/lưu→Kibana trực quan. Phân biệt thu dữ liệu, biến đổi, lưu/tìm và hiển thị. |
| 12 | Scraping trích nội dung từ trang; crawling duyệt theo URL/link; spider trong framework định nghĩa phạm vi và logic phân tích. Chúng có thể phối hợp, không phải ba thứ loại trừ nhau. |
| 13 | Scrapy: tổ chức dự án và spider; trang HTML có thể xem như cây để chọn dữ liệu. Lệnh cài/tạo dự án trong slide là ví dụ hướng dẫn, không được thực hiện trong yêu cầu này. |
| 14 | Luồng Scrapy: spider tạo request→engine→scheduler→downloader→response→spider→item pipeline. Engine điều phối; pipeline làm sạch/kiểm tra/lưu item. |
| 15 | Ví dụ spider sinh URL theo ngày, chọn dữ liệu bằng XPath, đưa vào item. Đoạn mã là minh họa, không hoàn chỉnh để chạy ngay; vòng ngày cần tránh bỏ sót ngày cuối và xử lý lỗi. |
| 16 | Các kỹ thuật: fusion, fuzzing, classification, clustering, similarity, đặc trưng và PCA. Chúng phục vụ các nhiệm vụ khác nhau, không phải bước bắt buộc theo một thứ tự cố định. |
| 17 | Data fusion hợp nguồn ở giai đoạn sớm, sau trích đặc trưng hoặc ở mức quyết định. Ví dụ kết hợp PCAP, log đăng nhập và thông tin host để cảnh báo có bối cảnh hơn. |
| 18 | Fuzzing tạo đầu vào biến đổi/bất thường để phát hiện lỗi. Black/grey/white-box khác mức biết nội bộ/feedback. “Fuzzying” trong tiêu đề là cách viết sai; hình nói về **fuzzing**, không phải logic mờ. |
| 19 | Classification dùng dữ liệu có nhãn để học quy tắc gán nhãn cho dữ liệu mới. Ví dụ phân “normal/attack”. Làm sạch và tách tập huấn luyện/đánh giá là cần thiết. |
| 20 | Clustering gom đối tượng tương tự mà không cần nhãn lớp có sẵn. Cụm lạ có thể đáng khảo sát nhưng chưa tự chứng minh độc hại. |
| 21 | Phân cụm phân cấp có gộp dần/tách dần; không phân cấp có K-means, mô hình xác suất và bản đồ tự tổ chức. Chọn theo dạng dữ liệu và mục tiêu. |
| 22 | K-means: chọn k, khởi tạo tâm, gán mỗi điểm vào tâm gần nhất, cập nhật tâm bằng trung bình, lặp tới hội tụ. Cần thang đo phù hợp. |
| 23 | Hình hai khởi tạo minh họa kết quả/SSE khác nhau. K-means nhạy với tâm đầu và có thể rơi vào nghiệm cục bộ; hội tụ không bảo đảm tối ưu toàn cục. |
| 24 | Similarity cao nghĩa gần nhau; dissimilarity thấp nghĩa gần nhau. Proximity gọi chung sự gần. Dùng trong nearest neighbor, phân loại, phân cụm và tương quan. |
| 25 | Bảng các độ đo: Minkowski, Euclidean, Manhattan, maximum, Pearson, Mahalanobis, cosine và chord. Chọn độ đo theo ý nghĩa dữ liệu; chuẩn hóa khi các chiều khác đơn vị. |
| 26 | Trích đặc trưng mạng: duration, service, src/dst bytes, count, tỷ lệ cùng dịch vụ/lỗi SYN, nhóm đặc trưng theo host và cổng đích. Chuyển gói/log thô thành vector số có ý nghĩa cho phát hiện. |
| 27 | PCA đổi từ N chiều sang k<N chiều qua các trục trực giao giữ nhiều phương sai. Ví dụ 2 chiều tương quan mạnh, PC1 giữ 99,4% phương sai nên có thể giảm còn 1 chiều. |
| 28 | Đồ thị phương sai theo thành phần giúp chọn số chiều; hình minh họa PCA và khoảng cách. Giữ nhiều phương sai không luôn giữ mọi tín hiệu tấn công. |
| 29 | Phân tích mã độc theo chữ ký/bất thường/đặc tả, và theo tĩnh/động/lai. Tĩnh xem cấu trúc/code không chạy mẫu; động quan sát hành vi khi chạy trong môi trường kiểm soát; lai phối hợp. |
| 30 | Chữ ký so mẫu với kho đã biết; bất thường so quan sát với baseline rồi ngưỡng. Chữ ký dễ bỏ biến thể mới; bất thường dễ nhầm thay đổi hợp pháp. |
| 31 | Phát hiện bằng PCA: chuẩn hóa quan sát theo profile huấn luyện→chiếu→tính độ lệch/khoảng cách→so ngưỡng→cảnh báo. Phải giữ cùng phép biến đổi cho dữ liệu mới. |
| 32 | Pattern matching so quan sát với mẫu. Ma trận TP/FP/FN/TN và các tỷ lệ dùng để đánh giá; mẫu trông giống hay accuracy cao chưa đủ nói hệ thống tốt. |
| 33 | Mô hình lan mã độc logistic dA/dt=αA(1−A): A là tỷ lệ nhiễm, 1−A còn có thể nhiễm. Lây chậm lúc đầu, nhanh ở giữa, chậm khi gần bão hòa; mô hình không có phục hồi nên không mô tả mọi dịch thực tế. |

### Những ý phải hiểu sâu

**Pipeline nghiên cứu:** xác định câu hỏi → chọn nguồn dữ liệu → làm sạch/chuẩn hóa → trích đặc trưng → xây/hiệu chỉnh mô hình → kiểm tra trên dữ liệu chưa dùng → giải thích kết quả và giới hạn. Ví dụ “phát hiện SYN flood” cần nhãn hoặc tiêu chí kiểm chứng, cửa sổ thời gian, tỷ lệ SYN/kết nối hoàn tất, và đo cả cảnh báo nhầm.

**Classification và clustering.** Classification biết trước lớp đích từ nhãn; clustering tìm cấu trúc nhóm. Một thuật toán phân cụm không tự biết cụm nào “tấn công”. Cần phân tích bối cảnh hoặc dữ liệu kiểm chứng để gán ý nghĩa.

**K-means.** Tối thiểu hóa tổng bình phương khoảng cách trong cụm: SSE=Σᵢ‖xᵢ−μ[cᵢ]‖². Khoảng cách bị chi phối nếu một chiều là byte hàng triệu còn chiều khác là tỷ lệ 0–1; vì vậy thang đo cần được xem xét. K-means phù hợp hơn với cụm có hình dạng tương đối gọn theo khoảng cách đã chọn và có thể bị ngoại lệ kéo tâm.

**Các độ đo cần nhận ra:** Euclidean=√Σ(xᵢ−yᵢ)²; Manhattan=Σ|xᵢ−yᵢ|; maximum=max|xᵢ−yᵢ|; Minkowski bậc p=(Σ|xᵢ−yᵢ|ᵖ)^(1/p). Cosine=(x·y)/(‖x‖‖y‖) so hướng vector, không phải độ lớn; không xác định với vector 0. Pearson so biến thiên quanh trung bình. Mahalanobis xét cả thang đo và tương quan qua ma trận hiệp phương sai: √((x−y)ᵀΣ⁻¹(x−y)); thiếu căn là dạng bình phương khoảng cách. Chord trên vector chuẩn hóa liên hệ cosine: √(2−2cosθ). Không có một độ đo tốt nhất cho mọi dữ liệu.

**PCA theo từng bước:** lấy trung bình/chuẩn hóa phù hợp → tính hiệp phương sai → tìm vector/trị riêng → chọn các trục có trị riêng lớn → chiếu dữ liệu. Với dữ liệu mới, dùng trung bình, độ lệch chuẩn và trục đã học; không học lại riêng từng điểm. Bất thường có thể biểu hiện bằng khoảng cách trong không gian PCA hoặc sai số tái dựng ngoài các trục giữ lại. Cần chọn ngưỡng bằng dữ liệu kiểm chứng.

**Ma trận nhầm lẫn:** TP=tấn công được báo đúng; FP=bình thường bị báo tấn công; FN=tấn công bị bỏ sót; TN=bình thường được nhận đúng. Recall=TP/(TP+FN); specificity=TN/(TN+FP); FPR=FP/(FP+TN); FNR=FN/(FN+TP); accuracy=(TP+TN)/tổng. Bổ sung precision=TP/(TP+FP), giúp biết bao nhiêu cảnh báo thật sự đúng. Nếu chỉ 1% mẫu là tấn công, mô hình luôn báo bình thường đạt 99% accuracy nhưng bỏ sót tất cả tấn công.

**Lan truyền mã độc.** Khi A nhỏ, A(1−A)≈A nên tăng gần hàm mũ; khi A≈0,5 tốc độ lớn nhất; khi A→1 tốc độ giảm. Nghiệm logistic với A(0)=A₀ là A(t)=1/[1+((1−A₀)/A₀)e^(−αt)]. Vá/cách ly giảm số máy dễ nhiễm hoặc cơ hội tiếp xúc; để mô tả phục hồi cần mở rộng mô hình.

## 6. Các điểm cần sửa hoặc đọc thận trọng

| Vị trí | Điểm trong slide | Cách học đúng |
|---|---|---|
| CĐ1, 29–32 | “Confidence”, “Non-repudation” | Dùng Confidentiality và Non-repudiation. |
| CĐ1, 41 | NIST 8 ký tự/đổi định kỳ như quy tắc chung | Đối chiếu bản hiện hành; tách mô hình tính entropy khỏi chính sách xác thực. |
| CĐ1, 41–45 | Entropy/Levenshtein được dùng để nói độ mạnh | Entropy lý tưởng cần giả thiết ngẫu nhiên; khoảng cách chuỗi chỉ đo mức khác nhau. |
| CĐ2, 11 | Sh=64 nhưng tính 65; RET/SP 4B thiếu giải thích | P₁=64/4096; bố trí frame/địa chỉ tuyệt đối chưa được cho đủ. |
| CĐ2, 29/32 | Tràn ARP và tràn CAM dễ bị gộp | ARP cache ánh xạ IP–MAC; CAM/FDB của switch ánh xạ MAC–port. |
| CĐ2, 46 | Birthday cho 0,41/0,59 | Đó là xấp xỉ; chính xác 0,38170668/0,61829332. |
| CĐ2, 47 | Số máy làm tròn xuống | Làm tròn lên: 19.532 và 195.313 khi R=100 gói/s. |
| CĐ3, 7 | Bất đối xứng được gọi “3 khóa” | Mỗi chủ thể có cặp public/private; không dùng một public key chung cho mọi người. |
| CĐ3, 10 | Hạng chữ khóa được dùng trực tiếp làm thứ tự cột | Phân biệt dãy hạng [4,1,5,2,3,6] với thứ tự vị trí theo alphabet [2,4,5,1,3,6]; giải theo quy ước slide để khớp bản mã. |
| CĐ3, 19 | Điều kiện ghi ghi ≥ | Đúng là L(S)≤L(O) cho “không ghi xuống”. |
| CĐ3, 21 | OTP tuyệt đối tránh replay | Giảm dùng lại khi xử lý đúng, vẫn có thể bị lấy và dùng thời gian thực. |
| CĐ3, 31 | Firewall “không chặn từ trong” | Phụ thuộc vị trí/luật; chỉ không kiểm soát luồng không đi qua nó. |
| CĐ3, 39 | Tỷ lệ mất gói trung bình 10% | 12,24% theo tổng gói; 8,57% theo trung bình tỷ lệ theo thời gian. |
| CĐ4, 18 | “Fuzzying” | Hình minh họa fuzzing, không phải fuzzy logic. |
| CĐ4, 25 | Một số cách viết độ đo rút gọn | Phân biệt distance/squared distance và ý nghĩa similarity/dissimilarity. |

## 7. Tự kiểm tra trước khi ôn thi

Bạn đã nắm phần chính nếu giải thích được các câu sau bằng lời của mình và có ví dụ:

1. Một website bị đọc trộm dữ liệu, sửa điểm và nghẽn truy cập vi phạm những thuộc tính nào?
2. Nhận dạng khác xác thực/cấp quyền thế nào? Vì sao đăng nhập đúng chưa đủ quyền sửa file?
3. Điểm yếu khác lỗ hổng, nguy cơ và tác động ra sao?
4. Vì sao mã hóa không có xác thực đối tác vẫn có thể bị MITM?
5. Tràn buffer tác động địa chỉ trở về bằng cách nào trong mô hình cổ điển?
6. ARP spoofing, DNS giả và IP spoofing khác nhau ở đâu?
7. Virus, worm, Trojan, ransomware và rootkit khác chức năng gì?
8. BLP đọc/ghi thế nào và vì sao cấm ghi xuống?
9. Firewall, IDS, IPS và DMZ mỗi thứ làm gì?
10. Signature và anomaly đánh đổi bỏ sót/cảnh báo nhầm ra sao?
11. Classification, clustering, K-means và PCA khác mục tiêu gì?
12. Vì sao accuracy cao chưa đủ? Bạn tính được FP/FN/precision/recall không?

Khi làm bài số, luôn ghi **giả thiết → công thức → thay số → đơn vị → kết luận**, và phân biệt số tối đa, trung bình, tỷ lệ theo thời gian với tỷ lệ trên toàn bộ gói.
