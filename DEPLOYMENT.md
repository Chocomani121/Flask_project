# VPS Deployment Guide

## Deploy to VPS at 45.77.35.16

### Prerequisites
- SSH access to VPS
- Python 3.8+ installed on VPS
- MySQL/MariaDB database access

### Step 1: Connect to VPS via SSH
```bash
ssh root@45.77.35.16
# or
ssh your_username@45.77.35.16
```

### Step 2: Clone Repository
```bash
cd /home
git clone https://github.com/Chocomani121/Flask_project.git
cd Flask_project
```

### Step 3: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables
Create a `.env` file in the project root:
```bash
cp .env.example .env
nano .env  # Edit with your credentials
```

Fill in your production values:
```
SECRET_KEY=your_production_secret_key_here
SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@host:port/database
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

### Step 6: Update app/__init__.py
Change the import from `ConfigDevelopment` to `Config`:
```python
from app.config import Config

def create_app(config_class=Config):
    # ...
```

This will use environment variables instead of hardcoded credentials.

### Step 7: Test the App
```bash
python3 run.py
# Should see: Running on http://127.0.0.1:5000
```

### Step 8: Setup Gunicorn (Production Server)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Step 9: Setup Nginx (Reverse Proxy) - Optional
Create `/etc/nginx/sites-available/flask_app`:
```nginx
server {
    listen 80;
    server_name 45.77.35.16;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /home/Flask_project/app/static;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 10: Setup Systemd Service (Auto-start)
Create `/etc/systemd/system/flask_app.service`:
```ini
[Unit]
Description=Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/home/Flask_project
ExecStart=/home/Flask_project/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable flask_app
sudo systemctl start flask_app
sudo systemctl status flask_app
```

### Troubleshooting
- Check logs: `journalctl -u flask_app -n 50 -f`
- Check port: `sudo netstat -tuln | grep 5000`
- Test DB connection: `mysql -h your_host -u username -p database`

