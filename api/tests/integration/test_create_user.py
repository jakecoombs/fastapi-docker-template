def test_create_user(api_client, users):
    # Given
    request = users[0]

    # When
    response = api_client.post("/users/", json=request)

    # Then
    assert response.status_code == 200

    json_response = response.json()
    assert json_response["name"] == request["name"]
    assert json_response["email"] == request["email"]
    assert "id" in json_response


def test_create_user_already_registered(api_client, users, set_up_users):
    # Given
    request = users[0]

    # When
    response = api_client.post("/users/", json=request)

    # Then
    assert response.status_code == 400
