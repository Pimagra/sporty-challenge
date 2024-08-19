from assertpy import assert_that
from backend.clients.base.request import APIRequest
from backend.clients.cats_client import CatsClient

client = CatsClient()
api_request = APIRequest()

class TestBackend:

    # Test to validate that the random facts endpoint returns information correctly
    def test_get_random_facts(self):
        # Call the get random facts endpoint
        response = api_request.get(client.get_random_facts())

        # Assertions on the response
        assert_that(response.status_code, "Error in Endpoint. Code 200 was not returned").is_equal_to(200)
        assert_that(response.as_dict['_id'], "ID attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['user'], "User attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['text'], "Text attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['updatedAt'], "Updated At attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['type'], "Type attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['createdAt'], "Created At attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['deleted'], "Deleted attribute is not returned").is_type_of(bool)

    # Test to validate that getting facts by ID works correctly
    def test_get_fact_by_id(self):
        # Call the get fact by ID
        response = api_request.get(client.get_fact_by_id('591f98803b90f7150a19c229'))

        # Assertions on the response
        assert_that(response.status_code, "Error in Endpoint. Code 200 was not returned").is_equal_to(200)
        assert_that(response.as_dict['status']['verified'], "Verified attribute is not returned").is_type_of(bool)
        assert_that(response.as_dict['_id'], "ID attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['text'], "Text attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['source'], "Source attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['updatedAt'], "Updated At attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['type'], "Type attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['createdAt'], "Created At attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['deleted'], "Deleted attribute is not returned").is_type_of(bool)
        assert_that(response.as_dict['used'], "Used attribute is not returned").is_type_of(bool)
        assert_that(response.as_dict['user']['name']['first'], "First name attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['user']['name']['last'], "Last name attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['user']['_id'], "ID attribute is not returned").is_type_of(str)
        assert_that(response.as_dict['user']['photo'], "Photo attribute is not returned").is_type_of(str)

    # Negative test to validate that getting fact by a non-existing ID returns an error
    def test_negative_get_fact_by_non_existing_id(self):
        # Call endpoint with a non-existing ID
        response = api_request.get(client.get_fact_by_id('aaaaxxxxx'))

        # Assertions
        assert_that(response.status_code, "Error in Endpoint. Code 400 was not returned").is_equal_to(400)
        assert_that(response.as_dict['message']).is_equal_to('Cast to ObjectId failed for value "aaaaxxxxx" (type string) at path "_id" for model "Fact"')
