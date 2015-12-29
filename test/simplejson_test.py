import simplejson


obj = {
    'name': 'jhc',
    'age': 27
}

json = simplejson.dumps(obj)

print json
print type(json)
