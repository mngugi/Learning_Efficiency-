#!/usr/bin/env bash

set -e

echo "🚀 Starting Learning Efficiency (Production Mode)"

# 1️⃣ Create virtual environment if missing
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# 2️⃣ Activate virtual environment
source venv/bin/activate

# 3️⃣ Upgrade pip
pip install --upgrade pip

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Run migrations
echo "🗄️ Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Collect static files (important in production)
python manage.py collectstatic --noinput

# 7️⃣ Start Gunicorn WSGI server
echo "🌐 Starting Gunicorn server at http://127.0.0.1:8000"
gunicorn learning_efficiency.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
