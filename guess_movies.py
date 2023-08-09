import random
def make_ques(movie):
    n=len(movie);
    q=[];
    for i in range(n):
        if(movie[i]!=' '):
            q.append('*')
        else:
            q.append(' ')
    ques=''.join(q)
    return ques;

def ask_ques(ques,selected_movie):
    ans=[];
    letter=input(("What is your first guess letter(you may want to start with vowels)"));
    n=len(ques);
    for i in range(n):
        if letter==selected_movie[i]:
            ans.append(letter);
        else:
            ans.append('*');
    prev_answ=''.join(ans);
    return prev_answ;
pp1name=input("Please enter your name Player 1");
pp2name=input("Please enter your name Player 2");
pp1=0;
pp2=0;
turn=0;
movies=['Pappu','Lappu','Jhappu','Tappu'];
want_to_play=True;
while(want_to_play):
    if turn%2==0 :
        print("It is your turn to guess the movie",pp1name);
        selected_movie=random.choice(movies);
        ques=make_ques(selected_movie);
        print("Guess the movie",ques);
        while(True):
            prev_answer=ask_ques(ques,selected_movie);
            if prev_answer==selected_movie:
                print("You have choosen the right movie", pp1name);
                pp1+=1;
                print("Your Score", pp1)
                break;
            else:
                print(prev_answer)
                print("You may want to guess again or do you want to quit?");
                flag=int(input("Press 1 to continue or 0 to quit"))
                if(flag):
                    ques=prev_answer;
                else:
                    want_to_play=False;
                    break;
                
    else:
        print("It is your turn to guess the movie",pp1name);
        selected_movie=random.choice(movies);
        ques=make_ques(selected_movie);
        print("Guess the movie",ques);
        while(True):
            prev_answer=ask_ques(ques,selected_movie);
            if answer==selected_movie:
                print("You have choosen the right movie", pp1name);
                pp1+=1;
                print("Your Score", pp1)
                break;
            else:
                print(prev_answer)
                print("You may want to guess again or do you want to quit?");
                flag=int(input("Press 1 to continue or 0 to quit"))
                if(flag):
                    ques=prev_answer;
                else:
                    want_to_play=False;
                    break;









        

