## Reservamos Weather API

This repository contains a Flask API that allows users to compare the weather forecasts for the next 5 days of two different cities offered by Reservamos.

**Features:**

- Retrieves weather data from the OpenWeatherMap API using geographic coordinates provided by the Reservamos API.
- Compares weather forecasts for two cities upon request.
- Exposes an API endpoint `/weather/<city>` (GET) to retrieve weather data for a specific city.

**Requirements:**

- Python 3.8
- Flask
- requests

**Installation:**

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/reservamos-weather-api.git
   ```

2. Replace `API_KEY` and `RESERVAMOS_API_URL` in the `Dockerfile` with your actual OpenWeatherMap API key.

3. Install dependencies (recommended using a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

**Running the App:**

**Option 1: Using Docker:**

1. Build the Docker image:

   ```bash
   docker build -t weather-api .
   ```

2. Run the container:

   ```bash
   docker run -p 5000:5000 weather-api
   ```

**Option 2: Running Directly (Development):**

1. Start the development server:

   ```bash
   python app.py
   ```

**API Usage:**

Send a GET request to:

```
http://localhost:5000/weather/<city>
```

Replace `<city>` with the name of the desired city.

**Example Response:**

```json
{
  "city": "monterrey",
  "forecast": [
    {
      "date": "2024-02-28T00:00:00Z",
      "max_temp": 28.32,
      "min_temp": 15.44,
      "weather": "Cloud"
    },
    ...
  ]
}
```

**Environment Variables:**

- `API_KEY`: Your OpenWeatherMap API key (required)
- `RESERVAMOS_API_URL`: Reservamos API endpoint (required)

**Testing:**

Unit tests are included in the tests.py file to ensure the functionality of the API. You can run the tests using:

   ```bash
   python -m unittest tests.py
   ```

**Documentation:**

The API documentation is included within the Flask application's docstrings through comments. 

**Contributing:**

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

**License:**

This project is licensed under the MIT License. See the `LICENSE` file for details.
