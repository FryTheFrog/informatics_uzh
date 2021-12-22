#!/usr/bin/env python3
from public.exchange_rates import EXCHANGE_RATES


def convert(amount, from_currency, to_currency):
    is_valid = isinstance(amount, float) \
               and isinstance(from_currency, str) \
               and from_currency \
               and isinstance(to_currency, str) \
               and to_currency
    if not is_valid:
        raise Warning("invalid parameters")

    er = None
    if from_currency in EXCHANGE_RATES.keys():
        if to_currency in EXCHANGE_RATES[from_currency].keys():
            er = EXCHANGE_RATES[from_currency][to_currency]
    if to_currency in EXCHANGE_RATES.keys():
        if from_currency in EXCHANGE_RATES[to_currency].keys():
            er = 1 / EXCHANGE_RATES[to_currency][from_currency]

    if er is None:
        raise Warning("no exchange rate found: {}»{}".format(from_currency, to_currency))

    return amount * er
