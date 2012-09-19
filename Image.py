# -*- coding: utf-8 -*-
from pymaging import Image

# pretend to be PIL

open = Image.open
Image.verify = lambda self: True
