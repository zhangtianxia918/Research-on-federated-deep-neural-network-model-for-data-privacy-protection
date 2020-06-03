# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:24:38 2020

@author: zhangtianxia
"""

import numpy as np
import phe as paillier
import time

key_length = 128
pub_key, private_key = paillier.generate_paillier_keypair(n_length=key_length)

a = 10
b = 20
c = 30

encrypted_a= pub_key.encrypt(float(a))
encrypted_b= pub_key.encrypt(float(b))
encrypted_c= pub_key.encrypt(float(c))


encrypted_sum = ( encrypted_a + encrypted_b + encrypted_c )/3


decrypted_sum  = private_key.decrypt(encrypted_sum)

