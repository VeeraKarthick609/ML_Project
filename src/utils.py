import os
import sys

import numpy as np 
import pandas as pd
import dill

from src.exception import CustomException
from src.logger import logging

def save_object(file_path: str, object) -> None:
    """
    Function to save objects 

    Args:
    -----
     - `file_path`: str
     - `object`: object that needs to be saved

     Returns:
     --------
      - `None`
    """

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file:
            dill.dump(object, file)

    except Exception as e:
        raise CustomException(e, sys)