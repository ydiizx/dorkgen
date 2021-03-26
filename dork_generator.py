from random import choice
import argparse

def core(filein, max_dork, output):
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

    res = set()
    if not max_dork: max_dork = len(data_dict['keywords'])*len(data_dict['domain_ext'])
    while len(res) <= max_dork:
        # KW PF PT DE SF
        for KW in data_dict['keywords']:
            for DE in data_dict['domain_ext']:
                PF = choice(data_dict['pageformats'])
                PT = choice(data_dict['pagetypes'])
                SF = choice(data_dict['searchfunctions'])
                res.add(dorktypes[0].format(KW=KW, PF=PF, PT=PT, DE=DE))
                res.add(dorktypes[1].format(SF=SF, DE=DE, KW=KW))
                res.add(dorktypes[2].format(SF=SF, KW=KW, PF=PF, PT=PT, DE=DE))
                res.add(dorktypes[3].format(SF=SF, PT=PT, KW=KW, PF=PF, DE=DE))
                res.add(dorktypes[4].format(PT=PT, KW=KW, DE=DE))

    with open(output, 'w') as f:
        for i in res:
            f.write(i+"\n")

if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--filein", type=str, default="keywords.txt",
                     required=False, help="Your List of Keywords")
    arg.add_argument("-m", "--max_dork", type=int,default=None,
                     required=False, help="Max dork you want")
    arg.add_argument("-o", "--output", type=str,
                     default="result.txt", help="Your Result Output")
    args = vars(arg.parse_args())

    core(**args)
