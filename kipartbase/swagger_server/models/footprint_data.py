# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class FootprintData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, snapeda_uid=None, updated=None, local_footprint=None):
        """
        FootprintData - a model defined in Swagger

        :param name: The name of this FootprintData.
        :type name: str
        :param description: The description of this FootprintData.
        :type description: str
        :param comment: The comment of this FootprintData.
        :type comment: str
        :param snapeda: The snapeda of this FootprintData.
        :type snapeda: str
        :param snapeda_uid: The snapeda_uid of this FootprintData.
        :type snapeda_uid: str
        :param updated: The updated of this FootprintData.
        :type updated: datetime
        :param local_footprint: The local_footprint of this FootprintData.
        :type local_footprint: str
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'snapeda': str,
            'snapeda_uid': str,
            'updated': datetime,
            'local_footprint': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'snapeda_uid': 'snapeda_uid',
            'updated': 'updated',
            'local_footprint': 'local_footprint'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._snapeda = snapeda
        self._snapeda_uid = snapeda_uid
        self._updated = updated
        self._local_footprint = local_footprint

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FootprintData of this FootprintData.
        :rtype: FootprintData
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this FootprintData.

        :return: The name of this FootprintData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FootprintData.

        :param name: The name of this FootprintData.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FootprintData.

        :return: The description of this FootprintData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FootprintData.

        :param description: The description of this FootprintData.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this FootprintData.

        :return: The comment of this FootprintData.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this FootprintData.

        :param comment: The comment of this FootprintData.
        :type comment: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this FootprintData.

        :return: The snapeda of this FootprintData.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this FootprintData.

        :param snapeda: The snapeda of this FootprintData.
        :type snapeda: str
        """

        self._snapeda = snapeda

    @property
    def snapeda_uid(self):
        """
        Gets the snapeda_uid of this FootprintData.

        :return: The snapeda_uid of this FootprintData.
        :rtype: str
        """
        return self._snapeda_uid

    @snapeda_uid.setter
    def snapeda_uid(self, snapeda_uid):
        """
        Sets the snapeda_uid of this FootprintData.

        :param snapeda_uid: The snapeda_uid of this FootprintData.
        :type snapeda_uid: str
        """

        self._snapeda_uid = snapeda_uid

    @property
    def updated(self):
        """
        Gets the updated of this FootprintData.

        :return: The updated of this FootprintData.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this FootprintData.

        :param updated: The updated of this FootprintData.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def local_footprint(self):
        """
        Gets the local_footprint of this FootprintData.

        :return: The local_footprint of this FootprintData.
        :rtype: str
        """
        return self._local_footprint

    @local_footprint.setter
    def local_footprint(self, local_footprint):
        """
        Sets the local_footprint of this FootprintData.

        :param local_footprint: The local_footprint of this FootprintData.
        :type local_footprint: str
        """

        self._local_footprint = local_footprint

