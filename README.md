# stock-allocation

This is a program I use when investing, as it
simply eases the task of how figuring out how
to split my investments based on my overall
strategy.

## Installation & usage

You will need `make` and `docker` available
in your system. Then you can simply run
`make run -- sample.yaml`.

## Customization

Add a `yaml` file with your own investment splits
in order to customize this to your needs.

The sample provides ample clarification:

```yml
# This is what you currently
# have invested
portfolio:
    TSLA: 1000
    GOOG: 10000
    BNDW: 2000
    SPY:  5000

# This is the cash amount you have
# available to invest.
surplus: 20000

# This maps individual tickers
# to an asset class or your own
# pool. For example, you could decide
# to dedicate 3% of your assets towards
# green energy companies, so here you'd
# list X green energy tickers and map
# them to, say, a GREEN_ENERGY class.
investment_map:
    TSLA: BETS
    GOOG: BETS
    BNDW: BOND
    SPY:  MARKET

# This is how you'd like
# to diversify your investments, by "class".
# The amounts are percentages,
# so 10 means 10% of your total
# invested assets.
ideal_allocation_percent:
    BETS: 10
    MARKET: 80
    BOND: 10
```

Running `make run -- sample.yaml` gives you:

```console
$ make run -- sample.yaml
docker build -t stock-allocation .
Sending build context to Docker daemon  58.88kB
Step 1/4 : FROM python:3-alpine
 ---> 4c30403e92a1
Step 2/4 : RUN pip install pyyaml
 ---> Using cache
 ---> 49cac903e7ed
Step 3/4 : COPY . /src
 ---> 5de29841a972
Step 4/4 : WORKDIR /src
 ---> Running in 0b4b162b86d0
Removing intermediate container 0b4b162b86d0
 ---> a8abfdb3e64c
Successfully built a8abfdb3e64c
Successfully tagged stock-allocation:latest
docker run -ti stock-allocation python3 stock_allocation.py sample.yaml
Current allocation:
{
    "BETS": 11000,
    "BOND": 2000,
    "MARKET": 5000
}
Total to invest: 38000
Ideal allocations:
{
    "BETS": 3800.0,
    "BOND": 3800.0,
    "MARKET": 30400.0
}
This is how you should invest:
{
    "BOND": 2222.22,
    "MARKET": 17777.78
}
make: 'sample.yaml' is up to date.
```