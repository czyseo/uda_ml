#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__  import division

import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
num=len(enron_data)
print num
print len(enron_data['METTS MARK'])
n=0;
for k,v in enumerate(enron_data):
	if enron_data[v]['poi'] == True:
		n=n+1
print n
# print enron_data["PRENTICE JAMES"]
# print enron_data["COLWELL WESLEY"]
# print enron_data["SKILLING JEFFREY K"]

# print enron_data["LAY KENNETH L"]
# print enron_data["SKILLING JEFFREY K"]
# print enron_data["FASTOW ANDREW S"]
n1=0
m1=0
l1=0
l2=0
for k,v in enumerate(enron_data):
	if enron_data[v]['salary'] != 'NaN':
		n1=n1+1
	if enron_data[v]['email_address'] != 'NaN':
		m1=m1+1
	if enron_data[v]['total_payments'] == 'NaN':
		l1=l1+1
		if enron_data[v]['poi'] == True :
			l2=l2+1		
print n1
print m1
print l1
print l1/num
print l2
print l2/num
