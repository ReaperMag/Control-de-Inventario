from flask_sqlalchemy import SQLAlchemy
import os

from src import crear_app


app = crear_app()
# app.config.from_object(Config)
# print(app.config)





if __name__ == "__main__":
    
    port = int(os.environ.get("PORT",5000))
    
    app.run(debug=True, port=port, host = "0.0.0.0")