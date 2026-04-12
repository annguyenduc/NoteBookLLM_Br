### 1. Tạo mẫu Test Bridge hình tròn (Circular Spool Test)

Để mô phỏng chính xác cách in của cuộn spool (vành tròn, nhịp bridge cong), mình đã tạo một mẫu test chuyên biệt. Mẫu này gồm:
- **Đế và Hub trung tâm**: Để cố định mẫu trên bàn in.
- **4 Trụ (Spokes)**: Đỡ vành trên tại 4 điểm.
- **Vành trên (Bridge)**: Các đoạn vành 90 độ nối giữa các trụ sẽ buộc máy in phải thực hiện lệnh **Bridge** theo đường cong.

```python
import math
from pathlib import Path

def stl_facet(n, v1, v2, v3):