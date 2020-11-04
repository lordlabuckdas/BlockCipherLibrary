# Block Cipher Library

contains implementation of few famous modes of implementation of block ciphers

## TOC

* [Electronic CodeBook](#Electronic-CodeBook) - [code](./ECB.py)
* [Continuous Block Chaining](#Continuous-Block-Chaining) - [code](./CBC.py)
* [Propagating Continuous Block Chaining](#Propagating-Continuous-Block-Chaining) - [code](./PCBC.py)

## Concept

#### Electronic CodeBook

* breaks code into blocks and encrypts them
* likewise for decryption

#### Continuous Block Chaining

* breaks code into blocks, encrypts them and stores and also feeds the output to the encryption of next block

#### Propagating Continuous Block Chaining

* same as [Continuous Block Chaining](#Continuous-Block-Chaining), but adds an IV (Initialisation Vector) to the first block

