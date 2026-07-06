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

reports: gen-reports.py names
	python gen-reports.py > $@

pairs: gen-pairs.py names
	python gen-pairs.py > $@

org.svg: org.dot
	dot -Tsvg org.dot > $@

org.dot: make-graph.py reports
	python make-graph.py > $@

clean:
	rm -f $(ALL)
