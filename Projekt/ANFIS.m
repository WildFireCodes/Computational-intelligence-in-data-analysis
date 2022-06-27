%% wczytanie danych

close all; clear; clc;
x_train = readmatrix('train_set.csv');
x_test = readmatrix('test_set.csv');

%% model1

lab = x_test(:, 5);
pred = round(evalfis(model1, x_test(:, 1:4)));
acc = sum(lab == pred, 'all')/140;
[m, order] = confusionmat(lab, pred);
figure
confchart = confusionchart(m, order);

%% model2

lab2 = x_test(:, 5);
pred2 = round(evalfis(model2, x_test(:, 1:4)));
acc2 = sum(lab2 == pred2, 'all')/140;
[m2, order2] = confusionmat(lab2, pred2);
figure
confchart2 = confusionchart(m2, order2);

%% model3

lab3 = x_test(:, 5);
pred3 = round(evalfis(model3, x_test(:, 1:4)));
acc3 = sum(lab3 == pred3, 'all')/140;
[m3, order3] = confusionmat(lab3, pred3);
figure
confchart3 = confusionchart(m3, order3);