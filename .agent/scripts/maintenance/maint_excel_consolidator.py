import pandas as pd
import argparse
import os
from pathlib import Path

def consolidate_excel(input_path, output_path=None):
    """
    Gộp vật tư từ các sheet của file Excel dựa trên Tên và Mã vật tư.
    """
    if not os.path.exists(input_path):
        print(f"Lỗi: Không tìm thấy file tại {input_path}")
        return

    xls = pd.ExcelFile(input_path)
    all_data = []

    # Danh sách các tên cột tiềm năng
    ALIASES = {
        "Tên Vật tư": ["tên vật tư", "ten vat tu", "tên", "vật tư", "item name", "description"],
        "Mã Vật tư": ["mã vật tư", "ma vat tu", "mã", "code", "sku", "mã hàng"],
        "ĐVT": ["đvt", "dvt", "đơn vị", "unit"],
        "SL": ["sl", "số lượng", "qty", "quantity"]
    }

    def find_column(df_cols, target_key):
        cols_lower = [str(c).strip().lower() for c in df_cols]
        for alias in ALIASES[target_key]:
            if alias in cols_lower:
                return df_cols[cols_lower.index(alias)]
        # Phân tích mờ (fuzzy) nếu không khớp hoàn toàn
        for alias in ALIASES[target_key]:
            for i, c in enumerate(cols_lower):
                if alias in c:
                    return df_cols[i]
        return None

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        col_ten = find_column(df.columns, "Tên Vật tư")
        col_ma = find_column(df.columns, "Mã Vật tư")
        col_dvt = find_column(df.columns, "ĐVT")
        col_sl = find_column(df.columns, "SL")

        if not col_ten or not col_sl:
            print(f"Cảnh báo: Bỏ qua sheet '{sheet_name}' do thiếu cột Tên hoặc Số lượng.")
            continue

        # Chuẩn hóa dữ liệu
        temp_df = pd.DataFrame()
        temp_df["Tên Vật tư"] = df[col_ten].astype(str).str.strip()
        temp_df["Mã Vật tư"] = df[col_ma].astype(str).str.strip() if col_ma else ""
        temp_df["ĐVT"] = df[col_dvt].astype(str).str.strip() if col_dvt else ""
        temp_df["SL"] = pd.to_numeric(df[col_sl], errors='coerce').fillna(0)
        
        all_data.append(temp_df)

    if not all_data:
        print("Lỗi: Không có dữ liệu hợp lệ để gộp.")
        return

    combined = pd.concat(all_data, ignore_index=True)
    
    # Loại bỏ hàng trống
    combined = combined[combined["Tên Vật tư"] != "nan"]

    # Gộp theo Tên và Mã
    result = combined.groupby(["Tên Vật tư", "Mã Vật tư"], as_index=False).agg({
        "ĐVT": lambda x: x.replace("", pd.NA).dropna().iloc[0] if not x.replace("", pd.NA).dropna().empty else "",
        "SL": "sum"
    })

    # Thêm STT
    result.insert(0, "STT", range(1, len(result) + 1))

    # Sắp xếp theo tên
    result = result.sort_values(by="Tên Vật tư")
    result["STT"] = range(1, len(result) + 1)

    if not output_path:
        input_file = Path(input_path)
        output_path = input_file.parent / f"{input_file.stem}_Consolidated.xlsx"

    result.to_excel(output_path, index=False)
    print(f"Thành công! File đã được lưu tại: {output_path}")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script gộp vật tư Excel cho KDI Education")
    parser.add_argument("input", help="Đường dẫn file Excel đầu vào")
    parser.add_argument("-o", "--output", help="Đường dẫn file đầu ra (tùy chọn)")
    
    args = parser.parse_args()
    consolidate_excel(args.input, args.output)
