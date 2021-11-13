# def train_model(name_dataset, target, features):
# Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the
train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,
‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the
column: ‘diabetes_mellitus’

# def predict_prob(,,.):
# Predict the targets for both the train and test sets and add the prediction as a new column (use
predict_proba from the model to get the predicted probabilities) name the new column something
like predictions.

# def evaluate_fit(...):
# Compute the train and test roc_auc metric using roc_auc_score from sklearn.