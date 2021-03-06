# This file is part of gestmag_sga module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool

from .gestmag import *
from .party import *
from .product import *
from .stock import *


def register():
    Pool.register(
        Gestmag,
        Product,
        ShipmentIn,
        ShipmentOut,
        Party,
        Address,
        GestmagProductResult,
        module='gestmag_sga', type_='model')
    Pool.register(
        GestmagProduct,
        module='gestmag_sga', type_='wizard')
