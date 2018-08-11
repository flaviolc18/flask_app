def map_input(mode, option):

  threeRate = {1:"not at all", 2:"somewhat", 3:"very"}
  fiveRate = {1:"definitely should not see", 2:"maybe should not see", 3:"not sure if people should or should not see", 4:"maybe should see", 5:"definitely should see"}

  if mode == 3:
    return threeRate[option]
  elif mode == 5:
    return fiveRate[option]
  else:
    return 0