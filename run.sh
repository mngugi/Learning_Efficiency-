#!/usr/bin/env bash

set -e  # Stop on first error

echo "🚀 Starting Learning Efficiency Backend..."

# 1️⃣ Create virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# 2️⃣ Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# 3️⃣ Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# 4️⃣ Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# 5️⃣ Run migrations
echo "🗄️ Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Optional superuser creation
read -p "👤 Create superuser? (y/n): " CREATE_USER
if [ "$CREATE_USER" = "y" ]; then
    python manage.py createsuperuser
fi

# 7️⃣ Run development server
echo "🌐 Starting development server at http://127.0.0.1:8000"
python manage.py runserver
