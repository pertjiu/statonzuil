def lang_genoeg(lengte_centimeters):
    if lengte_centimeters >= 120:
        print("je bent lang genoeg")
    else:
        print('je bent te klein')


lang_genoeg(int(input('geef je lengte')))