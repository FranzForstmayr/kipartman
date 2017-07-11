# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.distributor_data import DistributorData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class DistributorNew(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, website=None, sku_url=None, email=None, phone=None, comment=None):
        """
        DistributorNew - a model defined in Swagger

        :param name: The name of this DistributorNew.
        :type name: str
        :param address: The address of this DistributorNew.
        :type address: str
        :param website: The website of this DistributorNew.
        :type website: str
        :param sku_url: The sku_url of this DistributorNew.
        :type sku_url: str
        :param email: The email of this DistributorNew.
        :type email: str
        :param phone: The phone of this DistributorNew.
        :type phone: str
        :param comment: The comment of this DistributorNew.
        :type comment: str
        """
        self.swagger_types = {
            'name': str,
            'address': str,
            'website': str,
            'sku_url': str,
            'email': str,
            'phone': str,
            'comment': str
        }

        self.attribute_map = {
            'name': 'name',
            'address': 'address',
            'website': 'website',
            'sku_url': 'sku_url',
            'email': 'email',
            'phone': 'phone',
            'comment': 'comment'
        }

        self._name = name
        self._address = address
        self._website = website
        self._sku_url = sku_url
        self._email = email
        self._phone = phone
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DistributorNew of this DistributorNew.
        :rtype: DistributorNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this DistributorNew.

        :return: The name of this DistributorNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DistributorNew.

        :param name: The name of this DistributorNew.
        :type name: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this DistributorNew.

        :return: The address of this DistributorNew.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this DistributorNew.

        :param address: The address of this DistributorNew.
        :type address: str
        """

        self._address = address

    @property
    def website(self):
        """
        Gets the website of this DistributorNew.

        :return: The website of this DistributorNew.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this DistributorNew.

        :param website: The website of this DistributorNew.
        :type website: str
        """

        self._website = website

    @property
    def sku_url(self):
        """
        Gets the sku_url of this DistributorNew.

        :return: The sku_url of this DistributorNew.
        :rtype: str
        """
        return self._sku_url

    @sku_url.setter
    def sku_url(self, sku_url):
        """
        Sets the sku_url of this DistributorNew.

        :param sku_url: The sku_url of this DistributorNew.
        :type sku_url: str
        """

        self._sku_url = sku_url

    @property
    def email(self):
        """
        Gets the email of this DistributorNew.

        :return: The email of this DistributorNew.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this DistributorNew.

        :param email: The email of this DistributorNew.
        :type email: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this DistributorNew.

        :return: The phone of this DistributorNew.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this DistributorNew.

        :param phone: The phone of this DistributorNew.
        :type phone: str
        """

        self._phone = phone

    @property
    def comment(self):
        """
        Gets the comment of this DistributorNew.

        :return: The comment of this DistributorNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this DistributorNew.

        :param comment: The comment of this DistributorNew.
        :type comment: str
        """

        self._comment = comment

