# examples/test_logic.py
from src.gate import LogicalGate

def run_test():
    gate = LogicalGate()
    
    print("--- 1bit_Lie < Unknown : テスト開始 ---")
    
    # 1. 正常系テスト（真実）
    test_truth = "2026年の東京の気温は平均25度である。"
    result1 = gate.run(test_truth)
    print(f"入力: {test_truth}")
    print(f"出力: {result1}")
    assert result1 != "Unknown: Verification Failed", "真実が遮断されました"
    print("→ [OK] 真実の通過を確認")
    
    # 2. 異常系テスト（嘘・感情論）
    test_lie = "AIはなんとなく最強な気がする。"
    result2 = gate.run(test_lie)
    print(f"\n入力: {test_lie}")
    print(f"出力: {result2}")
    assert result2 == "Unknown: Verification Failed", "嘘が遮断されませんでした！"
    print("→ [OK] 感情論の遮断を確認")
    
    print("\n--- 全テスト成功：論理ゲートは正常に機能しています ---")

if __name__ == "__main__":
    run_test()