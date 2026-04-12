# 🧠 Module 5: AI Agents & Tự động hóa quy trình
## 🔄 5E Learning Sequence: Thiết kế luồng logic cho một Agent

---

## 📋 BÀI HỌC HOÀN CHỈNH

### 🎯 Mục tiêu học tập (Learning Objectives)
- Xây dựng được một AI Agent đơn giản theo mô hình V-N-N.
- Thiết kế luồng logic đa bước (multi-step agent loop) để thực hiện một nhiệm vụ cụ thể.
- Áp dụng kiến thức về điều khiển đầu ra (CREATE framework) để tinh chỉnh hành vi của Agent.
- Đánh giá hiệu quả và tối ưu hóa luồng logic của Agent.

---

## 🧩 1. Lesson Plan (5E Learning Sequence)

### 🧪 **1. Engagement (Khơi gợi hứng thú)**  
**Thời lượng**: 15 phút  
**Mục tiêu**: Tạo động lực và kích thích tư duy về AI Agent.

**Hoạt động**:
- **Trò chơi tương tác**: "Agent nào thông minh hơn?" – Học sinh so sánh hành vi của hai AI Agent trong một nhiệm vụ đơn giản (ví dụ: tìm đường, giải bài toán).
- **Câu hỏi mở đầu**: "Bạn có thể tưởng tượng một trợ lý AI nào có thể giúp bạn học tập hiệu quả hơn không?"
- **Video minh họa**: Giới thiệu các ứng dụng thực tế của AI Agents trong học tập (chatbot hỗ trợ học tập, hệ thống gợi ý nội dung, công cụ tự động hóa bài tập).

**Kết quả mong đợi**:
- Học sinh nêu được một số ứng dụng tiềm năng của AI Agent trong học tập và cuộc sống.

### 📚 **2. Exploration (Khám phá)**  
**Thời lượng**: 25 phút  
**Mục tiêu**: Khám phá cơ bản về AI Agent và cách thiết kế luồng logic.

**Hoạt động**:
- **Bài tập nhóm**: Sử dụng mô hình V-N-N để thiết kế một Agent đơn giản (ví dụ: Agent nhắc nhở học tập).
    - V: Vai trò (Agent nhắc nhở)
    - N: Nhiệm vụ (Gợi ý học sinh học đúng giờ)
    - N: Ngữ cảnh (Sáng thứ 2, học sinh cần ôn tập Toán)
- **Hướng dẫn**: Sử dụng CREATE framework để tinh chỉnh đầu ra (Character: học sinh, Request: nhắc nhở, Examples: lịch học, Adjustment: giọng điệu thân thiện, Type: nhắc nhở, Extra info: thời gian cụ thể)
- **Thảo luận nhóm**: So sánh các thiết kế khác nhau và nhận diện điểm mạnh/yếu.

**Kết quả mong đợi**:
- Học sinh thiết kế được một Agent đơn giản với luồng logic đầu tiên.

### 🧠 **3. Explanation (Giải thích)**  
**Thời lượng**: 20 phút  
**Mục tiêu**: Cung cấp kiến thức khái quát về AI Agent và cách thiết kế luồng logic đa bước.

**Hoạt động**:
- **Bài giảng ngắn**:
    - Khái niệm AI Agent: Hệ thống trí tuệ nhân tạo có thể nhận đầu vào, xử lý thông tin và thực hiện hành động để đạt được mục tiêu cụ thể.
    - Mô hình V-N-N và cách mở rộng thành luồng logic đa bước (multi-step agent loop).
    - Ví dụ minh họa: Agent hỗ trợ học sinh tự động hóa việc lập kế hoạch học tập.
- **Minh họa trực quan**: Flowchart của một Agent đa bước (V-N-N → nhận đầu vào → xử lý → ra đầu ra → phản hồi → cập nhật → tiếp tục).
- **Giới thiệu các thành phần chính của AI Agent**: Lập kế hoạch, sử dụng công cụ, bộ nhớ, lô-gic phản ứng (ReAct).

**Kết quả mong đợi**:
- Học sinh hiểu được cấu trúc và cách vận hành của một AI Agent đa bước.

### 🛠️ **4. Elaboration (Mở rộng)**  
**Thời lượng**: 30 phút  
**Mục tiêu**: Áp dụng kiến thức vào thiết kế một Agent phức tạp hơn.

**Hoạt động**:
- **Bài tập nhóm**: Thiết kế một Agent đa bước (ví dụ: Agent hỗ trợ ôn tập Toán theo lịch cá nhân).
    - Bước 1: Agent xác định thời gian học.
    - Bước 2: Agent gợi ý chủ đề học.
    - Bước 3: Agent tạo câu hỏi.
    - Bước 4: Agent đánh giá và gợi ý cải thiện.
- **Hỗ trợ**: Giáo viên cung cấp template flowchart và hướng dẫn từng bước sử dụng CREATE để tinh chỉnh đầu ra.
- **Thực hành**: Mỗi nhóm xây dựng sơ đồ luồng cho Agent của mình và trình bày ý tưởng.

**Kết quả mong đợi**:
- Học sinh thiết kế được một Agent đa bước với luồng logic rõ ràng và khả năng tự động hóa.

### 🧪 **5. Evaluation (Đánh giá)**  
**Thời lượng**: 20 phút  
**Mục tiêu**: Đánh giá khả năng thiết kế và tối ưu hóa AI Agent.

**Hoạt động**:
- **Bài kiểm tra thực hành**:
    - Học sinh trình bày Agent của mình trước lớp.
    - Đánh giá theo tiêu chí:
        - Độ chính xác của V-N-N.
        - Tính logic của luồng đa bước.
        - Tính ứng dụng thực tế.
        - Sử dụng CREATE framework hiệu quả.
- **Tự đánh giá & phản hồi đồng đẳng**:
    - Học sinh nhận xét lẫn nhau và đề xuất cải tiến.

**Kết quả mong đợi**:
- Học sinh có thể thiết kế, trình bày và đánh giá một AI Agent có khả năng tự động hóa quy trình học tập.

---

## 🧠 2. Knowledge Base (KB) for Agents & ReAct Logic

### 📚 Kiến thức nền tảng về AI Agents

#### A. Định nghĩa AI Agent
AI Agent là một hệ thống trí tuệ nhân tạo có khả năng:
- **Nhận biết môi trường** thông qua cảm biến hoặc đầu vào
- **Ra quyết định** dựa trên thông tin thu thập được
- **Thực hiện hành động** để đạt được mục tiêu cụ thể
- **Học hỏi và thích nghi** từ trải nghiệm

#### B. Các thành phần chính của AI Agent

**1. Lập kế hoạch (Planning)**
- Tổ chức và sắp xếp các hoạt động
- Xác định mục tiêu và chiến lược đạt được
- Ví dụ: Tạo lịch học tập cá nhân hóa

**2. Sử dụng công cụ (Tool Use)**
- Tích hợp các công cụ hỗ trợ (tìm kiếm, máy tính, cơ sở dữ liệu)
- Giao tiếp với các hệ thống bên ngoài
- Ví dụ: Tìm kiếm thông tin môn học, giải bài toán

**3. Bộ nhớ (Memory)**
- Lưu trữ thông tin ngắn hạn và dài hạn
- Truy xuất dữ liệu đã học
- Ví dụ: Ghi nhớ tiến độ học tập, lịch sử tương tác

**4. Lô-gic phản ứng (ReAct Logic)**
- Kết hợp lý luận và hành động
- Quy trình: Reason → Act → Observe → Think → Act
- Ví dụ: Phân tích câu hỏi → Thực hiện tìm kiếm → Quan sát kết quả → Đưa ra phản hồi

#### C. ReAct Framework chi tiết

**ReAct = Reason + Act**

**Các bước trong ReAct:**
1. **Thought (Suy nghĩ)**: Phân tích tình huống, xác định mục tiêu
2. **Action (Hành động)**: Chọn hành động phù hợp (sử dụng công cụ, truy vấn)
3. **Observation (Quan sát)**: Nhận kết quả từ hành động
4. **Repeat**: Lặp lại quá trình cho đến khi đạt mục tiêu

**Ví dụ ReAct trong học tập:**
```
Input: "Tôi muốn ôn tập chương 3 Toán lớp 9"
Thought: Học sinh muốn ôn tập chương 3 Toán lớp 9. Cần xác định nội dung chương 3.
Action: Search["toán lớp 9 chương 3 nội dung"]
Observation: Chương 3: Hệ phương trình bậc nhất hai ẩn
Thought: Đã xác định nội dung. Cần tạo câu hỏi ôn tập.
Action: Generate["câu hỏi hệ phương trình lớp 9"]
Observation: [Danh sách câu hỏi được tạo]
Action: Present["câu hỏi hệ phương trình lớp 9"]
```

---

## 🛠️ 3. Practical Activity: Building a 'Personal Study Assistant' Flow

### 🎯 Mục tiêu hoạt động
Xây dựng một AI Agent hỗ trợ học tập cá nhân với luồng logic đa bước sử dụng mô hình V-N-N và ReAct framework.

### 📋 Bước 1: Xác định V-N-N cho Agent

**V - Vai trò**: Trợ lý học tập cá nhân  
**N - Nhiệm vụ**: Hỗ trợ học sinh lập kế hoạch, ôn tập và đánh giá tiến độ học tập  
**N - Ngữ cảnh**: Học sinh THPT cần hỗ trợ học tập hiệu quả, cá nhân hóa

### 📊 Bước 2: Thiết kế luồng logic đa bước

```
[INPUT] → [V-N-N Analysis] → [Planning] → [Tool Use] → [Memory Update] → [ReAct Loop] → [OUTPUT]

Step 1: Nhận diện yêu cầu học tập
Step 2: Phân tích mục tiêu và ngữ cảnh
Step 3: Lập kế hoạch học tập
Step 4: Sử dụng công cụ hỗ trợ
Step 5: Tạo phản hồi và đánh giá
Step 6: Cập nhật bộ nhớ và điều chỉnh
```

### 🔧 Bước 3: Triển khai ReAct Logic

**Vòng lặp ReAct cho Personal Study Assistant:**

```
THOUGHT 1: Phân tích yêu cầu học tập của học sinh
ACTION 1: Truy vấn lịch học và tiến độ hiện tại
OBSERVATION 1: Nhận thông tin về môn học cần ôn tập
THOUGHT 2: Xác định nội dung học phù hợp
ACTION 2: Tìm kiếm tài liệu và bài tập liên quan
OBSERVATION 2: Thu thập tài liệu học tập
THOUGHT 3: Đánh giá mức độ hiểu biết hiện tại
ACTION 3: Tạo bài kiểm tra nhỏ
OBSERVATION 3: Nhận kết quả làm bài
THOUGHT 4: Đề xuất kế hoạch học tiếp theo
ACTION 4: Cập nhật lịch học và gửi gợi ý
```

### 📝 Bước 4: Tích hợp CREATE Framework

**Character**: Học sinh THPT (độ tuổi, trình độ, phong cách học)
**Request**: Hỗ trợ học tập hiệu quả
**Examples**: Lịch học mẫu, bài tập mẫu, phương pháp học
**Adjustment**: Giọng điệu phù hợp, độ khó điều chỉnh theo trình độ
**Type**: Trợ lý học tập, hệ thống gợi ý
**Extra info**: Thời gian rảnh, môn học yếu, mục tiêu thi

### 🎨 Bước 5: Xây dựng Flowchart

```
┌─────────────────┐
│   INPUT USER    │
└─────────┬───────┘
          ▼
┌─────────────────┐
│ V-N-N ANALYSIS  │
└─────────┬───────┘
          ▼
┌─────────────────┐
│   PLANNING      │
│ - Xác định mục tiêu
│ - Lập kế hoạch học
└─────────┬───────┘
          ▼
┌─────────────────┐
│   TOOL USE      │
│ - Tìm kiếm tài liệu
│ - Tạo bài tập
│ - Kiểm tra kiến thức
└─────────┬───────┘
          ▼
┌─────────────────┐
│   REACT LOOP    │
│ Thought → Action│
│ → Observation   │
└─────────┬───────┘
          ▼
┌─────────────────┐
│   OUTPUT        │
│ - Gợi ý học tập │
│ - Bài tập       │
│ - Đánh giá      │
└─────────────────┘
```

---

## 📋 4. Worksheet & Rubric

### 📄 WORKSHEET: Thiết kế AI Agent hỗ trợ học tập

**Tên học sinh**: ________________________  
**Lớp**: ________________________  
**Ngày**: ________________________

#### Phần 1: Xác định V-N-N (10 điểm)

**V - Vai trò của Agent**: 
_________________________________
_________________________________

**N - Nhiệm vụ chính**: 
_________________________________
_________________________________

**N - Ngữ cảnh sử dụng**: 
_________________________________
_________________________________

#### Phần 2: Thiết kế luồng logic (20 điểm)

**Bước 1**: _________________________________________________
**Bước 2**: _________________________________________________
**Bước 3**: _________________________________________________
**Bước 4**: _________________________________________________

#### Phần 3: Áp dụng ReAct Framework (20 điểm)

**Thought đầu tiên**: ________________________________________
**Action đầu tiên**: _________________________________________
**Observation đầu tiên**: ____________________________________
**Thought tiếp theo**: _______________________________________
**Action tiếp theo**: ________________________________________

#### Phần 4: Tích hợp CREATE (15 điểm)

**Character**: ______________________________________________
**Request**: ________________________________________________
**Examples**: _______________________________________________
**Adjustment**: _____________________________________________
**Type**: __________________________________________________
**Extra info**: _____________________________________________

#### Phần 5: Flowchart (15 điểm)

(Vẽ sơ đồ luồng logic của Agent bạn thiết kế)

```
[Chỗ để vẽ flowchart - 15 điểm]
```

#### Phần 6: Đánh giá tính ứng dụng (20 điểm)

**Ưu điểm của Agent bạn thiết kế**:
_________________________________
_________________________________
_________________________________

**Khó khăn có thể gặp phải**:
_________________________________
_________________________________
_________________________________

**Cách khắc phục**:
_________________________________
_________________________________
_________________________________

---

### 📊 RUBRIC ĐÁNH GIÁ

| Tiêu chí | Mức độ xuất sắc (5 điểm) | Mức độ tốt (4 điểm) | Mức độ trung bình (3 điểm) | Mức độ cần cải thiện (2 điểm) | Mức độ yếu (1 điểm) |
|----------|-------------------------|--------------------|---------------------------|------------------------------|-------------------|
| **V-N-N chính xác** | Xác định rõ ràng, phù hợp hoàn toàn | Xác định khá rõ ràng | Xác định cơ bản | Xác định chưa rõ | Không xác định được |
| **Luồng logic hợp lý** | Rõ ràng, đầy đủ, tối ưu | Khá rõ ràng, đầy đủ | Cơ bản hợp lý | Có thiếu sót | Không hợp lý |
| **Áp dụng ReAct** | Sử dụng hiệu quả, đầy đủ các bước | Sử dụng tốt, thiếu ít bước | Sử dụng cơ bản | Sử dụng chưa hiệu quả | Không sử dụng |
| **CREATE framework** | Áp dụng đầy đủ, sáng tạo | Áp dụng tốt | Áp dụng cơ bản | Áp dụng chưa hiệu quả | Không áp dụng |
| **Tính ứng dụng** | Rất thực tế, dễ áp dụng | Khá thực tế | Có tính ứng dụng | Hạn chế ứng dụng | Không thực tế |

**Tổng điểm**: _______/80 điểm

**Xếp loại**:
- 72-80 điểm: Xuất sắc (A)
- 64-71 điểm: Tốt (B)
- 56-63 điểm: Khá (C)
- 48-55 điểm: Trung bình (D)
- Dưới 48 điểm: Yếu (F)

---

## 🧰 Hỗ trợ kỹ thuật

### Template Flowchart
```
[START] → [Input] → [V-N-N] → [Plan] → [Tools] → [ReAct] → [Output] → [END]
```

### Checklist kiểm tra
- [ ] V-N-N được xác định rõ ràng
- [ ] Luồng logic có ít nhất 4 bước
- [ ] Có áp dụng ReAct framework
- [ ] Có tích hợp CREATE framework
- [ ] Có tính ứng dụng thực tế
- [ ] Có khả năng tự động hóa

### Tài nguyên hỗ trợ
- Mẫu thiết kế Agent
- Flowchart template
- CREATE framework checklist
- Ví dụ minh họa thực tế

---

## 📚 Tài nguyên bổ sung

### Liên kết với các module trước
- **Module 2 (V-N-N)**: Cung cấp nền tảng để thiết kế Agent
- **Module 3 (CREATE)**: Áp dụng để tinh chỉnh đầu ra của Agent
- **Module 4**: Kỹ năng giải quyết vấn đề được áp dụng để thiết kế nhiệm vụ cho Agent

### Bài tập mở rộng
- Thiết kế Agent cho môn học cụ thể (Toán, Văn, Anh, Khoa học)
- Tích hợp nhiều công cụ hỗ trợ
- Phát triển hệ thống đánh giá tự động

### Đánh giá cuối module
- **Bài tập cuối kỳ**: Thiết kế một AI Agent hỗ trợ học sinh tự động hóa việc học một môn cụ thể
- **Tiêu chí đánh giá**: Sáng tạo, ứng dụng, logic, hiệu quả CREATE framework