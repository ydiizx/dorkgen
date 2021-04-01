from random import choice
import argparse
import time 
import concurrent.futures 

count = 0

def worker(dork_type):
    global count
    print("WORKER")
    for KW in data_dict['keywords']:
        for DE in data_dict['domain_ext']:
            for PT in data_dict['pagetypes']:
                for PF in data_dict['pageformats']:
                    for SF in data_dict['searchfunctions']:
                        temp_dict = dict(
                                KW=KW, 
                                DE=DE,
                                PT=PT,
                                PF=PF,
                                SF=SF, 
                                NB=choice(numbers))
                        out.write(dork_type.format(**temp_dict))
                        count += 1
    return "SUCCESS" 
def core(filein, max_dork, output):
    global data_dict
    global out 
    global numbers

    out = open(output, 'w')
    data_dict = dict()
    data = [
        ("domain_ext", "preset3_domainextensions.txt"),
        ("keywords", filein),
        ("pagetypes", "default_pagetypes.txt"),
        ("pageformats", "default_pageformats.txt"),
        ("searchfunctions", "default_searchfunctions.txt"),
    ]
 
    for i in data:
        if i[0] == "keywords":
            data_dict[i[0]] = [x.split("\n")[0]
                               for x in open(i[1], 'r').readlines()]
        elif i[0] == "domain_ext":
            data_dict[i[0]] = [x.split("\n")[0] for x in open(i[1], 'r').readlines()]
        else:
            data_dict[i[0]] = open(i[1], 'r').readlines()[0].split()
 
    dorktypes = list()
 
    for i in [x.split("\n")[0] for x in open("dorktypes.txt", 'r').readlines()]:
        temp = ""
        for j in i:
            if j == "(":
                temp += "{"
            elif j == ")":
                temp += "}"
            else:
                temp += j
        dorktypes.append(temp)
    
    numbers =  list(range(1,30,3))

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(dorktypes)+1) as executor:
        completed = executor.map(worker, dorktypes)

    res = list(completed)
    print(count)
    #if not max_dork: max_dork = len(data_dict['keywords'])*len(data_dict['domain_ext'])\
     #       * (len(data_dict['pagetypes']) * len(data_dict['pageformats']) * len(data_dict['searchfunctions']) + len(numbers))
    #print(max_dork)

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
