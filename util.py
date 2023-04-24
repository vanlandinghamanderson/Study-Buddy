import json

def parse_user(query_result):
    '''
    this function jsonifies user query results
    '''
    result_list = []
    for element in query_result:
        result_list.append({'fist_name': element.first_name, 'last_name': element.last_name, 'major': element.major})

    return json.dumps({'all_user':result_list})