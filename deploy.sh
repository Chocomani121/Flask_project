#!/bin/bash
# Flask App Deployment Script for VPS

set -e

VPS_IP="45.77.35.16"
PROJECT_PATH="/home/Flask_project"
VENV_PATH="$PROJECT_PATH/venv"

echo "Starting Flask App Deployment to VPS..."

# Step 1: Connect and prepare VPS
echo "Step 1: Preparing VPS..."
ssh root@$VPS_IP << 'EOF'
    # Update system
    apt-get update
    apt-get install -y python3 python3-pip python3-venv git mysql-client nginx
    
    # Create project directory
    mkdir -p /home
    cd /home
    
    # Clone or update repository
    if [ -d "Flask_project" ]; then
        cd Flask_project
        git pull origin main
    else
        git clone https://github.com/Chocomani121/Flask_project.git
        cd Flask_project
    fi
    
    # Create virtual environment
    python3 -m venv venv
    source venv/bin/activate
    
    # Install dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install gunicorn
    
    # Create .env if it doesn't exist
    if [ ! -f ".env" ]; then
        cp .env.example .env
        echo "⚠️  Please edit .env with your production credentials"
    fi
    
    echo "✅ VPS Preparation Complete!"
    echo "Next steps:"
    echo "1. Edit .env file with production credentials"
    echo "2. Update app/__init__.py to use Config instead of ConfigDevelopment"
    echo "3. Run: gunicorn -c gunicorn_config.py run:app"
EOF

echo "✅ Deployment script completed!"
echo "Connect to VPS and verify:"
echo "  ssh root@$VPS_IP"
echo "  cd /home/Flask_project"
echo "  source venv/bin/activate"
echo "  python run.py"
