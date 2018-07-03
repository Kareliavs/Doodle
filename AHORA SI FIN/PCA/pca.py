"""Apply PCA to a CSV file and plot its datapoints (one per line).
The first column should be a category (determines the color of each datapoint),
the second a label (shown alongside each datapoint)."""
import sys
import pandas
import pylab as pl
from sklearn import preprocessing
from sklearn.decomposition import PCA
import json
contenido=open('Airplane.ndjson', "r+")
archivos =json.load(contenido)
def main():
	"""Load data."""
	try:
		csvfile = "Airplanetsne.csv"#sys.argv[1]
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
	contenido.seek(0)  # rewind
   	json.dump(archivos, contenido)
   	contenido.truncate()



def plotpca(xdata, ydata, target_names, items, filename):
	"""Make plot."""
	pca = PCA(n_components=2)
	components = pca.fit(xdata).transform(xdata)
	print(components)
	# Percentage of variance explained for each components
	print('explained variance ratio (first two components):',
			pca.explained_variance_ratio_)

	#pl.figure()  # Make a plotting figure
	#pl.subplots_adjust(bottom=0.1)

	# NB: a maximum of 7 targets will be plotted
	j=1
	for i in range(1000):#, (c, m, target_name) in enumerate(zip(
			#'rbmkycg', 'o^s*v+x', target_names)):
		print("hola",i)
		j=j+1
		#xi = zip(components[ydata == i, 0])
		#yi = zip(components[ydata == i, 1])
		#print(xi[0],yi[1])
		#print("adios")
		#pl.scatter(components[ydata == i, 0], components[ydata == i, 1],
		#		color=c, marker=m, label=target_name)
		for n, x, y in zip(
				(ydata == i).nonzero()[0],
				components[ydata == i, 0],
				components[ydata == i, 1]):
			if n<1000:			
				archivos[n]['cx'] = x
				archivos[n]['cy'] = y
		
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
