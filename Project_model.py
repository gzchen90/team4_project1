#split the data into train(0.75) and test(0.25)
from sklearn.cross_validation import train_test_split
train, test = train_test_split(movie_df, test_size = 0.25)

#fit lasso CV model
#predictor_list is the list of variables that we want to use for modelling
#here I get it from the column names -predictors and movie title. you
#can create your own directly from the name list
predictor_list = list(train.columns.values)
predictor_list.remove('domestic_gross')
predictor_list.remove('tomatoRating')
predictor_list.remove('new_title')

#fit the lasso model, which get selection and estimation at one step.
#if you want to see which variable is significant, there is an easy way:
#just look at the coefficients, greater than 0 means that it is used for prediction

from sklearn.linear_model import LassoCV
clf = LassoCV(cv=20).fit(train[predictor_list],train.domestic_gross)
Y_pred = clf.predict(test[predictor_list])

print(clf.coef_)

#calculate the mean_squared_error
from sklearn.metrics import mean_squared_error
print mean_squared_error(Y_pred, test.domestic_gross)
