

# ☀️ Renewable Energy Info API (FastAPI)

A simple and educational **FastAPI** web application that provides structured information about **solar energy**.  
It demonstrates how to build a lightweight REST API in Python, with **CORS support** for frontend integration (e.g., React, Vue, or plain JavaScript apps).

----------

## 🚀 Features

-   ⚡ Built with **FastAPI**, one of the fastest Python web frameworks
    
-   🌍 **CORS enabled**, allowing easy frontend integration
    
-   🔆 Returns detailed **solar energy information** in JSON format
    
-   🧩 Clean, modular structure for easy expansion (add more energy types later)
    
-   💻 Ready for deployment on **Render**, **Railway**, or **Vercel**
    

----------

## 🧱 Project Structure

```
renewable-energy-api/
│
├── main.py           # FastAPI app (the code you provided)
├── requirements.txt  # Dependencies (optional but recommended)
└── README.md         # Project documentation

```

----------

## 🧩 Example Response

### Endpoint

```
GET /

```

### Response JSON

```json
{
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
    "electricity": true,
    "heating": true,
    "lighting": true,
    "transportation": false
  }
}

```

----------

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/abdellahaarab/fastapi-solar-energy.git
cd fastapi-solar-energy

```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

```

### 3️⃣ Install dependencies

Create a file `requirements.txt` (if you don’t already have one):

```txt
fastapi
uvicorn

```

Then install:

```bash
pip install -r requirements.txt

```

----------

## ▶️ Run the Server

Start the FastAPI app with **Uvicorn**:

```bash
uvicorn main:app --reload

```

You should see something like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000

```

----------

## 🌐 Test the API

Open your browser or use **curl**:

```bash
curl http://127.0.0.1:8000/

```

Or visit directly:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You’ll get the solar energy JSON response.

----------

## 🔄 CORS Configuration

This line enables cross-origin requests (useful for frontends):

```python
allow_origins=["*"]

```

⚠️ In production, **replace `"*"`** with your actual frontend domain, for example:

```python
allow_origins=["https://yourfrontend.app"]

```

----------

## 🧰 Technologies Used

Component

Description

**FastAPI**

Modern, high-performance web framework for Python

**Uvicorn**

ASGI server for running FastAPI apps

**CORS Middleware**

Enables safe frontend-backend communication

----------

## 🧪 Example Frontend Integration

Here’s how you could fetch the API data using **JavaScript**:

```html
<script>
fetch("http://127.0.0.1:8000/")
  .then(res => res.json())
  .then(data => {
    console.log("Energy Info:", data);
    document.body.innerHTML = `
      <h1>${data.type}</h1>
      <p>${data.description}</p>
      <ul>${data.advantages.map(a => `<li>${a}</li>`).join("")}</ul>
    `;
  });
</script>

```

----------

## 🌞 Future Improvements

-   Add multiple renewable sources (wind, hydro, geothermal)
    
-   Create a `/energy/{type}` endpoint to retrieve specific energy info
    
-   Build a simple TailwindCSS-based frontend dashboard
    

----------

## 🧑‍💻 Author

**Dr. Abdellah**  
🎥 YouTube: [@dkn4.hackers](https://www.youtube.com/@dkn4.hackers)  
💡 Developer | Educator | Renewable Energy & AI Projects

----------

## 🛡️ License

Licensed under the **MIT License** — free to use, modify, and share with attribution.
