from typesafe_sdk import Choice, TypeSafeClient

message = input("請輸入一句客服問題：")

with TypeSafeClient() as client:
    response = client.system_one(
        state=message,
        questions={
            "department": Choice(
                instructions="判斷這個問題應該屬於哪一類",
                criteria={
                    "account": "登入、密碼、帳號、安全性問題",
                    "billing": "付款、扣款、訂閱、退款問題",
                    "technical": "程式錯誤、功能異常、系統技術問題",
                    "other": "其他問題"
                }
            )
        }
    )

result = response.answers["department"]

print("分類結果：", result.choice)
print("信心值：", result.confidence)
print("各類別機率：", result.probabilities)