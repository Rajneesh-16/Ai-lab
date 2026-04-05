from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Dataset
X = [
 ['Sunny','Hot','High','Weak'],
 ['Sunny','Hot','High','Strong'],
 ['Overcast','Hot','High','Weak'],
 ['Rain','Mild','High','Weak'],
 ['Rain','Cool','Normal','Weak'],
 ['Rain','Cool','Normal','Strong'],
 ['Overcast','Cool','Normal','Strong'],
 ['Sunny','Mild','High','Weak'],
 ['Sunny','Cool','Normal','Weak'],
 ['Rain','Mild','Normal','Weak']
]

y = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes']

# Encode features
enc = [LabelEncoder() for _ in range(4)]
X_enc = list(zip(*[enc[i].fit_transform([row[i] for row in X]) for i in range(4)]))

# Encode target
y_enc = LabelEncoder().fit_transform(y)

# Train model
model = DecisionTreeClassifier()
model.fit(X_enc, y_enc)

# Test sample
test = ['Sunny','Cool','High','Strong']
test_enc = [enc[i].transform([test[i]])[0] for i in range(4)]

pred = model.predict([test_enc])
print("Prediction:", "Play" if pred[0]==1 else "Don't Play")

# -------- TREE VISUALIZATION --------
plot_tree(model, filled=True,
          feature_names=['Outlook','Temp','Humidity','Wind'],
          class_names=['No','Yes'])
plt.show()

'''                Outlook
        ┌─────────┼─────────┐
     Sunny     Overcast     Rain
       │            │          │
   Humidity       Yes       Wind
   ┌───────┐                ┌───────┐
 High    Normal           Weak    Strong
  │         │               │         │
 No        Yes             Yes       No'''