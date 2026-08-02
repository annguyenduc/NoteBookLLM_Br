import re
import json
import uuid
import datetime
import zipfile
import os

def parse_full_time(time_part1, response_part):
    # time_part1: "g Apr 4, 2026, 2:32:40" or "ng Apr 4, 2026, 2:29:42"
    # response_part: "PM GMT+07:00 Chào bạn..."
    
    # Extract date part 1
    match1 = re.search(r'([A-Z][a-z]{2}\s+\d{1,2},\s+\d{4},\s+\d{1,2}:\d{2}:\d{2})', time_part1)
    # Extract AM/PM and Timezone from response_part
    match2 = re.search(r'^([AP]M\s+GMT[+-]\d{2}:\d{2})', response_part)
    
    if match1 and match2:
        full_str = f"{match1.group(1)} {match2.group(1)}"
        # Example: "Apr 4, 2026, 2:32:40 PM GMT+07:00"
        try:
            # Note: strptime doesn't handle GMT+07:00 well with %z in some versions, but we can try
            # For simplicity, we just parse the main parts
            dt = datetime.datetime.strptime(match1.group(1), "%b %d, %Y, %H:%M:%S")
            if "PM" in match2.group(1) and dt.hour < 12:
                dt = dt.replace(hour=dt.hour + 12)
            elif "AM" in match2.group(1) and dt.hour == 12:
                dt = dt.replace(hour=0)
            return dt.timestamp(), match2.end()
        except Exception as e:
            return datetime.datetime.now().timestamp(), 0
    elif match1:
        try:
            dt = datetime.datetime.strptime(match1.group(1), "%b %d, %Y, %H:%M:%S")
            return dt.timestamp(), 0
        except:
            pass
            
    return datetime.datetime.now().timestamp(), 0

def convert_txt_to_json(input_file, output_json):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by separator (50 '=' chars)
    blocks = re.split(r'={50,}', content)
    conversations_by_date = {} # Key: "YYYY-MM-DD"
    
    for block in blocks:
        block = block.strip()
        if not block: continue
        
        # Extract fields
        time_match = re.search(r'THỜI GIAN:\s*(.*)', block)
        user_match = re.search(r'NGƯỜI DÙNG:\s*(.*?)(?=GEMINI:|$)', block, re.DOTALL)
        gemini_match = re.search(r'GEMINI:\s*(.*)', block, re.DOTALL)
        
        if not (time_match and user_match and gemini_match):
            continue
            
        time_str_raw = time_match.group(1).strip()
        user_text = user_match.group(1).strip()
        gemini_text_raw = gemini_match.group(1).strip()
        
        timestamp, response_start = parse_full_time(time_str_raw, gemini_text_raw)
        gemini_text = gemini_text_raw[response_start:].strip()
        
        date_str = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        
        if date_str not in conversations_by_date:
            conversations_by_date[date_str] = []
            
        conversations_by_date[date_str].append({
            "user": user_text,
            "assistant": gemini_text,
            "timestamp": timestamp
        })

    # Build the ChatGPT structure
    final_json = []
    
    for date_str, messages in conversations_by_date.items():
        # Sort messages in each conversation by timestamp
        messages.sort(key=lambda x: x["timestamp"])
        
        conv_id = str(uuid.uuid4())
        mapping = {}
        root_id = str(uuid.uuid4())
        
        # Root node
        mapping[root_id] = {
            "id": root_id,
            "message": None,
            "parent": None,
            "children": []
        }
        
        prev_node = root_id
        
        for i, msg in enumerate(messages):
            # User Message
            user_id = str(uuid.uuid4())
            mapping[prev_node]["children"].append(user_id)
            mapping[user_id] = {
                "id": user_id,
                "message": {
                    "id": user_id,
                    "author": {"role": "user", "name": None, "metadata": {}},
                    "create_time": msg["timestamp"],
                    "update_time": None,
                    "content": {"content_type": "text", "parts": [msg["user"]]},
                    "status": "finished_successfully",
                    "end_turn": None,
                    "weight": 1.0,
                    "metadata": {},
                    "recipient": "all"
                },
                "parent": prev_node,
                "children": []
            }
            
            # Assistant Message
            ast_id = str(uuid.uuid4())
            mapping[user_id]["children"].append(ast_id)
            mapping[ast_id] = {
                "id": ast_id,
                "message": {
                    "id": ast_id,
                    "author": {"role": "assistant", "name": None, "metadata": {}},
                    "create_time": msg["timestamp"] + 1,
                    "update_time": None,
                    "content": {"content_type": "text", "parts": [msg["assistant"]]},
                    "status": "finished_successfully",
                    "end_turn": None,
                    "weight": 1.0,
                    "metadata": {},
                    "recipient": "all"
                },
                "parent": user_id,
                "children": []
            }
            
            prev_node = ast_id

        final_json.append({
            "title": f"Gemini History - {date_str}",
            "create_time": messages[0]["timestamp"],
            "update_time": messages[-1]["timestamp"],
            "mapping": mapping,
            "current_node": prev_node,
            "conversation_id": conv_id,
            "id": conv_id
        })
        
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)

def zip_file(input_file, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file, "conversations.json")

if __name__ == "__main__":
    input_txt = r'd:\TEst_gravity\MyActivity_Conversation.txt'
    output_json = r'd:\TEst_gravity\conversations.json'
    output_zip = r'd:\TEst_gravity\MyActivity_Gemini_Import.zip'
    
    print(f"Bắt đầu chuyển đổi từ {input_txt}...")
    convert_txt_to_json(input_txt, output_json)
    print(f"Đã tạo {output_json}")
    zip_file(output_json, output_zip)
    print(f"Đã nén thành {output_zip}")
