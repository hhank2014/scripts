#!/usr/bin/env python
class test:
	name = "hank"
	country = "China"

	@classmethod
	def getName(cls):
		return cls.name
	@classmethod
	def setName(cls,name):
		cls.name = name
	
	def getCountry(cls):
		return cls.country

	@classmethod
	def setCountry(cls,country):
		cls.country = country
p = test()
p.setName("Jack")
print p.getName()

p.setCountry("USA")
print p.getCountry()
