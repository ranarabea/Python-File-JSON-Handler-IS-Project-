import os
import json
user_g = []
def ready():
    job_list = []
    if os.path.exists('jobs.txt'):
        if not os.path.exists('users_main.txt'):
            with open('jobs.txt','w') as f:
                json.dump([],f)

    else:
        with open('jobs.txt', 'w') as f:
            json.dump(job_list, f)
ready()
while True:

    print('hello sir: '
    '\nif you want sign up please press 1'
    '\nif you want log in please press 2'
    '\nif you want exit please press 3')
    f_input = input()


    def sign_up(name, email, password, type):

        if os.path.exists('users_main.txt'):
            with open('users_main.txt', 'r') as f:
                users = json.load(f)
            for i in users:
                if i[2] == email:
                    print('this email is alraedy exists pls try again.')
                    return
            id = users[-1][0] + 1
            all = [id,name,email,password,type]
            users.append(all)
            with open('users_main.txt', 'w') as f:
                json.dump(users, f)
            with open(name +'_' + str(id) +'.txt','w') as f:
                pass

        else:
            users = []
            all = [1, name, email, password, type]
            users.append(all)
            with open('users_main.txt', 'x') as fl:
                json.dump(users, fl)
            with open(name + '_' + '1' + '.txt', 'x') as f:
                pass

    def login(email , password):
        if os.path.exists('users_main.txt'):
            with open('users_main.txt','r') as f:
                sort_users = json.load(f)
            for user in sort_users:
                if email in user and password in user:
                    global user_g
                    user_g = user

                    return
            print('wrong email or password , pls try again')
            return

        else:
            print('ops pls try again or try to do sign up ')

    def start(user):
        if user[-1] == 'client':
            print('hello mr,'+user[1]
                +'\n if you want add a new job press 1 '
                +'\n if you want to take a look at who wants to job press 2'
                +'\n if you want to return to main page press 3')
            option = input()
            if option == '1':
                title = input('give me a title:')
                details = input('give me a details:')
                job_list =[user[0],title , details]
                print('job has been added successfully')

                with open('jobs.txt','r') as f:
                    jobs = json.load(f)
                jobs.append(job_list)
                with open('jobs.txt','w') as f:
                    json.dump(jobs,f)
                start(user_g)
            elif option == '2':
                with open(user_g[1] + '_' + str(user_g[0]) + '.txt', 'r') as f:
                    test = f.readlines()
                if len(test) == 0 :
                    print(' you not have  any requests now <3 ')

                else:
                    ids = []
                    ids_names = []
                    with open(user_g[1] + '_' + str(user_g[0]) + '.txt', 'r') as f:
                        requests = json.load(f)
                        test_2 = f.readlines()
                    if len(test_2) == 0:
                        print('till now you don`t have any requests')
                        return


                    for req in requests:
                        print(req[1]+ ': ' +req[2]+ 'and his id :' + str(req[0]))
                        ids_names.append([req[1],str(req[0])])
                        ids.append(req[0])
                    print('who will you chosse.?'+
                    '\n when you decide ,  if you accept write his id'+
                    '\n if not write his name ')
                    respon = input()
                    for resp in ids_names:
                        if respon == resp[1]:
                            ids.remove(req[0])
                            print(ids)
                            with open(resp[0]+'_'+resp[1]+'.txt','r') as f:
                                test2 = f.readlines()
                                if len(test2) == 0:
                                    with open(resp[0] + '_' +resp[1]+'.txt','w') as f:
                                        json.dump([   [  user_g[0],user_g[1],user_g[2],'accrpted'  ]   ],f)
                                else:
                                    with open(resp[0] + '_' +resp[1]+'.txt','r') as f:
                                        date = json.load(f)
                                    date.append([  user_g[0],user_g[1],user_g[2],'accrpted'  ])
                                    with open(resp[0] + '_' +resp[1]+'.txt','w') as f:
                                        json.dump(date,f)
                                    with open(user_g[1] + '_' + str(user_g[0]) + '.txt', 'r') as f:
                                        date_ = json.load(f)
                                    for i in date_:
                                        if i[0] not in ids:
                                            date_.remove(i)
                                            with open(user_g[1] + '_' + str(user_g[0]) + '.txt', 'w') as f:
                                                json.dump(date_, f)



                    if respon == resp[0]:
                            ids.remove(req[0])
                            with open(resp[0] + '_' + resp[1] + '.txt', 'r') as f:
                                test2 = f.readlines()
                                if len(test2) == 0:
                                    with open(resp[0] + '_' + resp[1] + '.txt', 'w') as f:
                                        json.dump([[user_g[0], user_g[1], user_g[2], 'refused']], f)
                                else:
                                    with open(resp[0] + '_' + resp[1] + '.txt', 'r') as f:
                                        date = json.load(f)
                                    date.append([user_g[0], user_g[1], user_g[2], 'refused'])
                                    with open(resp[0] + '_' + resp[1] + '.txt', 'w') as f:
                                        json.dump(date, f)
                                    with open(user_g[1]+ '_'+str(user_g[0])+'.txt','r') as f:
                                        date_ = json.load(f)
                                    for i in date_:
                                        print(ids)
                                        if i[0] not in ids:
                                            date_.remove(i)
                                            with open(user_g[1]+ '_'+str(user_g[0])+'.txt','w') as f:
                                                json.dump(date_,f)

            elif option == '3':
                return
        elif user[-1] == 'freelancer':
            print('hello mr ,'+user[1])
            with open('jobs.txt','r') as f:
                jobs = json.load(f)
                if jobs == []:
                    print(' oh sorry not exists any jobs today. ')
                else:
                    id_of_jobs = []
                    print('this is all jobs exists now:\n')
                    for job in jobs:
                        print('---------------------')
                        print('id client is: '+str(job[0]) + '     ' + job[1])
                        print('      ' + job[2])
                        print('---------------------')
                        id_of_jobs.append(str(job[0]))

                    print('if you like any jobs and you want send a request to take it , write it`s id ' +
                        '\n if you want serach for a specific job write it titile' +
                        '\n if it doesn`t suit you write thx'  )
                    request = str(input())

                    if request in id_of_jobs:
                        with open('users_main.txt','r') as f:
                            users = json.load(f)
                        for user in users :

                            if request == str(user[0]):
                                with open(user[1] + '_' + str(user[0]) + '.txt','r') as f:
                                    lines = f.readlines()
                                if len(lines) == 0:
                                    with open(user[1] + '_' + str(user[0])+'.txt','w') as f:
                                        json.dump([[user_g[0],user_g[1],'want this job ']],f)
                                        print(' your request has been sent successfully <3')
                                else:
                                    print('in else')
                                    with open(user[1] + '_' + str(user[0])+'.txt','r') as f:
                                        date = json.load(f)
                                    date.append([user_g[0] , str(user_g[1]),'want this job '])
                                    with open(user[1] + '_' + str(user[0])+'.txt','w') as f :
                                        json.dump(date,f)
                                    print(' your request has been sent successfully <3')

                    elif request == 'thx' or 'thanks':
                        return
                    else:
                        print('this id isn`t not exist ')
                        return



    def input_(prom):
        if prom == '1':
            name = input('enter your name: ')
            email = input('enter your email: ')
            password = input('enter your password: ')
            type = input('enter your type(client or freelancer): ')
            sign_up(name , email , password ,type)
        elif prom == '2':
            email = input('pls put your email:')
            password = input('pls put your password:')
            login(email,password)
            if user_g != []:
                start(user_g)

        elif prom == '3':
            quit()

    input_(f_input)



