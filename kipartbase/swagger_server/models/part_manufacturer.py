# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.manufacturer_data import ManufacturerData
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PartManufacturer(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, website=None, email=None, phone=None, comment=None, id=None, part_name=None):
        """
        PartManufacturer - a model defined in Swagger

        :param name: The name of this PartManufacturer.
        :type name: str
        :param address: The address of this PartManufacturer.
        :type address: str
        :param website: The website of this PartManufacturer.
        :type website: str
        :param email: The email of this PartManufacturer.
        :type email: str
        :param phone: The phone of this PartManufacturer.
        :type phone: str
        :param comment: The comment of this PartManufacturer.
        :type comment: str
        :param id: The id of this PartManufacturer.
        :type id: int
        :param part_name: The part_name of this PartManufacturer.
        :type part_name: str
        """
        self.swagger_types = {
            'name': str,
            'address': str,
            'website': str,
            'email': str,
            'phone': str,
            'comment': str,
            'id': int,
            'part_name': str
        }

        self.attribute_map = {
            'name': 'name',
            'address': 'address',
            'website': 'website',
            'email': 'email',
            'phone': 'phone',
            'comment': 'comment',
            'id': 'id',
            'part_name': 'part_name'
        }

        self._name = name
        self._address = address
        self._website = website
        self._email = email
        self._phone = phone
        self._comment = comment
        self._id = id
        self._part_name = part_name

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PartManufacturer of this PartManufacturer.
        :rtype: PartManufacturer
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this PartManufacturer.

        :return: The name of this PartManufacturer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartManufacturer.

        :param name: The name of this PartManufacturer.
        :type name: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this PartManufacturer.

        :return: The address of this PartManufacturer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this PartManufacturer.

        :param address: The address of this PartManufacturer.
        :type address: str
        """

        self._address = address

    @property
    def website(self):
        """
        Gets the website of this PartManufacturer.

        :return: The website of this PartManufacturer.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this PartManufacturer.

        :param website: The website of this PartManufacturer.
        :type website: str
        """

        self._website = website

    @property
    def email(self):
        """
        Gets the email of this PartManufacturer.

        :return: The email of this PartManufacturer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PartManufacturer.

        :param email: The email of this PartManufacturer.
        :type email: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this PartManufacturer.

        :return: The phone of this PartManufacturer.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this PartManufacturer.

        :param phone: The phone of this PartManufacturer.
        :type phone: str
        """

        self._phone = phone

    @property
    def comment(self):
        """
        Gets the comment of this PartManufacturer.

        :return: The comment of this PartManufacturer.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this PartManufacturer.

        :param comment: The comment of this PartManufacturer.
        :type comment: str
        """

        self._comment = comment

    @property
    def id(self):
        """
        Gets the id of this PartManufacturer.

        :return: The id of this PartManufacturer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartManufacturer.

        :param id: The id of this PartManufacturer.
        :type id: int
        """

        self._id = id

    @property
    def part_name(self):
        """
        Gets the part_name of this PartManufacturer.

        :return: The part_name of this PartManufacturer.
        :rtype: str
        """
        return self._part_name

    @part_name.setter
    def part_name(self, part_name):
        """
        Sets the part_name of this PartManufacturer.

        :param part_name: The part_name of this PartManufacturer.
        :type part_name: str
        """

        self._part_name = part_name

