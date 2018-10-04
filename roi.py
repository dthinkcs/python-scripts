def money_in_bank_given(initial, time_weeks):
  """
    >>> money_in_bank_given(35, 4)
    560
    >>> money_in_bank_given(35, 8)
    8960
    >>> money_in_bank_given(35, 16)
    2293760
    >>> money_in_bank_given(35, 12)
    143360
    
    >>> # power of compounding
    >>> # skillset: AD creation and customer acquisition
  """
  return initial * 2 ** time_weeks
