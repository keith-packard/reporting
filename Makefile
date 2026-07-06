INPUT = reports pairs
ALL = bottom-up top-down no-memory

all: $(ALL)
	cmp bottom-up top-down && cmp top-down no-memory

bottom-up: bottom-up.py $(INPUT)
	python bottom-up.py > $@

top-down: top-down.py $(INPUT)
	python top-down.py > $@

no-memory: no-memory.py $(INPUT)
	python no-memory.py > $@

clean:
	rm -f $(ALL)
