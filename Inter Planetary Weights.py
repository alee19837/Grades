#Lee, Adam
#Inter Planetary Weights Code

#Named Constant
fMERCURY = 0.38
fVENUS = 0.91
fMOON = 0.165
fMARS = 0.38
fJUPITER = 2.34
fSATURN = 0.93
fURANUS = 0.92
fNEPTUNE = 1.12
fPLUTO = 0.066


#User info (Input)
pName = input('What is your name? ')
pWeight = float(input('What is your weight on Earth? '))

# Compute
# Weight = Earth Weight x Surface Gravity Factor
nMercury = pWeight * fMERCURY
nVenus = pWeight * fVENUS
nMoon = pWeight * fMOON
nMars = pWeight * fMARS
nJupiter = pWeight * fJUPITER
nSaturn = pWeight * fSATURN
nUranus = pWeight * fURANUS
nNeptune = pWeight *fNEPTUNE
nPluto = pWeight *fPLUTO


#Output to screen
print( 'Here are your weights on these planets:')
print( format( 'Your weight on Mercury:',"23s"), format(nMercury,"10.2f"))
print( format( 'Your weight on Venus:',"23s"), format(nVenus,"10.2f"))
print( format( 'Your weight on Moon:',"23s"), format(nMoon,"10.2f"))
print( format( 'Your weight on Mars:',"23s"), format(nMars,"10.2f"))
print( format( 'Your weight on Jupiter:',"23s"), format(nJupiter,"10.2f"))
print( format( 'Your weight on Saturn:',"23s"), format(nSaturn,"10.2f"))
print( format( 'Your weight on Uranus:',"23s"), format(nUranus,"10.2f"))
print( format( 'Your weight on Neptune:',"23s"), format(nNeptune,"10.2f"))
print( format( 'Your weight on Pluto:',"23s"), format(nPluto,"10.2f"))
