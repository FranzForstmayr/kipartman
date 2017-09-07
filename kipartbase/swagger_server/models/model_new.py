# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.model_category_ref import ModelCategoryRef
from swagger_server.models.model_data import ModelData
from swagger_server.models.upload_file_ref import UploadFileRef
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ModelNew(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, category=None, image=None, model=None):
        """
        ModelNew - a model defined in Swagger

        :param name: The name of this ModelNew.
        :type name: str
        :param description: The description of this ModelNew.
        :type description: str
        :param comment: The comment of this ModelNew.
        :type comment: str
        :param snapeda: The snapeda of this ModelNew.
        :type snapeda: str
        :param category: The category of this ModelNew.
        :type category: ModelCategoryRef
        :param image: The image of this ModelNew.
        :type image: UploadFileRef
        :param model: The model of this ModelNew.
        :type model: UploadFileRef
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'snapeda': str,
            'category': ModelCategoryRef,
            'image': UploadFileRef,
            'model': UploadFileRef
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'category': 'category',
            'image': 'image',
            'model': 'Model'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._snapeda = snapeda
        self._category = category
        self._image = image
        self._model = model

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelNew of this ModelNew.
        :rtype: ModelNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this ModelNew.

        :return: The name of this ModelNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModelNew.

        :param name: The name of this ModelNew.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ModelNew.

        :return: The description of this ModelNew.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModelNew.

        :param description: The description of this ModelNew.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this ModelNew.

        :return: The comment of this ModelNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this ModelNew.

        :param comment: The comment of this ModelNew.
        :type comment: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this ModelNew.

        :return: The snapeda of this ModelNew.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this ModelNew.

        :param snapeda: The snapeda of this ModelNew.
        :type snapeda: str
        """

        self._snapeda = snapeda

    @property
    def category(self):
        """
        Gets the category of this ModelNew.

        :return: The category of this ModelNew.
        :rtype: ModelCategoryRef
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ModelNew.

        :param category: The category of this ModelNew.
        :type category: ModelCategoryRef
        """

        self._category = category

    @property
    def image(self):
        """
        Gets the image of this ModelNew.

        :return: The image of this ModelNew.
        :rtype: UploadFileRef
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this ModelNew.

        :param image: The image of this ModelNew.
        :type image: UploadFileRef
        """

        self._image = image

    @property
    def model(self):
        """
        Gets the model of this ModelNew.

        :return: The model of this ModelNew.
        :rtype: UploadFileRef
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ModelNew.

        :param model: The model of this ModelNew.
        :type model: UploadFileRef
        """

        self._model = model
