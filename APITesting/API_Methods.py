import json

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    request = p.request.new_context()

    # Get Request
    response = request.get("https://jsonplaceholder.typicode.com/posts/15")

    print(response.status)
    print(response.headers)
    print(response.body())
    print(response.json())

    assert response.status == 200

    # POST Request
    payload = {
        "userId": 20,
        "title": "Playwright",
        "body": "API Testing"
    }
    with open("user.json", "r") as file:
        payload = json.load(file)

    response = request.post("https://jsonplaceholder.typicode.com/posts",
                            data = payload
                            )

    assert response.status == 201
    print(response.json())

    # PUT
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1,
    }

    response = request.post("https://jsonplaceholder.typicode.com/posts/1",
                           data=payload
                           )

    print(response.status)
    assert response.status == 200

    # Delete Request
    response = request.delete("https://jsonplaceholder.typicode.com/posts/1")

    print(response.status)
    assert response.status == 200