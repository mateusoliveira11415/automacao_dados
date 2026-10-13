from auto_process import write_functions as wfuncs


def return_prior(prior):
    return prior

def recieve_prior(prior):
    match prior[0]:
        case c:
            if c.isdigit():
                return return_prior(wfuncs.render_simple_compound(infor=prior, write=False))
            if c.islower():
                return return_prior(wfuncs.render_complex(infor=prior, write=False))
            return "Nenhuma condição ativada"
