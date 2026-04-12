---
file_id: CONV_Atoms_conv_atoms_v07_6
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v07 6

# Tài liệu học tập: Chuyển đổi Python sang Blockly XML cho YoloBit và Robot Rover

## Thông tin chung

| Thuộc tính | Giá trị |
|------------|---------|
| **Tiêu đề** | Chuyển đổi Python sang Blockly XML cho YoloBit và Robot Rover |
| **Mô tả** | Tài liệu hướng dẫn chuyển đổi cú pháp Python sang định dạng Blockly XML, áp dụng cho các thiết bị YoloBit và Robot Rover trên nền tảng Ohstem |
| **Đối tượng học viên** | Kỹ sư phần mềm, giáo viên STEM, sinh viên kỹ thuật |
| **Ngôn ngữ** | Tiếng Việt |
| **Phiên bản** | LOM v4.4 Supreme |

---

## # Mục tiêu học tập

Sau khi hoàn thành tài liệu này, người học sẽ có khả năng:

- Hiểu cơ chế ánh xạ cú pháp Python sang Blockly XML
- Chuyển đổi các cấu trúc lập trình cơ bản (biến, hàm, điều kiện, vòng lặp) sang định dạng khối lệnh
- Tạo tệp JSON hoàn chỉnh để import vào nền tảng Ohstem
- Áp dụng kiến thức cho điều khiển robot Rover và thiết bị YoloBit

---

## # 1. Ánh xạ cú pháp Python sang Blockly XML

### ## 1.1. Biến và gán giá trị

#### Cú pháp Python:
```python
x = 5
```

#### Blockly XML tương ứng:
```xml
<block type="variables_set">
  <field name="VAR">x</field>
  <value name="VALUE">
    <block type="math_number">
      <field name="NUM">5</field>
    </block>
  </value>
</block>
```

> **Lưu ý:** Trường `VAR` chứa tên biến, đầu vào `VALUE` chứa block biểu thức [vv07] - Mục 2: Biến và hàm. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 1.2. Sử dụng biến trong biểu thức

#### Cú pháp Python:
```python
y = x + 10
```

#### Blockly XML tương ứng:
```xml
<block type="variables_set">
  <field name="VAR">y</field>
  <value name="VALUE">
    <block type="math_arithmetic">
      <field name="OP">ADD</field>
      <value name="A">
        <block type="variables_get">
          <field name="VAR">x</field>
        </block>
      </value>
      <value name="B">
        <block type="math_number">
          <field name="NUM">10</field>
        </block>
      </value>
    </block>
  </value>
</block>
```

> **Lưu ý:** Sử dụng block `variables_get` với trường `VAR` khớp với định danh biến [vv07] - Mục 2: Biến và hàm. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 1.3. Hàm tự định nghĩa

#### Cú pháp Python:
```python
def my_function():
    print("Hello World")
```

#### Blockly XML tương ứng:
```xml
<block type="procedures_defnoreturn">
  <field name="NAME">my_function</field>
  <statement name="STACK">
    <!-- Nội dung thân hàm -->
  </statement>
</block>
```

> **Lưu ý:** Tên hàm đặt tại trường `NAME`, nội dung thân hàm nằm trong thẻ `<statement name="STACK">` [vv07] - Mục 2: Biến và hàm. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # 2. Cấu trúc điều khiển và toán học

### ## 2.1. Cấu trúc điều kiện IF

#### Cú pháp Python:
```python
if condition:
    do_something()
```

#### Blockly XML tương ứng:
```xml
<block type="controls_if">
  <mutation elseif="0" else="0"></mutation>
  <value name="IF0">
    <!-- Điều kiện -->
  </value>
  <statement name="DO0">
    <!-- Thân lệnh -->
  </statement>
</block>
```

> **Lưu ý:** Điều kiện đặt trong `<value name="IF0">`, thân lệnh trong `<statement name="DO0">`. Nhánh `else if` và `else` được định nghĩa qua thuộc tính `mutation` [vv07] - Mục 3: Khối điều khiển và toán học. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 2.2. Vòng lặp WHILE và FOR

#### Vòng lặp WHILE:
```python
while condition:
    do_something()
```

```xml
<block type="controls_whileUntil">
  <field name="MODE">WHILE</field>
  <value name="BOOL">
    <!-- Điều kiện -->
  </value>
  <statement name="DO">
    <!-- Thân vòng lặp -->
  </statement>
</block>
```

#### Vòng lặp FOR:
```python
for i in range(5):
    do_something()
```

```xml
<block type="controls_repeat_ext">
  <value name="TIMES">
    <block type="math_number">
      <field name="NUM">5</field>
    </block>
  </value>
  <statement name="DO">
    <!-- Thân vòng lặp -->
  </statement>
</block>
```

> **Lưu ý:** Vòng lặp `while` sử dụng block `controls_whileUntil`, vòng lặp `for` sử dụng `controls_repeat_ext` [vv07] - Mục 3: Khối điều khiển và toán học. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 2.3. Phép toán số học và so sánh

#### Phép toán số học:
```xml
<block type="math_arithmetic">
  <field name="OP">ADD</field>  <!-- ADD, SUB, MUL, DIV -->
  <value name="A">...</value>
  <value name="B">...</value>
</block>
```

#### Phép so sánh:
```xml
<block type="logic_compare">
  <field name="OP">EQ</field>  <!-- EQ, NEQ, GT, LT, GTE, LTE -->
  <value name="A">...</value>
  <value name="B">...</value>
</block>
```

> **Lưu ý:** Các phép toán sử dụng block `math_arithmetic`, phép so sánh sử dụng block `logic_compare` [vv07] - Mục 3: Khối điều khiển và toán học. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # 3. Điều khiển Robot và Extension

### ## 3.1. Ánh xạ hàm thư viện rover

#### Cú pháp Python:
```python
rover.move(100, 100)
rover.stop()
rover.servo.write_angle(90)
```

#### Blockly XML tương ứng:
```xml
<block type="rover_move">
  <value name="LEFT_SPEED">
    <block type="math_number"><field name="NUM">100</field></block>
  </value>
  <value name="RIGHT_SPEED">
    <block type="math_number"><field name="NUM">100</field></block>
  </value>
</block>

<block type="rover_stop"></block>

<block type="rover_servo_write_angle">
  <value name="ANGLE">
    <block type="math_number"><field name="NUM">90</field></block>
  </value>
</block>
```

> **Lưu ý:** Các hàm thư viện `rover` được ánh xạ trực tiếp sang các block tương ứng theo định nghĩa trong `definition.js` [vv07] - Mục 4: Khối điều khiển robot và extension. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 3.2. Cảm biến và xử lý dữ liệu

Các khối cảm biến (dò line, siêu âm) trả về giá trị thường được đặt bên trong khối `logic_compare` hoặc gán vào biến.

```xml
<block type="logic_compare">
  <field name="OP">GT</field>
  <value name="A">
    <block type="sensor_ultrasonic_read"></block>
  </value>
  <value name="B">
    <block type="math_number"><field name="NUM">10</field></block>
  </value>
</block>
```

> **Lưu ý:** Các khối cảm biến trả về giá trị thường được đặt bên trong khối `logic_compare` hoặc gán vào biến [vv07] - Mục 4: Khối điều khiển robot và extension. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # 4. Cấu trúc tệp và Định dạng dữ liệu

### ## 4.1. ID duy nhất cho mỗi block

Mỗi block và biến bắt buộc phải có một ID duy nhất, có thể sinh bằng `Blockly.utils.idGenerator.genUid()` hoặc thuật toán sinh chuỗi ngẫu nhiên tương đương.

```javascript
const uniqueId = Blockly.utils.idGenerator.genUid();
```

> **Lưu ý:** Mỗi block và biến bắt buộc phải có một ID duy nhất [vv07] - Mục 5: Sinh ID và vị trí khối. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 4.2. Cấu trúc tệp JSON hoàn chỉnh

Tệp JSON xuất ra để import vào app.ohstem.vn bao gồm các trường:

```json
{
  "xmlText": "<xml>...</xml>",
  "python": "print('hello')",
  "mode": "blockly",
  "name": "project_name",
  "extensions": ["rover", "yolobit"],
  "device": "yolobit"
}
```

> **Lưu ý:** Tệp JSON bao gồm các trường: `xmlText`, `python`, `mode`, `name`, `extensions`, và `device` [vv07] - Mục 6: Tạo chuỗi XML/JSON hoàn chỉnh. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 4.3. Cấu trúc XML Blockly

Chuỗi XML Blockly phải được bao bọc trong thẻ `<xml>` với namespace và có phần khai báo `<variables>` ở đầu:

```xml
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="var_id" type="">variable_name</variable>
  </variables>
  <!-- Các block chính -->
</xml>
```

> **Lưu ý:** XML Blockly phải có namespace và phần khai báo `<variables>` ở đầu [vv07] - Mục 6: Tạo chuỗi XML/JSON hoàn chỉnh. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # 5. Cơ chế chuyển đổi nâng cao

### ## 5.1. So sánh với hệ thống MakeCode

Hệ thống MakeCode (sử dụng trong Minecraft Education) chuyển đổi cả Blocks và Static Python về mã trung gian Static TypeScript trước khi biên dịch.

> **Lưu ý:** MakeCode chuyển đổi cả Blocks và Static Python về mã trung gian Static TypeScript [vv07] - Phần nghiên cứu Minecraft Education Edition. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 5.2. Khối xám (Grey Block)

"Khối xám" được sử dụng để hiển thị các đoạn mã text không thể chuyển đổi trực tiếp sang khối lệnh chuẩn, giúp duy trì tính toàn vẹn của chương trình khi chuyển đổi hai chiều.

> **Lưu ý:** "Khối xám" giúp duy trì tính toàn vẹn của chương trình khi chuyển đổi hai chiều [vv07] - Phần nghiên cứu Minecraft Education Edition. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### ## 5.3. Static Python trong MakeCode

Static Python trong MakeCode thực chất là một tập con (subset) của Python được ánh xạ một-một tới các API TypeScript, không phải là MicroPython đầy đủ.

> **Lưu ý:** Static Python là tập con của Python được ánh xạ một-một tới API TypeScript [vv07] - Phần nghiên cứu Minecraft Education Edition. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # Bài tập thực hành

### ## Bài 1: Chuyển đổi đơn giản
Chuyển đoạn code Python sau sang Blockly XML:
```python
speed = 50
if sensor_value > 100:
    rover.move(speed, speed)
else:
    rover.stop()
```

### ## Bài 2: Vòng lặp điều kiện
Chuyển đoạn code Python sau sang Blockly XML:
```python
count = 0
while count < 5:
    rover.servo.write_angle(90)
    count = count + 1
```

### ## Bài 3: Tạo tệp JSON hoàn chỉnh
Tạo tệp JSON hoàn chỉnh để import vào Ohstem cho đoạn code sau:
```python
def move_forward():
    rover.move(100, 100)
    
move_forward()
```

---

## # Kiểm tra đánh giá

### ## Câu hỏi trắc nghiệm

1. Block nào được sử dụng để gán giá trị cho biến?
   - A. `variables_get`
   - B. `variables_set`
   - C. `math_number`
   - D. `logic_compare`

2. Trường nào chứa tên biến trong block gán giá trị?
   - A. `VALUE`
   - B. `NUM`
   - C. `VAR`
   - D. `OP`

3. Block nào được sử dụng cho vòng lặp `while`?
   - A. `controls_repeat_ext`
   - B. `controls_for`
   - C. `controls_whileUntil`
   - D. `controls_flow_statements`

### ## Đáp án
1. B
2. C
3. C

---

## # Tài nguyên bổ sung

- [ ] Mẫu tệp JSON mẫu
- [ ] Danh sách tất cả các block hỗ trợ
- [ ] Video hướng dẫn chuyển đổi
- [ ] Bộ thử nghiệm chuyển đổi online

---

## # Ghi chú cuối cùng

> **Lưu ý quan trọng:** Tất cả các block và biến phải có ID duy nhất để đảm bảo tính toàn vẹn của chương trình Blockly. Việc bỏ qua bước này có thể gây ra lỗi khi import vào nền tảng Ohstem [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)