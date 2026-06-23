# Media Checklist - AI Trung hoc 1

- Khoa hoc: `INT_HCM_Tri tue nhan tao Trung hoc 1`
- Pham vi: `Cau 01-30` cua 3 file draft `nho`, `hieu`, `van_dung`
- Trang thai: `PREVIEW_ONLY - MEDIA MATERIALIZED`
- Muc dich: Lam checklist de agent san xuat media dung de, dung file nguon, dung quy tac review

## 1. Tai lieu goc can bam theo

- `GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_draft_nho.md`
- `GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_draft_hieu.md`
- `GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_draft_van_dung.md`

## 2. Hard Rules Cho Agent Media

1. Anh code/block phai duoc chup tu cong cu that, uu tien PRG/Dancing with AI that. Khong dung anh AI gia lap screenshot.
2. Moi anh code/block phai co file nguon vat ly di kem de human load check.
3. Mac dinh voi khoa hoc nay: file nguon vat ly la `.sb3`.
4. Neu sau nay co bien the OhStem thi thay `.sb3` bang `.json`, nhung checklist hien tai van uu tien `.sb3`.
5. Neu mot cau co video demo code thi video do phai co file `.sb3` di kem.
6. Anh giao dien/chuong trinh phai remove background sach, ro net, khong watermark.
7. Nhan hien thi trong de dung theo quy tac `so_cau.so_thu_tu_media` nhu `3.1`, `3.2`, `22.1`.
8. Ten file tren disk giu convention hien tai, khong ep doi schema cu.

## 3. Quy Uoc Ten File

### 3.1. Mot anh code hoac mot anh giao dien

- Nhan hien thi: `4.1`
- Ten file de xuat: `cau_04_1.png`
- File nguon de xuat: `cau_04_source.sb3`

### 3.2. Nhieu anh dap an A/B/C/D

- Nhan hien thi: `22.1`, `22.2`, `22.3`, `22.4`
- Ten file de xuat: `cau_22_a.png`, `cau_22_b.png`, `cau_22_c.png`, `cau_22_d.png`
- File nguon de xuat:
  - Neu moi dap an la mot chuong trinh rieng: `cau_22_a.sb3`, `cau_22_b.sb3`, `cau_22_c.sb3`, `cau_22_d.sb3`
  - Neu chi la bo block minh hoa trong cung 1 question pack: `cau_22_source_pack.sb3`

### 3.3. Cach doc cot `Source rule` trong bang duoi

- `none`: khong can media
- `optional`: chi san xuat neu team chon render media de review
- `source_pack`: 1 file `.sb3` cho toan bo cau
- `source_per_option`: 1 file `.sb3` cho moi dap an/media option

## 4. Bang Checklist San Xuat

| Cau | Muc do | Muc uu tien | Asset can tao | Ten file de xuat | Source rule | Ghi chu review |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| 01 | Nho | none | Khong can media | - | none | Cau ly thuyet text |
| 02 | Nho | optional | 4 anh dap an da render cho full review | `cau_02_a.png` -> `cau_02_d.png` | source_per_option | Moi dap an co 1 `.sb3` de human load check |
| 03 | Nho | bat_buoc | 4 anh block PRG | `cau_03_1.png` -> `cau_03_4.png` | source_pack | Moi anh la 1 block/cong cu: `Translate`, `Speak`, `go to face landmark`, `use model` |
| 04 | Nho | bat_buoc | 1 anh code toa do | `cau_04_1.png` | source_pack | Human phai doc duoc chuoi `go to x/y`, `change x`, `change y` |
| 05 | Nho | none | Khong can media | - | none | Cau Boolean dang text |
| 06 | Nho | nen_co | 1 anh block hoi lien tiep | `cau_06_1.png` | source_pack | Minh hoa bien `Answer` bi ghi de |
| 07 | Nho | optional | 4 anh icon/block da render cho full review | `cau_07_a.png` -> `cau_07_d.png` | source_per_option | Moi dap an co 1 `.sb3` ung voi 1 cong cu/extension |
| 08 | Nho | nen_co | 1 anh code face sensing | `cau_08_1.png` | source_pack | Phai the hien logic bam theo landmark trong `forever` |
| 09 | Nho | nen_co | 1 anh block `use model` | `cau_09_1.png` | source_pack | Human check vi tri dan link model |
| 10 | Nho | nen_co | 1 anh code mau camera + model | `cau_10_1.png` | source_pack | Nen co `turn video on` va `use model` |
| 11 | Hieu | nen_co | 2 anh block/flow de so sanh hanh vi | `cau_11_1.png`, `cau_11_2.png` | source_pack | So sanh luong tuan tu voi luong sai |
| 12 | Hieu | nen_co | 2 anh block `Translate` va `Speak/Text to Speech` | `cau_12_1.png`, `cau_12_2.png` | source_pack | Dung de user check dung hanh vi cua 2 nhom lenh |
| 13 | Hieu | nen_co | 4 anh block AI hoac code ngan | `cau_13_1.png` -> `cau_13_4.png` | source_pack | Moi anh ung voi 1 cong cu AI o cot A |
| 14 | Hieu | bat_buoc | 2 anh code so sanh | `cau_14_1.png`, `cau_14_2.png` | source_pack | Anh 1: `change y by ...`; Anh 2: bam `nose bridge` trong `forever` |
| 15 | Hieu | none | Khong can media | - | none | Cau logic ve `Answer`, bien, list |
| 16 | Hieu | none | Khong can media | - | none | Cau list dang text |
| 17 | Hieu | none | Khong can media | - | none | Cau `broadcast` dang text |
| 18 | Hieu | none | Khong can media | - | none | Luong Translate + TTS dang text ro rang |
| 19 | Hieu | nen_co | 1 anh block face sensing | `cau_19_1.png` | source_pack | Can thay logic cap nhat lien tuc va camera |
| 20 | Hieu | none | Khong can media | - | none | Cau to hop cong cu dang text |
| 21 | Hieu | nen_co | 3 anh review loi camera/model | `cau_21_1.png`, `cau_21_2.png`, `cau_21_3.png` | source_pack | Goi y: `turn video on`, `use model`, va screenshot camera xam/xung dot |
| 22 | Van dung | bat_buoc | 4 anh code dap an | `cau_22_a.png` -> `cau_22_d.png` | source_per_option | Moi dap an la 1 chuong trinh mau rieng, phai co `.sb3` tuong ung |
| 23 | Van dung | optional | 4 anh dap an da render cho full review | `cau_23_a.png` -> `cau_23_d.png` | source_per_option | Moi dap an co 1 `.sb3` de human check luong nhap, luu, dich, doc |
| 24 | Van dung | bat_buoc | 4 anh code dap an | `cau_24_a.png` -> `cau_24_d.png` | source_per_option | Human can check ro `forever`, su kien `space`, landmark, va case dat `x,y` co dinh |
| 25 | Van dung | nen_co | 4 anh code/block dap an | `cau_25_a.png` -> `cau_25_d.png` | source_per_option | Uu tien the hien `use model`, `turn video on`, va co che kich hoat khi detect dung |
| 26 | Van dung | nen_co | 1 anh code mau luu danh sach | `cau_26_1.png` | source_pack | Minh hoa `List` dung de luu ten hoc vien da diem danh |
| 27 | Van dung | bat_buoc | 4 anh chuong trinh mau dap an | `cau_27_a.png` -> `cau_27_d.png` | source_per_option | Phai load check duoc logic diem danh + list + face emotion |
| 28 | Van dung | bat_buoc | 4 anh chuong trinh mau dap an | `cau_28_a.png` -> `cau_28_d.png` | source_per_option | Human can check ro reset costume goc va bat dong thoi nhieu phu kien |
| 29 | Van dung | bat_buoc | 4 anh chuong trinh mau dap an | `cau_29_a.png` -> `cau_29_d.png` | source_per_option | Anh A phai the hien dieu kien `10 giay khong phat hien ai thi turn video off` |
| 30 | Van dung | bat_buoc | 4 anh chuong trinh mau dap an | `cau_30_a.png` -> `cau_30_d.png` | source_per_option | Uu tien the hien `broadcast`, camera bat dung luc, va luong song song |

## 5. Thu Tu San Xuat De Xuat

1. Lam het nhom `bat_buoc` truoc.
2. Moi cau co code image phai tao file `.sb3` truoc, sau do moi chup PNG.
3. Nhom `source_per_option` phai dam bao moi anh dap an load lai duoc tren playground.
4. Nhom `nen_co` lam sau khi nhom `bat_buoc` da xong.
5. Nhom `optional` chi lam neu human muon day muc review len bang media.

## 6. Definition Of Done Cho Agent Media

1. Dung so luong file PNG theo checklist.
2. Dung so luong file `.sb3` theo `Source rule`.
3. Anh ro net, remove background, khong watermark.
4. Moi PNG code/block doi chieu duoc voi file `.sb3` tuong ung.
5. Ten file tren disk nhat quan theo `cau_XX_*`.
6. Khi gan vao de, nhan hien thi media theo quy tac `so_cau.so_thu_tu_media`.

## 7. Ghi Chu Ban Giao

- Batch `batch_1_required` va `batch_2_recommended` da duoc materialize vao thu muc Media.
- Trang thai chi tiet cua tung cau duoc theo doi trong file manifest `.csv`.
- Checklist nay khong doi ten file cu tren disk.
- Checklist nay duoc viet de agent san xuat asset ma khong phai tu suy doan lai tung cau.
