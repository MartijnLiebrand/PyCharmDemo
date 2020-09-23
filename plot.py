import matplotlib.pyplot as plt

data = [21,22,23,4,5,6,77,8,9,10,60,53,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 20
plt.xlabel("Phred Score")
plt.ylabel("Aantal gemeten Phred Scores")
plt.axis([-0.5, 100.5, 0, 10])
plt.title("")
plt.hist(data, num_bins)
plt.show()


#kan je een plot maken van de verdeling van wijnen op basis van alcoholpercentages?