from random import choice


def core():
    data_dict = dict()
    data = [
        ("domain_ext", "preset3_domainextensions.txt"),
        ("keywords", "keywords.txt"),
        ("pagetypes", "default_pagetypes.txt"),
        ("pageformats", "default_pageformats.txt"),
        ("searchfunctions", "default_searchfunctions.txt"),
    ]
    for i in data:
        if i[0] == "keywords":
            data_dict[i[0]] = [x.split("\n")[0]
                               for x in open(i[1], 'r').readlines()]
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
    max_dork = 20000
    res = set()
    while len(res) <= max_dork:
        # KW PF PT DE SF
        for DE in data_dict['domain_ext']:
            KW = choice(data_dict['keywords'])
            PF = choice(data_dict['pageformats'])
            PT = choice(data_dict['pagetypes'])
            SF = choice(data_dict['searchfunctions'])
            res.add(dorktypes[0].format(KW=KW, PF=PF, PT=PT, DE=DE))
            res.add(dorktypes[1].format(SF=SF, DE=DE, KW=KW))
            res.add(dorktypes[2].format(SF=SF, KW=KW, PF=PF, PT=PT, DE=DE))
            res.add(dorktypes[3].format(SF=SF, PT=PT, KW=KW, PF=PF, DE=DE))
            res.add(dorktypes[4].format(PT=PT, KW=KW, DE=DE))
    with open('result.txt', 'w') as f:
        for i in res:
            f.write(i+"\n")

        # for KW in data_dict['keywords']:
        #     for DE in data_dict['domain_ext']:
        #         for PT in data_dict["pagetypes"]:
        #             for PF in data_dict['pageformats']:
        #                 f.write(dorktypes[0].format(
        #                     KW=KW, PF=PF, PT=PT, DE=DE)+"\n")
        #                 for SF in data_dict['searchfunctions']:
        #                     f.write(dorktypes[1].format(SF=SF, DE=DE, KW=KW))
        #                     f.write(dorktypes[2].format(
        #                         SF=SF, KW=KW, PF=PF, PT=PT, DE=DE))
        #                     f.write(dorktypes[3].format(
        #                         SF=SF, KW=KW, PF=PF, PT=PT, DE=DE))
        #                     f.write(dorktypes[4].format(PT=PT, KW=KW, DE=DE))


core()
