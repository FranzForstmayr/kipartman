# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.distributor_data import DistributorData
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Distributor(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, website=None, sku_url=None, email=None, phone=None, comment=None, allowed=None, id=None):
        """
        Distributor - a model defined in Swagger

        :param name: The name of this Distributor.
        :type name: str
        :param address: The address of this Distributor.
        :type address: str
        :param website: The website of this Distributor.
        :type website: str
        :param sku_url: The sku_url of this Distributor.
        :type sku_url: str
        :param email: The email of this Distributor.
        :type email: str
        :param phone: The phone of this Distributor.
        :type phone: str
        :param comment: The comment of this Distributor.
        :type comment: str
        :param allowed: The allowed of this Distributor.
        :type allowed: bool
        :param id: The id of this Distributor.
        :type id: int
        """
        self.swagger_types = {
            'name': str,
            'address': str,
            'website': str,
            'sku_url': str,
            'email': str,
            'phone': str,
            'comment': str,
            'allowed': bool,
            'id': int
        }

        self.attribute_map = {
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

        self._name = name
        self._address = address
        self._website = website
        self._sku_url = sku_url
        self._email = email
        self._phone = phone
        self._comment = comment
        self._allowed = allowed
        self._id = id

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Distributor of this Distributor.
        :rtype: Distributor
        """
        return deserialize_model(dikt, cls)

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
        :type name: str
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
        :type address: str
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
        :type website: str
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
        :type sku_url: str
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
        :type email: str
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
        :type phone: str
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
        :type comment: str
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
        :type allowed: bool
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
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

