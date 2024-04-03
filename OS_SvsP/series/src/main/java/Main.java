//public class Main {
//    public static void main(String[] args) {
//        KNNClassifier knnClassifier = new KNNClassifier();
//        knnClassifier.run();
//
//        LogisticRegressionClassifier logisticRegressionClassifier = new LogisticRegressionClassifier();
//        logisticRegressionClassifier.run();
//
//        RandomForestClassifier randomForestClassifier = new RandomForestClassifier();
//        randomForestClassifier.run();
//    }
//}

import smile.data.*;


public class Main {
    public static void main(String[] args) throws Exception {
        var iris = Read.arff("path/to/iris.arff", "class");
        System.out.println("Dataset loaded.");


    }
}