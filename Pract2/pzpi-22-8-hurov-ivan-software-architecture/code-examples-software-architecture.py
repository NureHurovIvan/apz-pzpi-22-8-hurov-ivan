# gateway.py — API Gateway для ChatGPT-подібного сервісу 
from fastapi import FastAPI, Request 
from services.auth_service import is_authenticated 
from services.chat_service import get_response 
 
app = FastAPI() 
 
@app.post("/chat") 
async def chat_endpoint(request: Request): 
    data = await request.json() 
    user_input = data.get("message") 
     
    # Авторизація користувача 
    if not is_authenticated(request): 
        return {"error": "Unauthorized"} 
 
    # Отримання відповіді з моделі 
    response = get_response(user_input) 
    return {"response": response} 
# services/chat_service.py — Обробка повідомлення через модель 
def get_response(message: str) -> str: 
    # У реальному світі тут була б інтеграція з GPT через API 
    if "hello" in message.lower(): 
        return "Hi there! How can I assist you today?" 
    return "Sorry, I didn't quite get that." 
# services/auth_service.py — Імітація авторизації 
def is_authenticated(request) -> bool: 
    # Простий приклад: авторизовано, якщо в заголовку є "X-Auth-Token" 
    return "X-Auth-Token" in request.headers
