import math
annual_volatility = int(input("Input annualized volatility (if 75%, enter 75)\n"))
d = annual_volatility / math.sqrt(365)
LVR = d * d / 8
a_LVR = LVR * 365 / 100
volume_as_percent_TVL = int(input("Input daily volume as a percentage of pool TVL (if 11%, enter 11)\n"))
fees_in_BPS = int(input("Input fees in BPS (if 30 bps, enter 30)\n"))
risk_premia = int(input("Input annual risk premia (if you don't know enter 5 for 5%)\n"))
hurdle = a_LVR + risk_premia
income = fees_in_BPS * volume_as_percent_TVL * 365 / 10000
print('Opportunity Cost: {:.1%}\n'.format(hurdle/100))
print('Promixate Pool Fees: {:.1%}\n'.format(income/100))
if income > hurdle:
    print("LPing may be profitable")
else:
    gap = (hurdle - income) / 100
    print("LPing is definitely not profitable\n")
    print('Shitcoin reward apy to breakeven is: {:.1%}\n'.format(gap))
