Name: Hecheng Sun
Email: hsun17@u.rochester.edu
Course: CSC240
Final Project
Prediction of Within 30 Days Re-admission For Patients Hospitalized with Diabetes by Libsvm

************ Files *********
- Code  			---> Folder for data preprocessing code
	- diabetic_data3.csv		---> Modified original database
	- digitalized3.csv		---> The output after running Transform3.py
	- Transform3.py			---> The source code of data preprocessing
	- csv2libsvm.py			---> The program to convert a digitalized csv file to libsvm format (from https://github.com/zygmuntz/phraug)
- libsvm-3.23			---> Folder for standard classification (The goal of this project)
- libsvm-3.23-For multiclasses	---> Folder for multi-class classification (Extra experiment)
- Final_project_report.pdf	---> The project report
- README.txt			---> This file



************ Instructions ***

There are 3 ways to test the result:


Method 1: Only see the final result
	1. In command line, navigate to libsvm-3.23, and type the training command:
		./svm-train -m 10000 -t 0 my.train my.model
		or
		./svm-train -m 10000 -w1 9 -h 0 my.train my.model

	2. After the training is finished, type the predicting command:
		./svm-predict my.test my.model output
	Result like Accuracy, Precision, Recall, AUC should appear


Method 2: Build from the beginning 
	1. In command line, navigate to Code, and type the data-preprocessing command command:
		python Transform3.py

	2. A new file called "digitalized3.csv" should appear (or replacing the old one). Open that file with Excel or Numbers. Delete the last column, and move the newly last column (the second last before deleting) to the left of the first column (Don't forget to delete after moving!). Save, and move to the next step.
	
	3. Run the command:
		python csv2libsvm.py digitalized3.csv svmliblized3.data 
	A new file called "svmliblized3.data" should appear (or replacing the old one). Copy this file to /libsvm-3.23/tools (You may need to overwrite the old file with the same name).

	4. In command line, navigate to /libsvm-3.23/tools. Run the error checking command:
		python checkdata.py svmliblized3.data 
	If the program return "No error", run the subset command:
		python subset.py -s 1 svmliblized3.data 60000 my.train my.test
	Two new file should appear: "my.train" and "my.test". Copy them to /libsvm-3.23.

	5. In command line, navigate to libsvm-3.23, and type the training command:
		./svm-train -m 10000 -t 0 my.train my.model
		or
		./svm-train -m 10000 -w1 9 -h 0 my.train my.model

	6. After the training is finished, type the predicting command:
		./svm-predict my.test my.model output
	Result like Accuracy, Precision, Recall, AUC should appear

	
Method 3: Build the experiment for multi-class classification
	Procedure are almost the same as the method 2. There are two differences:

	1. Change the "readmitted_digitalized(readm)" function in Transform3.py to the commented out code, so that each original label has its own label in SVM.

	2. Instead of using the tools and program in libsvm-3.23, use everything in libsvm-3.23-For multiclasses. The reason is that the tool for calculating precision, recall, and AUC does not support multi-class classification.





************ Results *******

See 'Final project report.pdf' for details

************ References ************
See 'Final project report.pdf' for details





