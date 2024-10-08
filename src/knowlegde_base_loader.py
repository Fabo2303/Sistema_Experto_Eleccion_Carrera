def knowledge_base_loader():
    knowledge_base = []

    with open('data/knowledge_base.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(' THEN ')
                conditions_str = parts[0].strip()
                conclusion = parts[1].strip()
                conditions = {}
                for condition in conditions_str.split(' AND '):
                    key, value = condition.split('=')
                    if '{' in value:
                        conditions[key.strip()] = value.strip('{}').split(',')
                    else:
                        conditions[key.strip()] = value.strip()
                movie = conclusion.split('=')[1].strip()
                knowledge_base.append({
                    'conditions': conditions,
                    'movie': movie
                })

    return knowledge_base
