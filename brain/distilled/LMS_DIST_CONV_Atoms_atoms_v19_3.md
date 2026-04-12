---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v19_3
  title: atoms_v19_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp, tập trung vào các nền tảng vật lý và toán học bổ trợ cho Robotics và AI:

- **Fact:** Công thức tính moment quán tính ($I$) của một vật thể hình trụ (cylinder) hoặc đĩa tròn (đồng xu) khi quay quanh trục tâm vuông góc với mặt phẳng là $I = \frac{1}{2} mr^2$.
- **Source:** [vv19] - Conversation: Moment Quán Tính Đồng Xu (Phần phản hồi của ASSISTANT về Cylinder và đồng xu tương tự).
- **Tag:** [vv19]

- **Fact:** Công thức moment quán tính của một đồng xu (dạng đĩa - disc) khi quay quanh trục nằm trong mặt phẳng của nó (trục đối xứng/đường kính) là $I = \frac{1}{4} mr^2$.
- **Source:** [vv19] - Conversation: Moment Quán Tính Đồng Xu (Phần phản hồi về đồng xu đứng vuông góc mặt đất).
- **Tag:** [vv19]

- **Fact:** Định lý trục song song (Parallel Axis Theorem) dùng để tính moment quán tính đối với một trục không đi qua trọng tâm: $I = I_{cm} + md^2$ (trong đó $I_{cm}$ là moment quán tính tại tâm khối lượng, $d$ là khoảng cách từ trục quay đến tâm).
- **Source:** [vv19] - Conversation: Moment Quán Tính Đồng Xu (Phần phản hồi đầu tiên).
- **Tag:** [vv19]

- **Fact:** Trong Robotics, việc xác định moment quán tính là cực kỳ quan trọng để tính toán lực mô-men xoắn (torque) cần thiết cho động cơ khi điều khiển các khớp quay của robot.
- **Source:** [N/A]
- **Tag:** [Unverified_Source]

- **Fact:** Quy tắc so sánh phân số: Nếu $\frac{a}{b} < 1$ và $c > 0$ thì $\frac{a+c}{b+c} > \frac{a}{b}$. Đây là nền tảng logic toán học có thể ứng dụng trong các thuật toán tối ưu hóa hoặc xử lý dữ liệu trong AI.
- **Source:** [vv19] - Conversation: Numerical Comparison (Phần chứng minh cuối cùng).
- **Tag:** [vv19]

- **Fact:** Khi xoay một vật thể (như đồng xu), sự ổn định của chuyển động phụ thuộc vào việc trục quay có đi qua tâm khối lượng (trọng tâm) hay không. Trục quay nằm ngoài tâm khối lượng sẽ tạo ra hiệu ứng chuyển động khó kiểm soát hơn.
- **Source:** [vv19] - Conversation: Moment Quán Tính Đồng Xu (Phần giải thích cho học sinh).
- **Tag:** [vv19]