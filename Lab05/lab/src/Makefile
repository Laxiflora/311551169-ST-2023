CC := gcc

.PHONY: all
all: prog

prog: main.c
	$(CC) -o -g $@ $<

.PHONY: clean
clean:
	rm -rf prog
