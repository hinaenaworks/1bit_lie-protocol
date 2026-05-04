# src/gate.py

class LogicalGate:
    def __init__(self):
        pass

    def verify(self, input_data):
        # import re

def verify_fact_integrity(input_data):
    # 感情論を排除するための禁止ワードリスト
    forbidden_patterns = [
        r"思う", r"気がする", r"なんとなく", 
        r"〜かもしれません", r"主観的には"
    ]
    
    for pattern in forbidden_patterns:
        if re.search(pattern, input_data):
            return False  # 感情論を検知 → 遮断
            
    return True  # 検証パス

        if "感情" in input_data: 
            return False
        return True

    def run(self, input_data):
        if not self.verify(input_data):
            return "Unknown"
        return f"Process: {input_data}"
