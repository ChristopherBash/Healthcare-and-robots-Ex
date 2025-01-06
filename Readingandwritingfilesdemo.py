import random, os

os.chdir('C:\\Sample')

#Quiz data.  Keys are states and values are the capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento',
'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island':
'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}

#Create the quizzes and answer key files

for quizNum in range(35):
    
    quizfile=open('capitalsquiz%s.txt' % (quizNum +1),'w')
    answerKeyFile=open('capitalsquiz_answers%s.txt' % (quizNum+1),'w')

    # Write out the header for the quiz.
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' '*20)+ 'State Capitals Quiz (Form%s)'  % (quizNum +1))
    quizfile.write('\n\n')

    #Shuffle the order of the states
    states=list(capitals.keys())
    random.shuffle(states)

    if quizNum==0:
       print (states)
    

    #Loop through all 50 states, making a question for each.
    for questionnum in range(50):
        #Get right and wrong answers
        correctanswer=capitals[states[questionnum]]
        wronganswers=list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers=random.sample(wronganswers,3)
        answeroptions=wronganswers+[correctanswer]
        random.shuffle(answeroptions)

        #Write the question and answer options to the quiz file
        quizfile.write('%s. What is the capital of %s?\n'  % (questionnum+1,states[questionnum]))
        for i in range(4):
            quizfile.write('     %s.  %s\n' % ('ABCD'[i],answeroptions[i]))
        quizfile.write('\n')

        #Write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionnum+1,'ABCD'[answeroptions.index(correctanswer)]))

quizfile.close()
answerKeyFile.close()
                            
                

        

        
        
                         


    
    

    
    
