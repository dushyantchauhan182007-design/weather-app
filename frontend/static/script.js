document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("getWeather");
  const cityInput = document.getElementById("cityInput");
  const resultDiv = document.getElementById("result");

  button.addEventListener("click", async () => {
    const city = cityInput.value.trim();
    resultDiv.innerHTML = ""; // clear previous results

    if (!city) {
      resultDiv.innerHTML = "<p>Please enter a city name.</p>";
      return;
    }

    try {
      const response = await fetch(`/weather?city=${encodeURIComponent(city)}`);
      const data = await response.json();

      if (data.error) {
        resultDiv.innerHTML = `<p>${data.error}</p>`;
        return;
      }

      resultDiv.innerHTML = `
        <div class="weather-card">
          <h2>${data.city}</h2>
          <img src="${data.icon}" alt="Weather icon">
          <p><strong>${data.temperature}°C</strong></p>
          <p>${data.description}</p>
        </div>
      `;
    } catch (err) {
      resultDiv.innerHTML = "<p>Error fetching weather data. Please try again.</p>";
      console.error(err);
    }
  });
});
