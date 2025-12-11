# Quick VPS Deployment Guide - 45.77.35.16

## Quick Start (3 Steps)

### 1. SSH to VPS
```bash
ssh root@45.77.35.16
```

### 2. Deploy
```bash
cd /home
git clone https://github.com/Chocomani121/Flask_project.git
cd Flask_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
cp .env.example .env
```

### 3. Edit Configuration
```bash
nano .env
```

Add your production credentials:
```
SECRET_KEY=generate_a_random_key_here
SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@database_host:3306/database_name
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

### 4. Update app/__init__.py
Change line 7 from:
```python
from app.config import ConfigDevelopment
```

To:
```python
from app.config import Config
```

And change line 23 from:
```python
def create_app(config_class=ConfigDevelopment):
```

To:
```python
def create_app(config_class=Config):
```

### 5. Test Locally
```bash
python3 run.py
# Visit: http://45.77.35.16:5000
```

### 6. Run with Gunicorn (Production)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

Or use config file:
```bash
gunicorn -c gunicorn_config.py run:app
```

## Using Systemd Service (Auto-start)

Create service file:
```bash
sudo nano /etc/systemd/system/flask_app.service
```

Paste:
```ini
[Unit]
Description=Flask Application
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/home/Flask_project
Environment="PATH=/home/Flask_project/venv/bin"
ExecStart=/home/Flask_project/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 run:app
Restart=always
RestartSec=10

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

Monitor logs:
```bash
journalctl -u flask_app -f
```

## Using Nginx as Reverse Proxy

```bash
sudo nano /etc/nginx/sites-available/flask_app
```

Paste:
```nginx
server {
    listen 80;
    server_name 45.77.35.16;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /home/Flask_project/app/static;
        expires 30d;
    }
}
```

Enable:
```bash
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Troubleshooting

**Port already in use:**
```bash
sudo lsof -i :5000
sudo kill -9 <PID>
```

**Permission denied:**
```bash
sudo chown -R www-data:www-data /home/Flask_project
```

**Database connection error:**
```bash
mysql -h your_db_host -u username -p
```

**Check Nginx logs:**
```bash
sudo tail -f /var/log/nginx/error.log
```

## Useful Commands

```bash
# Stop Flask app
sudo systemctl stop flask_app

# Start Flask app
sudo systemctl start flask_app

# Restart Flask app
sudo systemctl restart flask_app

# View logs
journalctl -u flask_app -n 50 -f

# Update code
cd /home/Flask_project
git pull origin main
sudo systemctl restart flask_app
```

