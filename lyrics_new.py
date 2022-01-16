
lyrics = "Were not in love We share no stories Just something \in\ your eyes Dont be afraid The shadows know me Lets leave the world behind Take me through the night Fall into the dark side We dont need the light Well live on the dark side I see it Lets feel it While were still young \and\ fearless Let go of the light Fall into the dark side Fall into the dark side Give into the dark side Let go of the light Fall into the dark side Beneath the sky As black \as\ diamonds Were running out of time Dont wait \for\ truth To come \and\ blind us Lets just believe their lies Believe it I see it I know that you can feel it No secrets worth keeping So fool me like Im dreaming Take me through the night Fall into the dark side We dont need the light Well live on the dark side I see it Lets feel it While were still young \and\ fearless Let go of the light Fall into the dark side Fall into the dark side Give into the dark side Let go of the light Fall into the dark side Take me through the night Fall into the dark side We dont need the light Well live on the dark side I see it Lets feel it While were still young \and\ fearless Let go of the light Fall into the dark side"
print(lyrics)


def freq(str):
    
    str = str.split()
    str2 = []

    for i in str:             
  
        # checking for the duplicacy
        if i not in str2:
  
            # insert value in str2
            str2.append(i) 
              
    for i in range(0, len(str2)):
  
        # count the frequency of each word(present 
        # in str2) in str and print
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))


freq(lyrics)
