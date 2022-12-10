import pytest
from pytest_django_crud.models import *
from response_methods import *
from loguru import logger
import requests
import json
from django.db import connection
from django.test.client import encode_multipart, MULTIPART_CONTENT, BOUNDARY
# pytest.mark.django_db(transaction=True)


@pytest.mark.django_db
def test_valid_data(end_point,
                              payload,
                              request_method,
                              formdata,
                              content_type,
                              expected_data):
    logger.info(f'Validating end point : {end_point}')
    end_point = end_point + '?'
    for param in payload:
        end_point = end_point + '&' + param + "=" + str(payload[param])
    # Post Method Validations
    logger.info(f'Validating End Point : {end_point}')
    if request_method == 'post':
        if content_type == '':
            content_type = MULTIPART_CONTENT if request_method == 'post'\
                else 'application/octet-stream'
        response = server.post(end_point,
                               data=formdata,
                               content_type=content_type,
                               secure=True)
        validate_response_status_code(response.status_code)

        model_name = eval(list(expected_data.keys())[0])
        filter_data = list(expected_data.values())[0]
        instance = model_name.objects.filter(**filter_data).all().values()
        logger.info("*" * 100)
        logger.info("In Post")
        logger.info(filter_data)
        logger.info(instance)
        if not instance:
            pytest.fail('Data is not inserted into db...!!')

    elif request_method == 'delete':
        response = server.delete(end_point,
                               data=formdata,
                               secure=True)
        validate_response_status_code(response.status_code)
        model_name = eval(list(expected_data.keys())[0])
        filter_data = list(expected_data.values())[0]
        instance = model_name.objects.filter(**filter_data).all().values()
        logger.info("*" * 100)
        logger.info("In Delete")
        logger.info(filter_data)
        logger.info(instance)
        if instance:
            pytest.fail('Data is not deleted from db...!!')
    
    elif request_method == 'patch':
        if content_type == '':
            content_type = "application/octet-stream"
        response = server.patch(end_point,
                               data=formdata,
                               content_type=content_type,
                               secure=True)
        validate_response_status_code(response.status_code)
        model_name = eval(list(expected_data.keys())[0])
        filter_data = list(expected_data.values())[0]
        instance = model_name.objects.filter(**filter_data).all().values()
        logger.info("*" * 100)
        logger.info("In Patch")
        logger.info(filter_data)
        logger.info(instance)
        if not instance:
            pytest.fail('Data is not inserted into db...!!')
    
    # Get Method Validations
    else:
        response = server.get(
            end_point, secure=True)
        validate_response_status_code(response.status_code)
        response_content = get_response_content(response)
        logger.info('In Get')
        logger.info(response_content)
        logger.info(expected_data)
        if {'content_validation': False} == expected_data:
            return ' '
        if 'str' in str(type(expected_data)):
            validate_str_content(actual_data=response_content,
                                 expected_data=expected_data)
        elif 'dict' in str(type(expected_data)):
            validate_response_content(actual_response=response_content,
                                       expected_response=expected_data)
        elif ('list' in str(type(expected_data)) and len(expected_data) == 0)\
                or ('dict' in str(type(expected_data)
                                  ) and len(expected_data) == 0):
            validate_str_content(actual_data=response_content,
                                  expected_data=expected_data)
        elif 'dict' in str(type(expected_data[0])):
            validate_response_content(actual_response=response_content[0],
                                       expected_response=expected_data[0])
