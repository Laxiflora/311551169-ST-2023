CC=gcc
CFLAGS=-fsanitize=address
SRCS = $(wildcard *.c)
EXECUTABLES = $(SRCS:.c=)
USE_CFLAG=1
OUT_DATA=$(SRCS:.c=.out)
valgrind: CFLAGS=

all: valgrind asan

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

valgrind: $(EXECUTABLES)

asan: $(EXECUTABLES)

clean:
	rm -f $(EXECUTABLES)
	rm -f $(OUT_DATA)

