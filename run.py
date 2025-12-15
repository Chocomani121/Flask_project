from app import create_app
from app.config import ConfigDevelopment
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


#python3.14 run.py to run 