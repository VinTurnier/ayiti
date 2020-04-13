from __future__ import unicode_literals
import pickle
import re

DEPARTMENTS = []

class Department(object):

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            self.__dict__[k] = v
    
    def __repr__(self):
        return "<Department:{0}>".format(self.name)
    
    def __str__(self):
        return self.name


def load_departments():

    from pkg_resources import resource_stream
    with resource_stream(__name__, 'department.pkl') as pklfile:
        for s in pickle.load(pklfile):
            departement = Department(**s)  
            DEPARTMENTS.append(departement)
            globals()[departement.name] = departement


load_departments()
print(DEPARTMENTS)
print(Ouest.coordinates)