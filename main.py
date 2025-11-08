from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Renewable Energy Info API",
    description="A simple FastAPI app providing structured data about various renewable energy sources.",
    version="1.1.0"
)

# Enable CORS for frontend integration (React, Vue, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------------------------
# 📚 Renewable Energy Data
# --------------------------------------------------------------------
ENERGY_DATA = {
    "solar": {
        "type": "Renewable Energy",
        "source": "Sunlight",
        "description": "Solar energy captures energy from the sun and converts it into heat or electricity.",
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
    },
    "wind": {
        "type": "Renewable Energy",
        "source": "Wind currents",
        "description": "Wind energy converts the kinetic energy from moving air into electricity using wind turbines.",
        "advantages": [
            "Zero emissions during operation",
            "Highly scalable for large or small installations",
            "Efficient use of land space (e.g., farms)",
            "Low operational costs"
        ],
        "uses": {
            "electricity": True,
            "heating": False,
            "lighting": True,
            "transportation": False
        }
    },
    "hydro": {
        "type": "Renewable Energy",
        "source": "Flowing water",
        "description": "Hydropower harnesses the energy of moving water, typically from rivers or dams, to generate electricity.",
        "advantages": [
            "Reliable and continuous power source",
            "Can provide water storage and flood control",
            "Low greenhouse gas emissions",
            "Efficient energy conversion"
        ],
        "uses": {
            "electricity": True,
            "heating": False,
            "lighting": True,
            "transportation": False
        }
    },
    "geothermal": {
        "type": "Renewable Energy",
        "source": "Earth’s internal heat",
        "description": "Geothermal energy taps into the Earth's natural heat for power generation and direct heating applications.",
        "advantages": [
            "Stable energy production (24/7)",
            "Small land footprint",
            "Low emissions",
            "Highly efficient for heating systems"
        ],
        "uses": {
            "electricity": True,
            "heating": True,
            "lighting": False,
            "transportation": False
        }
    },
    "biomass": {
        "type": "Renewable Energy",
        "source": "Organic materials (plants, waste, wood)",
        "description": "Biomass energy uses organic materials to produce heat, electricity, or biofuels for transportation.",
        "advantages": [
            "Utilizes waste products",
            "Carbon neutral (if managed sustainably)",
            "Can be stored and used on demand",
            "Reduces landfill waste"
        ],
        "uses": {
            "electricity": True,
            "heating": True,
            "lighting": True,
            "transportation": True
        }
    }
}

# --------------------------------------------------------------------
# 🌍 Routes
# --------------------------------------------------------------------

@app.get("/")
def home():
    """Root endpoint with a friendly welcome message."""
    return {
        "message": "Welcome to the Renewable Energy Info API 🌞",
        "available_endpoints": {
            "list_all": "/list",
            "get_specific": "/energy/{type}",
            "example": "/energy/solar"
        },
        "info": "This API provides information about different renewable energy sources."
    }


@app.get("/list")
def list_energy_sources():
    """List all available renewable energy types."""
    return {"available_sources": list(ENERGY_DATA.keys())}


@app.get("/energy/{energy_type}")
def get_energy_info(energy_type: str):
    """Get information about a specific type of renewable energy."""
    energy_type = energy_type.lower()
    if energy_type not in ENERGY_DATA:
        raise HTTPException(status_code=404, detail="Energy type not found.")
    return ENERGY_DATA[energy_type]


@app.get("/compare/{type1}/{type2}")
def compare_energy_sources(type1: str, type2: str):
    """Compare advantages between two renewable energy sources."""
    type1, type2 = type1.lower(), type2.lower()

    if type1 not in ENERGY_DATA or type2 not in ENERGY_DATA:
        raise HTTPException(status_code=404, detail="One or both energy types not found.")

    advantages_1 = set(ENERGY_DATA[type1]["advantages"])
    advantages_2 = set(ENERGY_DATA[type2]["advantages"])

    comparison = {
        "energy_1": type1,
        "energy_2": type2,
        "common_advantages": list(advantages_1 & advantages_2),
        "unique_to_energy_1": list(advantages_1 - advantages_2),
        "unique_to_energy_2": list(advantages_2 - advantages_1)
    }

    return comparison

