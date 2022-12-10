import pytest
from loguru import logger
from django.db import connection


def list_compare(list1: list, list2: list, key: str = 'all_keys'):
    if list1 == list2:
        return True
    list1, list2 = set(list1), set(list2)
    matched_elements_in_list = list(set(list1).intersection(list2))
    mismatch_elements_list1 = list(list1 - list2)
    mismatch_elements_list2 = list(list2 - list1)
    pytest.fail(f'Data :{key} is not matching with the expected...!!'
                f'Matching values : {matched_elements_in_list}'
                f'Extra keys in Actual Data: {mismatch_elements_list1}'
                f'Extra Keys in Expected Data : {mismatch_elements_list2}')


def validate_response_content(actual_response,
                              expected_response: dict,
                              response_key='response_key'):
    if 'dict' not in str(type(actual_response)):
        pytest.fail('Expected Data Type : dict '
                    f'but response is of type : {str(type(actual_response))}')
    list_compare(actual_response.keys(), expected_response.keys(),
                 key=response_key)
    for response_key in actual_response:
        if 'list' in str(type(actual_response[response_key])) \
                and actual_response[response_key] \
                and 'dict' in str(type(actual_response[response_key][0])):
            logger.info(f'Validating keys from : {response_key}')
            validate_response_content(actual_response[response_key][0],
                                      expected_response[response_key][0],
                                      response_key=response_key)


def validate_response_status_code(status_code,
                                  expected_status_code: int = 200):
    if status_code != expected_status_code:
        pytest.fail('Status code is not matching with expected...!!'
                    f'Expected status code : {expected_status_code} Actual '
                    f'Status Code : {status_code}')


def connect_to_respective_schema(refnum):
    logger.info(f'Setting schema to {refnum}')
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {refnum}")


def validate_str_content(actual_data,
                         expected_data):
    if 'str' not in str(type(actual_data)):
        pytest.fail('Expected Data Type : Str '
                    f'but response is of type : {str(type(actual_data))}')
    if actual_data != expected_data:
        pytest.fail('Response content is not matching with expected '
                     f'Expected : {expected_data}',
                     f'Actual : {actual_data}')


def get_response_content(response):
    try:
        content = response.json()
    except:
        content = str(response.content)
    logger.info(f'Response Content is : {content}')
    return content
