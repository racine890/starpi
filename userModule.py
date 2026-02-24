# Used to parse responses
import urllib.parse


# Takes in a json string, and then removes # from it
def deleteComments(text):
    ntext = ""
    for line in text.split('\n'):
        if line.strip().startswith('#'):
            continue
        ntext+=line
    return ntext

# Compares the exposed routes to the request route to check if they matches
def getMatchingUrlScheme(url, responses_list):
    if url in responses_list:
        return url

    urlparts = url.split('/')

    # Looping over responses schemes
    for response in responses_list:
        rlparts = response.split('/')
        i = 0
        skip = False

        if len(rlparts) != len(urlparts):
            continue

        # Check if url matches response scheme
        for part in rlparts:
            if part != urlparts[i]:
                if len(part) > 0 and part[0] != '{' and part[-1] != '}':
                    skip = True
                    break
            i+=1
        if skip:
            continue

        return response
    return None

construct_response = lambda liste : [{'id': el[0], 'json': el[1], 'api': el[2]} for el in liste]

USE_MODULE_FUNCS = {
    'urlLibParse': urllib.parse
}