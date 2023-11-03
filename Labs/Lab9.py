# Import the requests library
import requests

# Define the Node API endpoint
node_api_url = "http://localhost:3000/widgets"

# Make a GET request to the Node API
response = requests.get(node_api_url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Create an empty list to store the widget names and colors
    widget_list = []

    # Loop through the data and extract the name and color of each widget
    for widget in data:
        name = widget["name"]
        color = widget["color"]

        # Format the name and color as a string
        widget_string = f"{name}: {color}"

        # Append the string to the widget list
        widget_list.append(widget_string)

    # Join the widget list with newlines
    widget_list_string = "\n".join(widget_list)

    # Print the widget list string
    print(widget_list_string)

else:
    # Print an error message if the response is not successful
    print(f"Error: {response.status_code}")
