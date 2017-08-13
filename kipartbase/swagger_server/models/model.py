# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.model_category import ModelCategory
from swagger_server.models.model_data import ModelData
from swagger_server.models.upload_file import UploadFile
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Model(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, id=None, category=None, image=None, model=None):
        """
        Model - a model defined in Swagger

        :param name: The name of this Model.
        :type name: str
        :param description: The description of this Model.
        :type description: str
        :param comment: The comment of this Model.
        :type comment: str
        :param snapeda: The snapeda of this Model.
        :type snapeda: str
        :param id: The id of this Model.
        :type id: int
        :param category: The category of this Model.
        :type category: ModelCategory
        :param image: The image of this Model.
        :type image: UploadFile
        :param model: The model of this Model.
        :type model: UploadFile
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'snapeda': str,
            'id': int,
            'category': ModelCategory,
            'image': UploadFile,
            'model': UploadFile
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'id': 'id',
            'category': 'category',
            'image': 'image',
            'model': 'model'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._snapeda = snapeda
        self._id = id
        self._category = category
        self._image = image
        self._model = model

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.
        :rtype: Model
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this Model.

        :return: The name of this Model.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Model.

        :param name: The name of this Model.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Model.

        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Model.

        :param description: The description of this Model.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this Model.

        :return: The comment of this Model.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Model.

        :param comment: The comment of this Model.
        :type comment: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this Model.

        :return: The snapeda of this Model.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this Model.

        :param snapeda: The snapeda of this Model.
        :type snapeda: str
        """

        self._snapeda = snapeda

    @property
    def id(self):
        """
        Gets the id of this Model.

        :return: The id of this Model.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Model.

        :param id: The id of this Model.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def category(self):
        """
        Gets the category of this Model.

        :return: The category of this Model.
        :rtype: ModelCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Model.

        :param category: The category of this Model.
        :type category: ModelCategory
        """

        self._category = category

    @property
    def image(self):
        """
        Gets the image of this Model.

        :return: The image of this Model.
        :rtype: UploadFile
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Model.

        :param image: The image of this Model.
        :type image: UploadFile
        """

        self._image = image

    @property
    def model(self):
        """
        Gets the model of this Model.

        :return: The model of this Model.
        :rtype: UploadFile
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Model.

        :param model: The model of this Model.
        :type model: UploadFile
        """

        self._model = model

