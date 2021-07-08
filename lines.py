from abc import abstractproperty
import codecs
import prosodic
prosodic.config['print_to_screen']=0 

# def get_lines_from_file(filename): #returns list of each line
#     f = codecs.open(filename, encoding='utf-8')
#     lines = []
#     for line in f.readlines(): 
#         lines.append(line)
#     f.close()
#     return lines

def get_lines_from_file(filename): #returns whole text
    f = codecs.open(filename, encoding='utf-8')
    lines = ''
    lines = f.read()
    f.close()
    return lines

# text = get_lines_from_file('paradiselost.txt')
# text = get_lines_from_file('thenight.txt')
text = get_lines_from_file('roadnottaken.txt')

def parse(text):
    text = prosodic.Text(text)
    text.parse() # must parse text before most methods are available
    print('CHILDREN', text.children)
    scansion_list = text.bestParses() #bestParse returns list of lines with caps/lower emphasis
    # print(text.numSyllables()) #'int' object not callable
    lines = text.lines() #returns a list of each line

    stanzas = []

    for i, stanza in enumerate(text.children):
        i = {}
        for line in stanza.descendants():
            line = prosodic.Text(str(line)) # make each line a text object to access text properties (like syllables) PROBS a better way, idk
            # syllable_list.append(len(line.syllables()))
            line.parse()
            i[str(line.bestParses())] = len(line.syllables()) #bestParse returns list of lines with caps/lower emphasis
            # syllable_list.append(line.num_syll())
        stanzas.append(i)
        #     scansion_list.append(row.get_meter())

    # for c1, c2 in zip(scansion_list, syllable_list):
        # print("%-60s %s" % (c1, c2)) #60 should probably not be hard coded and should be representative of avg line len or something
    for stanza in stanzas:
        for k, v in stanza.items():
            num = v
            print("{:<80} {:<40}".format(k, num))
        print('\n')

parse(text)