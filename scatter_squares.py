from matplotlib import colors
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5] 
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)
# #s is size of the dot

# plt.title("square numbers", fontsize = 24)
# plt.xlabel('value', fontsize = 14)
# plt.ylabel('square value', fontsize = 14 )

# plt.tick_params(axis='both',which = 'major', labelsize=14)

# plt.show()

# example 2
x_values1 = list(range(1, 5001))
y_values2 = [x**3 for x in x_values1]

plt.scatter(x_values1, y_values2,c =y_values2, cmap=plt.cm.Purples, edgecolor='none', s=40)
plt.axis([0, 5100, 0, (130*(10**9))])
# borders for x and y;

plt.show()