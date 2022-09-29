def test_save_correct_user_should_return_200(user):
    response = user.post('/users/register', json={'name':'ghiyati', 'surname': 'issam',
                                                  'email': 'issam@gmail.com', 'password':'123456789'})
    assert response.status_code == 200
    assert response.is_json == True


def test_login_correct_user_should_return_string(user):
    response = user.post('/users/login', json={'email': 'issam@gmail.com', 'password':'123456789'})
    assert response.status_code == 200
    assert isinstance(response.json, str)


def test_save_user_with_same_email_should_return_error(user):
    import random
    import string
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(20))
    # posting user with this email the 1st time
    user.post('/users/register', json={'name': name, 'surname': 'user',
                                       'email': name, 'password': '111'})

    # posting user with this email the 2nd time
    response = user.post('/users/register', json={'name': name, 'surname': 'user',
                                                  'email': name, 'password': '111'})

    assert response.status_code != 200
