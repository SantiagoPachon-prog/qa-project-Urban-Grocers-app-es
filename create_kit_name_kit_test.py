import data
import sender_stand_request

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()["authToken"]
    return token

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    assert response.status_code == 201
    assert kit_body['name'] == response.json()['name']

def negative_assert(kit_parameter):
    response = sender_stand_request.post_new_client_kit(kit_parameter, get_new_user_token())

    assert response.status_code == 400

def test_1_name_with_one_character():
    current_kit_body = get_kit_body(data.test_1)
    positive_assert(current_kit_body)

def test_2_max_characters_511():
    current_kit_body = get_kit_body(data.test_2)
    positive_assert(current_kit_body)

def test_3_no_characters():
    current_kit_body = get_kit_body(data.test_3)
    negative_assert(current_kit_body)

def test_4_max_characters_exceeded():
    current_kit_body = get_kit_body(data.test_4)
    negative_assert(current_kit_body)

def test_5_special_characters():
    current_kit_body = get_kit_body(data.test_5)
    positive_assert(current_kit_body)

def test_6_spaces_allowed():
    current_kit_body = get_kit_body(data.test_6)
    positive_assert(current_kit_body)

def test_7_includes_numbers_allowed():
    current_kit_body = get_kit_body(data.test_7)
    positive_assert(current_kit_body)

def test_8_no_kit_name():
    current_kit_body = get_kit_body(data.test_8)
    negative_assert(current_kit_body)

def test_9_type_numbers_only():
    current_kit_body = get_kit_body(data.test_9)
    negative_assert(current_kit_body)






