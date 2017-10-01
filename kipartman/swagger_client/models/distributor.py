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


class Distributor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'address': 'str',
        'website': 'str',
        'sku_url': 'str',
        'email': 'str',
        'phone': 'str',
        'comment': 'str',
        'allowed': 'bool',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'website': 'website',
        'sku_url': 'sku_url',
        'email': 'email',
        'phone': 'phone',
        'comment': 'comment',
        'allowed': 'allowed',
        'id': 'id'
    }

    def __init__(self, name=None, address=None, website=None, sku_url=None, email=None, phone=None, comment=None, allowed=None, id=None):
        """
        Distributor - a model defined in Swagger
        """

        self._name = None
        self._address = None
        self._website = None
        self._sku_url = None
        self._email = None
        self._phone = None
        self._comment = None
        self._allowed = None
        self._id = None

        if name is not None:
          self.name = name
        if address is not None:
          self.address = address
        if website is not None:
          self.website = website
        if sku_url is not None:
          self.sku_url = sku_url
        if email is not None:
          self.email = email
        if phone is not None:
          self.phone = phone
        if comment is not None:
          self.comment = comment
        if allowed is not None:
          self.allowed = allowed
        self.id = id

    @property
    def name(self):
        """
        Gets the name of this Distributor.

        :return: The name of this Distributor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Distributor.

        :param name: The name of this Distributor.
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Distributor.

        :return: The address of this Distributor.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Distributor.

        :param address: The address of this Distributor.
        :type: str
        """

        self._address = address

    @property
    def website(self):
        """
        Gets the website of this Distributor.

        :return: The website of this Distributor.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this Distributor.

        :param website: The website of this Distributor.
        :type: str
        """

        self._website = website

    @property
    def sku_url(self):
        """
        Gets the sku_url of this Distributor.

        :return: The sku_url of this Distributor.
        :rtype: str
        """
        return self._sku_url

    @sku_url.setter
    def sku_url(self, sku_url):
        """
        Sets the sku_url of this Distributor.

        :param sku_url: The sku_url of this Distributor.
        :type: str
        """

        self._sku_url = sku_url

    @property
    def email(self):
        """
        Gets the email of this Distributor.

        :return: The email of this Distributor.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Distributor.

        :param email: The email of this Distributor.
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this Distributor.

        :return: The phone of this Distributor.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Distributor.

        :param phone: The phone of this Distributor.
        :type: str
        """

        self._phone = phone

    @property
    def comment(self):
        """
        Gets the comment of this Distributor.

        :return: The comment of this Distributor.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Distributor.

        :param comment: The comment of this Distributor.
        :type: str
        """

        self._comment = comment

    @property
    def allowed(self):
        """
        Gets the allowed of this Distributor.

        :return: The allowed of this Distributor.
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """
        Sets the allowed of this Distributor.

        :param allowed: The allowed of this Distributor.
        :type: bool
        """

        self._allowed = allowed

    @property
    def id(self):
        """
        Gets the id of this Distributor.

        :return: The id of this Distributor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Distributor.

        :param id: The id of this Distributor.
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
        if not isinstance(other, Distributor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
