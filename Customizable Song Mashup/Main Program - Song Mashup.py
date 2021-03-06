#Programming Assignment 2 - Linh Chi Pham
#Due: Mon, Mar 8, before 10:30pm

#This program analyses people's mentality in a long-distance relationship
#through two songs: Lost in Japan(Shawn Mendes) & Go the Distance (Michael Bolton)
#and lets users create their own song for their loved one from far away.

def main():
    print("       People's feelings and emotions in the context of long distance")
    print("               - A song analysis and Customized application - ")
    print()
    
    #Menu
    print("Please select an option from the following menu:")
    print("A. Song Analysis: Lost in Japan (Shawn Mendes) & Go the Distance (Michael Bolton)")
    print("B. Create a song for your loved one from far away")
    print()
    
    user_choice = input("Enter upper-case letter of your selected option: ")
         
    if user_choice == "A":
        print()

        #PART 1
        print("1. TEXTUAL INFO") #Average word length
        
        #1st song
        print("* Lost in Japan - Shawn Mendes")
        inputfile = open("lostinjapan.txt", "r")
        song1 = inputfile.read()
        word = song1.split()
        numWords = len(word)
        print("Number of words: ", numWords)

        #Remove punctuation from string
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        totalChar = 0
        for i in word: 
            for ch in i:
                if ch not in punctuation:
                    totalChar += len(ch)
       
        print("Number of characters: ", totalChar)
        average_word_length = totalChar / numWords
        print("-> Average word length: ", round(average_word_length, 2))
        print()
        inputfile.close()
        
        #2nd song
        print("* Go the Distance - Michael Bolten")
        inputfile = open("gothedistance.txt", "r")
        song2 = inputfile.read()
        word = song2.split()
        numWords = len(word)
        print("Number of words: ", numWords)
        
        #Remove punctuation from string
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        totalChar = 0
        for i in word:
            for ch in i:
                if ch not in punctuation:
                    totalChar += len(ch)
       
        print("Number of characters: ", totalChar)
        average_word_length = totalChar / numWords
        print("-> Average word length: ", round(average_word_length, 2))
        inputfile.close()
        print()

        #PART 2
        print("2. CONTENT") 

        print("a, Lost in Japan: Feelings of longing")
        print("* Key Lines:")
        
        #Print and count specific lines that are repeated most frequently
        inputfile = open("lostinjapan.txt", "r") 
        song1 = inputfile.read()
        feelings = ["I just wanna see ya", "Can't get you off my mind",
                    "The only thing I'm thinkin' 'bout is you and I"]
        total_lines = 0
        for lines in feelings:
            print(lines)
            total_lines += song1.count(lines)
        print()
        print("-> The lines above are repeated", total_lines, "times throughout the song  to emphasize the" )
        print("   singer's yearning for his loved one.")
    
        inputfile.close()
        print()
        
        print("b, Go the Distance: Firm belief that love will overcome distance")
        print("* Lines: ")
        
        #Print and count lines that start with I will/ I'll
        inputfile = open("gothedistance.txt", "r")
        song2 = inputfile.readlines()
        counter = 0
        for i in song2:
            if i.startswith("I will") or i.startswith("I'll"):
                print(i[:-1]) #slice string by -1 to remove blank line
                counter += 1
        print()
        print('-> Sentences beginning with "I will" are repeated', counter, "times, emphasizing the")
        print("   singer's determination to cross whatever boundary that exists in between.")
  
        print()

        #Print and count lines that contain "go the distance"
        print("* Lines: ")
        counter2 = 0
        for line in song2:
            if "go the distance" in line:
                print(line[:-1])
                counter2 += 1
        print()
        print('-> The phrase "go the distance" appears a total of', counter2, "times in the song, showing")
        print("   the singer's acknowledgement of hardships and determination.")
        print()

        #PART 3
        print("c, CONCLUSION")
        print('"Lost in Japan" and "Go The Distance" both carry a message:')
        print("-> Distance is just a test of how far love can travel. It means so little when")
        print("   someone means so much to you.")
        inputfile.close()
        print()
        
    elif user_choice == "B":
        print()
        print("* Creator's Note:")
        print("If you have someone special that's far away, this program helps make plans for")
        print("when you two meet up in the future and customize your own song to express how")
        print("much you miss them.")
        print()
        inputfile = open("lostinjapan.txt", "r")
        song1 = inputfile.read()
        
        #user-inputted answers to specific questions
        print("First, answer some detail questions below.")
        print("For the best result, format your answers like the given examples.")
        print()
        
        #Replace specific words in the original songs with user-inputted texts
        original_time = "tonight"
        new_time = input("- A time you two would like to meet (ie.tonight): ")
        #store into a new variable
        song1_1 = song1.replace(str(original_time), str(new_time))

        original_distance = "a couple hundred"
        new_distance = eval(input("- Distance between you two (in miles): "))
        #user-inputted numbers turned into strings to be replaced
        song1_2 = song1_1.replace(str(original_distance), str(new_distance))
                                    
        original_country = "Japan"
        new_country = input("- Your special one's location (country/city): ")
        song1_3 = song1_2.replace(original_country,new_country)

        transportation1 = "fly"
        transportation2 = input("- How would you travel there (ie.fly): ")
        song1_4 = song1_3.replace(transportation1,transportation2.lower())
                
        original_location = "your hotel"
        new_location = input("- A specific place where you two would meet (ie.your place): ")
        song1_5 = song1_4.replace(original_location,new_location)

        print()
        
        #Customized song - Mashup version of Lost in Japan and Go the Distance
        #Mashup demo in folder
        print("* Find your song below and send it to your loved one!")
        print()

        #first line from song 1
        song1_5 = song1_5.split("\n") #split song1_5 into list
        for line in song1_5: 
            if "idea" in line: 
                print(line)

        #next 2 lines from song 2
        inputfile2 = open("gothedistance.txt", "r")
        song2 = inputfile2.read()
        song2 = song2.split("\n")
        uniquelines2 = [] #blank list
        for line in song2:
            if "shooting" in line:
                print(line)
            #remove duplicated lines
            if line not in uniquelines2: 
                if "harms" in line:
                    #add 1 line containing "harms" into blank list
                    uniquelines2.append(line) 
        for line in uniquelines2:
            print(line)
        
        #next 2 lines from song 1   
        for line in song1_5:
            if "crazy" in line:
                print(line)
            elif "see ya" in line:
                print(line)
        print()

        #print lines with user-inputted texts 
        uniquelines = [] 
        for line in song1_5:                                                        
            if line not in uniquelines: 
                if "plans" in line and "baby" not in line:
                    #add 1 line that has "plans" but no "baby" into blank list
                    uniquelines.append(line)   
                elif "miles" in line:
                    uniquelines.append(line) 
                elif "was thinkin'" in line:
                    uniquelines.append(line)             
        for line in uniquelines:
            print(line)
            
        #next line from song 1   
        for line in song1_5:
            if "leave" in line:
                print(line)
        print()
        
        #last 3 lines from song 2
        for line in song2:
            if "dreamed" in line:
                print(line)
            elif "unknown" in line:
                print(line)
            elif "wander" in line:
                print(line)
        print()
        print("* Thank you for using! Hope you have had a wonderful experience.")
        
    else: 
        print("The option you chose does not exist. Please select either A or B.")

main()
