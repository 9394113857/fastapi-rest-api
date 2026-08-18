New-Item -ItemType Directory -Force app, app\core, app\db, app\models, app\schemas, app\repositories, app\services, app\api, app\api\routes, tests | Out-Null

New-Item -ItemType File -Force `
    app\__init__.py, `
    app\core\__init__.py, `
    app\db\__init__.py, `
    app\models\__init__.py, `
    app\schemas\__init__.py, `
    app\repositories\__init__.py, `
    app\services\__init__.py, `
    app\api\__init__.py, `
    app\api\routes\__init__.py | Out-Null

 #   tree /F

# 🔍 Just check the directories:
Get-ChildItem app -Directory


# 🛠️ Now create the Python package files:
New-Item -ItemType File -Force app\__init__.py, app\core\__init__.py, app\db\__init__.py, app\models\__init__.py, app\schemas\__init__.py, app\repositories\__init__.py, app\services\__init__.py, app\api\__init__.py, app\api\routes\__init__.py | Out-Null

# Then verify:
Get-ChildItem app -Recurse -Filter "__init__.py"

# ▶️ Start the server:
uvicorn app.main:app --reload --port 5000


