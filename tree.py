
import sys
import csv
import pickle
import pandas as pd

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def case_1():
    print("hello")

    file_str = input("Enter the name of the data file\n")

    data = pd.read_csv(file_str, sep=',')

    print("Length: ", len(data))
    #print("Shape: ", data.shape())

    #print("Data: ", data.head())

    global X
    X = data.values[:, 0:1]
    Y = data.values[:, 0]

    #x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)

    #clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 3, min_samples_leaf = 100)

    global classifier
    classifier = tree.DecisionTreeClassifier()
    classifier = classifier.fit(X, Y)
    #tree = clf_gini.fit(x_train, y_train)

    tree_file = open(file_str + ".model", "wb")
    pickle.dump(classifier, tree_file)
    tree_file.close()

    print("Tree saved")
    main()

    #clf_gini.predict([1,1,0,0,0])

    #predict = clf_gini.predict(x_test)

    #print("Accuracy ", accuracy_score(x_test, predict)*100)


	    
	
def case_2():
    print("Tree saved")
    main()

		
	
def case_3():

    print("1: Enter new case\n")
    print("2: Quit\n")
    choice = input("Enter choice\n")

    if (choice == '2'):
        return

    elif (choice == '1'):
        #new_data = input("Enter new data\n")
        new_data = ['1','1','0','0','1']
        label = classifier.predict(X,new_data)
        print (label[0])

	main()
		
	
def case_4():

    model_name = input("Enter name of model file\n")
    model = open(model_name, "rb")
    print("Model opened\n")
    case_3()

def main():

    print("\n\n\n")
    print("Choose an option\n")
    print("1: Learn a decision tree from training data\n")
    print("2: Save the tree\n")
    print("3: Apply the tree to new cases\n")
    print("4: Load a tree model saved previously and apply the model to new cases\n")
    print("5: Quit\n")

    #choice = input("Enter choice\n");

    choice = input("Enter choice\n")

    if (choice == '1'):
        case_1()

    elif (choice == '2'):
        case_2()

    elif (choice == '3'):
        case_3()

    elif (choice == '4'):
        case_4()

    elif (choice == '5'):
        #sys.exit()
        return


main()
