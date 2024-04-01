import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Load data
    a= time.time()
    df = pd.read_csv(r"Crop_recommendation.csv")
    X = df.drop('label', axis=1)
    y = df['label']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    b= time.time()
    tl = b-a
    print("Time taken to load data: ", tl)

    st = time.time()
    #create new a knn model
    knn = KNeighborsClassifier()
    #create a dictionary of all values we want to test for n_neighbors
    params_knn = {'n_neighbors': np.arange(1,10), 'p': [1, 2]}
    #use gridsearch to test all values for n_neighbors
    knn_gs = GridSearchCV(knn, params_knn, cv=5)
    #fit model to training data
    knn_gs.fit(X_train, y_train)

    #save best model
    knn_best = knn_gs.best_estimator_
    #check best n_neigbors value
    print(knn_gs.best_params_)

    #create a new random forest classifier
    rf = RandomForestClassifier()
    #create a dictionary of all values we want to test for n_estimators
    params_rf = {'n_estimators': [50, 100, 150], 'criterion': ['gini', 'entropy']}
    #use gridsearch to test all values for n_estimators
    rf_gs = GridSearchCV(rf, params_rf, cv=5)
    #fit model to training data
    rf_gs.fit(X_train, y_train)

    #save best model
    rf_best = rf_gs.best_estimator_
    #check best n_estimators value
    print(rf_gs.best_params_)


    #create a new logistic regression model
    log_reg = LogisticRegression(max_iter=1000, solver='liblinear')
    #fit the model to the training data
    log_reg.fit(X_train, y_train)
    
    svc = SVC()
    #create a dictionary of all values we want to test for n_estimators
    params_svc = {'C': [0.1, 1, 10], 'gamma': [0.1, 0.01, 0.001]}
    #use gridsearch to test all values for n_estimators
    svc_gs = GridSearchCV(svc, params_svc, cv=5)
    #fit model to training data
    svc_gs.fit(X_train, y_train)

    #save best model
    svc_best = svc_gs.best_estimator_
    print(svc_gs.best_params_)

    nb = GaussianNB()
    nb.fit(X_train, y_train)

    #test the three models with the test data and print their accuracy scores
    print('knn: {}'.format(knn_best.score(X_test, y_test)))
    print('rf: {}'.format(rf_best.score(X_test, y_test)))
    print('log_reg: {}'.format(log_reg.score(X_test, y_test)))
    print('svc: {}'.format(svc_best.score(X_test, y_test)))
    print('nb: {}'.format(nb.score(X_test, y_test)))


    #create a dictionary of our models
    estimators=[('knn', knn_best), ('rf', rf_best), ('log_reg', log_reg) , ('svc', svc_best), ('nb', nb)]
    #create our voting classifier, inputting our models
    ensemble = VotingClassifier(estimators, voting='hard')

    #fit model to training data
    ensemble.fit(X_train, y_train)
    #test our model on the test data
    print("Accuracy: ", ensemble.score(X_test, y_test))
    et = time.time()
    ts = (et-st) + tl

    sp = time.time()
    comm.bcast(X_train, root=0)
    comm.bcast(y_train, root=0)
    comm.bcast(X_test, root=0)
    comm.bcast(y_test, root=0)



elif rank == 1:
    X_train = comm.bcast(None, root=0)
    y_train = comm.bcast(None, root=0)
    X_test = comm.bcast(None, root=0)
    y_test = comm.bcast(None, root=0)
    #create new a knn model
    knn = KNeighborsClassifier()
    #create a dictionary of all values we want to test for n_neighbors
    params_knn = {'n_neighbors': np.arange(1, 10), 'p': [1, 2]}
    #use gridsearch to test all values for n_neighbors
    knn_gs = GridSearchCV(knn, params_knn, cv=5)
    #fit model to training data
    knn_gs.fit(X_train, y_train)

    #save best model
    knn_best = knn_gs.best_estimator_
    #check best n_neigbors value
    print(knn_gs.best_params_)
    comm.send(knn_best, dest=0, tag=11)

elif rank == 2:
    X_train = comm.bcast(None, root=0)
    y_train = comm.bcast(None, root=0)
    X_test = comm.bcast(None, root=0)
    y_test = comm.bcast(None, root=0)
    #create a new random forest classifier
    rf = RandomForestClassifier()
    #create a dictionary of all values we want to test for n_estimators
    params_rf = {'n_estimators': [50, 100, 150], 'criterion': ['gini', 'entropy']}
    #use gridsearch to test all values for n_estimators
    rf_gs = GridSearchCV(rf, params_rf, cv=5)
    #fit model to training data
    rf_gs.fit(X_train, y_train)

    #save best model
    rf_best = rf_gs.best_estimator_
    comm.send(rf_best, dest=0, tag=22)
    #check best n_estimators value
    print(rf_gs.best_params_)

elif rank == 3:
    X_train = comm.bcast(None, root=0)
    y_train = comm.bcast(None, root=0)
    X_test = comm.bcast(None, root=0)
    y_test = comm.bcast(None, root=0)
    #create a new logistic regression model
    log_reg = LogisticRegression(max_iter=1000, solver='liblinear')
    #fit the model to the training data
    log_reg.fit(X_train, y_train)

    #save best model
    comm.send(log_reg, dest=0, tag=33)

elif rank == 4:
    X_train = comm.bcast(None, root=0)
    y_train = comm.bcast(None, root=0)
    X_test = comm.bcast(None, root=0)
    y_test = comm.bcast(None, root=0)
    #create a new logistic regression model
    svc = SVC()
    #create a dictionary of all values we want to test for n_estimators
    params_svc = {'C': [0.1, 1, 10], 'gamma': [0.1, 0.01, 0.001]}
    #use gridsearch to test all values for n_estimators
    svc_gs = GridSearchCV(svc, params_svc, cv=5)
    #fit model to training data
    svc_gs.fit(X_train, y_train)

    #save best model
    svc_best = svc_gs.best_estimator_
    comm.send(svc_best, dest=0, tag=44)

elif rank == 5:
    X_train = comm.bcast(None, root=0)
    y_train = comm.bcast(None, root=0)
    X_test = comm.bcast(None, root=0)
    y_test = comm.bcast(None, root=0)
    #create a new logistic regression model
    nb = GaussianNB()
    #fit the model to the training data
    nb.fit(X_train, y_train)

    #save best model
    comm.send(nb, dest=0, tag=55)


if rank == 0:
    knn_best = comm.recv(source=1, tag=11)
    rf_best = comm.recv(source=2, tag=22)
    log_reg = comm.recv(source=3, tag=33)
    svc_best = comm.recv(source=4, tag=44)
    nb = comm.recv(source=5, tag=55)
    #test the three models with the test data and print their accuracy scores
    print('knn: {}'.format(knn_best.score(X_test, y_test)))
    print('rf: {}'.format(rf_best.score(X_test, y_test)))
    print('log_reg: {}'.format(log_reg.score(X_test, y_test)))
    print('svc: {}'.format(svc_best.score(X_test, y_test)))
    print('nb: {}'.format(nb.score(X_test, y_test)))

    #create a dictionary of our models
    estimators=[('knn', knn_best), ('rf', rf_best), ('log_reg', log_reg) , ('svc', svc_best), ('nb', nb)]
    #create our voting classifier, inputting our models
    ensemble = VotingClassifier(estimators, voting='hard')
    #fit model to training data
    ensemble.fit(X_train, y_train)
    #test our model on the test data
    print("Accuracy: ", ensemble.score(X_test, y_test))
    ep = time.time()
    tp = (ep-sp) + tl
    print("Sequntial time: ", ts)
    print("Parallel time: ", tp)
    print("Speedup: ", ts/tp)
    print("Number of processors: ", size)
    print("Efficiency: ", (ts/tp)/6)