# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PartData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, octopart=None, updated=None):
        """
        PartData - a model defined in Swagger

        :param name: The name of this PartData.
        :type name: str
        :param description: The description of this PartData.
        :type description: str
        :param comment: The comment of this PartData.
        :type comment: str
        :param octopart: The octopart of this PartData.
        :type octopart: str
        :param updated: The updated of this PartData.
        :type updated: datetime
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'octopart': str,
            'updated': datetime
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'octopart': 'octopart',
            'updated': 'updated'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._octopart = octopart
        self._updated = updated

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PartData of this PartData.
        :rtype: PartData
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this PartData.

        :return: The name of this PartData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartData.

        :param name: The name of this PartData.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PartData.

        :return: The description of this PartData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartData.

        :param description: The description of this PartData.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this PartData.

        :return: The comment of this PartData.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this PartData.

        :param comment: The comment of this PartData.
        :type comment: str
        """

        self._comment = comment

    @property
    def octopart(self):
        """
        Gets the octopart of this PartData.

        :return: The octopart of this PartData.
        :rtype: str
        """
        return self._octopart

    @octopart.setter
    def octopart(self, octopart):
        """
        Sets the octopart of this PartData.

        :param octopart: The octopart of this PartData.
        :type octopart: str
        """

        self._octopart = octopart

    @property
    def updated(self):
        """
        Gets the updated of this PartData.

        :return: The updated of this PartData.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this PartData.

        :param updated: The updated of this PartData.
        :type updated: datetime
        """

        self._updated = updated
