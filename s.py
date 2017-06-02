import music
from microbit import*
while True:
    careless_whisper = ("C#6:4","B5:2","F#5:3","D5:4","C#6:4","B5:2","F#5:3","D5:4","R:2","A5:4","G5:2","D5:3","B4:4","A5:4","G5:2",
                     "D5:6","R:4","G5:4","F#5:2","D5:4","B4:4","G4:15","F#4:4","G4:4","A4:4","B4:4","C#5:4","D5:4","E5:4","F#5:4",
                     "C#6:4","B5:2","F#5:3","D5:4","C#6:4","B5:2","F#5:3","D5:4","R:2","A5:4","G5:2","D5:3","B4:4","A5:4","G5:2",
                     "D5:6","R:4","G5:4","F#5:2","D5:4","B4:4","G4:15","F#4:4","G4:4","A4:4","B4:4","C#5:4","D5:4","E5:4","F#5:4",
                     "B4:16")
                     
    marvin_gaye = ("G4:6","A4:6","C5:6","E5:12")
    
    if button_a.is_pressed():
        music.play(careless_whisper)
        
    if button_b.is_pressed():
        music.play(marvin_gaye)
