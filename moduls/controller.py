


from moduls import models
from moduls.models import sum

# def controller_save_data(file_name, data):
#     models.save_data(file_name, data)


def controller_save(a,b):
    result = sum(a,b)
    return result


