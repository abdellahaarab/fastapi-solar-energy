from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_energy_info():
    return {
        "type": "Renewable Energy",
        "source": "Sunlight",
        "description": "Solar energy is energy from the sun that is converted into thermal or electrical energy.",
        "advantages": [
            "Clean and sustainable",
            "Reduces electricity bills",
            "Low maintenance costs",
            "Reduces carbon footprint"
        ],
        "uses": {
            "electricity": True,
            "heating": True,
            "lighting": True,
            "transportation": False
        }
    }
