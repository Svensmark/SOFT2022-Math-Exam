import json
data = [
    {
        'activity': 't1',
        "duration": 8,
        "predecessors": []
    },
    {
        'activity': 't2',
        "duration": 2,
        "predecessors": []
    },
    {
        'activity': 't3',
        "duration": 5,
        "predecessors": []
    },
    {
        'activity': 't4',
        "duration": 10,
        "predecessors": ['t1','t2']
    },
    {
        'activity': 't5',
        "duration": 6,
        "predecessors": ['t1','t2']
    },
    {
        'activity': 't6',
        "duration": 5,
        "predecessors": ['t2','t3']
    },
    {
        'activity': 't7',
        "duration": 5,
        "predecessors": ['t4']
    },
    {
        'activity': 't8',
        "duration": 9,
        "predecessors": ['t5','t6']
    },
    {
        'activity': 't9',
        "duration": 2,
        "predecessors": ['t6']
    },
    {
        'activity': 'end',
        "duration": 0,
        "predecessors": ['t7','t8','t9']
    }
]


def calculate_critical_path(data):
    critical_path = []
    for activity in data:
        predecessors = activity['predecessors']
        if not predecessors:
            es = 0
            ef = activity['duration'] + es
        elif predecessors:
            ef_list = [d['ef'] for d in data if d['activity'] in predecessors]
            es = max(ef_list)
            ef = es + activity['duration']
        activity['es'] = es
        activity['ef'] = ef
    for index, dactivity in enumerate(reversed(data)):
        durations = []
        if index == 0:
            dactivity['lf'] = dactivity['ef']
        else:
            items = [ditem for ditem in data if dactivity['activity'] in ditem['predecessors']]
            durations = []
            for ditem in items:
                durations.append(ditem['ls'])
            dactivity['lf'] = min(durations)
        dactivity['ls'] = dactivity['lf'] - dactivity['duration']
        dactivity['slack'] = dactivity['lf'] -  dactivity['ef']
    for item in data:
        if item['slack'] == 0:
            critical_path.append(item['activity'])
    return critical_path

critical_path = calculate_critical_path(data)
print(json.dumps(critical_path, indent=4, sort_keys=True))