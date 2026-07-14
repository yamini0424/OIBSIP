import requests

# Enter your WeatherAPI key here
API_KEY = "22a4b68e33d2411793c142700261407"

print("=" * 40)
print("      WEATHER APPLICATION")
print("=" * 40)

while True:
    location = input("\nEnter City Name or ZIP Code: ").strip()

    # Check if input is empty
    if location == "":
        print("Please enter a valid city or ZIP code.")
        continue

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if API returned an error
        if "error" in data:
            print("\nError:", data["error"]["message"])
        else:
            print("\n------ Current Weather ------")
            print("City          :", data["location"]["name"])
            print("Region        :", data["location"]["region"])
            print("Country       :", data["location"]["country"])
            print("Temperature   :", data["current"]["temp_c"], "°C")
            print("Humidity      :", data["current"]["humidity"], "%")
            print("Condition     :", data["current"]["condition"]["text"])
            print("Wind Speed    :", data["current"]["wind_kph"], "km/h")
            print("------------------------------")

    except requests.exceptions.ConnectionError:
        print("No internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except Exception as e:
        print("An unexpected error occurred:", e)

    choice = input("\nDo you want to search another location? (Y/N): ").strip().lower()

    if choice != "y":
        print("\nThank you for using the Weather Application!")
        break