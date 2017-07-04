# coding: utf-8

"""
    Simple API

    A simple API to learn how to write OpenAPI Specification

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name=None, last_name=None, username=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'username': 'username'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._username = username

    @property
    def first_name(self):
        """
        Gets the first_name of this InlineResponse200.

        :return: The first_name of this InlineResponse200.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this InlineResponse200.

        :param first_name: The first_name of this InlineResponse200.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this InlineResponse200.

        :return: The last_name of this InlineResponse200.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this InlineResponse200.

        :param last_name: The last_name of this InlineResponse200.
        :type: str
        """

        self._last_name = last_name

    @property
    def username(self):
        """
        Gets the username of this InlineResponse200.

        :return: The username of this InlineResponse200.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this InlineResponse200.

        :param username: The username of this InlineResponse200.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
