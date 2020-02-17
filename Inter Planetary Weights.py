#Adam
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
pWeight = float( input('What is your weight on Earth? '))

# Compute
# Weight = Earth Weight * Surface Gravity Factor
nMercury = pWeight * fMERCURY
nVenus = pWeight * fVENUS
nMoon = pWeight * fMOON
nMars = pWeight * fMARS
nJupiter = pWeight * fJUPITER
nSaturn = pWeight * fSATURN
nUranus = pWeight * fURANUS
nNeptune = pWeight * fNEPTUNE
nPluto = pWeight * fPLUTO


#Output to screen
print( 'Here are your weights on these planets:')
print( format( 'Your weight on Mercury is:',"30s"), format(nMercury,"10.2f"))
print( format( 'Your weight on Venus is:',"30s"), format(nVenus,"10.2f"))
print( format( 'Your weight on Moon is:',"30s"), format(nMoon,"10.2f"))
print( format( 'Your weight on Mars is:',"30s"), format(nMars,"10.2f"))
print( format( 'Your weight on Jupiter is:',"30s"), format(nJupiter,"10.2f"))
print( format( 'Your weight on Saturn is:',"30s"), format(nSaturn,"10.2f"))
print( format( 'Your weight on Uranus is:',"30s"), format(nUranus,"10.2f"))
print( format( 'Your weight on Neptune is:',"30s"), format(nNeptune,"10.2f"))
print( format( 'Your weight on Pluto is:',"30s"), format(nPluto,"10.2f"))
