def lambda_handler(event, context):
    name = event["name"]
    print(f"Hello, {name}!")

if __name__ == "__main__":
    lambda_handler({"name": "Daniel"}, None)