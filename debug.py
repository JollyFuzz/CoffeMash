import sys
sys.path.append(".")
from orders.app import app


if __name__ == "__main__":
    # Используем uvicorn с поддержкой перезагрузки и логирования ошибок
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)