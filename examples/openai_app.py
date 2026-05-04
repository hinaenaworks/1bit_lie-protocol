# examples/openai_app.py
from src.gate import LogicalGate

gate = LogicalGate()

def main():
    user_input = "感情論たっぷりのAIの回答候補"
    result = gate.run(user_input)
    print(f"Gate Output: {result}")

if __name__ == "__main__":
HEAD
    main()

