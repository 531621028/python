#coding:utf-8

import re
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logging.debug('This is debug message')


def calculate(exp):
	regex = r'\(([^()]+)\)'
	while True:
		val = re.split(regex,exp,1)
		logging.debug('val'+str(val))
		if len(val) == 3: 
			first,center,last = val
			result = mul_div(center)
			logging.debug('result'+str(result))
			exp,count= re.subn(regex,str(result),exp,1)
			logging.debug('exp'+str(exp))
		else:
			break
	return mul_div(exp)
def mul_div(exp):
	if '(' in exp or ')' in exp:
		raise Exception()
	regex = r'(\d+\.?\d*[*/]-?\d+\.?\d*)'
	while True:
		val = re.split(regex,exp,1)
		logging.debug('val'+str(val))
		if len(val) == 3: 
			first,center,last = val
			if '*' in center:
				op1,op2 = re.split('\*',center)
				result = float(op1) * float(op2)
			elif '/' in center:
				op1,op2 = re.split('/',center)
				result = float(op1) / float(op2)
			else:
				result = center[1:-1]
			exp,count= re.subn(regex,str(result),exp,1)
			logging.debug('exp'+str(exp))
		else:
			break
	return add_sub(exp)

def add_sub(exp):
	exp = re.sub('--','+',exp)
	exp = re.sub('\+-','-',exp)
	exp = re.sub('-\+','-',exp)
	exp = re.sub('\+\+','+',exp)
	regex = r'(-?\d+\.?\d*)'
	ops = re.findall(regex,exp)
	result = float(0)
	for op in ops:
		result += float(op)
	return result

if __name__ == '__main__':
	exp = '8/9'
	#print (mul_div('43*1'))
	print(Calculate(exp))