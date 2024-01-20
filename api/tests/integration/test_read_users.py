def test_read_users(api_client, users, set_up_users):
    # Given
    expected_users = users

    # When
    response = api_client.get("/users/")

    # Then
    assert response.status_code == 200
    assert len(response.json()) == len(expected_users)
