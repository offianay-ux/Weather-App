# 🌤️ Weather App

A full-stack real-time weather application built with **Flask** and vanilla **HTML/CSS/JavaScript**. Features a cinematic animated UI with a bento-grid results layout.

---

## 📸 Features

- **Animated landing page** — title and search bar start large and centered, then smoothly animate up into a compact navbar after searching
- **Bento-grid layout** — weather results displayed in tiles of varying sizes across the full page width
- **Real-time data** — fetches live weather from the OpenWeatherMap API
- **Dynamic weather emojis** — icon changes based on current weather condition
- **Glassmorphism UI** — deep purple gradient background with glowing orbs and smooth animations
- **Full weather details** — temperature, feels like, min/max, humidity, wind speed, pressure, sunrise & sunset
- **Error handling** — graceful messages for invalid cities or network timeouts

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript (Fetch API) |
| API | OpenWeatherMap REST API |
| Fonts | Nunito + Outfit (Google Fonts) |

---

## 📁 Project Structure

```
Weather App/
├── main.py               # Flask backend
└── templates/
    └── index.html        # Frontend UI
```

---

## ⚙️ Setup & Installation

### 1. Clone or download the projec

### 2. Install dependencies

### 3. Run the app

### 4. Open in browser

To get your own free API key:
1. Sign up at [openweathermap.org](https://openweathermap.org)
2. Go to **API Keys** in your account dashboard
3. Copy your key and replace it in `main.py`

---

## 🌡️ How It Works

1. User types a city name and hits **Search**
2. The frontend sends a `GET` request to `/weather?city=<cityname>`
3. Flask calls the OpenWeatherMap API and parses the JSON response
4. Temperature is converted from **Kelvin → Celsius** (`K - 273.15`)
5. Sunrise/sunset Unix timestamps are formatted into readable time
6. Data is returned as JSON to the frontend and rendered in the bento grid



## 📦 Dependencies
flask
requests



## 📄 License

This project is open source and available under the [MIT License](LICENSE).
