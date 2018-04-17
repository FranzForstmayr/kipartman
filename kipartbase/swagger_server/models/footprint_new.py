# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.footprint_category_ref import FootprintCategoryRef
from swagger_server.models.footprint_data import FootprintData
from swagger_server.models.upload_file_ref import UploadFileRef
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class FootprintNew(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, snapeda_uid=None, updated=None, local_footprint=None, category=None, image=None, footprint=None):
        """
        FootprintNew - a model defined in Swagger

        :param name: The name of this FootprintNew.
        :type name: str
        :param description: The description of this FootprintNew.
        :type description: str
        :param comment: The comment of this FootprintNew.
        :type comment: str
        :param snapeda: The snapeda of this FootprintNew.
        :type snapeda: str
        :param snapeda_uid: The snapeda_uid of this FootprintNew.
        :type snapeda_uid: str
        :param updated: The updated of this FootprintNew.
        :type updated: datetime
        :param local_footprint: The local_footprint of this FootprintNew.
        :type local_footprint: str
        :param category: The category of this FootprintNew.
        :type category: FootprintCategoryRef
        :param image: The image of this FootprintNew.
        :type image: UploadFileRef
        :param footprint: The footprint of this FootprintNew.
        :type footprint: UploadFileRef
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'snapeda': str,
            'snapeda_uid': str,
            'updated': datetime,
            'local_footprint': str,
            'category': FootprintCategoryRef,
            'image': UploadFileRef,
            'footprint': UploadFileRef
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'snapeda_uid': 'snapeda_uid',
            'updated': 'updated',
            'local_footprint': 'local_footprint',
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
        self._category = category
        self._image = image
        self._footprint = footprint

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FootprintNew of this FootprintNew.
        :rtype: FootprintNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this FootprintNew.

        :return: The name of this FootprintNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FootprintNew.

        :param name: The name of this FootprintNew.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FootprintNew.

        :return: The description of this FootprintNew.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FootprintNew.

        :param description: The description of this FootprintNew.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this FootprintNew.

        :return: The comment of this FootprintNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this FootprintNew.

        :param comment: The comment of this FootprintNew.
        :type comment: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this FootprintNew.

        :return: The snapeda of this FootprintNew.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this FootprintNew.

        :param snapeda: The snapeda of this FootprintNew.
        :type snapeda: str
        """

        self._snapeda = snapeda

    @property
    def snapeda_uid(self):
        """
        Gets the snapeda_uid of this FootprintNew.

        :return: The snapeda_uid of this FootprintNew.
        :rtype: str
        """
        return self._snapeda_uid

    @snapeda_uid.setter
    def snapeda_uid(self, snapeda_uid):
        """
        Sets the snapeda_uid of this FootprintNew.

        :param snapeda_uid: The snapeda_uid of this FootprintNew.
        :type snapeda_uid: str
        """

        self._snapeda_uid = snapeda_uid

    @property
    def updated(self):
        """
        Gets the updated of this FootprintNew.

        :return: The updated of this FootprintNew.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this FootprintNew.

        :param updated: The updated of this FootprintNew.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def local_footprint(self):
        """
        Gets the local_footprint of this FootprintNew.

        :return: The local_footprint of this FootprintNew.
        :rtype: str
        """
        return self._local_footprint

    @local_footprint.setter
    def local_footprint(self, local_footprint):
        """
        Sets the local_footprint of this FootprintNew.

        :param local_footprint: The local_footprint of this FootprintNew.
        :type local_footprint: str
        """

        self._local_footprint = local_footprint

    @property
    def category(self):
        """
        Gets the category of this FootprintNew.

        :return: The category of this FootprintNew.
        :rtype: FootprintCategoryRef
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this FootprintNew.

        :param category: The category of this FootprintNew.
        :type category: FootprintCategoryRef
        """

        self._category = category

    @property
    def image(self):
        """
        Gets the image of this FootprintNew.

        :return: The image of this FootprintNew.
        :rtype: UploadFileRef
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this FootprintNew.

        :param image: The image of this FootprintNew.
        :type image: UploadFileRef
        """

        self._image = image

    @property
    def footprint(self):
        """
        Gets the footprint of this FootprintNew.

        :return: The footprint of this FootprintNew.
        :rtype: UploadFileRef
        """
        return self._footprint

    @footprint.setter
    def footprint(self, footprint):
        """
        Sets the footprint of this FootprintNew.

        :param footprint: The footprint of this FootprintNew.
        :type footprint: UploadFileRef
        """

        self._footprint = footprint

