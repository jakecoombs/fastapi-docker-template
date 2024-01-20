def test_read_user(api_client, users, set_up_users):
    # Given
    user_id = 1
    expected_user = users[0]

    # When
    response = api_client.get(f"/users/{user_id}")

    # Then
    assert response.status_code == 200

    user = response.json()
    assert user["id"] == user_id
    assert user["name"] == expected_user["name"]
    assert user["email"] == expected_user["email"]


def test_read_user_not_found(api_client):
    # Given
    user_id = 1

    # When
    response = api_client.get(f"/users/{user_id}")

    # Then
    assert response.status_code == 404
