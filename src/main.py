from automaton import DFA, NFA

if __name__ == '__main__':
    nfa = NFA()
    nfa.set_alphabet(['0', '1'])
    nfa.add_state('q0')
    nfa.add_state('q1')
    nfa.add_state('q2')
    nfa.add_transition('0', 'q0', 'q0')
    nfa.add_transition('1', 'q0', 'q0')
    nfa.add_transition('1', 'q0', 'q1')
    nfa.add_transition('0', 'q1', 'q2')
    nfa.set_initial_state('q0')
    nfa.set_final_states(['q2'])
    nfa.traverse('101001011101')
    # dfa = DFA()
    # dfa.set_alphabet(['0', '1'])
    # dfa.add_state('q0')
    # dfa.add_state('q1')
    # dfa.add_state('q2')
    # dfa.add_state('q3')
    # dfa.add_state('q4')
    # dfa.add_state('q5')
    # dfa.set_initial_state('q0')
    # dfa.set_final_states(['q2', 'q5'])
    # dfa.add_transition('0', 'q0', 'q1')
    # dfa.add_transition('1', 'q0', 'q2')
    # dfa.add_transition('1', 'q1', 'q3')
    # dfa.add_transition('0', 'q1', 'q4')
    # dfa.add_transition('0', 'q2', 'q4')
    # dfa.add_transition('1', 'q2', 'q4')
    # dfa.add_transition('0', 'q3', 'q5')
    # dfa.add_transition('1', 'q3', 'q4')
    # dfa.add_transition('0', 'q4', 'q4')
    # dfa.add_transition('1', 'q4', 'q4')
    # dfa.add_transition('0', 'q5', 'q4')
    # dfa.add_transition('1', 'q5', 'q4')
    
    # dfa.traverse('1010010111010')

