"""
Tools for calculating savings needed for retirement.
"""
def num_years_from_savings(num_years_contributing, yearly_contribution,
                           yearly_retirement_withdrawal,
                           market_yearly_return = 0.04,
                           inflation_yearly_rate = 0.035,
                           max_years = 100):
    """
    Given a yearly contribution to investments for a given
    number of years, if you withdraw a given amount (inflation
    adjusted) every year after the investment period, how
    many years can you continue to withdraw?

    num_years_contributing = initial number of years during
       which you are contributing to your investments
       without withdrawing from them.  E.g. 30 years
    yearly_contribution = amount you contribute every year
       during the initial investment period in today's
       dollars. E.g. $60,000
    yearly_retirement_withdrawal = amount you withdraw
       every year after the initial investment period
       in today's dollars. E.g. $90,000
    market_yearly_return = The estimated yearly growth of
       your investments.  E.g 0.05 = 5%
    inflation_yearly_rate = The estimated yearly inflation
       rate.  E.g 0.035 = 3.5%
    max_years = the maximum possible number of years you
       could live after retirement

    Returns the number of years after the initial investment
    period for which you could continue withdrawing the
    amount specified before using up all of your
    investments.
    """
    # Calculate the amount your investments will be
    # worth in today's dollars after the investment
    # period.
    multiplier = (1. + market_yearly_return) / \
                 (1. + inflation_yearly_rate)
    investments = yearly_contribution * \
                  sum(multiplier ** i for i
                      in range(1, num_years_contributing + 1))

    # Withdraw yearly_retirement_withdrawal every year
    # and continue scaling the remaining investments
    # by multiplier every year, until investments go
    # to zero.  Then return the number of years this
    # took.
    for num_years_retired in range(1, max_years + 1):
        investments -= yearly_retirement_withdrawal
        investments *= multiplier
        if investments < 0:
            break

    return num_years_retired - 1
