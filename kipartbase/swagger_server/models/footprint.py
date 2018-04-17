# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.footprint_category import FootprintCategory
from swagger_server.models.footprint_data import FootprintData
from swagger_server.models.upload_file import UploadFile
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Footprint(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, snapeda_uid=None, updated=None, local_footprint=None, id=None, category=None, image=None, footprint=None):
        """
        Footprint - a model defined in Swagger

        :param name: The name of this Footprint.
        :type name: str
        :param description: The description of this Footprint.
        :type description: str
        :param comment: The comment of this Footprint.
        :type comment: str
        :param snapeda: The snapeda of this Footprint.
        :type snapeda: str
        :param snapeda_uid: The snapeda_uid of this Footprint.
        :type snapeda_uid: str
        :param updated: The updated of this Footprint.
        :type updated: datetime
        :param local_footprint: The local_footprint of this Footprint.
        :type local_footprint: str
        :param id: The id of this Footprint.
        :type id: int
        :param category: The category of this Footprint.
        :type category: FootprintCategory
        :param image: The image of this Footprint.
        :type image: UploadFile
        :param footprint: The footprint of this Footprint.
        :type footprint: UploadFile
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'snapeda': str,
            'snapeda_uid': str,
            'updated': datetime,
            'local_footprint': str,
            'id': int,
            'category': FootprintCategory,
            'image': UploadFile,
            'footprint': UploadFile
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'snapeda_uid': 'snapeda_uid',
            'updated': 'updated',
            'local_footprint': 'local_footprint',
            'id': 'id',
            'category': 'category',
            'image': 'image',
            'footprint': 'footprint'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._snapeda = snapeda
        self._snapeda_uid = snapeda_uid
        self._updated = updated
        self._local_footprint = local_footprint
        self._id = id
        self._category = category
        self._image = image
        self._footprint = footprint

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Footprint of this Footprint.
        :rtype: Footprint
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this Footprint.

        :return: The name of this Footprint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Footprint.

        :param name: The name of this Footprint.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Footprint.

        :return: The description of this Footprint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Footprint.

        :param description: The description of this Footprint.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this Footprint.

        :return: The comment of this Footprint.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Footprint.

        :param comment: The comment of this Footprint.
        :type comment: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this Footprint.

        :return: The snapeda of this Footprint.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this Footprint.

        :param snapeda: The snapeda of this Footprint.
        :type snapeda: str
        """

        self._snapeda = snapeda

    @property
    def snapeda_uid(self):
        """
        Gets the snapeda_uid of this Footprint.

        :return: The snapeda_uid of this Footprint.
        :rtype: str
        """
        return self._snapeda_uid

    @snapeda_uid.setter
    def snapeda_uid(self, snapeda_uid):
        """
        Sets the snapeda_uid of this Footprint.

        :param snapeda_uid: The snapeda_uid of this Footprint.
        :type snapeda_uid: str
        """

        self._snapeda_uid = snapeda_uid

    @property
    def updated(self):
        """
        Gets the updated of this Footprint.

        :return: The updated of this Footprint.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Footprint.

        :param updated: The updated of this Footprint.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def local_footprint(self):
        """
        Gets the local_footprint of this Footprint.

        :return: The local_footprint of this Footprint.
        :rtype: str
        """
        return self._local_footprint

    @local_footprint.setter
    def local_footprint(self, local_footprint):
        """
        Sets the local_footprint of this Footprint.

        :param local_footprint: The local_footprint of this Footprint.
        :type local_footprint: str
        """

        self._local_footprint = local_footprint

    @property
    def id(self):
        """
        Gets the id of this Footprint.

        :return: The id of this Footprint.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Footprint.

        :param id: The id of this Footprint.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def category(self):
        """
        Gets the category of this Footprint.

        :return: The category of this Footprint.
        :rtype: FootprintCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Footprint.

        :param category: The category of this Footprint.
        :type category: FootprintCategory
        """

        self._category = category

    @property
    def image(self):
        """
        Gets the image of this Footprint.

        :return: The image of this Footprint.
        :rtype: UploadFile
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Footprint.

        :param image: The image of this Footprint.
        :type image: UploadFile
        """

        self._image = image

    @property
    def footprint(self):
        """
        Gets the footprint of this Footprint.

        :return: The footprint of this Footprint.
        :rtype: UploadFile
        """
        return self._footprint

    @footprint.setter
    def footprint(self, footprint):
        """
        Sets the footprint of this Footprint.

        :param footprint: The footprint of this Footprint.
        :type footprint: UploadFile
        """

        self._footprint = footprint

