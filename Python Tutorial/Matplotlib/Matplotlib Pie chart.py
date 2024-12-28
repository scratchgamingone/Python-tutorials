import matplotlib.pyplot as plt
plt.figure()
values = [3, 12, 5, 8]
labels = ['a', 'b', 'c', 'd']
plt.pie(values, labels=labels, autopct='%.2f')
plt.show()
