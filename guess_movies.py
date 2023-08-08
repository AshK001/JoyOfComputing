import random
pp1name=input("Please enter your name Player 1");
pp2name=input("Please enter your name Player 2");
pp1=0;
pp2=0;
turn=0;
movies=[];
want_to_play=True;
while(want_to_play):
    if turn%2==0 :
        while(want_to_play):
            print("It is your turn to guess the movie",pp1name);
            selected_movie=random.choice(movies);
            ques=make_ques(select_movie);
            print("Guess the movie",ques);
            answer=ask_ques(ques,selected_movie);
            prev_answ=answer;
            if answer==select_movie:
                print("You have choosen the right movie", pp1name);
                pp1+=1;
            else:
                print("Your answer was incorrect");
                want_to_play=int(input("Do you want to play further, press 1 or 0"));
                turn+=1;
                if(want_to_play):
                    pass;
                else:
                    break;
    
    else:
        while(want_to_play):
            print("It is your turn to guess the movie",pp2name);
            selected_movie=random.choice(movies);
            ques=make_ques(select_movie);
            print("Guess the movie",ques);
            answer=ask_ques(ques,selected_movie);
            if answer==select_movie:
                print("You have choosen the right movie", pp2name);
                pp2+=1;
            else:
                print("Your answer was incorrect");
                turn+=1;
                want_to_play=int(input("Do you want to play further, press 1 or 0"))
                if(want_to_play):
                    pass;
                else:
                    break;

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
    letter=input(("What is your first guess letter( you may want to start with vowels)"));
    n=len(ques);
    for i in range(n):
        if letter==selected_movie[i]:
            ans.append(letter);
        else:
            ans.append('*');
    return ans;








        

