library('e1071')
MyData <- read.csv(file="data/processed.cleveland.data", header=TRUE, sep=",")
col_names = c('age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num')
colnames(MyData)= col_names
MyData <- na.omit(MyData)
MyData<-MyData[!(MyData$ca=="?" | MyData$thal=='?'),]


MyData$ca<-as.factor(MyData$ca)
MyData$thal<-as.factor(MyData$thal)
MyData$ca<-as.numeric(MyData$ca)
MyData$thal<-as.numeric(MyData$thal)
MyData$num<-as.factor(MyData$num)



summary(MyData)
str(MyData)

x <- subset(MyData, select=-num)
y <- MyData$num
 
svm_model1 <- svm(x,y)
summary(svm_model1)

pred <- predict(svm_model1,x)
results <-table(pred,y)

print((results['0','0']+results['1','1']+results['2','2']+results['3','3']+results['4','4'])/sum(results))


