from bot.client import BinanceClient

client = BinanceClient()

result = client.test_connection()

print("\n========== RESULT ==========")

print(result)

print("============================")