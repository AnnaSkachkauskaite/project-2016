import sys

def main():
	f = open("result", "r")
	line = f.readline()
	cnt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
	cnt1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	while True:
		line = f.readline()
		if line == "":
			break
		cnt[int(line[6])] += int(line.split("-")[-1])
		cnt1[int(line[6])] += 1.0
	i = 0
	while i < 10:
		if cnt1[i] > 0:
			cnt[i] = cnt[i] / (cnt1[i] * 100000.0)
		i += 1
	print(cnt)
	f.close()

if __name__ == "__main__":
	main()