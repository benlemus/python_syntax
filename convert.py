def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if unit_in == 'c' or unit_in =='f':
        if unit_out == 'c' or unit_out == 'f':
          if unit_in == unit_out:
              return temp
          else:
            if unit_in == 'c':
                return (temp * 9/5) + 32
            elif unit_in == 'f':
                return (temp - 32) * 5/9 
        else:
            if unit_out != 'c' or 'f':
                invalid_unit = unit_out
          
            return f'invalid unit [{invalid_unit}]'
    else:
        if unit_in != 'c' or 'f':
              invalid_unit = unit_in
        return f'invalid unit [{invalid_unit}]'


  

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

