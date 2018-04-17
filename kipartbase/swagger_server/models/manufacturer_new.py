# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.manufacturer_data import ManufacturerData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ManufacturerNew(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, website=None, email=None, phone=None, comment=None):
        """
        ManufacturerNew - a model defined in Swagger

        :param name: The name of this ManufacturerNew.
        :type name: str
        :param address: The address of this ManufacturerNew.
        :type address: str
        :param website: The website of this ManufacturerNew.
        :type website: str
        :param email: The email of this ManufacturerNew.
        :type email: str
        :param phone: The phone of this ManufacturerNew.
        :type phone: str
        :param comment: The comment of this ManufacturerNew.
        :type comment: str
        """
        self.swagger_types = {
            'name': str,
            'address': str,
            'website': str,
            'email': str,
            'phone': str,
            'comment': str
        }

        self.attribute_map = {
            'name': 'name',
            'address': 'address',
            'website': 'website',
            'email': 'email',
            'phone': 'phone',
            'comment': 'comment'
        }

        self._name = name
        self._address = address
        self._website = website
        self._email = email
        self._phone = phone
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManufacturerNew of this ManufacturerNew.
        :rtype: ManufacturerNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this ManufacturerNew.

        :return: The name of this ManufacturerNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManufacturerNew.

        :param name: The name of this ManufacturerNew.
        :type name: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this ManufacturerNew.

        :return: The address of this ManufacturerNew.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ManufacturerNew.

        :param address: The address of this ManufacturerNew.
        :type address: str
        """

        self._address = address

    @property
    def website(self):
        """
        Gets the website of this ManufacturerNew.

        :return: The website of this ManufacturerNew.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this ManufacturerNew.

        :param website: The website of this ManufacturerNew.
        :type website: str
        """

        self._website = website

    @property
    def email(self):
        """
        Gets the email of this ManufacturerNew.

        :return: The email of this ManufacturerNew.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ManufacturerNew.

        :param email: The email of this ManufacturerNew.
        :type email: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this ManufacturerNew.

        :return: The phone of this ManufacturerNew.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this ManufacturerNew.

        :param phone: The phone of this ManufacturerNew.
        :type phone: str
        """

        self._phone = phone

    @property
    def comment(self):
        """
        Gets the comment of this ManufacturerNew.

        :return: The comment of this ManufacturerNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this ManufacturerNew.

        :param comment: The comment of this ManufacturerNew.
        :type comment: str
        """

        self._comment = comment

