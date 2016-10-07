import sys

def main():
	in_file = sys.argv[1]
	f = open(in_file, "r")
	line = f.readline()
	cnt = 0
	while True:
		line = f.readline()
		if line == "":
			break
		if line[0] == '1':
			cnt += 1
	print(in_file, " -- ", cnt)
	f.close()

if __name__ == "__main__":
	main()