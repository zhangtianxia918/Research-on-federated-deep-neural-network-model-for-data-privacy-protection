# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:07:47 2020

@author: zhangtianxia
"""
import numpy as np
import phe as paillier
import time


# # 同态加密初始化
key_length = 1024
pub_key, private_key = paillier.generate_paillier_keypair(n_length=key_length) 
# encrypted_re_net_conv1 = re_net1_conv1
# decrypted_re_net_conv1 = re_net1_conv1

def encrypt_vector(public_key, x):
    return [public_key.encrypt(float(i)) for i in x]


def decrypt_vector(private_key, x):
    return np.array([private_key.decrypt(i) for i in x])

def sum_encrypted_vectors(x, y):
    if len(x) != len(y):
        raise ValueError('Encrypted vectors must have the same size')
    return [x[i] + y[i] for i in range(len(x))]

def div_encrypted_vectors(x, y):
    return [x[i]/y for i in range(len(x))]




net1_weight = np.load("P1_l4weight.npy", allow_pickle=True)
re_net1_weight = net1_weight.reshape((-1,1))

net2_weight = np.load("P2_l4weight.npy", allow_pickle=True)
re_net2_weight = net2_weight.reshape((-1,1))

net3_weight = np.load("P3_l4weight.npy", allow_pickle=True)

re_net3_weight = net3_weight.reshape((-1,1))

size = net1_weight.shape

net_weight = (net1_weight + net2_weight + net3_weight)/3 # 直接模型平均


encrypted_re_net1_weight= encrypt_vector(pub_key, re_net1_weight)

encrypted_re_net2_weight= encrypt_vector(pub_key, re_net2_weight)

encrypted_re_net3_weight= encrypt_vector(pub_key, re_net3_weight)


encrypted_re_net_weight  = sum_encrypted_vectors(encrypted_re_net1_weight, 
                                                 encrypted_re_net2_weight)

encrypted_re_net_weight  = sum_encrypted_vectors(encrypted_re_net_weight, 
                                                 encrypted_re_net3_weight)

encrypted_re_net_weight = div_encrypted_vectors(encrypted_re_net_weight,3)


decrypted_re_net_weight  = decrypt_vector(private_key,encrypted_re_net_weight)

decrypted_net_weight = decrypted_re_net_weight.reshape(size)

# 从经过同态加密运算的decrypted_net_weight 和 运算的net_weight 结果是相同的














