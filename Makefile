ifeq (run, $(firstword $(MAKECMDGOALS)))
  runargs := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
  $(eval $(runargs):;@true)
endif

run:
	docker build -t stock-allocation .
	docker run -ti stock-allocation python3 stock_allocation.py $(runargs)