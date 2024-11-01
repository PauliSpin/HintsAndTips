import json

def generate_and_read_json():
    # Create a Python dictionary
    data = {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "skills": ["Python", "JavaScript", "Data Analysis"],
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        }
    }

    # Convert the dictionary to a JSON string and save to a file
    json_output = json.dumps(data, indent=4)
    with open("output.json", "w") as json_file:
        json_file.write(json_output)
    
    print("JSON output created and saved to output.json")

    # Read the JSON content from the file
    with open("output.json", "r") as json_file:
        loaded_data = json.load(json_file)
    
    print("JSON content read from output.json:")
    print(json.dumps(loaded_data, indent=4))

# Call the function
generate_and_read_json()
