import matplotlib.pyplot as plt
from PIL import Image


def main():
	img = plt.imread("high_resolution_satellite_image.png")
	fig, ax = plt.subplots()
	
	ax.imshow(img)
	x = 38.392535
	y = -110.789353
	ax.imshow(img, extent=[38.384917, 38.427722, -110.818972, -110.765000])
	
	ax.plot(x, y, '--', linewidth=1, color='firebrick')
	fig.savefig('graph.png')


if __name__ == '__main__':  main()

