def test_save_correct_user_should_return_200(user):
    response = user.post('/users', json={'email': 'issam@gmail.com', 'password':'123456789', 'role':'admin'})
    assert response.status_code == 200
    assert response.is_json == True


def test_login_correct_user_should_return_string(user):
    response = user.post('/users/login', json={'email': 'issam@gmail.com', 'password':'123456789'})
    assert response.status_code == 200
    assert isinstance(response.json, str)

