#!/usr/bin/env python

from distutils.core import setup

'Packaging instructions from: http://diveintopython3.org/packaging.html'
setup(name='Padding',
      py_modules=['Padding'],
      version='0.4',
      description='Padding methods for password based encryption',
      keywords = ["padding", "CMS", 'CMS Padding', 'Bit Padding', 'Null Padding', 'Random Padding', 'PKCS', "RFC 5652", "PKCS#5", "PKCS#7", "RFC 1423"],
      
      author='Peio Popov',
      author_email='peio@peio.org',
      license = 'Public Domain',
      url = 'http://pypi.python.org/pypi/Padding',

      classifiers = ['Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security :: Cryptography'],
        long_description = '''\

Padding - Padding methods for password based encryption
---------------------------------------------

Append and remove padding to/from a string. 

I. Functions:
appendPadding(str, blocksize=AES_blocksize, mode='CMS'):
 Pad (append padding to) string for use with symmetric encryption algorithm
    Input: (string) str - String to be padded
           (int)    blocksize - block size of the encryption algorithm. Usually 8 or 16 bytes
           (string) mode - padding scheme one in (CMS, Bit, ZeroLen, Null, Space, Random)
    Return:(string) Padded string according to chosen padding mode

removePadding(str, blocksize=AES_blocksize, mode='CMS'):
  Remove padding from string 
  Input: (str) str - String to be padded
         (int) blocksize - block size of the algorithm. Usually 8 or 16 bytes
         (string) mode - padding scheme one in (CMS, Bit, ZeroLen, Null, Space, Random)
  Return:(string) Decrypted string without padding

II. Blocksizes:
DES (Triple DES), CAST5 and Blowfish have block size of 64 bits = 8 bytes
DES_blocksize = 8 
CAST5_blocksize = 8
Blowfish_blocksize = 8

AES has fixed block size of 128 bits = 16 bytes and this is the default blocksize
AES_blocksize = 16

III. Mode:
MODES ={
(0,'CMS')     : 'Pad with bytes all of the same value as the number of padding bytes. Default mode used in Cryptographic Message Syntax (CMS as defined in RFC 5652, PKCS#5, PKCS#7 and RFC 1423 PEM)',
(1,'Bit')     : 'BitPadding: Pad with 0x80 (10000000) followed by zero (null) bytes. Described in ANSI X.923 and ISO/IEC 9797-1',
(2,'ZeroLen') : 'Pad with zeroes except make the last byte equal to the number (length) of padding bytes',
(3,'Null')    : 'Pad with null bytes. Only for encrypting of text data.',
(4,'Space')   : 'Pad with spaces. Only for encrypting of text data.',
(5,'Random')  : 'ISO 10126 Padding (withdrawn in 2007): Pad with random bytes + last byte equal to the number of padding bytes'         
       }

CMS mode is the default one

Examples in the README.txt file
'''
      )

