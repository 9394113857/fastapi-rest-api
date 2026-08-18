# 📋 Get All Mobiles:
Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/" -Method Get

# 🔎 Get Mobile By ID
Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/1" -Method Get


# ➕ Next: POST/Create
$body = @{
    name = "iPhone 17"
    price = 79999
    ram = "8GB"
    storage = "256GB"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/" -Method Post -ContentType "application/json" -Body $body

📱 name    : iPhone 17
💰 price   : 79999
🧠 ram     : 8GB
💾 storage : 256GB
🆔 id      : 1


# ✏️ Update Mobile:
$body = @{
    name = "iPhone 17 Pro"
    price = 99999
    ram = "12GB"
    storage = "512GB"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/1" -Method Put -ContentType "application/json" -Body $body

# 🔎 Next: verify the updated record:
Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/1" -Method Get

# 🗑️ Final CRUD operation: DELETE:
Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/1" -Method Delete

# 🏁 One final verification:
Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/" -Method Get

ep brooo 😎🔥 that is normal. Nothing is broken.

Invoke-RestMethod gives you no visible output for an empty JSON array [] in this PowerShell situation.

We already know the DELETE succeeded:

Mobile deleted successfully

So /mobiles/ is empty. ✅

# 🔎 If you want to see the actual []:
(Invoke-RestMethod -Uri "http://127.0.0.1:5000/mobiles/" -Method Get) | ConvertTo-Json

or 

curl.exe http://127.0.0.1:5000/mobiles/

That is exactly correct after deleting the only record. ✅

🏆 Backend local checkpoint complete
🐍 FastAPI                  ✅
🏗️ Modular architecture    ✅
📦 Repository layer        ✅
⚙️ Service layer           ✅
📋 Pydantic schemas        ✅
🗄️ SQLAlchemy              ✅
🔄 Alembic                 ✅
💾 SQLite                  ✅
❤️ Health endpoint         ✅
➕ POST                     ✅
📋 GET                     ✅
🔎 GET by ID               ✅
✏️ PUT                     ✅
🗑️ DELETE                  ✅

And importantly, we haven't touched the frontend. 😎

🛑 Now STOP the server

