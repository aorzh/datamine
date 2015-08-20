# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

from sklearn import datasets
from sklearn.cross_validation import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
from io import BytesIO


def index(request):
    context_dict = {}
    # загрузка данных iris
    dataset = datasets.load_iris()
    # процесс настройки модели CART по выборке данных
    model = DecisionTreeClassifier()
    model.fit(dataset.data, dataset.target)
    # print(model)
    # предсказание
    expected = dataset.target
    predicted = model.predict(dataset.data)
    # оценка качества работы предсказательной модели
    report = metrics.classification_report(expected, predicted)
    matrix = metrics.confusion_matrix(expected, predicted)

    # Another example
    lr = linear_model.LinearRegression()
    boston = datasets.load_boston()
    y = boston.target

    # cross_val_predict returns an array of the same size as `y` where each entry
    # is a prediction obtained by cross validated:
    predicted = cross_val_predict(lr, boston.data, y, cv=10)

    fig, ax = plt.subplots()
    ax.scatter(y, predicted)
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    # fig.show()

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict['model'] = model
    context_dict['report'] = report
    context_dict['matrix'] = matrix

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('mainapp/index.html', context_dict, context)
