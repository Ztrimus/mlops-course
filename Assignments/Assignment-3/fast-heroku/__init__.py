from app.fastapp import app
import uvicorn
# main driver function
if __name__ == "__main__":
    uvicorn.run(app)