#split the data into train(0.75) and test(0.25)
from sklearn.cross_validation import train_test_split
train, test = train_test_split(movie_df, test_size = 0.25)

#fit lasso CV model
predictor_list = list(train.columns.values)
predictor_list.remove('domestic_gross')
predictor_list.remove('target2')

from sklearn.linear_model import LassoCV
clf = LassoCV(cv=3).fit(train[predictor_list],train.domestic_gross)
Y_pred = clf.predict(test[predictor_list])

print(clf.coef_)

#calculate the mean_squared_error
from sklearn.metrics import mean_squared_error
print mean_squared_error(Y_pred, test.domestic_gross)
