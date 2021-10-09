def transact(environment, t, to_agent, from_agent, settlement_type, amount, description):
    "Function that ensures a correct transaction between agents"
    environment.measurement['period'].append(t)
    environment.measurement['to_agent'].append(to_agent)
    environment.measurement['from_agent'].append(from_agent)
    environment.measurement['settlement_type'].append(settlement_type)
    environment.measurement['amount'].append(amount)
    environment.measurement['description'].append(description)
