from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

## g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the train data. 
# Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, 
# ‘hepatic_failure’, ‘immunosuppression’, ‘leukemia’, ‘lymphoma’, 
# ‘solid_tumor_with_metastasis’. Use as target the column: ‘diabetes_mellitus’

## h. Predict the targets for both the train and test sets and add the prediction 
# as a new column (use predict_proba from the model to get the predicted probabilities) 
# name the new column something like predictions.


def logit(name_target, name_features, name_train, name_test):
    F = name_train[name_features]
    y = name_train[name_target]
    Ftest = name_test[name_features]

    lregr = LogisticRegression(penalty='l2', C=100.0, 
                           fit_intercept=True, 
                           intercept_scaling=1, 
                           solver='liblinear', max_iter=500)
    lregr.fit(F,y.values.ravel())
    name_train['prob_hat'] = lregr.predict_proba(F)[:,1]
    name_test['prob_hat'] = lregr.predict_proba(Ftest)[:,1]
    return name_train, name_test
    

# features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
#             'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
# target = ['diabetes_mellitus']
# trainset, testset = logit(target, features, trainset, testset)

## i. Compute the train and test roc_auc metric using roc_auc_score from sklearn.

def auc_score(name_target, name_prhat, name_dataset):
    return roc_auc_score(name_dataset[name_target], name_dataset[name_prhat])

# auc_score(target, 'prob_hat', testset)
# auc_score(target, 'prob_hat', trainset)