# vim: set fileencoding=utf-8 :

def textextract(data, startstr, endstr, startpos = None):
    """ extracts a text from data, which is between startstr and endstr
        if startstr is '' it will extract from the beginning of data
        if endstr   is '' it will extract until the end of data
        the optional parameter startpos will indicate the startposition from where startstr will be searched
        and if startpos is something else than None it will return a tuple of the extracted string and the endposition of this string """
    returnPos = True
    if startpos is None:
        returnPos = False
        startpos = 0
    if startstr == '':
        pos1 = startpos
    else:
        pos1 = data.find(startstr, startpos)
        if pos1 < 0:
            if returnPos:
                return None, -1
            else:
                return None
        pos1 += len(startstr)

    if endstr == '':
        r = data[pos1:]
        pos2 = pos1 + len(r)
    else:
        pos2 = data.find(endstr, pos1)
        if pos2 < 0:
            r = None
        else:
            r = data[pos1:pos2]
            pos2 += len(endstr)
    if returnPos:
        return r, pos2
    return r





def formatCoords(coords):
    return "[%d:%d:%d]" % (coords[0], coords[1], coords[2])

def formatRes(resources):
    return "m:%d c:%d d:%d" % (resources["metal"], resources["crystal"], resources["deuterium"])
