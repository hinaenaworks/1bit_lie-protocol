# src/gate.py

class LogicalGate:
    def __init__(self):
        pass

    def verify(self, input_data):
        # ここに検証ロジックを書く
        if "感情" in input_data: 
            return False
        return True

    def run(self, input_data):
        if not self.verify(input_data):
            return "Unknown"
        return f"Process: {input_data}"
