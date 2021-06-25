# Test functions goes here
import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
	
	def test_1_E1(self):

		inFile = 'Enc_T1.txt'
		outFile = 'Enc_res1.txt'
		EncFile = open(inFile,'w+')
		inType = 'jahsnu'
		outType = '1001011101110001'
		EncFile.write(inType)
		EncFile.close()
		encode(inFile, outFile)
		outFile = open(outFile,'r')
		output = outFile.readlines()
		isValid = (output[0]==outType)
		self.assertTrue(isValid)

	def test_2_D1(self):
		
		inFile = 'Enc_res1.txt'
		outFile = 'Dec_res1.txt'
		decode(inFile, outFile)
		f_decode = open(outFile,'r')
		output = f_decode.readlines()
		outType = 'jahsnu'
		isValid = (output[0]==outType)
		self.assertTrue(isValid)
   
	def test_3_E2(self):

		inFile = 'Enc_T2.txt'
		outFile = 'Enc_res2.txt'
		EncFile = open(inFile,'w+')
		inType = 'P{;/*&6@#}'
		outType = '1100110111101111000001010011100101'
		EncFile.write(inType)
		EncFile.close()
		encode(inFile, outFile)
		outFile = open(outFile,'r')
		output = outFile.readlines()
		isValid = (output[0]==outType)
		self.assertTrue(isValid)


	def test_4_D2(self):
		
		inFile = 'Enc_res2.txt'
		outFile = 'Dec_res2.txt'
		decode(inFile, outFile)
		f_decode = open(outFile,'r')
		output = f_decode.readlines()
		outType = 'P{;/*&6@#}'
		isValid = (output[0]==outType)
		self.assertTrue(isValid)
		
	def test_5_E3(self):

		inFile = 'Enc_T3.txt'
		outFile = 'Enc_res3.txt'
		EncFile = open(inFile,'w+')
		inType = '6615{}//*'
		outType = '1111110100111001010000110'
		EncFile.write(inType)
		EncFile.close()
		encode(inFile, outFile)
		outFile = open(outFile,'r')
		output = outFile.readlines()
		isValid = (output[0]==outType)
		self.assertTrue(isValid)


	def test_6_D3(self):
		inFile = 'Enc_res3.txt'
		outFile = 'Dec_res3.txt'
		decode(inFile, outFile)
		f_decode = open(outFile,'r')
		output = f_decode.readlines()
		outType = '6615{}//*'
		isValid = (output[0]==outType)
		self.assertTrue(isValid)



if __name__ == '__main__':
	unittest.main()
