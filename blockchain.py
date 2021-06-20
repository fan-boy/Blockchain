#Create a blockchain
"""
Created on Fri Jun 18 23:12:58 2021

@author: aadityashete
"""

import datetime
import hashlib
import json
from flask import Flask,jsonify

#Build the blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof =1,previous_hash = '0')


    def create_block(self,proof, previous_hash):
        block = {'index':len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof':proof,
                 'previous_hash':previous_hash
            }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain(-1)
    
    def proof_of_work(self,prevProof):
        newProof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(newProof**2 - prevProof**2 ).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof = True
            else:
                newProof+=1
                
        return newProof
            