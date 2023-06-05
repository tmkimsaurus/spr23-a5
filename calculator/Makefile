calculator: main.o addition.o subtraction.o multiplication.o division.o
	cc -o calculator main.o addition.o subtraction.o multiplication.o division.o

main.o: main.c
	cc -c main.c

addition.o: operations.h
	cc -c addition.c

subtraction.o: operations.h
	cc -c subtraction.c

multiplication.o: operations.h
	cc -c multiplication.c

division.o: operations.h
	cc -c division.c

clean:
	rm -f calculator main.o addition.o subtraction.o multiplication.o division.o

.PHONY: clean
