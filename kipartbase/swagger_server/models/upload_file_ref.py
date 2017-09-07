# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class UploadFileRef(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None):
        """
        UploadFileRef - a model defined in Swagger

        :param id: The id of this UploadFileRef.
        :type id: int
        """
        self.swagger_types = {
            'id': int
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UploadFileRef of this UploadFileRef.
        :rtype: UploadFileRef
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self):
        """
        Gets the id of this UploadFileRef.

        :return: The id of this UploadFileRef.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UploadFileRef.

        :param id: The id of this UploadFileRef.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
