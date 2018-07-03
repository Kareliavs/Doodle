"""Apply PCA to a CSV file and plot its datapoints (one per line).
The first column should be a category (determines the color of each datapoint),
the second a label (shown alongside each datapoint)."""
import sys
import pandas
import pylab as pl
from sklearn import preprocessing
from sklearn.decomposition import PCA


def main():
	"""Load data."""
	try:
		csvfile = "Airplane.csv"#sys.argv[1]
	except IndexError:
		print '%s\n\nUsage: %s [--3d] <csv_file>' % (__doc__, sys.argv[0])
		return
	data = pandas.read_csv(csvfile, index_col=(0, 1))

	# first column provides labels
	ylabels = [a for a, _ in data.index]
	print(ylabels)
	labels = [text for _, text in data.index]
	encoder = preprocessing.LabelEncoder().fit(ylabels)

	xdata = data.as_matrix(data.columns)
	ydata = encoder.transform(ylabels)
	target_names = encoder.classes_
	plotpca(xdata, ydata, target_names, labels, csvfile)


def plotpca(xdata, ydata, target_names, items, filename):
	"""Make plot."""
	pca = PCA(n_components=2)
	components = pca.fit(xdata).transform(xdata)

	# Percentage of variance explained for each components
	print('explained variance ratio (first two components):',
			pca.explained_variance_ratio_)

	#pl.figure()  # Make a plotting figure
	#pl.subplots_adjust(bottom=0.1)

	# NB: a maximum of 7 targets will be plotted
	for i in range(50):#, (c, m, target_name) in enumerate(zip(
			#'rbmkycg', 'o^s*v+x', target_names)):
		print(i,components[ydata == i, 0],components[ydata == i, 1])
		#pl.scatter(components[ydata == i, 0], components[ydata == i, 1],
		#		color=c, marker=m, label=target_name)
		for n, x, y in zip(
				(ydata == i).nonzero()[0],
				components[ydata == i, 0],
				components[ydata == i, 1]):
			print(n,x,y)
			#pl.annotate(
			#		items[n],
			#		xy=(x, y),
			#		xytext=(5, 5),
			#		textcoords='offset points',
			#		color=c,
			#		fontsize='small',
			#		ha='left',
			#		va='top')
	#pl.legend()
	#pl.title('PCA of %s' % filename)
	#pl.show()


if __name__ == '__main__':
	main()
