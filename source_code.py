setwd()
prc=read.csv("Prostate_Cancer.csv")
View(prc)
prc=prc[-1]
str(prc)
table(prc$diagnosis_result)
prc$diagnosis <- factor(prc$diagnosis_result, levels = c("B", "M"), labels = c("Benign", "Malignant"))
round(prop.table(table(prc$diagnosis)) * 100, digits = 1)
normalize <- function(x) { return ((x - min(x)) / (max(x) - min(x))) }
prc_n <- as.data.frame(lapply(pcr[2:9], normalize))
prc_train <- prc_n[1:599,]
prc_test <- prc_n[599:1000,]
prc_train_labels <- prc[1:599, 1]
prc_test_labels <- prc[599:1000, 1]
install.packages(“class”)
library(class)
sqrt(15) //for k values
prc_test_pred <- knn(train = prc_train, test = prc_test,cl = prc_train_labels, k=10)
prc_test_pred
table(prc_test_target,prc_test_pred)
install.packages("gmodels")
CrossTable(x=prc_test_pred,y=prc_test_target,prop.chisq = FALSE) //confusion matrix
patient_id=can$id[565:569]
p_id=as.data.frame(patient_id)
test_diagnosis=can_pred
cbind(p_id,test_diagnosis)
