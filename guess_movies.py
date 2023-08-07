pp1name=input("Please enter your name Player 1");
pp2name=input("Please enter your name Player 2");
pp1=0;
pp2=0;
turn=0;
movies=[];
want_to_play=True;
while(want_to_play==True):
    if turn%2==0 :
    print("It is your turn to guess the movie",pp1name);
    select_movie=choose_q(movies);
    ques=make_ques(select_movie);
    answer=ask_ques(ques);
    if answer==select_movie:
        print("You have choosen the right movie", pp1name);
        pp1+=1;
    else:
        print("Your answer was incorrect");
        want_to_play=int(input("Do you want to play further, press 1 or 0"))
    turn+=1;
    
else:
    print("It is your turn to guess the movie",pp2name);
    select_movie=choose_q(movies);
    ques=make_ques(select_movie);
    answer=ask_ques(ques);
    if answer==select_movie:
        print("You have choosen the right movie", pp2name);
        pp2+=1;
    else:
        print("Your answer was incorrect");
        turn+=1;

