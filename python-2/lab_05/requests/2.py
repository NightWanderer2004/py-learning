import requests

response = requests.get("https://random.dog/woof.json")

if response.status_code == 200:
    data = response.json()
    image_url = data["url"]

    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open("random_dog.jpg", "wb") as file:
            file.write(image_response.content)
        print("Image downloaded successfully!")
    else:
        print("Failed to download the image.")
else:
    print("Failed to fetch data from the API.")
