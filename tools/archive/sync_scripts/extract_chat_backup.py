import sys
import os
import re
from html.parser import HTMLParser

class ActivityParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content_cell = False
        self.current_text = []
        self.activities = []
        self.last_tag = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get('class', '')
        if tag == 'div' and 'content-cell' in cls:
            self.in_content_cell = True
            self.current_text = []
        self.last_tag = tag

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_content_cell:
            text = ' '.join(self.current_text).strip()
            if text:
                self.activities.append(text)
            self.in_content_cell = False

    def handle_data(self, data):
        if self.in_content_cell:
            self.current_text.append(data)

def extract_conversation(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = ActivityParser()
    parser.feed(html_content)

    with open(output_file, 'w', encoding='utf-8') as f:
        for activity in parser.activities:
            # Clean up text
            # Often Google My Activity has "Prompted <query>" then timestamp then result
            if activity.startswith('Prompted'):
                f.write('='*50 + '\n')
                # Try to separate Prompted, Time and Content
                # Example: "Prompted Bắt đầu nghiên cứu Mar 31, 2026, 8:28:11 PM GMT+07:00 Tôi đã hoàn thành nghiên cứu..."
                match = re.match(r'Prompted\s+(.*?)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4},\s+.*?\s+(.*)', activity, re.DOTALL)
                if match:
                    prompt = match.group(1).strip()
                    time_stuff = activity[len('Prompted') + len(prompt):activity.find(match.group(3))].strip()
                    content = match.group(3).strip()
                    f.write(f"THỜI GIAN: {time_stuff}\n")
                    f.write(f"NGƯỜI DÙNG: {prompt}\n")
                    f.write(f"GEMINI: {content}\n")
                else:
                    f.write(f"{activity}\n")
                f.write('\n')
            elif 'Products:' in activity:
                continue # Skip metadata cells
            else:
                # Other cells like titles or standalone text
                if len(activity) > 5:
                    f.write(f"CHÚ THÍCH/TIÊU ĐỀ: {activity}\n\n")

if __name__ == "__main__":
    input_path = r'd:\TEst_gravity\MyActivity.txt'
    output_path = r'd:\TEst_gravity\MyActivity_Conversation.txt'
    print(f"Bắt đầu trích xuất từ {input_path}...")
    extract_conversation(input_path, output_path)
    print(f"Đã hoàn thành! Kết quả tại {output_path}")
