
import sys
import csv

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def case_1():

	file_str = input("Enter the name of the data file\n")
	
	with open(file_str) as csv_file:
		csv_reader = csv.reader(csv_file, delimeter=',')
		line_count = 0
		for row in csv_reader:
			if (line_count == 0):
				print("Header {", ".join(row)}")
				line_count += 1
			else:
				classifier = DecisionTreeClassifier(min_samples_split = 100)
				features = list(data2)
				train, test = train_test_split(data2, test_size = .1)
				x_train = train[features]
				X_test = test[features]
				decisiontree = classifier.fit(x_train, y_train)
				
	
	
def case_2():

		
	
def case_3():

	print("1: Enter new case\n")
	print("2: Quit\n")
	choice = input("Enter choice\n");
	
	if (choice == 2):
		return
		
	else if (choice == 1):
		
		
	
def case_4():

def main():

	print("Choose an option\n")
	print("1: Learn a decision tree from training data\n")
	print("2: Save the tree\n")
	print("3: Apply the tree to new cases\n")
	print("4: Load a tree model saved previously and apply the model to new cases\n")
	print("5: Quit\n")
	
	#choice = input("Enter choice\n");
	
	while(1):
		choice = input("Enter choice\n");
		if (choice == 1):
			case_1()
		
		else if (choice == 2):
			case_2()
			
		else if (choice == 3):
			case_3()
		
		else if (choice == 4):
			case_4()
		
		else if (choice == 5):
			#sys.exit()
			return
		
	
