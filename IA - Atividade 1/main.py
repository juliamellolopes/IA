import json

# funcao do agente aspirador
def reactive_vacuum_agent(location, status, performance):
    #se a sala estiver suja, muda o status para limpo
    if status == "Dirty":
        performance += 1
        status = "Clean"
        # print("Suck")
    #se o aspirador estiver na localizacao A, muda para a localizacao B
    if location == "A":
        location = "B"
        # print("Right")
        return location, status, performance
    #de o aspirador estiver na localizacao B, muda para a localizacao A
    elif location == "B":
        location = "A"
        # print("Left")
        return location, status, performance

#abre o arquivo .json com os estados iniciais (1 a 8)
with open("initial_states.json", "r") as f:
    initial_states = json.load(f)

total_performance = 0  #variavel que armazena todas os metodos de desempenho
num_configurations = len(initial_states)  #obtem o tamanho do dicionario initial_states

# itera sobre as localizacoes e os valores dos estados iniciais
for state_key, state_values in initial_states.items():
    print("\nState:", state_key)
    performance = 0  #inicializa o desempenho para o estado atual para calcular a performance de cada estado
    #itera sobre a lista de localizacoes e status do estado atual
    for location_status in state_values:
        for location, status in location_status.items():
            #atualiza o local, status e desempenho usando a funcao do agente do aspirador
            location, status, performance = reactive_vacuum_agent(location, status, performance)
            total_performance += performance  #atualiza o metodo de desempenho total
            print("Performance:", performance)  #printa o desempenho de cada estado

#calcula e printa a media geral do desempenho
print("Media geral:", total_performance / num_configurations)