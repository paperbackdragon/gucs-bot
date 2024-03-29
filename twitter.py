import urllib2
import json

def search(query, limit = 5):

    url = "http://search.twitter.com/search.json?q={0}&rpp={1}&page=1".format(urllib2.quote(query), limit)
    handle = urllib2.urlopen(url)

    result = ""

    for line in handle:
        result += line

    handle.close()
    decoded = json.loads(result)
    return parse(decoded)


def parse(decoded):

    theresults = []
    for result in decoded[u'results']:
         user = result[u'from_user']
         text = result[u'text']
         theresults += [(user, text)]

    return theresults         




def main():
    print "dsf"
    results = search("george orwell")

    for result in results:
        print result[0] + ": " + result[1]
        print " "

if __name__ == "__main__":
    main()
