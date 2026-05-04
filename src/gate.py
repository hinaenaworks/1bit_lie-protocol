import re

class LogicalGate:
    def __init__(self):
        # 感情論を排除するための禁止ワードリスト
        self.forbidden_patterns = [
            r"思う", r"気がする", r"なんとなく", 
            r"〜かもしれません", r"主観的には"
        ]

    def verify(self, input_data):
        # 感情論や曖昧な表現が含まれていないか検証
        for pattern in self.forbidden_patterns:
            if re.search(pattern, input_data):
                return False  # 感情論を検知 → 遮断
        return True  # 検証パス

    def run(self, input_data):
        if not self.verify(input_data):
            return "Unknown: Verification Failed"
        return f"Process Success: {input_data}"