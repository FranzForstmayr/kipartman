# coding: utf-8

"""
    Kipartman

    Kipartman api specifications

    OpenAPI spec version: 1.0.0
    Contact: --
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Manufacturer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, website=None, email=None, phone=None, comment=None, id=None):
        """
        Manufacturer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'address': 'str',
            'website': 'str',
            'email': 'str',
            'phone': 'str',
            'comment': 'str',
            'id': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'address': 'address',
            'website': 'website',
            'email': 'email',
            'phone': 'phone',
            'comment': 'comment',
            'id': 'id'
        }

        self._name = name
        self._address = address
        self._website = website
        self._email = email
        self._phone = phone
        self._comment = comment
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Manufacturer.

        :return: The name of this Manufacturer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Manufacturer.

        :param name: The name of this Manufacturer.
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Manufacturer.

        :return: The address of this Manufacturer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Manufacturer.

        :param address: The address of this Manufacturer.
        :type: str
        """

        self._address = address

    @property
    def website(self):
        """
        Gets the website of this Manufacturer.

        :return: The website of this Manufacturer.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this Manufacturer.

        :param website: The website of this Manufacturer.
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """
        Gets the email of this Manufacturer.

        :return: The email of this Manufacturer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Manufacturer.

        :param email: The email of this Manufacturer.
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this Manufacturer.

        :return: The phone of this Manufacturer.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Manufacturer.

        :param phone: The phone of this Manufacturer.
        :type: str
        """

        self._phone = phone

    @property
    def comment(self):
        """
        Gets the comment of this Manufacturer.

        :return: The comment of this Manufacturer.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Manufacturer.

        :param comment: The comment of this Manufacturer.
        :type: str
        """

        self._comment = comment

    @property
    def id(self):
        """
        Gets the id of this Manufacturer.

        :return: The id of this Manufacturer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Manufacturer.

        :param id: The id of this Manufacturer.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

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
        if not isinstance(other, Manufacturer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
