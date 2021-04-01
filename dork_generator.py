from random import choice
import argparse
import time 
import concurrent.futures 

count = 0

def worker(dork_type):
    global count 
    parsing = list()
    # PARSING DORK_TYPE
    for i in range(0, len(dork_type)+1, 1):
        temp = dork_type[i-2:i]
        if temp:
            if temp[0].isupper() and temp[1].isupper():
                dork_type
                parsing.append(temp)

    dork_type = "".join(x for x in dork_type if not x.isupper())

    for u in data_dict[parsing[0]]:
        for n in data_dict[parsing[1]]:
            for c in data_dict[parsing[2]]:

                if len(parsing) >3:
                    for x in data_dict[parsing[3]]:

                        if len(parsing) > 4:
                            for w in data_dict[parsing[4]]:
                                out.write(dork_type.format(u,n,c,x,w)+"\n")
                                count += 1
                        else:
                            out.write(dork_type.format(u,n,c,x)+"\n")
                            count += 1
                else:
                    out.write(dork_type.format(u, n, c)+"\n")
                    count += 1

    return "SUCCESS" 
def core(filein, max_dork, output):
    global data_dict
    global out 
    global numbers

    out = open(output, 'w')
    data_dict = dict()
    data = [
        ("DE", "preset3_domainextensions.txt"),
        ("KW", filein),
        ("PT", "default_pagetypes.txt"),
        ("PF", "default_pageformats.txt"),
        ("SF", "default_searchfunctions.txt"),
    ]
 
    for i in data:
        if i[0] == "KW":
            data_dict[i[0]] = [x.split("\n")[0]
                               for x in open(i[1], 'r').readlines()]
        elif i[0] == "DE":
            data_dict[i[0]] = [x.split("\n")[0] for x in open(i[1], 'r').readlines()]
        else:
            data_dict[i[0]] = open(i[1], 'r').readlines()[0].split()
 
    dorktypes = [x.strip() for x in open('dorktypes.txt','r').readlines()]
 
    numbers =  list(range(1,30,3))

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(dorktypes)+1) as executor:
        completed = executor.map(worker, dorktypes)

    res = list(completed)
    print(count)

if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--filein", type=str, default="keywords.txt",
                     required=False, help="Your List of Keywords")
    arg.add_argument("-m", "--max_dork", type=int,default=None,
                     required=False, help="Max dork you want")
    arg.add_argument("-o", "--output", type=str,
                     default="result.txt", help="Your Result Output")
    args = vars(arg.parse_args())
    start = time.time()
    core(**args)
    end = time.time()
    print(end - start)
