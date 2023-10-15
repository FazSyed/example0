def test_square_area_8():
    area = square_area(8)
    assert (area==64)

def square_area(x):
    return x*x

def main():
    test_square_area_8()

if __name__ == "__main__":
    main()