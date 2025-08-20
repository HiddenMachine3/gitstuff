def compute_sum(a, b):
	return a + b


def test_compute_sum():
	assert compute_sum(1, 1) == 2

def main():
	print(compute_sum(1, 2))

if __name__ == "__main__":
	main()