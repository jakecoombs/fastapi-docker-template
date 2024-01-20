def test_read_root(api_client):
    # Given
    expected_response = {"msg": "Hello World"}

    # When
    response = api_client.get("/")

    # Then
    assert response.status_code == 200
    assert response.json() == expected_response
