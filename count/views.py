from django.shortcuts import render

def index(request):

    context = {}

    if request.method == 'POST':

        user_data = request.POST # get stored in dictionary.
        paragraph = user_data['paragraph'] # keyerror aauna sakcha
        
        wordlist = paragraph.split() # by default space le separate garcha

        # [a,b,c,d,e] words are stored something like this in list
        # Dictionary property

        wordcount = {}

        for word in wordlist:

            countword = wordlist.count(word) # tyo list ma word variable kati choti cha vanera count garcha
            wordcount[word] = countword # word lai key banayera count chahi value rakhcha

        context['response'] = wordcount # response vanni key chahi POST method ma matra create vacha
    

    return render(
        request,
        'count/index.html',
        context
    )
