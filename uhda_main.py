from config import get_env
from app import create_flask_app

# Jacob Pauls
# Nov 21, 2020
# uhda_main.py

app = create_flask_app()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)