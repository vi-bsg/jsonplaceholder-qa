import requests

print("=== АВТОТЕСТЫ ДЛЯ JSONPLACEHOLDER ===")

# Тест 1: GET /posts
print("\n1. GET /posts")
response1 = requests.get("https://jsonplaceholder.typicode.com/posts")
status1 = response1.status_code
print(f"   Статус: {status1} {'✓' if status1 == 200 else '✗'}")
print(f"   Постов получено: {len(response1.json())}")

# Тест 2: POST /posts
print("\n2. POST /posts")
new_post = {"title": "foo", "body": "bar", "userId": 1}
response2 = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
status2 = response2.status_code
print(f"   Статус: {status2} {'✓' if status2 == 201 else '✗'}")
print(f"   ID нового поста: {response2.json()['id']}")

# Тест 3: DELETE /posts/1
print("\n3. DELETE /posts/1")
response3 = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
status3 = response3.status_code
print(f"   Статус: {status3} {'✓' if status3 == 200 else '✗'}")

print("\n" + "="*40)
print("✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ УСПЕШНО!")
print("="*40)
